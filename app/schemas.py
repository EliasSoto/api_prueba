from pydantic import BaseModel
from typing import Optional

# Clase base para los campos comunes en los datos del usuario
class UserBaseModel(BaseModel):
    username: str  # Nombre de usuario
    email: str  # Correo electrónico del usuario


#VERDADEROS SCHEMAS
# Clase que define los datos necesarios para crear un usuario
class UserCreateModel(UserBaseModel):
    password: str  # Contraseña del usuario

# Clase que define cómo se ve un usuario en la base de datos, con ID y estado activo
class UserResponseModel(UserBaseModel):
    id: int  # ID único del usuario
    is_active: bool  # Indica si el usuario está activo

    # Configuración para permitir que Pydantic trabaje con objetos de la base de datos
    class Config:
        orm_mode = True
