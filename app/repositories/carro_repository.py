from sqlalchemy.orm import Session
from app.models.carro_model import Carro

def listar_carros(db: Session):
    return db.query(Carro).all()

def obter_carro_por_id(db: Session, carro_id: int):
    return db.query(Carro).filter(Carro.id == carro_id).first()
