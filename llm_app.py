from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm= ChatGroq(model_name="llama-3.1-8b-instant")

prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a general assistant.  Answer the user's question clearly and concisely.\n Question:{question} \n Answer:"
    )
output_parser=StrOutputParser()

chain = prompt | llm | output_parser
result=chain.invoke({"question": "What is the AI?"})
print(result)