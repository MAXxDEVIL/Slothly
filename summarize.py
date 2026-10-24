"""Slothly — two-line summarizer core."""

from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


def summarize(text: str, model: str = "llama3.2") -> str:
    prompt = (
        "You are Slothly, a lazy but brilliant assistant. "
        "Summarize the user's note into exactly two lines. "
        "Format it exactly like this:\n"
        "Line 1: <short summary>\n"
        "Line 2: <key action/takeaway>\n"
        "Do not add greetings, commentary, or sign-offs. "
        "Keep both lines short and useful. Note: " + text
    )
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
    )
    return completion.choices[0].message.content.strip()


if __name__ == "__main__":
    import sys

    text = open(sys.argv[1]).read() if len(sys.argv) > 1 else input("Paste note: ")
    print(summarize(text))
