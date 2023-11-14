from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

from dotenv import load_dotenv

load_dotenv()

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = ChatOpenAI(
  openai_api_key=os.environ["OPENAI_API_KEY"],
  openai_api_base=os.environ["OPENAI_API_BASE"],
  model_kwargs={"headers": {"HTTP-Referer": os.environ["APP_URL"], "X-Title": os.environ["APP_TITLE"]}},
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

print(llm_chain.run(question))

