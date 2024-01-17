from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder

from src.utils.response import ErrorResponseModel, ResponseModel

router = APIRouter()


@router.post("/", response_description="Adiciona um novo Sprite LPC")
async def add_bot_data(bot: BotsSchema = Body(...), token: dict = Depends(validate_token)):
    bot = jsonable_encoder(bot)
    new_bot = await add_bot(bot)
    return ResponseModel(new_bot, "Bot adicionado com sucesso!")


@router.get("/", response_description="Listar Bots")
async def get_bots(token: dict = Depends(validate_token)):    
    bots = await retrieve_bots_by_email(token["email"])
    return (
        ResponseModel(bots, "Bots listados com sucesso!")
        if bots
        else ErrorResponseModel("Ocorreu um erro", 404, "Ainda não temos bots!")
    )


@router.get("/{id}", response_description="Recupera um Bot pelo seu ID")
async def get_bot_data(id, token: dict = Depends(validate_token)):
    bot = await retrieve_bot(id)
    if bot:
        return ResponseModel(bot, "O bot foi encontrado!")
    return ErrorResponseModel("Ocorreu um erro!.", 404, "Bot não encontrado!")


@router.put("/{id}")
async def update_bot_data(
    id: str, req: BotsSchema = Body(...),
    token: dict = Depends(validate_token)
):
    req = jsonable_encoder(req)
    updated_bot = await update_bot(id, token["email"], req)
    if updated_bot:
        return ResponseModel(
            f"Bot com ID: {id} foi atualizado!",
            "Bot atualizado com exito!",
        )
    return ErrorResponseModel(
        "Ocorreu um erro!",
        404,
        "Nenhuma informação foi alterada!",
    )


@router.delete("/{id}", response_description="Deleta o Bot da base de dados!")
async def delete_bot_data(id: str, token: dict = Depends(validate_token)):
    deleted_bot = await delete_bot(id)
    if deleted_bot:
        return ResponseModel(f"Bot com ID: {id} removido", "Bot removido com sucesso!")
    return ErrorResponseModel(
        "Ocorreu um erro!", 404, "Bot com id {0} não existe!".format(id)
    )
