# 🏦 RBI Chatbot – Retrieval-Augmented Banking Intelligence Assistant

AI-powered chatbot for querying Reserve Bank of India (RBI) circulars, regulations, notifications, and banking guidelines using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and vector search.

---

# 🚀 Overview

RBI Chatbot is an enterprise-grade AI assistant designed to help users quickly access information from RBI publications, circulars, banking regulations, monetary policy documents, and regulatory guidelines.

Instead of manually searching through lengthy RBI documents, users can ask natural language questions and receive contextual, source-grounded responses generated using Retrieval-Augmented Generation (RAG).

The system combines:

* Document Processing Pipeline
* Vector Database Search
* LLM-powered Answer Generation
* FastAPI Backend
* Streamlit Dashboard
* PDF Processing & Embedding Pipeline

---

# ✨ Features

## Intelligent RBI Knowledge Assistant

* Natural Language Querying
* Context-Aware Responses
* RBI Circular Search
* Banking Regulation Assistance
* Policy Interpretation Support
* Source-backed Answers

---

## Retrieval-Augmented Generation (RAG)

* PDF Document Parsing
* Chunking & Embedding Generation
* Semantic Search
* Vector Similarity Retrieval
* Context Injection into LLM

---

## AI-Powered Response Generation

* LLM-based Answer Synthesis
* Context Grounding
* Hallucination Reduction
* Multi-document Retrieval

---

## Enterprise Reliability Features

* Circuit Breaker Pattern
* Retry Mechanisms
* Graceful Failure Handling
* Service Health Monitoring
* Logging & Diagnostics

---

## Dashboard

* Ask Questions in Natural Language
* View Retrieved Context
* Response Generation Metrics
* Service Status Monitoring

---

# 🏗️ System Architecture

```text
                    User Query
                         │
                         ▼
               Streamlit Frontend
                         │
                         ▼
                  FastAPI Backend
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
  Vector Search      LLM Service      Monitoring
       │                 │
       ▼                 ▼
   ChromaDB /       Ollama / LLM
   FAISS Store
       │
       ▼
 RBI Documents & Circulars
```

---

# 🧠 RAG Pipeline

## Step 1: Document Ingestion

RBI Circulars

Monetary Policy Documents

Regulatory Notifications

Master Directions

Banking Guidelines

---

## Step 2: Text Processing

```text
PDF
  │
  ▼
Text Extraction
  │
  ▼
Chunking
  │
  ▼
Embedding Generation
```

---

## Step 3: Vector Storage

* ChromaDB
* FAISS
* Semantic Indexing
* Similarity Search

---

## Step 4: Retrieval

```text
User Question
      │
      ▼
Embedding
      │
      ▼
Vector Search
      │
      ▼
Top-K Relevant Chunks
```

---

## Step 5: LLM Generation

```text
Retrieved Context
       +
User Question
       │
       ▼
LLM
       │
       ▼
Grounded Response
```

---

# 🛠️ Tech Stack

## Frontend

* Streamlit
* HTML/CSS
* Plotly
* Pandas

---

## Backend

* FastAPI
* Uvicorn
* Async Python
* Pydantic

---

## AI & NLP

* LangChain
* Sentence Transformers
* Ollama
* LLM Integration
* RAG Architecture

---

## Vector Database

* ChromaDB / FAISS

---

## Data Processing

* PyPDF
* PDFPlumber
* NumPy
* Pandas

---

## Reliability

* PyBreaker
* Retry Logic
* Health Checks
* Monitoring

---

# 📂 Project Structure

```text
rbi-chatbot/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── rag/
│   ├── vector_store/
│   ├── monitoring/
│   └── main.py
│
├── frontend/
│   ├── dashboard.py
│   ├── components/
│   └── utils/
│
├── data/
│   ├── circulars/
│   ├── regulations/
│   └── policy_documents/
│
├── embeddings/
│
├── logs/
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Gaurang-Joshi-learner/rbi-chatbot.git

cd rbi-chatbot
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Backend

```bash
uvicorn main:app --reload
```

---

## Start Frontend

```bash
npm install
npm run dev
```

---



---

# 📈 Example Queries

### Monetary Policy

```text
What was the latest RBI repo rate decision?
```

---

### Banking Regulations

```text
What are RBI guidelines for digital lending?
```

---

### KYC Compliance

```text
Explain RBI KYC requirements for banks.
```

---

### Priority Sector Lending

```text
What are the latest priority sector lending norms?
```

---

# 🔥 Advanced Features

* Circuit Breaker Architecture
* Fault Tolerance
* Retry Strategies
* Context-aware Retrieval
* Modular RAG Pipeline
* Scalable API Design
* Enterprise Monitoring

---


---

# 🔮 Future Enhancements

* Multi-Language Support
* Voice-Based Queries
* RBI News Monitoring
* Automated Circular Updates
* Fine-Tuned Banking LLM
* Real-Time Regulatory Alerts
* Multi-Agent Financial Assistant

---

# 💼 Placement Highlights

### Backend Engineering

* FastAPI
* Async APIs
* Service Architecture
* Circuit Breakers

### AI/ML

* Retrieval-Augmented Generation
* LLM Integration
* Semantic Search
* Vector Databases

### Software Engineering

* Fault Tolerance
* Monitoring
* Scalability
* Modular Design

### Domain Knowledge

* Banking Regulations
* Financial Compliance
* RBI Policy Documents

---



---



---


