from tkinter import Tk, Label, Entry, Button, Frame
from tkinter import ttk, PhotoImage


class App:
    def __init__(self, window):
        self.window = window
        self.window.title('Sistema Aduaneiro')
        self.window.config(padx=50,pady=25)
        self.window.iconphoto(False, PhotoImage(file='images/navio.png'))
        self.window.geometry("1200x400+100+100")

        Label(window, text='ID').grid(row=0, column=0, sticky='w')
        self.id_entry = Entry(window)
        self.id_entry.grid(row=0, column=1, pady=0)

        Label(window, text='TIPO').grid(row=1, column=0, sticky='w')
        self.tipo_entry = Entry(window)
        self.tipo_entry.grid(row=1, column=1)

        Label(window, text='STATUS').grid(row=2, column=0, sticky='w')
        self.status_entry = Entry(window)
        self.status_entry.grid(row=2, column=1)

        Label(window, text='DESCRIÇÃO').grid(row=3, column=0, sticky='w')
        self.descricao_entry = Entry(window)
        self.descricao_entry.grid(row=3, column=1)

        add_button = Button(window, text='Adicionar', command=self.add_data)
        add_button.grid(row=4, columnspan=2)

        self.tree = ttk.Treeview(window, columns=('ID', 'Tipo', 'Status', 'Descrição'), show='headings')
        self.tree.grid(row=0, column=2, rowspan=5, padx=10)

        self.tree.heading('ID', text='ID')
        self.tree.heading('Tipo', text='Tipo')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Descrição', text='Descrição')

    def add_data(self):
        id_value = self.id_entry.get()
        tipo_value = self.tipo_entry.get()
        status_value = self.status_entry.get()
        descricao_value = self.descricao_entry.get()

        self.tree.insert('', 'end', values=(id_value, tipo_value, status_value, descricao_value))

        self.id_entry.delete(0, 'end')
        self.tipo_entry.delete(0, 'end')
        self.status_entry.delete(0, 'end')
        self.descricao_entry.delete(0, 'end')

window = Tk()
app = App(window)
window.mainloop()