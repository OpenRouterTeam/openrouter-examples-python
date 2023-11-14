from litellm import completion
from dotenv import load_dotenv

load_dotenv()


OPENROUTER_ENDPOINTS = {
    "gpt-3.5-turbo": "openrouter/openai/gpt-3.5-turbo",
    "claude-2": "openrouter/anthropic/claude-2",
}

def call_llm(prompt, model_name, attachments=None, max_retries=2):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        }
    ]
    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )
    print(f"Using OpenRouter to call {model_name}...")
    response = completion(
        model=OPENROUTER_ENDPOINTS[model_name], 
        messages=messages,
        api_key=os.environ["OPENAI_API_KEY"],
    )
    return response

if __name__ == "__main__":
    response = call_llm(prompt="Twinkle Twinkle Little Starship ...", model_name="gpt-3.5-turbo")
    response_message = response["choices"][0]["message"]["content"]
    print(response_message)
