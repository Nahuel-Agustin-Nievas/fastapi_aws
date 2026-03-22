from fastapi import FastAPI
from .database import engine, Base
from .routes import pedidos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Servicio de Pedidos",
    description="Microservicio para gestión de pedidos",
    version="1.0.0"
)

app.include_router(
    pedidos.router,
    prefix="/api/pedidos",
    tags=["pedidos"]
)

@app.get("/health")
def health_check():
    return {"status": "ok", "servicio": "pedidos"}

@app.get("/probes/ready")
def readiness():
    return {"status": "ready"}