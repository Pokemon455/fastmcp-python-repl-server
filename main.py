from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from fastapi import FastAPI

llm = ChatOpenAI(
    model="Meta-Llama-3.1-8B-Instruct",
    api_key="your_api_key",
    base_url="https://api.sambanova.ai/v1",
    temperature=0.9
)

app=FastAPI()

@app.post("/frist_model")
def model(Human: str, System : str= "you are helpful assistant "):
    response = llm.invoke(
        [
            SystemMessage(content=System),
            HumanMessage(content=Human)
        ]
    )
    Result=response.content
    return {"response": Result}