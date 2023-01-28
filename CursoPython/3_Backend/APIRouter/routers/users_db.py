### Users DB API ###enter-your-module-name

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_chema


router = APIRouter(prefix="/userdb", 
                    tags=["userdb"],
                    responses={status.HTTP_404_NOT_FOUND:{"message":"No encontrado"}})


users_list= []


@router.get("/")
async def users():
    return users_list


@router.get("/{id}")
async def user(id: int):
    return search_user(id)


@router.get("/")
async def user(id: int):
    return search_user(id)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    #if type(search_user(user.id)) == User:
     #   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
    user_dict = dict(user)
    del user_dict["id"]

    id= db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_chema(db_client.local.users.find_one({"id": id}))
    
    return User(**new_user)


@router.put("/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,detail="No se ha actualizado el usuario")
    else:
        return "Se ha actualizado el usuario:",user



@router.delete("/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
            if saved_user.id == id:
                del users_list[index]
                found = True
            
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No hay usuario que eleminar")
    else:
        return "Se ha eliminado el usuario con id:", id


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}