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
