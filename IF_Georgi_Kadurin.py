




#----------------------------------------------
try:
    vanus=int(input("Kui vana sa oled? "))
    if vanus>=18:
        print("Kas te annate vanematele loa oma Tahvelit vaadata")
        o=input("jah vaõ ei ")
        if o.lower()=="jah":
            print({o})
            print("see on ligipääs teie vanemalt.")
            print("Tahvel on kinni.")
        elif o.upper()=="EI":
            print("sissepääs puudub.")
            print("Tahvel on kinni.")
    if vanus<18:
        print("juurdepääs vanemalt on automaatselt antud.")
except:
    ("Tahvel on kinni.")
print()
print()


#---------------------------------------------

try:
    päev=int(input("Mis päev ja mitu tundi täna on? "))
    if päev==1:
        n="esmaspäev"
        n="6 tundi"
    elif päev==2:
        n="Teisipäev"
        n="8 tundi"
    elif päev==3:
        n="kolmapäev"
        n="6 tundi"
    elif päev==4:
        n="neljapäev"
        n="5 tundi"
    elif päev==5:
        n="reede"
        n="7 rundi"
    elif päev==6:
        n="laupäev"
        n="0 tundi"
    elif päev==7:
        n="pühapäev"
        n="0 tundi"
    else:
        n="vali number"
    print(n)
except :
   print("!!!!!!")

#14.12.22
#------------------------------------

from math import *
from random import *
print("Распорядок дня")

try: 
    kell=int(input("Mis kell on praegu?  "))
    if kell==(0):
        print(f"magan")
    elif kell==(1):
        print("veel magan")
    elif kell==(2):
        print("tõusis vett jooma")
    elif kell==(3):
        print("magan")
    elif kell==(4):
        print("veel magan")
    elif kell==(5):
        print("tõusis tualetti")
    elif kell==(6): 
        print("ärkas üles")
    elif kell==(7):
        print("lähen koolis")
    elif kell==(8):
        print("koolis")
    elif kell==(9):
        print("ma õpin")
    elif kell==(10):
        print("veel õpin")
    elif kell==(11):
        print("sõin kohvikus")
    elif kell==(12):
        print("jäi haigeks")
    elif kell==(13): 
        print("viidi haiglasse")
    elif kell==(14):
        print("andis tablette")  
    elif kell==(15):
        print("magan jääma")
    elif kell==(16):
        print("magan")
    elif kell==(17):
        print("magan")
    elif kell==(18):
        print("tuli arst")
    elif kell==(19):
        print("haiglast välja lastud")
    elif kell==(20):
        print("kodus")
    elif kell==(21): 
        print("sööma")
    elif kell==(22):
        print("tööd tegemas")   
    elif kell==(23): 
        print("Arvuti mängima")
except:
     print("!!!!!!")

#-------------------------------------


from math import *
print("Tee ajakavast plokkskeem")
try:
    päev=print(input("Mis päev täna on?"))
    if päev=="esmaspäev":
        print("Täna on 10 tundi")
    elif päev=="teisipäev":
        print("Täna on 7 tundi")
    elif päev=="kolmapäev":
        print("Täna on 10 tundi")
    elif päev=="neljapäev":
        print("Täna on 8 tundi")
    elif päev=="reede":
        print("Täna on 9 tundi")
    elif päev=="laupäev":
        print("täna puhkepäev")
    elif päev=="pühapäev":
        print("täna puhkepäev")
    else:
        print(f"{päev}")
except:
    print("!!!!!")
