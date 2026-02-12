# Retrieval-Augmented-Generation-RAG-system
AI Shopping Agent is a local, privacy-first chatbot that uses Llama 3 to understand your shopping needs and Google Shopping (via SerpApi) to find the best real-time deals. Built with Streamlit for a clean, responsive UI.
# 🛍️ AI Shopping Agent (Local Llama 3 + SerpApi)

A neuro-symbolic AI agent that combines local Large Language Models (LLMs) with real-time internet search. 

This project uses **Llama 3** (running locally via Ollama) to understand user intent and **SerpApi** to fetch live product data (prices, images, ratings) from Google Shopping, displaying it all in a modern **Streamlit** interface.

## 🚀 Features
- **Neuro-Symbolic AI:** Uses Llama 3 for reasoning and SerpApi for factual data retrieval.
- **Privacy-First:** The "Brain" of the AI runs entirely on your local machine.
- **Visual Interface:** Beautiful product cards with images, prices, and "Buy Now" links.
- **Smart Routing:** The AI decides when to chat normally vs. when to search the web.

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Python)
- **AI Model:** Llama 3 (via Ollama)
- **Search Tool:** SerpApi (Google Shopping Engine)
- **Language:** Python 3.10+

---

## ⚙️ Prerequisites

Before running the project, you need to set up the environment.

### 1. Install Python
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### 2. Install Ollama (The AI Brain)
This project requires Ollama to run the Llama 3 model locally.
1. Download Ollama from [ollama.com](https://ollama.com).
2. Install it and open your terminal/command prompt.
3. Run the following command to download the model:
   ```bash
   ollama pull llama3
4. Verify it's running by typing "ollama list" in your terminal.

### 3. Get a SerpApi Key
This project uses SerpApi to search Google Shopping.

1. Go to SerpApi.com.

2. Sign up (Free tier available).

3. Copy your Private API Key.
📥 Installation
Clone the Repository

Bash
git clone [https://github.com/YOUR_USERNAME/ai-shopping-agent.git](https://github.com/YOUR_USERNAME/ai-shopping-agent.git)
cd ai-shopping-agent
Install Dependencies

Bash
pip install -r requirements.txt
#### ▶️ Usage
Start the App
Run the Streamlit application:

Bash
streamlit run app.py
1. Enter Your API Key
2. The app will open in your browser (usually http://localhost:8501).
3. On the left sidebar, paste your SerpApi Key.

(Optional: You can hardcode the key in app.py if you don't want to paste it every time).

Start Shopping!

Type queries like:

"Best mechanical keyboard under $50"

"Red Nike running shoes"

"Price of iPhone 15"

### 🐛 Troubleshooting
Error: connection refused
Make sure Ollama is running. Open a separate terminal and type ollama serve.

Error: Invalid API Key
Check your SerpApi dashboard and ensure you copied the key correctly into the sidebar.

The bot is slow

Local LLMs depend on your hardware. If Llama 3 is too slow, try a smaller model like phi3 by running ollama pull phi3 and updating the code to use model="phi3".

### 🤝 Contributing
Feel free to submit issues and enhancement requests!

### 📜 License
MIT


---

