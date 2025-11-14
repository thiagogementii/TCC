from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    marcaId = Column(Integer, ForeignKey("marcas.id"), nullable=False)
    ano = Column(Integer, nullable=False)
    preco = Column(Numeric(10, 2), nullable=False)
    km = Column(Integer, nullable=False)
    transmissao = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    imagem = Column(String, nullable=True)
    descricao = Column(String)

    # Relacionamento com marca
    marca_rel = relationship("Marca", back_populates="carros")
