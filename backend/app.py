from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Stylosense-AI",
        "message": "Welcome to Stylosense AI Backend"
    }

@app.get("/recommendation")
def recommendation():
    return {
        "customer": "Demo User",
        "recommended_dress": "Black Blazer with White Shirt"
    }
