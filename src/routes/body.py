from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder

from src.utils.response import ErrorResponseModel, ResponseModel

router = APIRouter()


@router.post("/", response_description="Adiciona um novo Sprite LPC")
async def add_body_data(body: BodysSchema = Body(...)):
    body = jsonable_encoder(body)
    new_body = await add_body(body)
    return ResponseModel(new_body, "Body adicionado com sucesso!")


@router.get("/", response_description="Listar Bodys")
async def get_bodys():    
    bodys = await retrieve_bodys_by_email(token["email"])
    return (
        ResponseModel(bodys, "Bodys listados com sucesso!")
        if bodys
        else ErrorResponseModel("Ocorreu um erro", 404, "Ainda não temos bodys!")
    )


@router.get("/{id}", response_description="Recupera um Body pelo seu ID")
async def get_body_data(id):
    body = await retrieve_body(id)
    if body:
        return ResponseModel(body, "O body foi encontrado!")
    return ErrorResponseModel("Ocorreu um erro!.", 404, "Body não encontrado!")


@router.put("/{id}")
async def update_body_data(
    id: str, req: BodysSchema = Body(...),
    
):
    req = jsonable_encoder(req)
    updated_body = await update_body(id, req)
    if updated_body:
        return ResponseModel(
            f"Body com ID: {id} foi atualizado!",
            "Body atualizado com exito!",
        )
    return ErrorResponseModel(
        "Ocorreu um erro!",
        404,
        "Nenhuma informação foi alterada!",
    )


@router.delete("/{id}", response_description="Deleta o Body da base de dados!")
async def delete_body_data(id: str):
    deleted_body = await delete_body(id)
    if deleted_body:
        return ResponseModel(f"Body com ID: {id} removido", "Body removido com sucesso!")
    return ErrorResponseModel(
        "Ocorreu um erro!", 404, "Body com id {0} não existe!".format(id)
    )
