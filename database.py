from pymongo import MongoClient
from bson import objectid

# cluster para conexão local com o mongoDB
cluster = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

client = MongoClient(cluster)

# Testando a conexão local com o mongoDB
print(client.list_database_names())

# Conectando ao database do projeto
db = client.ac

# Testando a conexão com o database do projeto
print(db.list_collection_names())

# Criando uma colection para testes
pessoa = {
    "nome": "Daniel Figueroa",
    "sexo": "Masculino",
    "endereco": "Avenida Brasil",
    "dataNascimento": "1988-01-03",
    "indicador": [{"nome": "João"}],
    "email": "daniel@gmail.com",
    "telefone": "73999998888"
}

# Conectando com a colection do projeto no mongoDB
dadosPessoas = db.dadosPessoas

### Iniciando o CRUD

# Create -  insert_one, insert_many
#cadastrar = dadosPessoas.insert_one(pessoa)

# Read - find, find_one
listar = dadosPessoas.find_one({"indicador": [{"nome": "João"}]})

print(listar)

# Update - update_one, update_many

# Delete - remove, remove_one, delete_many