# django
 Project for the purposes of studying the Django framework

Como rodar localmente:
- Pegar o arquivo `local_sentting.py.example` colocar dentro da pasta djangoecommerce
- Rodar o comando `./manage.py migrate` criar tabelas.
- Quando houver mudanças nas tabelas rodar `./manage.py makemigrations`

#### Comando para configurar o ambiente
```
django-admin startproject djangoecommerce .
```

#### Comando para rodar o servidor
```
./manage.py runserver
```

#### Comando para criar path no padrao MVC
```
python3 manage.py startapp "nomedapasta"
```

#### Comando para rodar testes
```
./manage.py test
```

#### Comando para criar um usuário adm
```
./manage.py createsuperuser
```
