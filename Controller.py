import os
from tkinter import filedialog

from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)

    def search(self, event=None):
        query = self.view.entry.get()

        if len(query) < 3:
            self.view.display_error("Sisesta otsisõna, mis on vähemalt 3 tähemärki pikk!")
            return

        query = query.lower()
        file_path = self.view.file_path
        results = self.model.search(query, file_path)

        self.view.display_results(results)

        self.view.entry.delete(0, 'end')

        self.view.display_result_count(len(results))

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.view.file_path = file_path
            short_file_name = os.path.basename(file_path)
            self.view.lbl_selected_file.config(text=f'Valitud {short_file_name}')

            self.view.lbl_a.config(state='normal')
            self.view.entry.config(state='normal')
            self.view.btn_search.config(state='normal')