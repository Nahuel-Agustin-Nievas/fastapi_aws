from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

SECRET_KEY = "clave-secreta-cambiar-en-produccion"
ALGORITHM = "HS256"

security = HTTPBearer()

def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id = payload.get("id")
        if usuario_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return usuario_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")