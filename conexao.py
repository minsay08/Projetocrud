import mysql
import mysql.connector

conn = mysql.connector.conect(
    username= 'yasmin',
    host='localhost',
    password= 'projeto123',
    db = 'projeto_crud_yr'
)

if conn.is_connected() :
    print('Banco de dados conectado com sucesso!')
else:
    print('Não conectado com o banco!')