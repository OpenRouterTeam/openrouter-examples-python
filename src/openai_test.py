from openai import OpenAI
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# gets API Key from environment variables
client = OpenAI(
    base_url=getenv("OPENROUTER_BASE_URL"),
    api_key=getenv("OPENROUTER_API_KEY"),
)

model = "openai/gpt-3.5-turbo"

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": getenv("APP_URL"),
        "X-Title": getenv("APP_TITLE"),
    },
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(completion.choices[0].message.content)

# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": getenv("APP_URL"),
        "X-Title": getenv("APP_TITLE"),
    },
    model=model,
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue

    print(chunk.choices[0].delta.content, end="")
print()
