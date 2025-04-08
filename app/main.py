from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    correo: str
    contraseña: str

@app.post("/registro")
def registrar_usuario(usuario: Usuario):
    return {"mensaje": f"Usuario {usuario.correo} registrado correctamente"}
