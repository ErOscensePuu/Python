# Inicia el server: uvicorn main:app --reload
# Deneter el server: CTRL+C

#Documentación con Swagger: http://127.0.0.1:8000/docs
#Documentación con Redocly: http://127.0.0.1:8000/redoc

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hola FastAPI!"

# Url local: http://127.0.0.1:8000

@app.get("/url")
async def url():
    return { "url_curso":"https://mouredev.com/python" }

#Url local: http://127.0.0.1:8000/url

@app.get("/sum")
async def sum_values():
    return 5+5

#Url local: http://127.0.0.1:8000/sum