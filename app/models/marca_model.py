from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    slug = Column(String, nullable=False, unique=True)
    logo = Column(String)
    quantidade = Column(Integer, default=0)

    # Relacionamento com carros
    carros = relationship("Carro", back_populates="marca_rel")

