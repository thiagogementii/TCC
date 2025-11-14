"""Script para verificar os dados inseridos no banco de dados"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.database import SessionLocal
from app.models.marca_model import Marca
from app.models.carro_model import Carro

db = SessionLocal()

try:
    # Contar marcas
    total_marcas = db.query(Marca).count()
    print(f"\n📊 Total de marcas no banco: {total_marcas}")

    # Listar marcas
    marcas = db.query(Marca).all()
    print("\n🏷️  Marcas cadastradas:")
    for marca in marcas:
        print(f"  - {marca.nome} (slug: {marca.slug}, quantidade: {marca.quantidade})")

    # Contar carros
    total_carros = db.query(Carro).count()
    print(f"\n🚗 Total de carros no banco: {total_carros}")

    # Listar alguns carros
    carros = db.query(Carro).limit(5).all()
    print("\n📋 Primeiros 5 carros cadastrados:")
    for carro in carros:
        marca = db.query(Marca).filter(Marca.id == carro.marcaId).first()
        print(f"  - {carro.nome} ({marca.nome}) - Ano: {carro.ano}, Preço: R$ {carro.preco:,.2f}")
        print(f"    Imagem: {carro.imagem if carro.imagem else '(vazio - preencher manualmente)'}")

    print("\n✅ Verificação concluída!")

except Exception as e:
    print(f"\n❌ Erro ao verificar dados: {e}")
    import traceback
    traceback.print_exc()
finally:
    db.close()

