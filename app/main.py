from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud, models

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI()

# Configuración de la aplicación
app.title = "CRUD API"
app.description = "Esta API permite crear, leer, actualizar y eliminar usuarios."

# Endpoints de la API

# Endpoint para crear un nuevo usuario
@app.post("/users/", tags=["Usuarios"], response_model=schemas.UserResponseModel)
def create_user(user_create: schemas.UserCreateModel, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user_create=user_create)

# Endpoint para obtener todos los usuarios
@app.get("/users/", tags=["Usuarios"], response_model=List[schemas.UserResponseModel])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# Endpoint para obtener un usuario por su ID
@app.get("/users/{user_username}", tags=["Usuarios"], response_model=schemas.UserResponseModel)
def read_user(user_username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user_username=user_username)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

# Endpoiint para eliminar un usuario por su ID
@app.delete("/users/{user_id}", tags=["Usuarios"], response_model=schemas.UserResponseModel)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user =crud.delete_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

# Endpoint para actualizar un usuario por su ID
@app.put("/users/{user_id}", tags=["Usuarios"], response_model=schemas.UserResponseModel)
def update_user(user_id: int, user_update: schemas.UserCreateModel, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id = user_id, user_update=user_update)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user