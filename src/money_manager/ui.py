import tkinter as tk
from tkinter import ttk

from typing import Dict

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
    def __init__(self, root: tk.Tk, app):
        super().__init__(root)
        self.root = root

        self.tabs: Dict[str, ttk.Frame] = {}

        r_0: int = 0
        c_0: int = 0
        r_1: int = 0
        c_1: int = 0

        self.grid(row=r_0, column=c_0, sticky='nsew')
        self.root.rowconfigure(r_0, weight=1)
        self.root.columnconfigure(c_0, weight=1)

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=r_1, column=c_1, sticky='nsew')

        self.tabs['dashboard'] = DashboardFrame(self.notebook, app)
        self.tabs['balances'] = BalancesFrame(self.notebook, app)
        self.tabs['accounts'] = AccountsFrame(self.notebook, app)

        for t in self.tabs:
            self.notebook.add(self.tabs[t], text=t.capitalize())
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

class DashboardFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.parent = parent
        self.app = app

        r_0: int = 0
        c_0: int = 0
        r_1: int = 0
        c_1: int = 0

        self.grid(row=r_0, column=c_0, sticky='nsew')
        self.parent.rowconfigure(r_0, weight=1)
        self.parent.columnconfigure(c_0, weight=1)

class BalancesFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.parent = parent
        self.app = app

        r_0: int = 0
        c_0: int = 0
        r_1: int = 0
        c_1: int = 0

        self.grid(row=r_0, column=c_0, sticky='nsew')
        self.parent.rowconfigure(r_0, weight=1)
        self.parent.columnconfigure(c_0, weight=1)

class AccountsFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.parent = parent
        self.app = app

        r_0: int = 0
        c_0: int = 0
        r_1: int = 0
        c_1: int = 0

        self.grid(row=r_0, column=c_0, sticky='nsew')
        self.parent.rowconfigure(r_0, weight=1)
        self.parent.columnconfigure(c_0, weight=1)