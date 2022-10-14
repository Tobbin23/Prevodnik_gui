import tkinter as tk
from tkinter import ttk

def st_combobox():
    ttk.Style().theme_use("clam")
    
    ttk.Style().map('TCombobox', fieldbackground=[('readonly', "blue")])
    ttk.Style().map('TCombobox', selectbackground=[('readonly', "white")])
    ttk.Style().map('TCombobox', selectforeground=[('readonly', "blue")])
    ttk.Style().map('TCombobox', background=[('readonly', "white")])
    ttk.Style().map('TCombobox', foreground=[('readonly', "white")])
    #     ohraniceni = tk.Frame(ws, bg="white",height=100, width=100)
    #     ohraniceni.place(anchor=tk.W)

    #     bold = ("helvetica", 12, "bold")

    ttk.Style().map("Vertical.TScrollbar",
              foreground=[("!active", "white"),("active", "blue")],
              background=[("!active","white"),("active","white")])
    ttk.Style().configure("Vertical.TScrollbar", troughcolor="blue",
                    lightcolor="blue")
    return

def st_Button():
    
    ttk.Style().configure("C.TButton",borderwidth=2 ,font=("calibri", 10, "bold","underline"))
    ttk.Style().map("C.TButton",
          foreground=[("!active", "blue"),("active", "white")],
          background=[("!active","white"),("active","blue")])
    
    ttk.Style().configure("B.TButton", font=("calibri", 10,"bold","underline"))#borderwidth=2
    ttk.Style().map("B.TButton",
            foreground=[("!active", "white"),("active", "blue")],
            background=[("!active","blue"),("active","white")])
    return

