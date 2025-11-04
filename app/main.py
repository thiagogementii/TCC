from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import carro_router

# Cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Concessionária")

# Inclui o router
app.include_router(carro_router.router)
