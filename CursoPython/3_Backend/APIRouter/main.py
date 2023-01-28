# Inicia el server: uvicorn main:app --reload
# Deneter el server: CTRL+C

#Documentación con Swagger: http://127.0.0.1:8000/docs
#Documentación con Redocly: http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from routers import products, jwt_auth_users, basic_auth_users, users, users_db
from fastapi.staticfiles import StaticFiles


app = FastAPI()

#Routers

app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)


#Recursos estaticos

#app.mount("/static", StaticFiles(directory="static"), name="static")
#Da error pero funciona la imagen en http://127.0.0.1:8000/static/images/python.jpg

@app.get("/")
async def root():
    return "¡Hola FastAPI!"


# Url local: http://127.0.0.1:8000


@app.get("/url")
async def url():
    return { "url_curso":"https://mouredev.com/python" }

#Url local: http://127.0.0.1:8000/url

