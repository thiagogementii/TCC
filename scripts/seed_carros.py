"""Seed script para inserir marcas e carros na base de dados.

Observações:
- Este arquivo NÃO executa inserções ao ser importado; rode-o diretamente:
    python scripts/seed_carros.py
- Revise `DATABASE_URL` em `.env` antes de executar para evitar inserir em um banco errado.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from decimal import Decimal
from app.core.database import SessionLocal, engine, Base
from app.models.marca_model import Marca
from app.models.carro_model import Carro


MARCAS = [
    {
        "nome": "Toyota",
        "slug": "toyota",
        "logo": "https://logo.clearbit.com/toyota.com",
        "quantidade": 0
    },
    {
        "nome": "Honda",
        "slug": "honda",
        "logo": "https://logo.clearbit.com/honda.com",
        "quantidade": 0
    },
    {
        "nome": "Volkswagen",
        "slug": "volkswagen",
        "logo": "https://logo.clearbit.com/vw.com",
        "quantidade": 0
    },
    {
        "nome": "Fiat",
        "slug": "fiat",
        "logo": "https://logo.clearbit.com/fiat.com",
        "quantidade": 0
    },
    {
        "nome": "Chevrolet",
        "slug": "chevrolet",
        "logo": "https://logo.clearbit.com/chevrolet.com",
        "quantidade": 0
    },
    {
        "nome": "Hyundai",
        "slug": "hyundai",
        "logo": "https://logo.clearbit.com/hyundai.com",
        "quantidade": 0
    },
    {
        "nome": "Nissan",
        "slug": "nissan",
        "logo": "https://logo.clearbit.com/nissan.com",
        "quantidade": 0
    },
    {
        "nome": "Jeep",
        "slug": "jeep",
        "logo": "https://logo.clearbit.com/jeep.com",
        "quantidade": 0
    },
    {
        "nome": "Renault",
        "slug": "renault",
        "logo": "https://logo.clearbit.com/renault.com",
        "quantidade": 0
    },
    {
        "nome": "Peugeot",
        "slug": "peugeot",
        "logo": "https://logo.clearbit.com/peugeot.com",
        "quantidade": 0
    },
]

# Carros com a estrutura simplificada
CARROS = [
    {
        "nome": "Corolla Altis",
        "marca_nome": "Toyota",
        "ano": 2024,
        "preco": Decimal("160000.00"),
        "km": 8500,
        "transmissao": "Automático",
        "imagem": "https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=800&q=80",
        "descricao": "Veículo zero km, com ar-condicionado digital, central multimídia com tela de 9 polegadas, sistema de som premium, câmera de ré, sensores de estacionamento, piloto automático adaptativo, faróis full LED, bancos em couro legítimo e pacote completo de assistências à condução. Estado impecável, ainda na garantia de fábrica.",
    },
    {
        "nome": "Civic Touring",
        "marca_nome": "Honda",
        "ano": 2023,
        "preco": Decimal("170000.00"),
        "km": 25000,
        "transmissao": "Automático",
        "imagem": "https://images.unsplash.com/photo-1590362891991-f776e747a588?w=800&q=80",
        "descricao": "Seminovo em excelente estado, único dono. Equipado com motor turbo de alto desempenho, câmbio CVT, teto solar panorâmico, sistema Honda Sensing completo (controle de cruzeiro adaptativo, assistente de permanência em faixa), bancos em couro com aquecimento, retrovisores rebatíveis automaticamente, e sistema multimídia com Apple CarPlay e Android Auto. Manutenções em dia na concessionária.",
    },
    {
        "nome": "T-Cross Highline",
        "marca_nome": "Volkswagen",
        "ano": 2024,
        "preco": Decimal("150000.00"),
        "km": 12000,
        "transmissao": "Automático",
        "imagem": "https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?w=800&q=80",
        "descricao": "SUV compacto praticamente zero, com apenas um ano de uso. Possui teto solar elétrico, rodas de liga leve diamantadas, central multimídia VW Play de 10 polegadas, ar-condicionado automático dual zone, câmera 360 graus, sensores dianteiros e traseiros, faróis e lanternas full LED, bancos revestidos em material premium e porta-malas amplo. Revisões feitas na concessionária autorizada.",
    },
    {
        "nome": "Pulse Abarth",
        "marca_nome": "Fiat",
        "ano": 2024,
        "preco": Decimal("135000.00"),
        "km": 6800,
        "transmissao": "Automático",
        "imagem": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800&q=80",
        "descricao": "Versão esportiva Abarth praticamente nova, com visual agressivo e alto desempenho. Equipado com rodas aro 18 exclusivas, suspensão esportiva rebaixada, bancos Sabelt com revestimento esportivo, câmbio CVT com modo manual, painel digital de 7 polegadas, central multimídia de 10.1 polegadas, som Beats, teto solar, e sistema ADAS completo. Perfeito estado de conservação.",
    },
    {
        "nome": "Onix Premier",
        "marca_nome": "Chevrolet",
        "ano": 2023,
        "preco": Decimal("100000.00"),
        "km": 18500,
        "transmissao": "Automático",
        "imagem": "https://images.unsplash.com/photo-1583267746897-c2b15c34ab18?w=800&q=80",
        "descricao": "Hatch premium em ótimo estado, único dono com baixa quilometragem. Conta com motor turbo eficiente, ar-condicionado digital automático, central multimídia MyLink de 8 polegadas com conectividade wireless, câmera de ré com linhas dinâmicas, sensor de estacionamento traseiro, controle de cruzeiro, volante multifuncional revestido em couro, rodas de liga leve e acabamento interno sofisticado. Nunca bateu.",
    },
    {
        "nome": "Creta Platinum",
        "marca_nome": "Hyundai",
        "ano": 2024,
        "preco": Decimal("145000.00"),
        "km": 9200,
        "transmissao": "Automático",
        "imagem": "https://images.unsplash.com/photo-1609521263047-f8f205293f24?w=800&q=80",
        "descricao": "SUV top de linha quase zero, com todos os opcionais de série. Possui teto solar panorâmico, central multimídia Bluelink de 10.25 polegadas, painel digital de 10.25 polegadas, carregador wireless para smartphone, ar-condicionado digital dual zone, sistema de som Bose premium, SmartSense (pacote de segurança avançado), faróis e lanternas full LED, bancos em couro Nappa com ventilação e aquecimento. Estado de showroom.",
    },
    {
        "nome": "Versa Exclusive",
        "marca_nome": "Nissan",
        "ano": 2023,
        "preco": Decimal("110000.00"),
        "km": 22000,
        "transmissao": "Automático",
        "imagem": "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?w=800&q=80",
        "descricao": "Sedan compacto bem conservado com baixa quilometragem. Equipado com central multimídia de 8 polegadas integrada com Apple CarPlay e Android Auto, ar-condicionado automático, controle de estabilidade e tração, câmera de ré, sensores traseiros, direção elétrica progressiva, bancos em tecido premium com ajustes múltiplos. Interior espaçoso e confortável, ideal para família. Todas as revisões em dia.",
    },
    {
        "nome": "Compass Limited",
        "marca_nome": "Jeep",
        "ano": 2024,
        "preco": Decimal("200000.00"),
        "km": 11500,
        "transmissao": "Automático",
        "imagem": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=800&q=80",
        "descricao": "SUV médio robusto e sofisticado, praticamente novo. Versão turbodiesel com tração 4x4, equipada com bancos em couro premium com costuras contrastantes, teto solar panorâmico comando de voz, sistema Uconnect de última geração com tela de 10.1 polegadas, painel digital personalizável de 10.25 polegadas, carregamento wireless, ar tri-zone, faróis full LED adaptativos, rodas aro 19, e pacote completo de segurança ativa. Veículo impecável.",
    },
    {
        "nome": "Kwid Zen",
        "marca_nome": "Renault",
        "ano": 2023,
        "preco": Decimal("70000.00"),
        "km": 28000,
        "transmissao": "Manual",
        "imagem": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800&q=80",
        "descricao": "Compacto econômico em ótimo estado de conservação. Perfeito para uso urbano, conta com ar-condicionado, direção elétrica, vidros e travas elétricas, central multimídia Media Evolution com tela de 8 polegadas, conectividade com smartphone, computador de bordo, sensor de estacionamento traseiro, e design moderno com grade frontal cromada. Motor 1.0 extremamente econômico. Pintura sem defeitos, pneus em bom estado.",
    },
    {
        "nome": "208 Griffe",
        "marca_nome": "Peugeot",
        "ano": 2024,
        "preco": Decimal("95000.00"),
        "km": 7500,
        "transmissao": "Automático",
        "imagem": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&q=80",
        "descricao": "Hatch premium com design diferenciado e tecnologia de ponta. Equipado com i-Cockpit 3D (painel digital tridimensional de 10 polegadas), central multimídia de 10 polegadas com navegação GPS, teto panorâmico em vidro, ar-condicionado automático digital, bancos com revestimento TEP (aspecto couro), rodas de liga leve diamantadas aro 17, faróis full LED com assinatura luminosa, e sistema de frenagem autônoma de emergência. Veículo seminovo em estado de zero.",
    },
]


def run():
    """Insere marcas e carros no banco. Use com cuidado."""
    # Debug: imprimir a DATABASE_URL
    import os
    print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")

    # Cria tabelas se necessário
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # Limpar tabelas existentes (opcional)
        print("Limpando dados existentes...")
        db.query(Carro).delete()
        db.query(Marca).delete()
        db.commit()

        # Inserir marcas
        print("Inserindo marcas...")
        marcas_dict = {}
        for m in MARCAS:
            marca = Marca(**m)
            db.add(marca)
            db.flush()  # Para obter o ID
            marcas_dict[m["nome"]] = marca.id

        db.commit()
        print(f"✓ Inseridas {len(MARCAS)} marcas com sucesso.")

        # Inserir carros
        print("Inserindo carros...")
        for c in CARROS:
            marca_nome = c.pop("marca_nome")
            carro_data = {
                **c,
                "marcaId": marcas_dict[marca_nome]
            }
            carro = Carro(**carro_data)
            db.add(carro)

        db.commit()

        # Atualizar quantidade de carros por marca
        print("Atualizando contagem de marcas...")
        for marca_id in marcas_dict.values():
            count = db.query(Carro).filter(Carro.marcaId == marca_id).count()
            db.query(Marca).filter(Marca.id == marca_id).update({"quantidade": count})

        db.commit()
        print(f"✓ Inseridos {len(CARROS)} carros com sucesso.")
        print("✓ Seed concluído!")

    except Exception as e:
        db.rollback()
        print("✗ Erro ao inserir dados:", e)
        import traceback
        traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    run()
