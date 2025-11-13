"""Script para criar todas as tabelas no banco de dados.

Execute este script antes de rodar o seed_carros.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.database import Base, engine
from app.models.marca_model import Marca
from app.models.carro_model import Carro

print("Criando tabelas no banco de dados...")

try:
    # Criar todas as tabelas
    Base.metadata.create_all(bind=engine)
    print("✓ Tabelas criadas com sucesso!")
    print("  - marcas")
    print("  - carros")
except Exception as e:
    print(f"✗ Erro ao criar tabelas: {e}")
    import traceback
    traceback.print_exc()

