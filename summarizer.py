from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="YOUR_API_KEY"  # Replace with your NVIDIA API key
)

def summarize_text(text):
    response = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-70b-instruct",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}],
        temperature=0.5,
        max_tokens=512
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    text = input("Enter text to summarize: ")
    summary = summarize_text(text)
    print("Summary:", summary)
