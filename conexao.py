import mysql
import mysql.connector

conn = mysql.connector.connect(
    user= 'yasmin',
    host='localhost',
    password= 'projeto123',
    database = 'projeto_crud'
)

if conn.is_connected() :
    print('Banco de dados conectado com sucesso!')
else:
    print('Não conectado com o banco!')