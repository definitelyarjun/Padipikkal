from fastapi import FastAPI
from typing import Optional
import schemas
import services

app = FastAPI()


@app.get("/")
def read_root(condition: Optional[bool] = True):
    if condition:
        return {"message": f'Hello World'}
    else:
        return {"message": f'Goodbye World'}

@app.get("/{id}")
def read_root(id: int = 5):
    return {"message": f'Hello World {id}'}


@app.post("/generate")
def generate(content: schemas.Content):
    return services.gemini(content=content)
    
@app.post("/weather")
def weather(location: schemas.Location):
    return services.weather(location=location)