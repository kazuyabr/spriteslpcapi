from datetime import datetime
from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.utils.validator import PyObjectId


class Hair(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    url: str
    gender: str
    
class Head(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    url: str
    gender: str
    
class BodyColor(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    url: str
    
class Body(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    list_body_color: List[BodyColor]
    gender: str
    
class Torso(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    url: str
    gender: str

class Legs(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    url: str
    gender: str

class Gloves(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    url: str
    gender: str

class Feet(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    url: str
    gender: str
    
class Gender(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    body_type: str
    
class Shadow(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    url: str
    
class SpriteLPCModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    hair: List[Hair] = []
    head: List[Head] = []
    body: List[Body] = []
    torso: List[Torso] = []
    legs: List[Legs] = []
    gloves: List[Gloves] = []
    feet: List[Feet] = []
    gender: List[Gender] = []
    shadow: List[Shadow] = []
    height: int
    width: int
    
    created: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str, datetime: lambda dt: dt.timestamp()}
        schema_extra = {
            "example": {
                "hair": [
                    {
                        "id": "614e44db9564d2de07108fda",
                        "name": "Long Hair",
                        "url": "http://example.com/longhair",
                        "gender": "male"
                    },
                    # Adicione outros cabelos aqui...
                ],
                "head": [
                    {
                        "id": "614e44db9564d2de07108fdb",
                        "name": "Round Head",
                        "url": "http://example.com/roundhead",
                        "gender": "male"
                    },
                    # Adicione outras cabeças aqui...
                ],
                # Adicione outras partes do corpo aqui...
                "gender": [
                    {
                        "id": "614e44db9564d2de07108fdc",
                        "name": "Male",
                        "url": "http://example.com/male",
                        "gender": "male"
                    },
                    # Adicione outros gêneros aqui...
                ]
            }
        }
        orm_mode = True
