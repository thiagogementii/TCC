from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano_fabricacao = Column(Integer)
    ano_modelo = Column(Integer)
    tipo = Column(String)
    descricao = Column(String)
    cor = Column(String)
    combustivel = Column(String)
    cambio = Column(String)
    motor = Column(String)
    potencia = Column(String)
    quilometragem = Column(Integer)
    preco = Column(Numeric(10, 2))
    portas = Column(Integer)
    placa = Column(String, unique=True)
    renavam = Column(String, unique=True)
    status = Column(String, default="Disponível")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
