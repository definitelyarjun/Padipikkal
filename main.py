from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


app = FastAPI()
"""
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
}
"""
class Text(BaseModel):
    text:str
class Parts(BaseModel):
    parts:List[Text]
class Content(BaseModel):
    contents:List[Parts]


class Details(BaseModel):
    q:str
class Location(BaseModel):
    locations: List[Details]

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
def generate(content: Content):
    response = requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyDSnDQ5U_dVZf8x3GKqi8HimU7sEy691HM", json=content.model_dump())
    response_body =response.json()
    return response_body["candidates"][0]["content"]["parts"][0]["text"]

@app.post("/weather")
def weather(location: Location):
  response = requests.post("http://api.weatherapi.com/v1/current.json?key=db654ef392014fada52113034250506&q=bulk", json=location.model_dump())
  response_body= response.json()
  return response_body["bulk"]

@app.post("/summary")
def