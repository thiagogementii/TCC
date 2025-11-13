from sqlalchemy.orm import Session
from app.models.marca_model import Marca

def listar_marcas(db: Session):
    return db.query(Marca).all()

def obter_marca_por_id(db: Session, marca_id: int):
    return db.query(Marca).filter(Marca.id == marca_id).first()

def obter_marca_por_slug(db: Session, slug: str):
    return db.query(Marca).filter(Marca.slug == slug).first()

