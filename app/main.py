from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def virtual_assistant():
    """ """
    return {"Hi": "Hello, I'm a Chatbot. What can I do for you? "}
