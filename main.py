from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "API is running smoothly."}

@app.get("/metrics")
def get_metrics():
    return {"cpu_usage": "12%", "memory_usage": "34%"}