# CNAB_python_back

Aplicação criada para gerenciamento de usuarios e lista de contatos. Após clonar o repositório executar os seguintes comandos:

```
docker-compose up --build ou python manage.py runserver
```

## Docker :

Na primeira vez que realizar o docker-compose up, em outra janela do temrinal executar:

```
docker exec cnab_python_back_web_1 python manage.py loaddata type.json
```

Migrações já foram executadas durante o build do docker, esse comando acima é para já carregar todos os 'types' pré cadastrados, existem views para criação de novos types de transação mas a principio 9 já são pre cadastrados.

## Local

### Windows

Se for executar o runserver localmente, na primeira vez é necessário executar antes :

no CNAB_bank/setting.py, modificar o Host para o local:

```
 DATABASE = {
    ...
    "HOST": "127.0.0.1",
    ...
 }
```

no terminal :

```
python manage.py migrate
```

Instalação das bibliotecas:

```
pip install requirements.txt
```

libs utilizadas:

```
* Django-rest-framework
* bcryptjs
* drf-espetacular
* black
* ipython
* ipdb
* django-cors-headers
* django-filter
```

após iniciar a aplicação para acessar a documentação da api basta acessar o endpoint:

```
http://localhost:8000/api/schema/swagger-ui/
```
