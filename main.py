from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"key": "Comming from fastapi docker ci/cd v2 container"}