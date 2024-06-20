import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from model import DB

db = DB()
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#fe4240', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="img/add.gif")
        btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#fe4240', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='img/update.gif')
        btn_edit_dialog = tk.Button(toolbar, text='Изменить', bg='#fe4240', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='img/delete.gif')
        btn_delete = tk.Button(toolbar, text='Удалить игрока', bg='#fe4240', bd=0, image=self.delete_img,
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='img/search.gif')
        btn_search = tk.Button(toolbar, text='Поиск по имени', bg='#fe4240', bd=0, image=self.search_img,
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='img/refresh.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#fe4240', bd=0, image=self.refresh_img,
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        # self.Logoss_img = tk.PhotoImage(file='Logoss.gif')
        # btn_Logoss = tk.Button(toolbar, bg='#fe4240', bd=0, image=self.Logoss_img, compound=tk.TOP, command=self.view_records)
        # btn_Logoss.pack(side=tk.RIGHT)

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

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM footballscaut WHERE id=?''', [self.tree.set(selection_item,
                                                                                         '#1')])
        self.db.conn.commit()
        self.view_records()

    def search_records(self, name):
        name = ('%' + name + '%',)
        self.db.c.execute('''SELECT * FROM footballscaut WHERE name || 
        age ||
        height || 
        position || 
        information || 
        citizenship || 
        club || 
        price || 
        pace || 
        shooting || 
        passing || 
        dribbling || 
        defending || 
        physicality LIKE ?''', name)
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
        label_pace = tk.Label(self, text='Скорость:')
        label_pace.place(x=100, y=225)
        label_shooting = tk.Label(self, text='Удар:')
        label_shooting.place(x=100, y=250)
        label_passing = tk.Label(self, text='Передачи:')
        label_passing.place(x=100, y=275)
        label_dribbling = tk.Label(self, text='Дриблинг:')
        label_dribbling.place(x=100, y=300)
        label_defending = tk.Label(self, text='Оборона:')
        label_defending.place(x=100, y=325)
        label_physicality = tk.Label(self, text='Физика:')
        label_physicality.place(x=100, y=350)

        self.var = tk.StringVar()
        self.var.trace_add("write", self.graf)

        self.var1 = tk.StringVar()
        self.var1.trace_add("write", self.graf)

        self.var2 = tk.StringVar()
        self.var2.trace_add("write", self.graf)

        self.var3 = tk.StringVar()
        self.var3.trace_add("write", self.graf)

        self.var4 = tk.StringVar()
        self.var4.trace_add("write", self.graf)

        self.var5 = tk.StringVar()
        self.var5.trace_add("write", self.graf)



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

        self.entry_pace = ttk.Entry(self, textvariable=self.var)
        self.entry_pace.place(x=200, y=225)

        self.entry_shooting = ttk.Entry(self, textvariable=self.var1)
        self.entry_shooting.place(x=200, y=250)

        self.entry_passing = ttk.Entry(self, textvariable=self.var2)
        self.entry_passing.place(x=200, y=275)

        self.entry_dribbling = ttk.Entry(self, textvariable=self.var3)
        self.entry_dribbling.place(x=200, y=300)

        self.entry_defending = ttk.Entry(self, textvariable=self.var4)
        self.entry_defending.place(x=200, y=325)

        self.entry_physicality = ttk.Entry(self, textvariable=self.var5)
        self.entry_physicality.place(x=200, y=350)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111, projection='polar')

        labels = ["Скорость", "Удар", "Передачи", "Дриблинг", "Оборона", "Физика"]

        # r = [100, 7, 9, 6, 1, 8]
        r = [1, 1, 1, 1, 1, 1]
        theta = np.deg2rad(np.linspace(0, 360, 7))

        a.axes.set_xticklabels(labels)
        a.axes.set_ylim(100)
        a.axes.set_xticks(theta)
        a.axes.plot(theta, self._get_r(r), color='black')

        self.ax = a.axes

        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.RIGHT)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=500)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=200, y=500)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_name.get(), self.entry_age.get(),
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

        self.grab_set()
        self.focus_set()
    def graf(self, name, index,mode, *args):
        try:

            # f = Figure(figsize=(5, 5), dpi=100)
            # a = f.add_subplot(111, projection='polar')
            #
            labels = ["Скорость", "Удар", "Передачи", "Дриблинг", "Оборона", "Физика"]

            r = [int(self.var.get()),
                 int(self.var1.get()),
                 int(self.var2.get()),
                 int(self.var3.get()),
                 int(self.var4.get()),
                 int(self.var5.get())]
            theta = np.deg2rad(np.linspace(0, 360, 7))
            self.ax.clear()
            self.ax.set_xticklabels(labels)
            #
            self.ax.set_xticks(theta)
            self.ax.plot(theta, self._get_r(r), color='black')
            # self.canvas.delete('all')
            # self.canvas = FigureCanvasTkAgg(f, self)
            self.canvas.draw()
            # self.canvas.get_tk_widget().pack(side=tk.RIGHT)
        except:
            pass

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

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск игрока')
        self.geometry('350x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


def update_progress(value):
    bar.step(value)

def navigate_to_app(root):
    update_progress(100)
    root.destroy()
    root.quit()

def screensaver():
    from tk_loader import Screensaver
    from random import randint

    global bar
    
    saver = tk.Tk()
    load_screen = Screensaver(saver, progress_func=update_progress, go_next=lambda:navigate_to_app(saver))

    image_id = randint(1, 4)
    load_screen.play_gif(f'loading_gifs/{image_id}.gif', 0.03)


    bar = ttk.Progressbar(orient='horizontal')
    bar.pack(fill='both')
    saver.title("FootScaut")
    saver.mainloop()

if __name__ == "__main__":
    screensaver()

    
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("FootScaut")
    root.geometry("1400x900+300+200")
    root.resizable(True, True)
    root.mainloop()
