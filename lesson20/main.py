from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
     return {"message": "hello world"}

@app.get("/greet/")
def read_root(name: str):
    return  {"message": f"hello, {name}!"}