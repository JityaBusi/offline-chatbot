# Setup Guide – Offline Customer Support Chatbot

This document provides step-by-step instructions to set up and run the Offline Customer Support Chatbot using Ollama and the Llama 3.2 model.

---

## 1. Prerequisites

Ensure the following are installed on your system:

* Python 3.8 or higher
* Git (optional, for cloning repository)
* Internet connection (only required for initial model download)

---

## 2. Install Ollama

1. Visit the official website: https://ollama.com
2. Download and install Ollama for your operating system (Windows/macOS/Linux)
3. Complete the installation process

---

## 3. Verify Ollama Installation

Open terminal/command prompt and run:

```bash
ollama --version
```

If installed correctly, it will display the installed version.

---

## 4. Download the Llama 3.2 Model

Run the following command:

```bash
ollama pull llama3.2:3b
```

* This will download the model (~2GB)
* Wait until the download completes

---

## 5. Test the Model (Optional)

```bash
ollama run llama3.2:3b
```

Type a sample query to confirm it works.
Type `exit` to quit.

---

## 6. Project Setup

### 6.1 Clone or Download the Repository

```bash
git clone <your-repo-link>
cd offline-chatbot
```

OR manually download and extract the project folder.

---

### 6.2 Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

---

### 6.3 Install Required Python Libraries

```bash
pip install requests datasets
```

---

## 7. Project Structure

Ensure the project directory is structured as follows:

```
offline-chatbot/
│
├── chatbot.py
├── setup.md
├── report.md
├── README.md
│
├── prompts/
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
│
└── eval/
    └── results.md
```

---

## 8. Run the Chatbot

Make sure Ollama is running in the background.

Then execute:

```bash
python chatbot.py
```

---

## 9. Output

* The script will:

  * Process 20 customer queries
  * Generate responses using:

    * Zero-shot prompting
    * One-shot prompting

* Results will be saved in:

```
eval/results.md
```

---

## 10. Evaluation

1. Open `eval/results.md`
2. Manually assign scores (1–5) for:

   * Relevance
   * Coherence
   * Helpfulness

---

## 11. Troubleshooting

### Issue: Cannot connect to Ollama

* Ensure Ollama is running
* Check endpoint: `http://localhost:11434`

---

### Issue: Slow responses

* Expected on CPU-based systems
* Performance depends on system RAM and processor

---

### Issue: Model not found

* Ensure you ran:

```bash
ollama pull llama3.2:3b
```

---

## 12. Notes

* The system runs **completely offline**
* No customer data is sent to external servers
* Suitable for privacy-sensitive applications

---

## 13. Run Summary

```bash
# Install model
ollama pull llama3.2:3b

# Install dependencies
pip install requests datasets

# Run chatbot
python chatbot.py
```

---
