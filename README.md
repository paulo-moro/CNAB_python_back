# CNAB_python_back

Aplicação criada para gerenciamento de usuarios e lista de contatos. Após clonar o repositório executar os seguintes comandos:

```
docker-compose up --build ou python manage.py runserver
```

em sequencia executar as migrações dentro do docker:

```
docker exec api python manage.py migrate
```

caso seja executado local

# Windows

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
```

após iniciar a aplicação para acessar a documentação da api basta acessar o endpoint:

```
http://localhost:8000/api/schema/swagger-ui/
```
