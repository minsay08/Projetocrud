from tkinter import *
from tkinter import ttk
import services
 
def main():
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        senha = senhaEntry.get()
        services.enviar_dados(nome, email, senha)
 
        # Para limpar os campos
 
        nomeEntry.delete(0, END)
        emailEntry.delete(0, END)
        senhaEntry.delete(0, END)
        services.enviar_dados(nome, email, senha)
 
    def deletar_user(email):
        email = emailEntry.get()
        services.remover_usuario(email)
       
 
 
 
 
    def listar_usuario():
        usuarios = services.listar_usuario()
        #criar uma janela para listar uusuario
        janela_listar = Toplevel(janela)
        janela_listar.title("lista de usuario")
        janela_listar.geometry("600x300")
 
        #criar uma Treeview (view, visualização) de lista de usuario, show= "headings" para limpar o cabesalio
        tree = ttk.Treeview(janela_listar, colums=("ID", "Nome", "Email"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("nome", text="Nome")
        tree.heading("Email", text="Email")
 
        #criar botao de voltar que ira fechar a tela de listar usuario
        voltar_botao = Button(janela_listar, text="voltar" , width=10, command=janela_listar.destroy)
        voltar_botao.pack(fill=BOTH, expand=True, side=BOTTOM)
 
        tree.pack(fill=BOTH, expand=True)
 
        #inserir os dados dos usuarios sa treeview
        for usuario in usuarios:
            #END vai inserir o iten no final da tabela
            tree.insert("", END, values=usuario)
 
 
    janela = Tk()
    janela.geometry('400x300')
    janela.title('Sistema de Gerenciamento de Usuário')
 
 
    titulo = Label(janela, text='CRUD', font=('Arial', 20))
    titulo.pack(pady=30)
 
    # Componentes de entrada
    # Nome
    nome = Label(janela, text='Nome:')
    nome.place(x=50, y=100)
 
    global nomeEntry
    nomeEntry = Entry(janela, width=30)
    nomeEntry.place(x=100, y=100)
 
    # Email
    email = Label(janela, text='Email:')
    email.place(x=50, y=130)
 
    global emailEntry
    emailEntry = Entry(janela, width=30)
    emailEntry.place(x=100, y=100)
 
    # Senha
    senha = Label(janela, text='Senha:')
    senha.place(x=50, y=160)
 
    # comando shor para esconder a senha
    global senhaEntry
    senhaEntry = Entry(janela, width=30, show='*')
    senhaEntry.place(x=50, y=160)
 
 
    enviar = Button(janela, text='Cadastrar', width=10, command=on_enviar)
    enviar.place(x=100, y=200)
 
    listar = Button(janela, text ='Listar Usuarios', width=10, command=listar_usuario())
    listar.place(x=200, y=200)
 
    janela.mainloop()
 
if __name__== '__main__':
    main()
    
