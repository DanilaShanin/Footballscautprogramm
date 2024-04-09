import tkinter as tk
from model import DB

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


        self.refresh_img = tk.PhotoImage(file='refresh.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#fe4240', bd=0, image=self.refresh_img,
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        self.Logoss_img = tk.PhotoImage(file='Logoss.gif')
        btn_Logoss = tk.Button(toolbar, bg='#fe4240', bd=0, image=self.Logoss_img,
                                compound=tk.TOP, command=self.view_records)
        btn_Logoss.pack(side=tk.RIGHT)

        self.tree = ttk.Treeview(self, columns=('ID', 'Name', 'age', 'height', 'position', 'information', 'citizenship',
                                                'club', 'price', 'pace', 'shooting', 'passing','dribbling', 'defending', 'physicality')
                                 , height=15, show='headings')
        self.tree.column("ID", width=10, anchor=tk.CENTER)
        self.tree.column("Name", width=150, anchor=tk.CENTER)
        self.tree.column("age", width=55, anchor=tk.CENTER)
        self.tree.column("height", width=55, anchor=tk.CENTER)
        self.tree.column("position", width=150, anchor=tk.CENTER)
        self.tree.column("information", width=400, anchor=tk.CENTER)
        self.tree.column("citizenship", width=100, anchor=tk.CENTER)
        self.tree.column("club", width=150, anchor=tk.CENTER)
        self.tree.column("price", width=100, anchor=tk.CENTER)
        self.tree.column("pace", width=100, anchor=tk.CENTER)
        self.tree.column("shooting", width=100, anchor=tk.CENTER)
        self.tree.column("passing", width=100, anchor=tk.CENTER)
        self.tree.column("dribbling", width=100, anchor=tk.CENTER)
        self.tree.column("defending", width=100, anchor=tk.CENTER)
        self.tree.column("physicality", width=100, anchor=tk.CENTER)

        self.tree.heading("ID", text='ID')
        self.tree.heading("Name", text='Имя')
        self.tree.heading("age", text='Возраст')
        self.tree.heading("height", text='Рост')
        self.tree.heading("position", text='Позиция')
        self.tree.heading("information", text='Информация')
        self.tree.heading("citizenship", text='Гражданство')
        self.tree.heading("club", text='Клуб')
        self.tree.heading("price", text='Цена')
        self.tree.heading("pace", text='Скорость')
        self.tree.heading("shooting", text='Удар')
        self.tree.heading("passing", text='Предачи')
        self.tree.heading("dribbling", text='Дриблинг')
        self.tree.heading("defending", text='Дриблинг')
        self.tree.heading("physicality", text='Физика')






        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, name, age, height, position, information, citizenship, club, price,pace, shooting, passing, dribbling, defending, physicality):
        self.db.insert_data(name, age, height, position, information, citizenship, club, price,pace, shooting, passing, dribbling, defending, physicality)
        self.view_records()

    def update_record(self, name, age, height, position, information, citizenship, club, price,pace, shooting, passing, dribbling, defending, physicality):
        self.db.c.execute(
            '''UPDATE footballscaut SET name=?, age=?, height=?, position=?, information=?, citizenship=?, club=?, price=?,pace=?, shooting=?, passing=?, dribbling=?, defending=?, physicality=? WHERE ID=?''',
            (name, age, height, position, information, citizenship, club, price,pace, shooting, passing, dribbling, defending, physicality,
             self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM footballscaut''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

 def init_edit(self):
        self.title('Внесение изменений')
        btn_edit = ttk.Button(self, text='Изменить')
        btn_edit.place(x=200, y=500)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_name.get(),
                                                                          self.entry_age.get(),
                                                                          self.entry_height.get(),
                                                                          self.entry_position.get(),
                                                                          self.entry_information.get(),
                                                                          self.entry_citizenship.get(),
                                                                          self.entry_club.get(),
                                                                          self.entry_price.get(),
                                                                          self.entry_pace.get(),
                                                                          self.entry_shooting.get(),
                                                                          self.entry_passing.get(),
                                                                          self.entry_dribbling.get(),
                                                                          self.entry_defending.get(),
                                                                          self.entry_physicality.get()))
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
        self.entry_pace.insert(0, row[9])
        self.entry_shooting.insert(0, row[10])
        self.entry_passing.insert(0, row[11])
        self.entry_dribbling.insert(0, row[12])
        self.entry_defending.insert(0, row[13])
        self.entry_physicality.insert(0, row[14])
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("FootScaut")
    root.geometry("1400x900+300+200")
    root.resizable(True, True)
    root.mainloop()
