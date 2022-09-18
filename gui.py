import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from decimal import Decimal
import time
from utils import dotaz, czk
# 	res1=(float(entry1.get()) / float(czk))/ btc
# 	sav = entry2.insert(0, res1)

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
# 		ent = (float(entry1.get())/czk)/str(btc)
# 		entry2.insert(0,round(Decimal(ent),18))
	else:
		entry1.insert(0, "nezadano")
		messagebox.showerror("Hodnota", "nezadana hodnota")
		entry1.delete(0, tk.END)
		
		
ws = tk.Tk()
ws.title("Python Guides")
ws.geometry("830x600")

# seznam = ("CZK", "EUR", "CHF")
# listbox = tk.Listbox(ws, width=12, height=12)
# for meny in seznam:
# 	listbox.insert(tk.END, meny)
seznam_fiat = ['AUD','GBP','CNY','DKK','EUR','HRK','JPY','CAD','HUF','NOK','PLN','RON','SEK','CHF','TRY','USD']
frame = tk.Frame(ws,height=50)
frame.place(x = 15, y = 26)
listbox = ttk.Combobox(frame,state = "readonly",width=8, values = seznam_fiat,font=("Arial", 15))
listbox.set("Fiat")
listbox.pack(padx = 1, pady=1)

seznam_krypto = ['BTCUSD','BTCEUR','BTCGBP','BTCPAX','GBPUSD','GBPEUR','EURUSD','XRPUSD','XRPEUR'
				 ,'XRPGBP','LTCUSD','LTCEUR','LTCGBP','ETHUSD','ETHEUR',
				 'ETHGBP','BCHUSD','BCHEUR','PAXUSD','XLMUSD',
				 'XLMGBP','LINKUSD','LINKEUR','LINKGBP','OMGUSD','OMGEUR','OMGGBP',
				 'USDCUSD','USDCEUR','AAVEUSD','AAVEEUR',
				 'BATUSD','BATEUR','UMAUSD','UMAEUR','DAIUSD','KNCUSD','KNCEUR','MKRUSD',
				 'ZRXUSD','ZRXEUR','GUSDUSD','ALGOUSD','ALGOEUR','AUDIOUSD'
				 ,'CRVUSD','CRVEUR','SNXUSD','SNXEUR','UNIUSD','UNIEUR',
				 'YFIEUR','COMPUSD','COMPEUR','GRTUSD','GRTEUR','LRCUSD','LRCEUR','USDTUSD',
				 'USDCUSDT','BTCUSDT','ETHUSDT','XRPUSDT','EURTEUR','EURTUSD','MANAUSD',
				 'MATICUSD','MATICEUR','SUSHIUSD','SUSHIEUR','CHZUSD','CHZEUR','ENJUSD','ENJEUR',
				 'HBAREUR','ALPHAUSD','ALPHAEUR','AXSUSD','AXSEUR','FTTUSD','FTTEUR','SANDUSD',
				 'STORJUSD','STORJEUR','ADAUSD','ADAEUR','FETUSD','FETEUR','SKLUSD','SKLEUR',
				 'CELEUR','SLPUSD','SLPEUR','SXPUSD','SXPEUR','SGBUSD','SGBEUR','AVAXUSD','AVAXEUR',
				 'DYDXEUR','FTMUSD','FTMEUR','SHIBUSD','SHIBEUR','AMPUSD','AMPEUR','ENSUSD','ENSEUR',
				 'GALAEUR','PERPUSD','PERPEUR','CTSIUSD','CTSIEUR','CVXUSD','CVXEUR','IMXUSD',
				 'NEXOUSD','NEXOEUR','ANTUSD','ANTEUR','GODSUSD','GODSEUR','RADUSD','RADEUR','BANDUSD',
				 'INJUSD','INJEUR','RLYUSD','RLYEUR','RNDRUSD','RNDREUR','VEGAUSD','VEGAEUR','1INCHUSD',
				 'SOLUSD','SOLEUR','APEUSD','APEEUR','MPLUSD','MPLEUR','DOTUSD','DOTEUR','NEARUSD','NEAREUR']
frame = tk.Frame(ws,height=50)
frame.place(x=670, y=26)
krypto_list = ttk.Combobox(frame,state = "readonly",width=8, values = seznam_krypto,font=("Arial", 15))
krypto_list.set("Krypto")
krypto_list.pack(padx = 1, pady=1)

ws.resizable(False, False) # nastaveni nemene velikosti geometry
v1=tk.StringVar() # promena ze vstupu do druheho vstupniho pole
v2=tk.StringVar()
castkaA = tk.StringVar()
kurzA = tk.StringVar()
kurzB = tk.StringVar()
kurzb = tk.StringVar()
# popis pole
l1 = tk.Label(ws, text="meny", font=("Arial", 25))

# pole pro vstup od uzivatele
entry1 =  tk.Entry(ws,font=("Arial",15),textvariable=v1)
#c,k,d,p,czk
l2 = tk.Label(ws, text= "BTC", font=("Arial", 25))
entry2 = tk.Entry(ws,font=("Arial",15),textvariable=v2)

castka_a = tk.Label(ws, text="castka")
castka_a.place(x=530, y=100)
L3 = tk.Label(ws, underline=4, wraplength=70,textvariable=castkaA, relief="sunken")
L3.place(x=600, y= 100)

kurz_1 = tk.Label(ws, text="kurz USD")
kurz_1.place(x=530, y = 125)
kurz = tk.Label(ws, textvariable=kurzA, relief="sunken")
kurz.place(x=600, y=125)

kurz_b = tk.Label(ws, text="kurz")
kurz_b.place(x=530, y=145)
kurz_B=tk.Label(ws, textvariable=kurzB) # uzivatel vybral menu 
kurz_B.place(x=560, y =145)
da_mena= tk.Label(ws, textvariable=kurzb, relief="sunken")
da_mena.place(x=600,y=145)

l3 = tk.Label(ws, text="/", font=("Arial", 25))

# tlacitka a volani na funkce 
f_b = tk.Button(ws,text="Fiat/BTC", command=fiat_krypto) # nedavat () jinak se funkce zavola automaticky
b_f = tk.Button(ws, text="BTC/Fiat" ,command=krypto_fiat)
b_s = tk.Button(ws, text="Smazat", command=smaz)
b_e = ttk.Button(ws, text="Exit", command=exit)
# fiat popis a pole vstupu
#l1.place(x=15,y=20)
entry1.place(x=130, y=26)

# krypto a pole vstupu
#l2.place(x=730, y=20)
entry2.place(x=380, y=26)

l3.place(x=360,  y=20)
# tlacitka
f_b.place(x=50, y=100)
b_f.place(x=140, y = 100)
b_s.place(x=230, y=100)
b_e.place(x=320, y = 100)
#listbox.place(x=15,y=22)
ws.mainloop()