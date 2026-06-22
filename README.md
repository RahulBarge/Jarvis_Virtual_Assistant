# 🎙️ Jarvis Virtual Assistant

Jarvis is a Python-based Virtual voice assistant that can listen to voice commands, respond using Google's Gemini AI, read the latest news headlines, and automate common web tasks.

## 🚀 Features

- 🎤 Voice Recognition
- 🔊 Text-to-Speech Responses
- 🤖 Gemini AI Integration
- 📰 Latest News Headlines
- 🌐 Open Websites Using Voice Commands
- 🔐 Secure API Key Management with `.env`
- 📂 Modular Project Structure

## 🛠️ Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- SoundDevice
- Google Gemini API
- MediaStack API
- Requests
- Python Dotenv

## 📁 Project Structure

```text
Jarvis/
│
├── main.py
├── speech.py
├── listener.py
├── commands.py
├── ai.py
├── news.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Jarvis-AI-Assistant.git

cd Jarvis-AI-Assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
Google_api=YOUR_GEMINI_API_KEY
news_api=YOUR_MEDIASTACK_API_KEY
```

## ▶️ Run Jarvis

```bash
python main.py
```

## 🎯 Available Commands

### Website Automation

- Open Google
- Open LinkedIn
- Open Instagram

### News

- News
- Latest News

### AI Assistant

Ask any question:

```text
What is Python?
Explain Object Oriented Programming
What is Machine Learning?
```

## 📌 Future Enhancements

- Weather Updates
- Stock Market Information
- Application Launcher
- Wake Word Detection
- Chat Memory
- System Automation
- WhatsApp Integration
- YouTube Music Control

## 🔒 Security

API keys are stored in a `.env` file and are excluded from GitHub using `.gitignore`.

Never upload your API keys publicly.

## 👨‍💻 Author

Rahul Barge

Electronics and Telecommunication Engineering Student

AI, Machine Learning, and Software Development Enthusiast

## ⭐ Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

## 📄 License

This project is intended for educational and personal use.
