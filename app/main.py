from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.routers import carro_router, marca_router

# Cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Concessionária",
    description="API REST para gerenciamento de carros e marcas",
    version="1.0.0"
)

# Configurar CORS para desenvolvimento com Angular
origins = [
    "http://localhost:4200",  # Angular default
    "http://localhost:3000",  # Caso use outra porta
    "http://127.0.0.1:4200",
    "http://127.0.0.1:3000",
    "*"  # Permite qualquer origem (apenas para desenvolvimento)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

# Rota raiz para teste
@app.get("/", tags=["Status"])
def root():
    return {
        "message": "API Concessionária está rodando!",
        "status": "online",
        "version": "1.0.0",
        "endpoints": {
            "carros": "/carros",
            "marcas": "/marcas",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }

# Health check endpoint
@app.get("/health", tags=["Status"])
def health_check():
    return {"status": "healthy"}

# Inclui os routers
app.include_router(carro_router.router)
app.include_router(marca_router.router)
