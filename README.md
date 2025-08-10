# Genarative AI Chatbot FAQ

This chatbot is designed to automate responses to frequently asked questions (FAQ), thereby improving service speed and enhancing user experience. The chatbot interface is presented as a floating action button, allowing easy access at any time.

This project is built using the LLaMA 3 LLM model with a cloud-hosted API approach, integrated via FastAPI as the backend service.

## 🚀 Features
- Automated FAQ Response: Provides quick and accurate answers to frequently asked questions.
- Floating Action Button UI: Allows easy chatbot access from the corner of the page.
- LLaMA 3 LLM Integration: Uses a cloud-based API for natural language processing.
- FastAPI Backend: Lightweight, fast, and easily extendable API service.


## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/muhammadelfikry/genarative-ai-chatbot-faq.git
cd genarative-ai-chatbot-faq
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment Variables
Create a ```.env``` file and fill in with:

```bash
# frontend/.env
DEVELOPMENT_ORIGIN=enter_your_local_address

# backend/.env
GROQ_API_KEY=enter_your_api_key
GROQ_MODEL=llama-3.3-70b-versatile
```

## ▶️ Running the Project

```bash
uvicorn main:app --reload
```
Access the API at: http://0.0.0.0:8000

## 📂 Folder Structure
```bash
genarative-ai-chatbot-faq/
│
├── backend/
│ ├── main.py           #FastAPI entry point
│ ├── config.py         #API configuration and settings
│ ├── prompt.txt        #Prompt template for LLaMA API
│ ├── requirements.txt  #Python dependencies list
│ └── middlewares.py    #FastAPI middleware
│
├── frontend/
│ ├── index.html        #Example floating chatbot integration
│ ├── css/              #Styling
│ └── js/               #Chatbot interaction scripts
│
└── README.md           #Project documentation
```

## 🌐 Demo
The chatbot will appear in the bottom right corner of the page as a floating action button that can be clicked to open the chat window.

<img width="1021" height="608" alt="Yellow   White Minimal Creative Portfolio Presentation" src="https://github.com/user-attachments/assets/a43f15e4-32ed-428f-9031-8025fc9e17f6" />

