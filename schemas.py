from pydantic import BaseModel
from typing import List

#Gemini Payload
class Text(BaseModel):
    text:str
class Parts(BaseModel):
    parts:List[Text]
class Content(BaseModel):
    contents:List[Parts]

#Weather Payload
class Details(BaseModel):
    q:str
class Location(BaseModel):
    locations: List[Details]