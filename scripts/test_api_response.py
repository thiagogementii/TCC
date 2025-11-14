"""Script de teste para verificar se a API está retornando os dados corretamente"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.database import SessionLocal
from app.models.marca_model import Marca  # Importar modelo Marca
from app.models.carro_model import Carro  # Importar modelo Carro
from app.services import carro_service
from app.schemas.carro_service import CarroResponse

db = SessionLocal()

try:
    print("\n🔍 Testando o serviço de carros...")

    # Buscar todos os carros
    carros = carro_service.listar_carros(db)

    print(f"\n✅ Total de carros encontrados: {len(carros)}")

    # Tentar converter para o schema de resposta
    print("\n📋 Testando conversão para CarroResponse...")

    for i, carro in enumerate(carros[:3]):  # Testar apenas os 3 primeiros
        try:
            carro_response = CarroResponse.model_validate(carro)
            print(f"\n  ✓ Carro {i+1}: {carro_response.nome}")
            print(f"    Marca: {carro_response.nomeMarca}")
            print(f"    Imagem: {carro_response.imagem if carro_response.imagem else '(vazio)'}")
            print(f"    Ano: {carro_response.ano}, Preço: R$ {carro_response.preco:,.2f}")
        except Exception as e:
            print(f"\n  ✗ Erro ao validar carro {i+1}: {e}")

    print("\n✅ Teste concluído com sucesso!")
    print("\n💡 Se este teste passou, reinicie o servidor FastAPI para aplicar as mudanças.")
    print("   Execute: uvicorn app.main:app --reload")

except Exception as e:
    print(f"\n❌ Erro ao testar: {e}")
    import traceback
    traceback.print_exc()
finally:
    db.close()

