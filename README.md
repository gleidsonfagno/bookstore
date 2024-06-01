# Bookstore

bookstore app

## criar um anbiente virtual

- 1 verifique as permisoes

```shell
Set-ExecutionPolicy RemoteSigned

```

- bra o PowerShell como administrador.
- Execute o seguinte comando para verificar a política de execução atual:

```shell
Get-ExecutionPolicy
```

- Se a política estiver definida como “Restricted”, você precisará alterá-la para permitir a execução de scripts.
- Para permitir a execução de scripts, execute o seguinte comando:

```shell
Set-ExecutionPolicy RemoteSigned

# S = para [sim]
```

- 2 Crie o abinte vitual

## Criando um anbiente virtual

```shell
python -m venv env

# executar o anbiente virtual
./env\Scripts\activate.ps1

```

## imstalar o poetry dentro do anbiente virtual

```shell
pip install poetry

poetry --version

poetry init

pytest instalado
factory-boy instalado

poetry add django

# fica no mesmo diretorio
poetry run django-admin startproject bookstore .

```

## Rodando Projetos em Django

```shell
poetry run python manage.py startapp api

poetry run python manage.py migrate

# verificar se o serve esta rodando 
poetry run python manage.py runserver

```

## O que é Serializers em Django Rest Framework?

Como integrar Django Models e Django Serializers

```shell
poetry run python manage.py startapp order

poetry run python manage.py startapp product
```

## Migrando Django Models

- declarar os modelos de admin.py de cada aplicativo
- dentro d o ``__init__.py``
- declara os nossos app (product e order) dentro do bookstore project (settings.py)
- deletar os models.py porque ja criamos um diretorio

***comando para gerencia os modulos***

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

Criando Serializers em Django
instalar

```bash
poetry add django-rest-framework
```

Criando Serializers em Django

### Resumo Exercício

1 Para o teste app `product`

```bash
python manage.py test order.tests.test_serializers
```

2 Pra o testes do app `order`

```bash
python manage.py test order.tests.test_serializers
```

Nesse exercício vamos construir nossos serializers baseado nos nossos modelos, além disso vamos construir testes unitários para garantir a qualidade dos nosso código.

Crie um PR e envie o link na plataforma da EBAC.

## ViewSets para alteração de dados