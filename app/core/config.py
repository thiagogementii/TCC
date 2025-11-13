import os
from dotenv import load_dotenv

load_dotenv()

# Configurações da aplicação
class Settings:
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # API
    API_TITLE: str = "API Concessionária"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "API REST para gerenciamento de carros e marcas"

    # CORS
    CORS_ORIGINS: list = [
        "http://localhost:4200",  # Angular development
        "http://localhost:3000",
        "http://127.0.0.1:4200",
        "http://127.0.0.1:3000",
    ]

    # Environment
    ENV: str = os.getenv("ENV", "development")

    # Se estiver em desenvolvimento, permite todas as origens
    @property
    def allowed_origins(self):
        if self.ENV == "development":
            return ["*"]
        return self.CORS_ORIGINS

settings = Settings()

