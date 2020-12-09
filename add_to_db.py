from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("C:\CalcularIMC\Database\pacientes.db")
c = conn.cursor()

result = c.execute("SELECT MAX(id) from pacientes")
for r in result:
    id = r[0]

class Database:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.heading = Label(master, text="Calculo de IMC",font=('arial 40 bold'))
        self.heading.place(x=400, y=0)

        self.nome = Label(master, text="Nome do Paciente: ",font=('arial 18 bold'))
        self.nome.place(x=0, y=70)

        self.altura = Label(master, text="Altura: ",font=('arial 18 bold'))
        self.altura.place(x=0, y=140)

        self.peso = Label(master, text="Peso: ",font=('arial 18 bold'))
        self.peso.place(x=0, y=220)

        self.nome_e = Entry(master, width = 25, font=('arial 18 bold'))
        self.nome_e.place(x=380, y=70)

        self.altura_e = Entry(master, width = 25, font=('arial 18 bold'))
        self.altura_e.place(x=380, y=140)

        self.peso_e = Entry(master, width = 25, font=('arial 18 bold'))
        self.peso_e.place(x=380, y=220)

        self.btn_add = Button(master, text="Calcular", width = 25, height=2, bg='steelblue', fg='white',  font=('arial 18 bold'), command=self.get_items)
        self.btn_add.place(x=520, y=420)

        self.tBox = Text(master, width = 60, height=18,)
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, "Ultimo Cadastro ID: ")

        

    def get_items(self, master, *args, **kwars):
        self.nome = self.nome_e.get()
        self.altura = self.altura_e.get()
        self.peso = self.peso_e.get()
        
        self.imc = float(self.peso) / float(self.altura ** 2)

        if self.nome =='' or self.peso =='' or self.altura =='':
            tkinter.messagebox.showinfo("Atenção", "Favor preencher todos os campos.!")
        else:
            sql = "INSERT INTO pacientes(nome, altura, peso, imc) VALUES(?,?,?,?)"
            c.execute(sql,(self.nome, self.altura, self.peso, self.imc))
            conn.commit()

            self.tBox.insert(END, "\n\nCadastro", str(self.nome) + str(self.imc))

            tkinter.messagebox.showinfo("Atenção", "IMC Calculado.!")


root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Calcular IMC")
root.mainloop()