from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Pedido
from ..schemas import PedidoCreate, PedidoResponse, PedidoUpdateEstado
from ..utils.http_client import obtener_usuario, obtener_producto
from typing import List
import asyncio

router = APIRouter()

@router.post("/", response_model=PedidoResponse, status_code=201)
async def crear_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    # Verificar usuario y producto en paralelo
    usuario, producto = await asyncio.gather(
        obtener_usuario(pedido.usuario_id),
        obtener_producto(pedido.producto_id)
    )

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if producto["stock"] < pedido.cantidad:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    precio_total = producto["precio"] * pedido.cantidad

    nuevo_pedido = Pedido(
        usuario_id=pedido.usuario_id,
        producto_id=pedido.producto_id,
        cantidad=pedido.cantidad,
        precio_total=precio_total
    )
    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)
    return nuevo_pedido

@router.get("/", response_model=List[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(Pedido).all()

@router.get("/{id}", response_model=PedidoResponse)
def obtener_pedido(id: int, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.patch("/{id}/estado", response_model=PedidoResponse)
def actualizar_estado(id: int, datos: PedidoUpdateEstado, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    pedido.estado = datos.estado
    db.commit()
    db.refresh(pedido)
    return pedido