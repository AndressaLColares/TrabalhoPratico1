# TrabalhoPratico1# Trabalho Prático 1 - Desenvolvimento de uma API REST para Gerenciamento de Entidades com Persistência em CSV com FastAPI

## Descrição Geral

Neste trabalho, foi desenvolvida uma aplicação web simples que utiliza uma API REST criada com o framework FastAPI. A API tem como objetivo gerenciar entidades relacionadas ao domínio escolhido no Trabalho Prático 1 (TP1). A principal funcionalidade da aplicação é permitir a manipulação de dados armazenados em arquivos CSV, com operações como leitura, escrita, atualização e exclusão de registros.

Além disso, funcionalidades extras foram implementadas para simular um cenário de aplicação real, incluindo:

- **Compactação de arquivos**: Permitindo a redução do tamanho dos dados armazenados.
- **Cálculo de hash**: Para garantir a integridade e segurança dos dados manipulados.
- **Logging (registro de operações)**: Para manter um histórico das ações realizadas na API, proporcionando maior controle e usabilidade.

## Objetivo

O objetivo principal desse trabalho foi praticar o desenvolvimento de APIs REST em Python, utilizando o framework FastAPI, além de explorar o uso de arquivos CSV para persistência de dados. Também foram abordadas funcionalidades adicionais que aumentam a robustez e a segurança da aplicação.

## Equipe

- **Andressa Colares - 471151**
- **Carlos Ryan Santos**

## Cadeira

- **Desenvolvimento de Software para Persistência**

## Professor

- **Prof. Francisco Victor da Silva Pinheiro**

## Tecnologias Utilizadas

- **FastAPI**: Framework utilizado para criação da API REST.
- **CSV**: Arquivo de persistência dos dados.
- **Python**: Linguagem de programação utilizada para o desenvolvimento da API.
- **Logging**: Registro das operações realizadas na API.
- **Hashlib**: Utilizado para geração de hashes de dados.
- **Zipfile**: Para compactação de arquivos.

## Funcionalidades

- **CRUD Completo**: Criar, ler, atualizar e excluir entidades.
- **Armazenamento em CSV**: Persistência dos dados em arquivos CSV.
- **Compactação de Arquivos**: Compressão dos arquivos de dados para economia de espaço.
- **Cálculo de Hash**: Geração de hash para cada registro, garantindo a integridade dos dados.
- **Logging**: Registro de todas as operações realizadas na API para análise posterior.

## Como Rodar a Aplicação

### Pré-requisitos

Certifique-se de ter o Python 3.8 ou superior instalado em sua máquina.

### Instalação

1. Clone o repositório:

    ```bash
    git clone git@github.com:AndressaLColares/TrabalhoPratico1.git
    ```

2. Instale as dependências:

    ```bash
    cd app
    pip install -r requirements.txt
    ```

### Execução

Para rodar a API localmente, execute o seguinte comando:

```bash
python -m uvicorn main:app --reload
