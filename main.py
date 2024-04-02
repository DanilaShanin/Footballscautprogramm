import tkinter as tk
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.view_records()
        
    def init_main(self):
        toolbar = tk.Frame(bg='#fe4240', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="add.gif")
        btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#fe4240', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

        def init_child(self):
        self.title('Добавить игрока')
        self.geometry('1000x1000+400+300')
        self.resizable(False, False)

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

        self.entry_pace = ttk.Entry(self)
        self.entry_pace.place(x=200, y=225)

        self.entry_shooting = ttk.Entry(self)
        self.entry_shooting.place(x=200, y=250)

        self.entry_passing = ttk.Entry(self)
        self.entry_passing.place(x=200, y=275)

        self.entry_dribbling = ttk.Entry(self)
        self.entry_dribbling.place(x=200, y=300)

        self.entry_defending = ttk.Entry(self)
        self.entry_defending.place(x=200, y=325)

        self.entry_physicality = ttk.Entry(self)
        self.entry_physicality.place(x=200, y=350)

    self.grab_set()
    self.focus_set()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("FootScaut")
    root.geometry("1400x900+300+200")
    root.resizable(True, True)
    root.mainloop()
