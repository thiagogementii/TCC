from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.carro_service import CarroResponse
from app.services import carro_service
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/carros", tags=["Carros"])

@router.get("/", response_model=List[CarroResponse])
def listar_carros(db: Session = Depends(get_db)):
    return carro_service.listar_carros(db)

@router.get("/{carro_id}", response_model=CarroResponse)
def obter_carro(carro_id: int, db: Session = Depends(get_db)):
    try:
        return carro_service.obter_carro_por_id(db, carro_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
