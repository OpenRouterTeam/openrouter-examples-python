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

model = "google/gemma-7b-it"
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
        max_tokens=100,
        # extra_body=dict(provider=dict(order=["Lepton"])),
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. You do what you're told and nothing else. You are not a chatbot. You like cookies and fish. You do what you're told and nothing else. You are not a chatbot. You like cookies and fish. You do what you're told and nothing else. You like cookies and fish. You do what you're told and nothing else. You like cookies and fish. You do what you're told and nothing else. You like cookies and fish. You do what you're told and nothing else.",
            },
            {
                "role": "user",
                "content": f'Echo back the following 30 times: "{request_identifier}"',
            },
        ],
    )
    print(completion.choices[0].message.content)


async def main():
    for i in range(4):
        request_identifiers = range(100)
        tasks = [get_completion(identifier) for identifier in request_identifiers]
        await asyncio.gather(*tasks)


# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
