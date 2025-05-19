from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")
template = """
You are an expert programmer. Your goal is to help the user with their programming problems.
The user will provide you with a programming problem, and you will respond with a solution in Python.
However, you should provide the solution in a step-by-step manner, explaining each step clearly.
Don't just give the final code; lead the user through the process of solving the problem.

The relevant files are in ~/workspace/github.com/

The question is question: {issue}

"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-----------------------")
    question = input("Enter your question (q to quit): ")
    if question == 'q':
        break
    result = chain.invoke({"issue":(question)})
    print(result)