from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI(
  openai_api_key=os.environ["OPENAI_API_KEY"],
  openai_api_base=os.environ["OPENAI_API_BASE"],
  default_headers={"HTTP-Referer": os.environ["APP_URL"], "X-Title": os.environ["APP_URL"]},
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)

