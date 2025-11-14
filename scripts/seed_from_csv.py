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
        csv_path = Path(__file__).parent / "carros_com_tipo.csv"

        if not csv_path.exists():
            print(f"✗ Arquivo CSV não encontrado: {csv_path}")
            return

        print("🚀 Iniciando seed do banco de dados...")
        print(f"📄 Lendo arquivo: {csv_path}")

        # Mapeamento de marcaId para nome da marca
        # Baseado nos IDs do CSV
        marcas_map = {
            1: 'Nissan',
            2: 'Fiat',
            3: 'Jeep',
            4: 'Renault',
            5: 'Volkswagen',
            6: 'Peugeot',
            7: 'Toyota',
            8: 'Honda',
            9: 'Chevrolet',
            10: 'Hyundai'
        }

        # Dicionário para armazenar marcas já criadas
        marcas_cache = {}

        # Contador de registros
        marcas_inseridas = 0
        carros_inseridos = 0

        # Criar/buscar todas as marcas primeiro
        for marca_id, marca_nome in marcas_map.items():
            marca = db.query(Marca).filter(Marca.id == marca_id).first()

            if not marca:
                # Criar nova marca com ID específico
                marca = Marca(
                    id=marca_id,
                    nome=marca_nome,
                    slug=criar_slug(marca_nome),
                    logo=None,
                    quantidade=0
                )
                db.add(marca)
                db.flush()
                marcas_inseridas += 1
                print(f"  ✓ Marca criada: {marca_nome} (ID: {marca_id})")

            marcas_cache[marca_id] = marca

        # Ler o CSV
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                marca_id = int(row['marcaId'])
                marca = marcas_cache.get(marca_id)

                if not marca:
                    print(f"  ⚠ Marca ID {marca_id} não encontrada, pulando carro {row['nome']}")
                    continue

                # Criar o carro
                carro = Carro(
                    nome=row['nome'],
                    marcaId=marca.id,
                    ano=int(row['ano']),
                    preco=Decimal(row['preco']),
                    km=int(row['km']),
                    transmissao=row['transmissao'],
                    tipo=row['tipo'],
                    imagem=row['imagem'],
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

    except Exception as e:
        db.rollback()
        print(f"\n❌ Erro ao popular banco de dados: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    seed_from_csv()

