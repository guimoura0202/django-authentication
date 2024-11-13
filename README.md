# Django Authentication Project

Fiz basicamente uma configuração inicial de um sistema de autenticação usando Django. 

## Estrutura do Projeto

- **authentication/**: Pasta principal do projeto Django.
- **auth_site/**: Aplicativo Django para gerenciar autenticação de usuários.
- **manage.py**: Arquivo principal de gerenciamento do Django.

## Explicação
- Criei, clonei e entrei no repositório;
- Criei as variáveis de ambiente com `python -m venv venv` e logo em seguida ativei elas com `venv\Scripts\activate`
- Instalei Django na minha venv e dei um `pip freeze > requirements.txt` pra puxar todas as dependências
- Executei `django-admin startproject authentication . ` e `python manage.py startapp auth_site ` pra criar o projeto e o app, respectivamente