from fastapi import FastAPI

app = FastAPI()


@app.get("/lab")
def root():
    return "not implemented yet"
