from typing import List

from pydantic import BaseModel, Field


class SpriteLPCSchema(BaseModel):
    gender: str = None

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "John Doe",
                "org_identity": "empresa-12345",
                "documents": [
                    "614e44db9564d2de07108fda",
                    "614e44db9564d2de07108fdb",
                    "614e44db9564d2de07108fdc",
                ],
                "description": "Descreva seu bot"
            }
        }
