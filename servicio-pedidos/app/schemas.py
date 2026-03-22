from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PedidoCreate(BaseModel):
    usuario_id: int
    producto_id: int
    cantidad: int

class PedidoResponse(BaseModel):
    id: int
    usuario_id: int
    producto_id: int
    cantidad: int
    precio_total: float
    estado: str
    creado_en: datetime

    class Config:
        from_attributes = True

class PedidoUpdateEstado(BaseModel):
    estado: str