from fastapi import FastAPI
from .database import engine, Base
from .routes import usuarios

# Crear tablas en la base de datos al arrancar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Servicio de Usuarios",
    description="Microservicio para gestión de usuarios y autenticación",
    version="1.0.0"
)

# Registrar las rutas
app.include_router(
    usuarios.router,
    prefix="/api/usuarios",
    tags=["usuarios"]
)

@app.get("/health")
def health_check():
    return {"status": "ok", "servicio": "usuarios"}

@app.get("/probes/ready")
def readiness():
    return {"status": "ready"}