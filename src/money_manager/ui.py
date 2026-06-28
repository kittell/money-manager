import tkinter as tk
from tkinter import ttk

class UserInterface:
    def __init__(self, app):
        self.app = app

        # Basic window setup
        root = tk.Tk()
        root.title(app._name)
        root.geometry('1200x800')

        # Theme
        try:
            style = ttk.Style(root)
            if 'clam' in style.theme_names():
                style.theme_use('clam')
        except Exception:
            pass

        # Mount main window
        main_window = MainWindow(root, app)
        root.mainloop()

        return

class MainWindow(ttk.Frame):
    def __init__(self, root: tk.Tk, app: Application):
        super().__init__(root)
        self.root = root

        r_0: int = 0
        c_0: int = 0
        r_1: int = 0
        c_1: int = 0

        self.grid(row=r_0, column=c_0, sticky='nsew')
        self.root.rowconfigure(r_0, weight=1)
        self.root.columnconfigure(c_0, weight=1)
