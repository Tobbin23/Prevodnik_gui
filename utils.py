import requests
import json
from user_agent import user
from datetime import date 
from sys import exit
from random_ip import generuj_ip
from decimal import Decimal
FALES_IP = generuj_ip


def Fiat_za_Fiat(penize:float=100,
                 fiat:float=None):
    
    prevod = float(penize) / float(fiat)
    return penize,fiat,round(prevod,3)
    
def Fiat_na_Krypto(cast:float=None,
               kurz:float=None,
               druha_mena:float=None,
               krypto:float=None, prevod=False):
    
    try:
        if prevod != False:
            prevod = cast /(kurz/ druha_mena ) * kurz # prevod z na czk
            btc_czk = float(krypto) * float(kurz)
            na_BTC = (float(prevod) / float(kurz)) / float(krypto)
        else:
            btc_czk = (float(cast) / float(kurz)) / float(krypto)
            return cast, kurz, krypto, btc_czk
    except ZeroDivisionError:
        print ("nelze 0")   
    
    #return f"kurz usd {kurz} eur {druha_mena}\n"\
           #f"prevod {round(prevod)}\n"\
           #f"BTC {na_BTC}"
    return cast,kurz, druha_mena, round(prevod),round(btc_czk,2), str(round(Decimal(na_BTC), 18))


def czk(satoshi:str=None):
    datum = date.today()
    try:
        posli_dotaz = requests.get(url=f"https://data.kurzy.cz/json/meny/b[6]cb{datum}.json", headers=user(), proxies={"http" : FALES_IP}).json()
        BTC_dotaz = requests.get(url="https://www.bitstamp.net/api/v2/ticker/btcusd", headers=user(),proxies={"http": FALES_IP}).json()
        btc= BTC_dotaz["last"]
        usd= posli_dotaz["kurzy"]["USD"]["dev_stred"]
        cz_k = (float(satoshi) * float(usd)) * float(btc)
        return round(cz_k,2)
    
    except requests.ConnectionError:
        return  "chyba spojeni"
    except requests.ConnectTimeout:
        return "timeout"
    except ValueError:
        return "chybova hodnota"
    except KeyError:
        return "chyby hodnota"  
    
def dotaz(castka:float=100000,
          zaklad_mena="USD",
          mena1="EUR", 
          COIN="BTC",
          fiatnaKrypto=False,
          fiatzaFiat=False):
    datum = date.today()
    try:
        
        
        
        if fiatnaKrypto != False:
            for poradnik in range(len([zaklad_mena,mena1, COIN])):
                if poradnik == 0:
                    posli_dotaz = requests.get(url=f"https://data.kurzy.cz/json/meny/b[6]cb{datum}.json", headers=user(),proxies={"http": FALES_IP} ).json()
                
                    kurz_zaklad = posli_dotaz["kurzy"][zaklad_mena]["dev_stred"]
                    kurz_data = posli_dotaz["kurzy"][mena1]["dev_stred"]
            
                if poradnik == 2:
                    BTC_dotaz = requests.get(url=f"https://www.bitstamp.net/api/v2/ticker/{COIN}", headers=user(),proxies={"http": FALES_IP}).json()
                    BTC_Data = BTC_dotaz["last"]
                else:
                    posli_dotaz = requests.get(url=f"https://data.kurzy.cz/json/meny/b[6]cb{datum}.json", headers=user(),proxies={"http": FALES_IP} ).json()
                    kurz_zaklad = posli_dotaz["kurzy"][zaklad_mena]["dev_stred"]
            try:
            
                #vypocet = (float(castka) / float(mena_data)) / float(BTC_Data)
#                 if mena1 != "USD":
#                     c,k,d,p,czk,b = Fiat_na_Krypto(cast=castka, kurz=kurz_zaklad,druha_mena=kurz_data, krypto=BTC_Data, prevod=True)
#                     return c,k,d,p,czk,b
                if mena1:
                    c, z,b,bb=  Fiat_na_Krypto(cast=castka, kurz=kurz_zaklad, krypto=BTC_Data, prevod=False)
                    return c,z,b,bb
                else:
                    kurz_zaklad = posli_dotaz["kurzy"][zaklad_mena]["dev_stred"]
                    czk(vklad=castka,usd=kurz_zaklad, btc=BTC_Data)
            except requests.ConnectionError:
                return  "chyba spojeni"
            except requests.ConnectTimeout:
                return "timeout"
            except ValueError:
                return "chybova hodnota"
            except KeyError:
                return "chyby hodnota"  

    except requests.ConnectionError:
        print("chyba spojeni ")
    except ValueError as VE:
        print("chybna hodnota")
    except KeyError:
        print("nezadal jsi menu !!!")
        
#btc = 21525.4
#czk = 24.831
#usd = czk


#def uzivatel():
    #while True:
        #try:
            #invest_castka = int(input("častka : ").upper())
            #mena = str(input("mena: " ).upper())
        
            #print(dotaz(castka=invest_castka,mena1=mena))
            
        #except ValueError:
            #exit()
            #break
        #except KeyboardInterrupt:
            #exit()
            #break
        #break
    
#print(dotaz(castka=100,mena1="CHF",fiatnaKrypto=True ))
# castka:float=100000,
#           zaklad_mena="USD",
#           mena1="EUR", 
#           COIN="BTC",
#           fiatnaKrypto=False,
#           fiatzaFiat=False):


