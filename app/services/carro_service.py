from sqlalchemy.orm import Session
from app.repositories import carro_repository

def listar_carros(db: Session):
    return carro_repository.listar_carros(db)

def obter_carro_por_id(db: Session, carro_id: int):
    carro = carro_repository.obter_carro_por_id(db, carro_id)
    if not carro:
        raise ValueError("Carro não encontrado")
    return carro
