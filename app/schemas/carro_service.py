from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CarroBase(BaseModel):
    nome: str
    marca: str
    modelo: str
    ano_fabricacao: int
    ano_modelo: int
    tipo: str
    descricao: str
    cor: str
    combustivel: str
    cambio: str
    motor: str
    potencia: str
    quilometragem: int
    preco: float
    portas: int
    placa: str
    renavam: str
    status: str = "Disponível"

class CarroResponse(CarroBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
