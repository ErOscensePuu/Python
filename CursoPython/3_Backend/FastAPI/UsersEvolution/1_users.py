from fastapi import FastAPI
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

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}