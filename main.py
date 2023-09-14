from tkinter import *

#importar caixas de mensagem
from tkinter import  messagebox


def enviar() -> None:
    nome = txt_nome.get()
    messagebox.showinfo("ENVIADO!",f"Bem vindo {nome}")
#Como apágar algo de um campo
    txt_nome.delete(0,END)


# Como criar uma tela

janela = Tk()

#como alterar o tamanho da janela (Altura x largura)
janela.geometry("350x280")

#como colocar titulo
janela.title("ola mundo")

#criando um label
label_nome = Label(
    janela,
    text="nome: ",
    foreground="blue",
    font="Tahoma 14 bold")

#Adicionando componente com grid
label_nome.grid(
    row=0,
    column=0
)


#Adicionar campo de texto

txt_nome = Entry(janela,font="Tahoma 14", width=25)

txt_nome.grid(row=0,column=1)

#adicionando botão

btn_enviar = Button(
    janela,
    text="enviar",
    background="red",
    foreground="white",
    font="Tahoma 14 bold",
    width=8,
    command=enviar
)

btn_enviar.grid(row=1,column=0)


#função que mantem a janela no S.O. (precisa ficar no fim do codigo,pois e ela que executa)
janela.mainloop()


