from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://usuario:password@localhost:5432/pedidos_db"
    USUARIOS_SERVICE_URL: str = "http://servicio-usuarios:8000"
    PRODUCTOS_SERVICE_URL: str = "http://servicio-productos:8000"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()