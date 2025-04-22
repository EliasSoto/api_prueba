from sqlalchemy.orm import Session
import models, schemas

# Crear un nuevo usuario
def create_user (db: Session, user_create: schemas.UserCreateModel):
    # Creamos un nuevo usuario usando los datos del modelo UserCreateModel
    db_user = models.User(username=user_create.username, email=user_create.email, password=user_create.password)
    db.add(db_user)  # Agregar el usuario a la sesión
    db.commit()  # Confirmar la transacción
    db.refresh(db_user)  # Refrescar el objeto con los datos más recientes
    return db_user  # Devolver el usuario creado

# Obtener todos los usuarios
def get_users (db: Session, skip: int = 0, limit: int = 100):
    # Obtener los usuarios desde la base de datos con paginación
    return db.query(models.User).offset(skip).limit(limit).all()

# Obtener un usuario por su ID
def get_user_by_username (db: Session, user_username: str):
    # Buscar un usuario por su ID en la base de datos
    return db.query(models.User).filter(models.User.username == user_username).first()

# Funcion para eliminaar un usuario por su ID de la base de datos
def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

# Funcion para actualizar un usuario por su ID de la base de datos
def update_user(db: Session, user_id: int, user_update: schemas.UserCreateModel):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.username = user_update.username
        user.email = user_update.email
        user.password = user_update.password
        db.commit()
        db.refresh(user)
    return user
