"""Script para adicionar a coluna 'tipo' à tabela carros

Execute este script para atualizar a estrutura do banco:
    python scripts/add_tipo_column.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.database import engine
from sqlalchemy import text


def add_tipo_column():
    """Adiciona a coluna tipo à tabela carros"""

    try:
        with engine.connect() as conn:
            print("🔧 Adicionando coluna 'tipo' à tabela carros...")

            # Adicionar a coluna tipo
            conn.execute(text("""
                ALTER TABLE carros 
                ADD COLUMN IF NOT EXISTS tipo VARCHAR(50) DEFAULT 'SUV'
            """))

            conn.commit()

            print("✅ Coluna 'tipo' adicionada com sucesso!")
            print("💡 Agora você pode executar o seed para popular os dados com os tipos corretos.")

    except Exception as e:
        print(f"❌ Erro ao adicionar coluna: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    add_tipo_column()

