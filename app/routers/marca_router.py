from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.carro_service import MarcaResponse
from app.services import marca_service
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/marcas", tags=["Marcas"])

@router.get("/", response_model=List[MarcaResponse])
def listar_marcas(db: Session = Depends(get_db)):
    return marca_service.listar_marcas(db)

@router.get("/{marca_id}", response_model=MarcaResponse)
def obter_marca(marca_id: int, db: Session = Depends(get_db)):
    try:
        return marca_service.obter_marca_por_id(db, marca_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/slug/{slug}", response_model=MarcaResponse)
def obter_marca_por_slug(slug: str, db: Session = Depends(get_db)):
    try:
        return marca_service.obter_marca_por_slug(db, slug)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

