from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=GoogleGenerativeAI(model='gemini-2.5-flash-lite', temperature=0.7)

result=model.invoke("what is Agentic Ai?")
print(result)
