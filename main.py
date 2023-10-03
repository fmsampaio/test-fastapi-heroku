from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "data" : "Simple FastAPI app for Heroku deployment"
    }