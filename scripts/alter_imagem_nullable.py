"""Script para alterar a coluna imagem para aceitar valores nulos

Execute este script para atualizar a estrutura da tabela carros:
    python scripts/alter_imagem_nullable.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.database import engine
from sqlalchemy import text

print("Alterando coluna 'imagem' para aceitar valores nulos...")

try:
    with engine.connect() as connection:
        # Alterar a coluna imagem para nullable
        connection.execute(
            text('ALTER TABLE carros ALTER COLUMN imagem DROP NOT NULL;')
        )
        connection.commit()
        print("✓ Coluna 'imagem' alterada com sucesso!")
        print("  Agora a coluna 'imagem' aceita valores nulos.")
except Exception as e:
    print(f"✗ Erro ao alterar coluna: {e}")
    import traceback
    traceback.print_exc()

