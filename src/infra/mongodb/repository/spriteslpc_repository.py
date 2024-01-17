from datetime import datetime, timezone

from bson import ObjectId

from src.infra.mongodb.database import sprites_collection
from src.models.spritelpc_model import SpriteLPCModel


def sprites_helper(sprite: SpriteLPCModel, created: bool = False) -> dict:
    if created:
        created_date = datetime.now(timezone.utc)
        updated_date = created_date
    else:
        created_date = sprite.created
        updated_date = datetime.now(timezone.utc)

    return {
        "_id": str(sprite.id),
        "hair": [hair.dict() for hair in sprite.hair],
        "head": [head.dict() for head in sprite.head],
        "body": [body.dict() for body in sprite.body],
        "torso": [torso.dict() for torso in sprite.torso],
        "legs": [legs.dict() for legs in sprite.legs],
        "gloves": [gloves.dict() for gloves in sprite.gloves],
        "feet": [feet.dict() for feet in sprite.feet],
        "gender": [gender.dict() for gender in sprite.gender],
        "shadow": [shadow.dict() for shadow in sprite.shadow],
        "height": sprite.height,
        "width": sprite.width,
        "created": str(created_date),
        "updated": str(updated_date)
    }

# Retrieve all sprites present in the database
async def retrieve_sprites():
    sprites = []
    async for sprite in sprites_collection.find():
        sprite_model = SpriteLPCModel.parse_obj(sprite)
        sprites.append(sprites_helper(sprite_model))
    return sprites

# Add a new sprite to the database
async def add_sprite(sprite_data: dict) -> dict:
    new_sprite = SpriteLPCModel(**sprite_data).dict()
    new_sprite.pop("_id", None)  # Remove _id field if present
    new_sprite.pop("id", None)  # Remove id field if present
    result = await sprites_collection.insert_one(new_sprite)
    inserted_sprite = await sprites_collection.find_one({"_id": result.inserted_id})
    return sprites_helper(SpriteLPCModel.parse_obj(inserted_sprite))

# Retrieve sprites by gender
async def retrieve_sprites_by_gender(gender: str):
    sprites_list = []
    async for sprite in sprites_collection.find({"gender": gender}):
        sprite_model = SpriteLPCModel.parse_obj(sprite)
        sprites_list.append(sprites_helper(sprite_model))
    return sprites_list

# Update a sprite with a matching ID
async def update_sprite(id: str, data: dict):
    if not data:
        return None
    
    data = {key: value for key, value in data.items() if value is not None}
    
    data.pop("_id", None)
    
    sprite = await sprites_collection.find_one({"_id": ObjectId(id)})
    
    if sprite:
        await sprites_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        
        updated_sprite = await sprites_collection.find_one({"_id": ObjectId(id)})
        return sprites_helper(SpriteLPCModel.parse_obj(updated_sprite))
    else:
        return None

# Delete a sprite from the database
async def delete_sprite(id: str):
    sprite = await sprites_collection.find_one({"_id": ObjectId(id)})
    if sprite:
        await sprites_collection.delete_one({"_id": ObjectId(id)})
        return True
    else:
        return False
