# Aps 2 Back - End Unisenai

## API de Eventos Acadêmicos

## API RESTful desenvolvida em Python utilizando FastAPI para gerenciamento de eventos acadêmicos, participantes e inscrições.

# 🛠️ Tecnologias

Python

FastAPI

Pydantic

Uvicorn

# 📦 Instalação

Clone ou baixe o projeto e entre na pasta.

Instale as dependências:

pip install -r requirements.txt

# ▶️ Executando o projeto

Execute o seguinte comando:

uvicorn main:app --reload

# 📚 Swagger

A documentação da API é disponibilizada automaticamente pelo FastAPI.

Após iniciar o projeto, acesse:

http://127.0.0.1:8000/docs


No Swagger é possível visualizar e testar todas as rotas da API.

# 📌 Funcionalidades
## 📅 Eventos

Cadastrar evento

Listar eventos

Consultar evento

Atualizar evento

Excluir evento

# 👤 Participantes

Cadastrar participante

Listar participantes

Consultar participante

Atualizar participante

Excluir participante

# 📝 Inscrições

Inscrever participante em evento

Consultar participantes inscritos

Verificar disponibilidade de vagas

Impedir inscrições duplicadas

# ✅ Validações

A API possui validações para os dados enviados, como:

Campos obrigatórios

E-mail válido

Capacidade maior que zero

Data válida

Campos de texto não vazios

# ⚠️ Tratamento de erros

A API trata situações como:

Evento não encontrado

Participante não encontrado

Participante já inscrito

Evento sem vagas

Dados inválidos

# 📁 Estrutura do projeto

O projeto utiliza uma separação baseada em MVC:

controller — responsável pelas rotas da API

model — responsável pelos modelos e validações

service — responsável pelas regras de negócio

main.py — responsável pela inicialização da aplicação

# 💾 Armazenamento

Os dados são armazenados em memória, utilizando estruturas do Python.

Não é utilizado banco de dados nesta versão do projeto.
