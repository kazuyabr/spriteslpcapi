from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder

from src.infra.mongodb.repository.spriteslpc_repository import retrieve_sprites
from src.utils.response import ErrorResponseModel, ResponseModel

router = APIRouter()


@router.get("/", response_description="Listar Bodys")
async def get_sprites():    
    sprites = await retrieve_sprites()
    return (
        ResponseModel(sprites, "Sprites listados com sucesso!")
        if sprites
        else ErrorResponseModel("Ocorreu um erro", 404, "Ainda não temos sprites!")
    )



