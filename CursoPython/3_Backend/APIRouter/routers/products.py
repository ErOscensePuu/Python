from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/products", 
                    tags=["porducts"],
                    responses={404:{"message":"No encontrado"}})

products_list=["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5",] 

@router.get("/")
async def products():
    return products_list

@router.get("/{id}", status_code=200)
async def products(id:int):
    users = filter(lambda user: user.id == id, products_list)
    try:
        return products_list[id]
    except:
        raise HTTPException(status_code=204,detail="No se ha encontrado el producto")
        
        


