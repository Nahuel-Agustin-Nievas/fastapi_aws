from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=False)
    producto_id = Column(Integer, nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_total = Column(Float, nullable=False)
    estado = Column(String, default="pendiente")
    creado_en = Column(DateTime, server_default=func.now())