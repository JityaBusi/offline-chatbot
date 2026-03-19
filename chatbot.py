import requests
import json

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "Error: Could not get response"


def load_template(path):
    with open(path, "r") as f:
        return f.read()


def main():
    zero_template = load_template("prompts/zero_shot_template.txt")
    one_template = load_template("prompts/one_shot_template.txt")

    queries = [
        "My discount code is not working at checkout",
        "How do I track my order?",
        "I received a damaged product, what should I do?",
        "Can I change my shipping address after placing an order?",
        "When will my order be delivered?",
        "How do I cancel my order?",
        "I was charged twice for my order",
        "What payment methods do you accept?",
        "How do I return an item?",
        "My order is delayed, what’s happening?",
        "Do you offer international shipping?",
        "How do I contact customer support?",
        "Can I exchange a product?",
        "Why was my payment declined?",
        "How do I apply a coupon code?",
        "Is my personal information सुरक्षित?",  # nice touch
        "How do I reset my account password?",
        "What if I receive the wrong item?",
        "Do you provide refunds?",
        "How long does shipping take?"
    ]

    with open("eval/results.md", "w", encoding="utf-8") as f:

        f.write("| Query # | Customer Query | Method | Response | Relevance | Coherence | Helpfulness |\n")
        f.write("|---------|---------------|--------|----------|-----------|------------|-------------|\n")

        for i, query in enumerate(queries, 1):

            zero_prompt = zero_template.replace("{query}", query)
            one_prompt = one_template.replace("{query}", query)

            zero_response = query_ollama(zero_prompt)
            one_response = query_ollama(one_prompt)

            f.write(f"| {i} | {query} | Zero-Shot | {zero_response} |  |  |  |\n")
            f.write(f"| {i} | {query} | One-Shot | {one_response} |  |  |  |\n")

            print(f"Done Query {i}")


if __name__ == "__main__":
    main()