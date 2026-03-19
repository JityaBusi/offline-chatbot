# offline-chatbot
Build an Offline Customer Support Chatbot with Ollama and Llama 3.2
# 🛍️ Offline Customer Support Chatbot (Ollama + Llama 3.2)

## 📌 Overview

This project implements a fully **offline customer support chatbot** for a fictional e-commerce store **"Chic Boutique"** using **Ollama** and the **Llama 3.2 (3B)** language model.

The chatbot processes customer queries such as order tracking, returns, and payment issues without sending any data to external servers, ensuring **data privacy, security, and zero API cost**.

---

## 🚀 Features

* ✅ Fully offline chatbot (no internet required after setup)
* ✅ Powered by Llama 3.2 via Ollama
* ✅ Supports 20+ customer support queries
* ✅ Implements **Zero-Shot** and **One-Shot Prompting**
* ✅ Manual evaluation with scoring (Relevance, Coherence, Helpfulness)
* ✅ Clean modular structure for easy extension

---

## 🧠 Key Concepts

* **Large Language Models (LLMs)** for text generation
* **Prompt Engineering** (Zero-shot vs One-shot)
* **Local AI Deployment** using Ollama
* **Privacy-focused AI systems**

---

## 🏗️ Project Structure

```
offline-chatbot/
│
├── chatbot.py              # Main script to run chatbot
├── setup.md                # Setup instructions
├── report.md               # Project analysis and findings
├── README.md               # Project documentation
│
├── prompts/
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
│
└── eval/
    └── results.md          # Output + evaluation scores
```

---

## ⚙️ Installation & Setup

### 1. Install Ollama

Download from: https://ollama.com

---

### 2. Pull the Model

```bash
ollama pull llama3.2:3b
```

---

### 3. Install Python Dependencies

```bash
pip install requests datasets
```

---

### 4. Run the Chatbot

```bash
python chatbot.py
```

---

## 🔄 How It Works

1. Loads customer queries (20 adapted e-commerce queries)
2. Applies:

   * Zero-shot prompt
   * One-shot prompt
3. Sends request to local Ollama server
4. Llama 3.2 generates response
5. Responses are saved in `eval/results.md`

---

## 📊 Evaluation

Each response is manually evaluated on:

| Metric      | Description          |
| ----------- | -------------------- |
| Relevance   | Accuracy of response |
| Coherence   | Clarity and grammar  |
| Helpfulness | Practical usefulness |

Scores range from **1 (Poor) to 5 (Excellent)**.

---

## 📈 Results Summary

| Metric      | Zero-Shot | One-Shot |
| ----------- | --------- | -------- |
| Relevance   | 4.1       | 4.6      |
| Coherence   | 4.5       | 4.8      |
| Helpfulness | 3.8       | 4.4      |

👉 One-shot prompting consistently produced more structured and helpful responses.

---

## ⚠️ Limitations

* ❌ No real-time data (order tracking, user info)
* ❌ Possible hallucinations
* ❌ Slower performance on CPU
* ❌ No multi-turn conversation memory

---

## 🔮 Future Improvements

* 🔗 Backend integration (Node.js / Flask)
* 📚 Retrieval-Augmented Generation (RAG)
* 🧠 Larger models (Llama 3 8B, Mistral)
* 💻 Web UI (React chatbot interface)
* 🔄 Multi-turn conversation support

---

## 🛡️ Why Offline AI?

This project demonstrates how AI can be deployed **locally** to:

* Protect sensitive customer data
* Comply with regulations (GDPR, DPDP)
* Eliminate API costs
* Ensure full control over infrastructure

---

## 📚 Technologies Used

* Python
* Ollama
* Llama 3.2 (3B)
* Requests Library
* Hugging Face Datasets

---

## 👨‍💻 Author

**Jitya Busi**
B.Tech (Final Year) | Full-Stack Developer

---

## ⭐ Final Note

This project highlights the potential of **privacy-first AI systems**.
With proper prompt engineering, even small local models can deliver **practical and reliable customer support automation**.

---
