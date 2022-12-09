import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from uprava_stylu import st_combobox, st_Button
from decimal import Decimal
from exit_delete import seznam
import time
import os
from utils import dotaz, czk
#   res1=(float(entry1.get()) / float(czk))/ btc
#   sav = entry2.insert(0, res1)


def refresh():
    ws.destroy()
    os.system("python3"+"  "+os.path.join(os.path.dirname(os.path.realpath((__file__))),"gui.py"))
    ws.mainloop()
def exit():
    ws.destroy()
def smaz():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

def krypto_fiat():
    """ Prevod z Bitcoinu na Fiat"""
    entry1.delete(0, tk.END)
    if entry2.get() != "":
        try:
            entry1.delete(0, tk.END)
            ent=czk(satoshi=float(entry2.get()))
            entry1.insert(0, en)
            #entry1.insert(0,"{:,.1f}".format(ent))
        except:
            entry1.delete(0, tk.END)
            en = czk(satoshi=(entry2.get()))
            entry1.insert(0, en)
    else:
        entry2.insert(0, "nezdano")
        messagebox.showerror("Hodnota", "nezadana hodnota")
        entry2.delete(0, tk.END)


def fiat_krypto():
    global kz, btc
    """ Prevod z Fiat meny na  Bitcoin"""
    entry2.delete(0, tk.END)
    if entry1.get() != "":
        try:
            
            en = float(entry1.get())
            #listbox.get(listbox.curselection()),
            
            c,k,d,p,czk,bt = dotaz(castka=round(float(en)),mena1=listbox.get(),COIN=krypto_list.get().lower(), fiatnaKrypto=True)
            castkaA.set(str(c)) # castka vkladu
            kurzA.set(str(k))  # jaky je kurz czk
            kurzB.set(str(listbox.get())) # jakou menu si vyzadal uzivatel
            kurzb.set(str(d)) # jaky je kuzr dane meny
            entry2.insert(0,str(bt))
            
        except:
            entry2.delete(0, tk.END)
            en =entry1.get().replace(",","")
            c, z ,b,btc= dotaz(castka=round(float(en)),mena1=listbox.get(), COIN=krypto_list.get().lower(),fiatnaKrypto=True)
            castkaA.set(str(c)) # castka vkladu
            kurzA.set(str(z))  # jaky je kurz czk
            kurzB.set(str(listbox.get())) # jakou menu si vyzadal uzivatel
            kurzb.set(str(b)) # jaky je kuzr dane meny
            entry2.insert(0,str(btc))
#       ent = (float(entry1.get())/czk)/str(btc)
#       entry2.insert(0,round(Decimal(ent),18))
    else:
        entry1.insert(0, "nezadano")
        messagebox.showerror("Hodnota", "nezadana hodnota")
        entry1.delete(0, tk.END)
        
        
#ws = ThemedTk(theme="aquativo")
ws= tk.Tk()
ws.title("Python Guides")
ws.resizable(False, False) # nastaveni nemene velikosti geometry
screen_width = ws.winfo_screenwidth()
screen_height = ws.winfo_screenheight()
vyska=630
sirka=400
center_x = int(screen_width/2 - vyska/ 2)
center_y = int(screen_height/2 - sirka / 2)


ws.geometry(f'{vyska}x{sirka}+{center_x}+{center_y}')
ws.configure(cursor="top_left_corner",background="#262626")#"#004c7f")
style = ttk.Style()
style.theme_use("clam")
ohraniceni = tk.Frame(ws, bg="white",height=100, width=100)
ohraniceni.place(anchor=tk.W)

bold = ("helvetica", 12, "bold")
ws.option_add("*TCombobox*Listbox*Background", "white")
ws.option_add("*TCombobox*Listbox*Foreground", "blue")
ws.option_add("*TCombobox*Listbox*Font",bold)
ws.option_add("*TCombobox*Listbox.selectBackground", "blue")

ws.option_add("*TCombobox*Listbox.selectForeground", "white")

st_combobox()

# # style.configure('TCombobox',
#                 background="white",
#                 foreground="blue",
#                 fieldbackground="white",
#                 darkcolor="blue",
#                 lightcolor="blue",
#                 selectbackgroun="blue",
#                 bordercolor="blue",
#                 insertcolor="blue",
#                 arrowcolor="blue")

v1=tk.StringVar() # promena ze vstupu do druheho vstupniho pole
v2=tk.StringVar()
castkaA = tk.StringVar()
kurzA = tk.StringVar()
kurzB = tk.StringVar()
kurzb = tk.StringVar()

seznam_fiat = ['AUD','GBP','CNY','DKK','EUR','HRK','JPY','CAD','HUF','NOK','PLN','RON','SEK','CHF','TRY','USD']
#frame = tk.Frame(ws,relief="sunken", bg="#325bff")
#nme = tk.Label(ws, text="Měny")
fa_r = tk.LabelFrame(ws,text="Měny",
                    fg="white",
                    borderwidth=6,
                    relief="sunken",
                    #labelwidget=nme,
                    bg="#515151",#"#325bff",
                    font=("helvetica",15,"bold"))

# label info autor a popis programu
autor_info= tk.Label(fa_r, text="Autor info",cursor= "hand2",relief="sunken",bd=2,width=10,background="white",foreground= "red", font= ('Aerial',8,"bold","underline"))#515151
autor_info.bind("<Button-1>", lambda e:open_url(e))
#autor_info.bind("<Enter>", lambda e:open_url(e))
autor_info.place(x=15,y=350)

# seznam fiat men 
listbox = ttk.Combobox(fa_r,state = "readonly",width=8,cursor= "hand2", style="my.TCombobox",values = seznam_fiat,font=("Arial", 15))
listbox.set("Fiat")
listbox.pack()



# style.configure("my.TCombobox",backgroudn="black",
#                 #fieldbackground="#1d2128",
#                 insertwidth="red",
#                 foreground="green",
#                 darkcolor="lime",
#                 selectbackground="green",
#                 lightcolor="green")

# seznam krypto men a paru 
krypto_list = ttk.Combobox(fa_r,state = "readonly",width=8,style="my.TCombobox", values =seznam,font=("Arial", 15))
#style.configure("K.TCombobox", selectbackground="blue")

krypto_list.set("Krypto")
krypto_list.pack(pady=40)
fa_r.place(bordermode=tk.OUTSIDE,x=508,height=398)


# nadpis pro labelframe
pole1 = tk.Label(ws, text="Fiat")
ram_fiat = tk.LabelFrame(ws,
                   borderwidth=6,
                   relief="sunken",
                   labelwidget=pole1,
                   bg="#515151",
                   fg="white",
                   font=("helvetica",15))

ram_fiat.place(x=150,y=20)#bordermode=tk.OUTSIDE)
# pole pro vstup od uzivatele
entry1 =  tk.Entry(ram_fiat,font=("Arial",15,"bold"),
                   borderwidth=10,width=29,
                   textvariable=v1,
                   bg="blue",
                   fg="white")
#c,k,d,p,czk
pole2 = tk.Label(ws, text="Krypto")
ram_krypto = tk.LabelFrame(ws,
                   borderwidth=6,
                   relief="sunken",
                   labelwidget=pole2,
                   bg="#515151",
                   fg="white",
                   font=("helvetica",15))

 
entry2 = tk.Entry(ram_krypto,font=("Arial",15,"bold"),cursor= "top_left_corner",
                   borderwidth=10,width=29,
                   textvariable=v2,
                   bg="blue",
                   fg="white")
ram_krypto.place(x=150,y=120)
entry1.grid(column=0, row=0)
# krypto a pole vstupu

entry2.grid(column=1, row=1)


#nadpis_1 = tk.Label(ws, text="Podrobnosti",bg="green", width=30)
nadpis = tk.Label(ws, text = "Podrobnosit",fg="white",
                  width=20,
                  bg="blue",
                  borderwidth=6,
                  relief="sunken",
                  font=("helvetica",10,"bold"))
l_f = tk.LabelFrame(ws,
                   borderwidth=6,
                   relief="sunken",
                   #text="Podrobnosti",
                   #relief="sunken",
                   labelwidget=nadpis,
                   bg="#515151",
#                  fg="white",
                   font=("helvetica",15,"bold"))


l_f.place(bordermode=tk.OUTSIDE,x=150,y=267,width=355,height=130)
castka_a = tk.Label(l_f, text="castka",bg="white",bd=5,
                    relief="sunken",
                    fg = "blue",
                    font=("helvetica",10,"bold"))

castka_a.grid(column=0, row=1)

L3 = tk.Label(l_f, underline=4,
              wraplength=70,
              textvariable=castkaA,
              bd=5,
              bg="blue",
              fg="white",
              font=("helvetica", 10,"bold"),
              relief="sunken")

L3.grid(column=1, row=1,ipadx=5)

kurz_1 = tk.Label(l_f, text="kurz",
                  bg="blue", bd=5,
                  relief="sunken",
                  fg="white",
                  font=("helvetica",10,"bold"))

kurz_1.grid(column=0, row=2)

kurz = tk.Label(l_f, textvariable=kurzA, bg="blue",
                borderwidth=6,relief="sunken",
                fg="white",
                font=("helvetica",10,"bold"))

kurz.grid(column=1, row=2,ipadx=5)

kurz_b = tk.Label(l_f, text="Aktualni cena",bg="blue",
                bd=5,relief="sunken",
                fg="white",
                font=("helvetica",10,"bold"))


kurz_b.grid(column=0, row=3)

kurz_B=tk.Label(l_f, textvariable=kurzB,bg="blue",
                bd=5,relief="sunken",
                fg="white",
                font=("helvetica",10,"bold")) # uzivatel vybral menu 

kurz_B.grid(column=2, row=2,ipadx=5)

da_mena= tk.Label(l_f, textvariable=kurzb, bg="blue",
                bd=5,relief="sunken",
                fg="white",
                font=("helvetica",10,"bold"))


da_mena.grid(column=2, row=3,ipadx=5)

# ws.state= ttk.Style()
# style.configure("TButton", background="black")

#ll = tk.Label(ws,text="Ovládání",fg="white",width=32, bg="red")

fr = tk.LabelFrame(ws,
                   borderwidth=6,
                   text="Ovladani",
                   relief="sunken",
                   #labelwidget=ll,
                   bg="#515151",#"#325bff",
                   fg="white",
                   font=("helvetica",15))

fr.place(bordermode=tk.OUTSIDE, height=398)#grid(column=0,row=0,pady=10,padx=30)


# tlacitka a volani na funkce
C_Button = st_Button()
f_b = ttk.Button(fr,text="Fiat/BTC",style="C.TButton",command=fiat_krypto) # nedavat () jinak se funkce zavola automaticky
b_f = ttk.Button(fr, text="BTC/Fiat",style="B.TButton" ,command=krypto_fiat)
b_s = ttk.Button(fr, text="Smazat",style="C.TButton", command=smaz)
b_e = ttk.Button(fr, text="Exit",style="B.TButton", command=exit)
b_r = ttk.Button(fr, text="Refresh", style="C.TButton", command=refresh)
# fiat popis a pole vstupu
entry1.grid(column=1, row=1)
# krypto a pole vstupu
entry2.grid(column=2, row=1)


f_b.grid(column=1, row=1 ,pady=10,ipadx=10, ipady=10)# fiat/btc
b_f.grid(column=1, row=2,pady=10,ipadx=10, ipady=10)# btc/fiat
b_s.grid(column=1, row=3,pady=10,ipadx=10, ipady=10)# smaz
b_e.grid(column=1, row=4,pady=10,ipadx=10, ipady=10)# exit
b_r.grid(column=1, row=5,pady=10,ipadx=10, ipady=10)#refresh


#
#listbox.place(x=15,y=22)
ws.mainloop()
