from openai import AsyncOpenAI
import asyncio
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# gets API Key from environment variables
client = AsyncOpenAI(
    base_url=getenv("OPENROUTER_BASE_URL"),
    api_key=getenv("OPENROUTER_API_KEY"),
)

# model = "google/gemma-7b-it"
# model = "nousresearch/nous-capybara-34b"
model = "microsoft/wizardlm-2-7b"
# model = "meta-llama/llama-2-13b-chat"
# model = "openai/gpt-3.5-turbo"


async def get_completion(request_identifier):
    # Non-streaming load test
    print(f"Request {request_identifier}")
    completion = await client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": getenv("APP_URL"),
            "X-Title": getenv("APP_TITLE"),
        },
        model=model,
        max_tokens=400,
        # extra_body=dict(provider=dict(order=["Lepton"])),
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. You do what you're told and nothing else. You are not a chatbot. You like cookies and fish. You do what you're told and nothing else. You are not a chatbot. You like cookies and fish. You do what you're told and nothing else. You like cookies and fish. You do what you're told and nothing else. You like cookies and fish. You do what you're told and nothing else. You like cookies and fish. You do what you're told and nothing else."
                * 30,
            },
            {
                "role": "user",
                "content": f'Echo back the following 100 times: "{request_identifier}"',
            },
        ],
    )
    if completion.choices:
        print(completion.choices[0].message.content)
    else:
        print("No completions found")


async def main():
    # for i in range(4):
    request_identifiers = range(10)
    tasks = [get_completion(identifier) for identifier in request_identifiers]
    await asyncio.gather(*tasks, return_exceptions=True)


# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
