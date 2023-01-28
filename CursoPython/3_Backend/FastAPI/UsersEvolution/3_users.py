from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list= [User(id=1, name= "Pascual", surname= "Ferrer", url= "https://puu.com", age= 18),
            User(id=2, name= "Moure", surname= "Dev", url= "https://mouredev.com", age= 35),
            User(id=3, name= "Brais", surname= "moure", url= "https://moure.dev", age= 33)]



@app.get("/usersjson")
async def usersjson():
    return [{"name":"Pascual","surname":"Ferrer","url":"https://puu.com", "age":18},
            {"name":"Moure","surname":"Dev","url":"https://mouredev.com", "age":35},
            {"name":"Brais","surname":"moure","url":"https://moure.dev", "age":33}]


@app.get("/users")
async def users():
    return users_list

# Path

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Query

#http://127.0.0.1:8000/userquery/?id=1

@app.get("/userquery/")
async def user(id: int):
    return search_user(id)


@app.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:    
        users_list.append(user)
        return user


@app.put("/user")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return "Se ha actualizado el usuario:",user



@app.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
            if saved_user.id == id:
                del users_list[index]
                found = True
            
    if not found:
        return {"error": "No se ha eliminado el usuario"}
    else:
        return "Se ha eliminado el usuario con id:", id


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}