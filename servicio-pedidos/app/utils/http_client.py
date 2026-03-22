import httpx
from ..database import settings

async def obtener_usuario(usuario_id: int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{settings.USUARIOS_SERVICE_URL}/api/usuarios/usuarios/{usuario_id}"
            )
            if response.status_code == 404:
                return None
            return response.json()
        except httpx.RequestError:
            return None

async def obtener_producto(producto_id: int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{settings.PRODUCTOS_SERVICE_URL}/api/productos/{producto_id}"
            )
            if response.status_code == 404:
                return None
            return response.json()
        except httpx.RequestError:
            return None