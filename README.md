# Oculis AI Chatbot

Oculis AI is an interactive chatbot application built using Streamlit, designed to provide engaging and mood-specific responses. The chatbot leverages the Gemini model to deliver dynamic dialogue tailored to user inputs, allowing for both text and voice interaction. The chatbot learns from user interactions over time, adapting to specific vocabulary and preferences.

## Features

- **Interactive User Interface**: Built using Streamlit for a smooth user experience.
- **Mood-Specific Responses**: Users can select from various moods (Normal, Technical, Funny, etc.) to tailor the chatbot’s responses.
- **Voice Input and Output**: Supports voice input through the microphone, making interactions hands-free.
- **User Learning Module**: Analyzes user input to adapt to personalized vocabulary and preferences.
- **Chat History**: Keeps a record of user interactions for continuity and context.

![WhatsApp Image 2025-01-31 at 19 57 51_8fabb641](https://github.com/user-attachments/assets/295cc17f-78d9-42bb-bddc-f35af4e0340b)


## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- Access to a terminal or command prompt

## Required Libraries

This project requires several Python libraries. Refer to `requirements.txt` file with the following content:
streamlit google-generativeai SpeechRecognition gTTS googletrans==4.0.0-rc1

## Setup Instructions

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [YOUR_REPOSITORY_URL]
   cd [YOUR_REPOSITORY_NAME]
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment:**
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   -On MacOs/Linux:
   ```bash
   source venv/bin/activate
   ```
4. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Set your API key:** Ensure to replace your-api-key with your actual API key in the command below:
   ```bash
   set API_KEY="your-api-key"
   ```
6. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```
The application will start and be available at http://localhost:8501.

## Future Improvements
This project is currently running locally and will be improved with the following features in the near future:

-Slack or Discord integration
-Hosting options to make it publicly accessible
-Additional mood variations and personality modules
-Better handling of user preferences and learning mechanisms

## Contributing
If you have suggestions for improvements or would like to contribute to this project, feel free to create a pull request or open an issue on the GitHub repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Thank you for using Oculis AI! We hope you enjoy interacting with our chatbot.
   


