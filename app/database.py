from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os
# usar un archivo .env para guardar la contraseña de la base de datos
# y no exponerla en el código fuente
from dotenv import load_dotenv
load_dotenv()

URL_DATABASE = os.getenv("URL_DATABASE")

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()

#Este archivo solo se usa para hacer la conexion con la base de datos y no tiene que ser modificado
#La base de datos usada es PostgreSQL