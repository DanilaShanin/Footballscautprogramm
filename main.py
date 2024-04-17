import tkinter as tk
from tkinter import ttk
import sqlite3
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np



class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#fe4240', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="add.gif")
        btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#fe4240', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='update.gif')
        btn_edit_dialog = tk.Button(toolbar, text='Изменить', bg='#fe4240', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='delete.gif')
        btn_delete = tk.Button(toolbar, text='Удалить игрока', bg='#fe4240', bd=0, image=self.delete_img,
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='search.gif')
        btn_search = tk.Button(toolbar, text='Поиск', bg='#fe4240', bd=0, image=self.search_img,
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        self.wether_img = tk.PhotoImage(file='wether.gif')
        btn_wether = tk.Button(toolbar, text='Погода', bg='#fe4240', bd=0, image=self.wether_img,
                                compound=tk.TOP, command=self.view_records)
        btn_wether.pack(side=tk.LEFT)

        self.money_img = tk.PhotoImage(file='money.gif')
        btn_money = tk.Button(toolbar, text='Валюта', bg='#fe4240', bd=0, image=self.money_img,
                                compound=tk.TOP, command=self.view_records)
        btn_money.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#fe4240', bd=0, image=self.refresh_img,
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        self.Logoss_img = tk.PhotoImage(file='Logoss.gif')
        btn_Logoss = tk.Button(toolbar, bg='#fe4240', bd=0, image=self.Logoss_img,
                                compound=tk.TOP, command=self.view_records)
        btn_Logoss.pack(side=tk.RIGHT)

        self.tree = ttk.Treeview(self, columns=('ID', 'Name', 'age', 'height', 'position', 'information', 'citizenship',
                                                'club', 'price')
                                 , height=15, show='headings')
        self.tree.column("ID", width=10, anchor=tk.CENTER)
        self.tree.column("Name", width=150, anchor=tk.CENTER)
        self.tree.column("age", width=55, anchor=tk.CENTER)
        self.tree.column("height", width=55, anchor=tk.CENTER)
        self.tree.column("position", width=150, anchor=tk.CENTER)
        self.tree.column("information", width=400, anchor=tk.CENTER)
        self.tree.column("citizenship", width=200, anchor=tk.CENTER)
        self.tree.column("club", width=150, anchor=tk.CENTER)
        self.tree.column("price", width=100, anchor=tk.CENTER)

        self.tree.heading("ID", text='ID')
        self.tree.heading("Name", text='Имя')
        self.tree.heading("age", text='Возраст')
        self.tree.heading("height", text='Рост')
        self.tree.heading("position", text='Позиция')
        self.tree.heading("information", text='Информация')
        self.tree.heading("citizenship", text='Гражданство')
        self.tree.heading("club", text='Клуб')
        self.tree.heading("price", text='Цена')

        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, name, age, height, position, information, citizenship, club, price):
        self.db.insert_data(name, age, height, position, information, citizenship, club, price)
        self.view_records()

    def update_record(self, name, age, height, position, information, citizenship, club, price):
        self.db.c.execute(
            '''UPDATE footballscaut SET name=?, age=?, height=?, position=?, information=?, citizenship=?, club=?, price=? WHERE ID=?''',
            (name, age, height, position, information, citizenship, club, price,
             self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM footballscaut''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM footballscaut WHERE id=?''', [self.tree.set(selection_item,
                                                                                         '#1')])
        self.db.conn.commit()
        self.view_records()

    def search_records(self, name):
        name = ('%' + name + '%',)
        self.db.c.execute('''SELECT * FROM footballscaut WHERE name LIKE ?''', name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('1000x1000+400+300')
        #self.resizable(False, False)

        label_name = tk.Label(self, text='Имя:')
        label_name.place(x=100, y=25)
        label_age = tk.Label(self, text='Возраст:')
        label_age.place(x=100, y=50)
        label_height = tk.Label(self, text='Рост:')
        label_height.place(x=100, y=75)
        label_position = tk.Label(self, text='Позиция')
        label_position.place(x=100, y=100)
        label_information = tk.Label(self, text='Информация:')
        label_information.place(x=100, y=125)
        label_citizenship = tk.Label(self, text='Гражданство:')
        label_citizenship.place(x=100, y=150)
        label_club = tk.Label(self, text='Клуб:')
        label_club.place(x=100, y=175)
        label_price = tk.Label(self, text='Цена:')
        label_price.place(x=100, y=200)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=25)

        self.entry_age = ttk.Entry(self)
        self.entry_age.place(x=200, y=50)

        self.entry_height = ttk.Entry(self)
        self.entry_height.place(x=200, y=75)

        self.entry_position = ttk.Entry(self)
        self.entry_position.place(x=200, y=100)

        self.entry_information = ttk.Entry(self)
        self.entry_information.place(x=200, y=125)

        self.entry_citizenship = ttk.Entry(self)
        self.entry_citizenship.place(x=200, y=150)

        self.entry_club = ttk.Entry(self)
        self.entry_club.place(x=200, y=175)

        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=200, y=200)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111, projection='polar')


        labels = ["Лень", "Аскетизм", "Высокомерие", "Коварство", "Мания величия", "Невежество"]



        r = [100, 7, 9, 6, 1, 8]
        theta = np.deg2rad(np.linspace(0, 360, 7))
        a.axes.set_xticklabels(labels)

        a.axes.set_xticks(theta)
        a.axes.plot(theta, self._get_r(r), color='black')



        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=300)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=200, y=300)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_name.get(), self.entry_age.get(),
                                                                       self.entry_height.get(),
                                                                       self.entry_position.get(),
                                                                       self.entry_information.get(),
                                                                       self.entry_citizenship.get(),
                                                                       self.entry_club.get(),
                                                                       self.entry_price.get()))

        self.grab_set()
        self.focus_set()
    def _get_r(self, r):
        return [*r, r[0]]
class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Внесение изменений')
        btn_edit = ttk.Button(self, text='Изменить')
        btn_edit.place(x=200, y=300)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_name.get(),
                                                                          self.entry_age.get(),
                                                                          self.entry_height.get(),
                                                                          self.entry_position.get(),
                                                                          self.entry_information.get(),
                                                                          self.entry_citizenship.get(),
                                                                          self.entry_club.get(),
                                                                          self.entry_price.get()))
        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM footballscaut WHERE id=?''',
                          (self.view.tree.set(self.view.tree.selection()[0], '#1'),))
        row = self.db.c.fetchone()
        self.entry_name.insert(0, row[1])
        self.entry_age.insert(0, row[2])
        self.entry_height.insert(0, row[3])
        self.entry_position.insert(0, row[4])
        self.entry_information.insert(0, row[5])
        self.entry_citizenship.insert(0, row[6])
        self.entry_club.insert(0, row[7])
        self.entry_price.insert(0, row[8])


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск игрока')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=200)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('footballscaut.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS footballscaut (id integer primary key, name text, age text, height text,
            position text, information text, citizenship text, club text, price text)''')
        self.conn.commit()

    def insert_data(self, name, age, height, position, information, citizenship, club, price):
        self.c.execute('''INSERT INTO footballscaut (name, age, height, position, 
        information, citizenship, club, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (name, age, height, position, information, citizenship, club, price))
        self.conn.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("FootScaut")
    root.geometry("1400x900+300+200")
    root.resizable(True, True)
    root.mainloop()
