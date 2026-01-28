# RAG Based Question Answering System

## 📌 Project Overview
This project implements a Retrieval-Augmented Generation (RAG) based Question Answering system using FastAPI and FAISS.
It retrieves relevant documents using vector search and generates accurate answers using LLMs.

## 🛠 Tech Stack
- Python
- FastAPI
- FAISS
- LangChain
- OpenAI / LLM
- Uvicorn

## ⚙️ Setup Steps
```bash
git clone https://github.com/dnyaneshwariKanse-art/rag-based-qa-system.git
cd rag-based-qa-system
pip install -r requirements.txt
uvicorn app.main:app --reload
