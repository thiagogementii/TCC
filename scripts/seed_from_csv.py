"""Script para popular o banco de dados a partir do arquivo CSV carros_30_sortidos.csv

Execute este script após criar as tabelas com init_db.py:
    python scripts/seed_from_csv.py
"""

import sys
import csv
from pathlib import Path
from decimal import Decimal

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.database import SessionLocal
from app.models.marca_model import Marca
from app.models.carro_model import Carro


def criar_slug(nome):
    """Cria um slug a partir do nome da marca"""
    return nome.lower().replace(" ", "-")


def seed_from_csv():
    """Lê o CSV e popula o banco de dados"""

    db = SessionLocal()

    try:
        # Caminho do arquivo CSV
        csv_path = Path(__file__).parent / "carros_30_sortidos.csv"

        if not csv_path.exists():
            print(f"✗ Arquivo CSV não encontrado: {csv_path}")
            return

        print("🚀 Iniciando seed do banco de dados...")
        print(f"📄 Lendo arquivo: {csv_path}")

        # Dicionário para armazenar marcas já criadas
        marcas_cache = {}

        # Contador de registros
        marcas_inseridas = 0
        carros_inseridos = 0

        # Ler o CSV
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                marca_nome = row['marca']

                # Criar ou buscar a marca
                if marca_nome not in marcas_cache:
                    # Verificar se a marca já existe no banco
                    marca = db.query(Marca).filter(Marca.nome == marca_nome).first()

                    if not marca:
                        # Criar nova marca
                        marca = Marca(
                            nome=marca_nome,
                            slug=criar_slug(marca_nome),
                            logo=None,  # Deixar vazio para preencher manualmente
                            quantidade=0
                        )
                        db.add(marca)
                        db.flush()  # Para obter o ID
                        marcas_inseridas += 1
                        print(f"  ✓ Marca criada: {marca_nome}")

                    marcas_cache[marca_nome] = marca
                else:
                    marca = marcas_cache[marca_nome]

                # Criar o carro
                carro = Carro(
                    nome=row['nome'],
                    marcaId=marca.id,
                    ano=int(row['ano']),
                    preco=Decimal(row['preco']),
                    km=int(row['km']),
                    transmissao=row['transmissao'],
                    imagem=None,  # Deixar vazio para preencher manualmente
                    descricao=row['descricao']
                )
                db.add(carro)
                carros_inseridos += 1

                # Atualizar quantidade de carros da marca
                marca.quantidade += 1

        # Commit de todas as alterações
        db.commit()

        print("\n" + "="*50)
        print("✅ Seed concluído com sucesso!")
        print(f"📊 Marcas inseridas: {marcas_inseridas}")
        print(f"🚗 Carros inseridos: {carros_inseridos}")
        print("="*50)
        print("\n💡 Dica: As imagens estão vazias. Preencha-as manualmente no banco de dados.")

    except Exception as e:
        db.rollback()
        print(f"\n❌ Erro ao popular banco de dados: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    seed_from_csv()

