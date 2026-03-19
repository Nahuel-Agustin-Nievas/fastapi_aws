from fastapi import FastAPI
from .database import engine, Base
from .routes import productos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Servicio de Productos",
    description="Microservicio para gestión de productos",
    version="1.0.0"
)

app.include_router(
    productos.router,
    prefix="/api/productos",
    tags=["productos"]
)

@app.get("/health")
def health_check():
    return {"status": "ok", "servicio": "productos"}

@app.get("/probes/ready")
def readiness():
    return {"status": "ready"}