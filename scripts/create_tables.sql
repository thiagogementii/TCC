-- SQL para criar as tabelas manualmente

-- Criar tabela marcas
CREATE TABLE IF NOT EXISTS marcas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL UNIQUE,
    slug VARCHAR NOT NULL UNIQUE,
    logo VARCHAR,
    quantidade INTEGER DEFAULT 0
);

-- Criar tabela carros
CREATE TABLE IF NOT EXISTS carros (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    "marcaId" INTEGER NOT NULL REFERENCES marcas(id),
    ano INTEGER NOT NULL,
    preco NUMERIC(10, 2) NOT NULL,
    km INTEGER NOT NULL,
    transmissao VARCHAR NOT NULL,
    imagem VARCHAR,
    descricao TEXT
);

-- Criar índices
CREATE INDEX IF NOT EXISTS idx_carros_marcaid ON carros("marcaId");

