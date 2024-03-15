import csv
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from tkinter.ttk import Treeview


class View(Tk):
    def __init__(self, controller, model):
        super().__init__()
        self.controller = controller
        self.model = model
        self.file_path = None
        self.selected_file = None
        self.__height = 400
        self.__width = 600
        self.default_font = font.Font(family='Verdana', size=14)

        self.title('Otsirakendus')
        self.center_window(self.__width, self.__height)

        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        (self.btn_choose_file, self.lbl_selected_file, self.lbl_a, self.entry,
         self.btn_search, self.lbl_result_count, self.text_box) = self.create_frame_widgets()

        self.entry.bind('<Return>', self.controller.search)

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame = Frame(self, bg='purple', height=15)
        frame.pack(expand=False, fill='both')
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='lightblue')
        frame.pack(expand=True, fill='both')
        return frame

    def create_frame_widgets(self):
        btn_choose_file = Button(self.top_frame, text='Vali fail', font=self.default_font, state='normal',
                                 command=self.controller.open_file)
        btn_choose_file.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        lbl_selected_file = Label(self.top_frame, text='Valitud ', font=self.default_font, state='normal')
        lbl_selected_file.grid(row=0, column= 1, padx=5, pady=5, sticky='ew')

        lbl_a = Label(self.top_frame, text='Sisesta otsisõna: ', font=self.default_font, state='disabled')
        lbl_a.grid(row=1, column=0, padx=5, pady=5, sticky='e')

        entry = Entry(self.top_frame, font=self.default_font, state='disabled')
        entry.grid(row=1, column=1, padx=5, pady=5, sticky='e')
        entry.focus()

        btn_search = Button(self.top_frame, text='Otsi', font=self.default_font, state='disabled',
                            command=self.controller.search)
        btn_search.grid(row=1, column=2, padx=5, pady=5, sticky='e')

        lbl_result_count = Label(self.top_frame, text='Kuvatavaid tulemusi', font=self.default_font, state='normal')
        lbl_result_count.grid(row=2, column=1, padx=5, pady=5)

        text_box = Treeview(self.bottom_frame, columns=[], show='headings')
        scrollbar = Scrollbar(self.bottom_frame, orient='vertical', command=text_box.yview)
        text_box.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        text_box.pack(expand=True, fill='both', padx=5, pady=5)

        return btn_choose_file, lbl_selected_file, lbl_a, entry, btn_search, lbl_result_count, text_box

    def display_results(self, results):
        if results:
            for col in self.text_box.get_children():
                self.text_box.delete(col)

            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                header = next(reader)
                self.text_box['columns'] = header
                for col in header:
                    self.text_box.column(col, width=70)
                    self.text_box.heading(col, text=col, anchor='center')

            for row in results:
                values = row.split(';')
                self.text_box.insert('', 'end', values=values)

        else:
            for child in self.text_box.get_children():
                self.text_box.delete(child)

    def display_error(self, message):
        messagebox.showerror('Viga', message)

    def display_result_count(self, count):
        self.lbl_result_count.config(text=f'Kuvatakse {count} tulemust.')