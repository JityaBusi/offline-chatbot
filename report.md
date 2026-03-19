# Offline Customer Support Chatbot using Ollama and Llama 3.2

## 1. Introduction

In modern e-commerce systems, customer support plays a critical role in ensuring user satisfaction and retention. Businesses handle a large number of queries related to order tracking, returns, payments, and product issues. While cloud-based Large Language Models (LLMs) provide powerful automation capabilities, they introduce concerns regarding data privacy, regulatory compliance, and operational cost.

This project explores the feasibility of building an **offline customer support chatbot** using **Ollama** and the **Llama 3.2 (3B)** model. By running the model locally, the system ensures that sensitive customer data never leaves the organization’s infrastructure, aligning with regulations such as GDPR, CCPA, and India's DPDP Act 2023.

The primary objective of this project is to:

* Build a fully functional offline chatbot
* Compare **zero-shot** and **one-shot prompting techniques**
* Evaluate the model’s performance based on relevance, coherence, and helpfulness

---

## 2. Methodology

### 2.1 Data Preparation

A set of **20 customer queries** was prepared by adapting real-world technical queries into e-commerce scenarios. These queries represent common customer concerns such as:

* Order tracking
* Payment issues
* Returns and refunds
* Account management

Example transformation:

* Technical: “My wifi driver is not working”
* Adapted: “My discount code is not working at checkout”

---

### 2.2 Prompt Engineering

Two prompting strategies were implemented:

#### Zero-Shot Prompting

The model is given instructions without any example.

**Template Structure:**

* Role assignment (customer support agent)
* Customer query
* Expected response section

#### One-Shot Prompting

The model is provided with one example before the actual query.

**Example Included:**

* Query: Return policy
* Response: Clear, concise, structured answer

This helps guide the model’s tone, clarity, and format.

---

### 2.3 System Architecture

The system operates entirely offline with the following workflow:

1. Python script formats the prompt
2. Sends HTTP POST request to Ollama API (`http://localhost:11434/api/generate`)
3. Llama 3.2 processes the prompt
4. Response is returned and logged
5. Results stored in `eval/results.md`

---

### 2.4 Evaluation Criteria

Each response was manually evaluated based on:

| Metric      | Description                             |
| ----------- | --------------------------------------- |
| Relevance   | How well the response answers the query |
| Coherence   | Clarity and grammatical correctness     |
| Helpfulness | Practical usefulness of the response    |

Each metric was scored from **1 (Poor) to 5 (Excellent)**.

---

## 3. Results and Analysis

### 3.1 Quantitative Results

After evaluating all 20 queries, the average scores were:

| Metric      | Zero-Shot | One-Shot |
| ----------- | --------- | -------- |
| Relevance   | 4.1       | 4.6      |
| Coherence   | 4.5       | 4.8      |
| Helpfulness | 3.8       | 4.4      |

---

### 3.2 Observations

#### 1. One-Shot Prompting Performs Better

One-shot prompting consistently produced:

* More structured responses
* Better tone and professionalism
* More actionable suggestions

Example:

* Zero-shot: Generic explanation
* One-shot: Clear steps (e.g., “Go to order history → click return”)

---

#### 2. Zero-Shot Responses Were Less Consistent

While often correct, zero-shot responses:

* Lacked structure
* Sometimes gave vague answers
* Missed actionable steps

---

#### 3. Coherence Was Strong in Both

The Llama 3.2 model demonstrated:

* Good grammar
* Fluent sentence construction
* Natural conversational tone

---

#### 4. Helpfulness Was the Biggest Difference

One-shot prompting improved helpfulness significantly by:

* Providing specific instructions
* Reducing ambiguity
* Aligning responses with expected customer support style

---

### 3.3 Example Comparison

**Query:** “My discount code is not working”

* **Zero-Shot Response:**
  Provided general troubleshooting without clear steps.

* **One-Shot Response:**
  Suggested checking expiry, eligibility, and applying code correctly.

👉 Conclusion: One-shot responses were more user-friendly and actionable.

---

## 4. Conclusion

This project demonstrates that it is feasible to build an effective **offline customer support chatbot** using Ollama and Llama 3.2.

Key findings:

* The model performs well for **basic customer support queries**
* **One-shot prompting significantly improves response quality**
* Offline deployment ensures **data privacy and zero API cost**

However, the model is best suited for:

* General FAQs
* Simple troubleshooting
* Non-critical interactions

---

## 5. Limitations

Despite its effectiveness, the system has several limitations:

1. **No Real-Time Data Access**

   * Cannot fetch live order status or user data

2. **Potential Hallucinations**

   * May generate incorrect but plausible responses

3. **Performance Constraints**

   * Slow response time on CPU-based systems

4. **Lack of Personalization**

   * Cannot tailor responses to individual users

---

## 6. Future Improvements

To enhance this system further:

1. **Integrate Backend Systems**

   * Connect to databases for real-time order tracking

2. **Implement RAG (Retrieval-Augmented Generation)**

   * Use company documents and policies for accurate responses

3. **Upgrade Model**

   * Use larger models like Llama 3 8B or Mistral 7B

4. **Build User Interface**

   * Develop a React-based chatbot interface

5. **Add Multi-Turn Conversation Support**

   * Maintain context across interactions

---

## 7. Final Remarks

This project highlights the growing importance of **local AI deployment** in privacy-sensitive environments. While cloud-based solutions remain powerful, offline LLMs offer a compelling alternative for organizations prioritizing **data security, compliance, and cost efficiency**.

The results confirm that with proper prompt engineering, even smaller models like Llama 3.2 (3B) can deliver meaningful and practical customer support automation.

---
