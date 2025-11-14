from pydantic import BaseModel
from typing import Optional

class MarcaBase(BaseModel):
    nome: str
    slug: str
    logo: Optional[str] = None
    quantidade: int = 0

class MarcaResponse(MarcaBase):
    id: int

    class Config:
        from_attributes = True

class CarroBase(BaseModel):
    nome: str
    marcaId: int
    ano: int
    preco: float
    km: int
    transmissao: str
    tipo: str
    imagem: Optional[str] = None
    descricao: Optional[str] = None

class CarroResponse(CarroBase):
    id: int
    nomeMarca: Optional[str] = None

    class Config:
        from_attributes = True
