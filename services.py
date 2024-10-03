from conexao import *
 
def enviar_dados(nome, email, senha):
    def  criar_usuario(nome, emial, senha):
        if conn.is_connected():
    
            print('Banco conectado com sucesso!')
    
            cursor = conn.cursor()
    
            sql = 'INSERT INTO usuario (nome, email, senha) values(%s,%s,%s)'
            values = (nome, email, senha)
    
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            cursor.close()
    
        else:
            print('Falha ao se conectar com o banco!')
    
        def listar_usuario():
            if conn.is_connected():
                print('Banco de dados conectado com sucesso!!!')
                cursor = conn.cursor()
    
                cursor.execute('Select id, nome, email, email from usuario;')
    
                usuarios = cursor.fetchall()
                return usuarios
            
            else:
                print('Falha ao conectar com o banco de dados!')
