from tinydb import TinyDB, Query

# Inicialização dos bancos de dados na pasta `data`
db = TinyDB('data/db.json')
db_funcionarios = TinyDB('data/funcionarios.json')

# Definição das consultas com `Query`
Cliente = Query()
Funcionario = Query()
Pousada = Query()
Reserva = Query()
