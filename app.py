import streamlit as st
import google.generativeai as genai
import os
import speech_recognition as sr
from gtts import gTTS
import tempfile
from io import StringIO, BytesIO

genai.configure(api_key=os.getenv("API_KEY"))

recognizer = sr.Recognizer()

st.set_page_config(page_title="Oculis AI")
st.title("֎ Oculis AI")

def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("https://i.pinimg.com/736x/59/ab/8f/59ab8f8c8afd93a73aaf28639ff1018f.jpg")


if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "speak_mode" not in st.session_state:
    st.session_state["speak_mode"] = False  
if "user_vocab" not in st.session_state:
    st.session_state["user_vocab"] = {}
if "user_preferences" not in st.session_state:
    st.session_state["user_preferences"] = {}


def get_mic_input():
    with sr.Microphone() as source:
        audio = recognizer.listen(source) 
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError as e:
            return f"Error with Google Speech Recognition: {e}"


def read_uploaded_file(uploaded_file):
    if uploaded_file is not None:
      
        content = uploaded_file.read()
        return content.decode("utf-8")  
    return ""


def get_gemini_response(user_input, mood, history=None, doc_content=None):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Reply to '{user_input}'"
    if history:
        prompt += f" corresponding to the following history: {history}"
    if doc_content:
        prompt += f" based on the following document content: {doc_content}"

    if mood == "Normal":
        response = model.generate_content(f"{prompt}")
    elif mood == "Technical":
        response = model.generate_content(f"Please answer in a technical way: {prompt}")
    elif mood == "Academic":
        response = model.generate_content(f"Provide an academic response to: {prompt}")
    elif mood == "Funny":
        response = model.generate_content(f"Make it funny: {prompt}")
    elif mood == "Serious":
        response = model.generate_content(f"Respond in a serious tone to: {prompt}")
    elif mood == "Flirt":
        response = model.generate_content(f"Use flirtatious language: {prompt}")
    elif mood == "Happy":
        response = model.generate_content(f"Respond with a cheerful tone: {prompt}")
    elif mood == "Sad":
        response = model.generate_content(f"Respond in a sad tone: {prompt}")
    elif mood == "Angry":
        response = model.generate_content(f"Answer in an angry manner: {prompt}")
    
    return response.text


def analyze_user_input(user_input):
    words = user_input.lower().split()
    for word in words:
        if word in st.session_state["user_vocab"]:
            st.session_state["user_vocab"][word] += 1
        else:
            st.session_state["user_vocab"][word] = 1



uploaded_file = st.file_uploader("Upload any document (text files preferred)", type=['txt', 'pdf', 'doc', 'docx'])


mood_options = ["Normal", "Technical", "Academic", "Funny", "Serious", "Flirt", "Happy", "Sad", "Angry"]
selected_mood = st.selectbox("Select AI Mood:", mood_options)


preserve_history = st.checkbox("Preserve Chat History")


user_text = st.text_input("Type your message:")


col1, col2 = st.columns(2)
with col1:
    text_submit = st.button("Send Text")
with col2:
    voice_submit = st.button("🎙️ Speak")

user_input = None
if text_submit and user_text:
    user_input = user_text
elif voice_submit:
    user_input = get_mic_input()
    st.write(f"🎤 You said: {user_input}")


if user_input and user_input.lower() != "stop":
    analyze_user_input(user_input)  

    history = " | ".join([f"{role}: {text}" for role, text in st.session_state["chat_history"]]) if preserve_history else None
    doc_content = read_uploaded_file(uploaded_file) if uploaded_file else None
    response_text = get_gemini_response(user_input, selected_mood, history, doc_content)


    st.session_state["chat_history"].append(("You", user_input))
    st.session_state["chat_history"].append(("Bot", response_text))

    st.subheader("Response:")
    st.write(response_text)


elif user_input and user_input.lower() == "stop":
    st.warning("Chatbot Stopped.")

st.subheader("Chat History:")
for role, text in st.session_state["chat_history"]:
    st.write(f"**{role}**: {text}")

user_preference_input = st.text_input("Update your preferences (comma-separated):")
if st.button("Update Preferences") and user_preference_input:
    preferences = [p.strip() for p in user_preference_input.split(',')]
    st.session_state["user_preferences"] = preferences
    st.success("Preferences Updated!")
