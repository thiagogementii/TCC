from sqlalchemy.orm import Session
from app.repositories import marca_repository

def listar_marcas(db: Session):
    return marca_repository.listar_marcas(db)

def obter_marca_por_id(db: Session, marca_id: int):
    marca = marca_repository.obter_marca_por_id(db, marca_id)
    if not marca:
        raise ValueError("Marca não encontrada")
    return marca

def obter_marca_por_slug(db: Session, slug: str):
    marca = marca_repository.obter_marca_por_slug(db, slug)
    if not marca:
        raise ValueError("Marca não encontrada")
    return marca

