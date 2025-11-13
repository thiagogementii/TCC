from sqlalchemy.orm import Session, joinedload
from app.models.carro_model import Carro

def listar_carros(db: Session):
    carros = db.query(Carro).options(joinedload(Carro.marca_rel)).all()
    # Adicionar nomeMarca a cada carro
    for carro in carros:
        carro.nomeMarca = carro.marca_rel.nome if carro.marca_rel else None
    return carros

def obter_carro_por_id(db: Session, carro_id: int):
    carro = db.query(Carro).options(joinedload(Carro.marca_rel)).filter(Carro.id == carro_id).first()
    if carro and carro.marca_rel:
        carro.nomeMarca = carro.marca_rel.nome
    return carro
