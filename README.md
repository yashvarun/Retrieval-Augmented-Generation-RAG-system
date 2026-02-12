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
