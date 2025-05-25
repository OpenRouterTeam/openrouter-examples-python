from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    [
        ("user", "{question}"),
        ("assistant", "Let's think step by step."),
    ]
)

llm = ChatOpenAI(model="openai/gpt-4.1-mini")

llm_chain = template | llm

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

print(llm_chain.invoke({"question": question}))
