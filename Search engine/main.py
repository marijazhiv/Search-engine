import formiranje_grafa
import os
from graph import Graph
from parser import Parser
from parserParagraf import ParserParagraf
from trie import Trie


def default_menu():
    print("SEARCH ENGINE")
    print()
    print("IZABERITE OPCIJU:")
    print("===================================================")
    print("1 - PRETRAGA DIREKTORIJUMA")
    print("2 - PROMENA DIREKTORIJUMA KOJI SE PRETRAZUJE")
    print("3 - IZLAZAK ")


def unos_opcije(unos):
    opcije = [1, 2, 3]
    if unos in opcije:
        return True
    return False


def validacija_opcije():
    while True:
        try:
            unos = input("Izaberite opciju: ")
            unos = int(unos)
            if unos_opcije(unos) == False:
                print("pogresan unos")
                continue
            return unos
        except:
            print("pogresan unos. pokusajte ponovo")
'''
def validacija_direktorijuma():  #putanje
    while True:
        try:
            path = input("Unesite putanju do fajla> ")
            if path == " ":
                #isExist = os.path.exists(path)
                print("pogresan unos. ne mozete uneti prazan direktorijum. ")
                continue
            return path
        except:
            print("pogresan unos. ne mozete uneti prazan direktorijum.") '''

def validacija_direktorijuma():  #putanje
    #isExist = os.path.exists(path)
    while True:
        try:
            path = input("Unesite putanju do fajla> ")
            isExist = os.path.exists(path)
            if isExist ==False:
                #isExist = os.path.exists(path)
                print("pogresan unos. direktorijum ne postoji ")
                continue
            return path
        except:
            print("pogresan unos. direktorijum ne postoji")
def validacija_reci():  #putanje
    while True:
        try:
            rec = input("Unesite rec koju trazite: ")
            if rec == " ":
                print("ne mozete uneti praznu rec ")
                continue
            return rec
        except:
            print("ne mozete uneti praznu rec.")
'''
def postoji_li_dir(pth):
    while True:
        try:
            path = input("Unesite putanju do fajla> ")
            isExist = os.path.exists(path)
            if isExist == os.path.exists(path):
                print("direktorijum ne postoji")
                continue
            return path
        except:
             print("direktorijum ne postoji") '''


#def opcija_dva(unos):
    #if unos==2:
        #path=input("Unesite putanju za izmenu direktorijuma")
def opcije(unos):
    if unos==3:
        print("IZASLI STE IZ APLIKACIJE. DOVIĐENJA!")
    elif unos==2:
        path=input("Unesite putanju do fajla> (izmena direktorijuma) ") 


def poziv():
    #path = input("Unesite putanju do fajla> ")
    path=validacija_direktorijuma()
    #isExist = os.path.exists(path)
    #while isExist==False:
        #print("pogresan unos. ovaj direktorijum ne postoji u folderu. pokusajte ponovo")
        #path = input("Unesite putanju do fajla> ")
    #path=postoji_li_dir(path)
    cvorovi, tries, graf = formiranje_grafa.prolazak_kroz_direktorijume(path)
    print
    default_menu()
    print()
    unos = validacija_opcije()
    #brojStranica=input("Unesite broj stranica koji zelite da Vam se prikaze: ")
    while unos != 3:
        if unos == 1:  # ako je izabrana opcija 1
            # dodati ogranicenje da ne moze prazan str da unese
            rec = validacija_reci()
            #pitanje=input("Da li zelte da ogranicite broj stranica koji ce Vam se prikazati. DA/NE")
            #if pitanje=="DA":
            brojStranica=input("Unesite broj stranica koji zelite da Vam se prikaze: ")
            brojStranica=int(brojStranica)
            splitovan_string = rec.split()
            operatori = ["AND", "OR", "NOT"]
            recnik_za_izraz = {}

            if len(splitovan_string) == 1:
                #formiranje_grafa.trazenje_reci(cvorovi, tries, graf, rec)
                #soritranje
                for i in splitovan_string:
                    recnik_za_rec = formiranje_grafa.trazenje_reci_sa_izbacivanjem (cvorovi, tries, graf, i)
                
                    for fajl in recnik_za_rec:
                        if fajl in recnik_za_izraz:
                            recnik_za_izraz[fajl] += recnik_za_rec[fajl]
                        else:
                            recnik_za_izraz[fajl] = recnik_za_rec[fajl]

                sortiran_recnik = formiranje_grafa.sortiranje(recnik_za_izraz)  #lista skupova
                for i in range(0, len(sortiran_recnik)):
                    print(i+1,")", sortiran_recnik[i][0] + " " + str(sortiran_recnik[i][1]))
                    if i==(brojStranica-1):
                        break
                    if i == 0:
                        isecakRec = isecak_stranice(sortiran_recnik[i][0], rec)
                        print("______________________________________________________________________________________________________")
                        print()
                        print(isecakRec)
                        print("______________________________________________________________________________________________________")
                        print()
                #isecak_stranice(path, rec)

            #elif len(splitovan_string) == 3 and splitovan_string[1] in operatori:
                #a = 0   #logicka pretraga
            elif len(splitovan_string) == 3 and splitovan_string[1]=="OR":    #malo veliko OR
                splitovan_string.remove("OR")
                for i in splitovan_string:
                    recnik_za_rec = formiranje_grafa.trazenje_reci_sa_izbacivanjem(cvorovi, tries, graf, i)
                
                    for fajl in recnik_za_rec:
                        if fajl in recnik_za_izraz:
                            recnik_za_izraz[fajl] += recnik_za_rec[fajl]
                        else:
                            recnik_za_izraz[fajl] = recnik_za_rec[fajl]

                #sortiran_recnik = formiranje_grafa.sortiranje(recnik_za_izraz)
                #for fajl in sortiran_recnik:
                    #print(fajl[0] + " " + str(fajl[1]))

                sortiran_recnik = formiranje_grafa.sortiranje(recnik_za_izraz)  #lista skupova
                for i in range(0, len(sortiran_recnik)):
                    print(sortiran_recnik[i][0] + " " + str(sortiran_recnik[i][1]))
                    if i==(brojStranica-1):
                        break
                    if i == 0:
                        isecakRec = isecak_stranice_viseReci(sortiran_recnik[i][0], rec)
                        print("______________________________________________________________________________________________________")
                        print()
                        print(isecakRec)
                        print("______________________________________________________________________________________________________")

            elif len(splitovan_string) == 3 and splitovan_string[1]=="AND":   
                splitovan_string.remove("AND")
                for i in splitovan_string:
                    recnik_za_rec = formiranje_grafa.trazenje_reci_sa_izbacivanjem(cvorovi, tries, graf, i)
                    if len(recnik_za_rec) == 0:
                        recnik_za_izraz = {}
                        break
                
                    if not recnik_za_izraz:
                        recnik_za_izraz = recnik_za_rec.copy()
                    else:
                        for fajl in recnik_za_rec:
                            if fajl in recnik_za_izraz:
                                recnik_za_izraz[fajl] += recnik_za_rec[fajl]

                        for fajl in list(recnik_za_izraz.keys()):
                            if fajl not in recnik_za_rec:
                                del recnik_za_izraz[fajl]
                    

                #sortiran_recnik = formiranje_grafa.sortiranje(recnik_za_izraz)
                #for fajl in sortiran_recnik:
                    #print(fajl[0] + " " + str(fajl[1]))

                sortiran_recnik = formiranje_grafa.sortiranje(recnik_za_izraz)  #lista skupova
                for i in range(0, len(sortiran_recnik)):
                    print(sortiran_recnik[i][0] + " " + str(sortiran_recnik[i][1]))
                    if i==(brojStranica-1):
                        break
                    if i == 0:
                        isecakRec = isecak_stranice_viseReci(sortiran_recnik[i][0], rec)
                        print("______________________________________________________________________________________________________")
                        print()
                        print(isecakRec)
                        print("______________________________________________________________________________________________________")
                        print()

            
            elif len(splitovan_string) == 3 and splitovan_string[1]=="NOT":   
                splitovan_string.remove("NOT")
                for i in splitovan_string:
                    recnik_za_rec = formiranje_grafa.trazenje_reci_sa_izbacivanjem(cvorovi, tries, graf, i)
                    if len(recnik_za_rec) == 0:
                        recnik_za_izraz = {}
                        break
                
                    if not recnik_za_izraz:
                        recnik_za_izraz = recnik_za_rec.copy()
                    else:
                        for fajl in recnik_za_rec:
                            if fajl in recnik_za_izraz:
                                recnik_za_izraz[fajl] += recnik_za_rec[fajl]

                        for fajl in list(recnik_za_izraz.keys()):
                            if fajl in recnik_za_rec:
                                del recnik_za_izraz[fajl]
                    

                #sortiran_recnik = formiranje_grafa.sortiranje(recnik_za_izraz)
                #for fajl in sortiran_recnik:
                    #print(fajl[0] + " " + str(fajl[1]))

                sortiran_recnik = formiranje_grafa.sortiranje(recnik_za_izraz)  #lista skupova
                for i in range(0, len(sortiran_recnik)):
                    print(sortiran_recnik[i][0] + " " + str(sortiran_recnik[i][1]))
                    if i==(brojStranica-1):
                        break
                    if i == 0:
                        isecakRec = isecak_stranice_viseReci(sortiran_recnik[i][0], rec)
                        print("______________________________________________________________________________________________________")
                        print()
                        print(isecakRec)
                        print("______________________________________________________________________________________________________")


            
            else:
                for i in splitovan_string:
                    recnik_za_rec = formiranje_grafa.trazenje_reci_sa_izbacivanjem(cvorovi, tries, graf, i)
                
                    for fajl in recnik_za_rec:
                        if fajl in recnik_za_izraz:
                            recnik_za_izraz[fajl] += recnik_za_rec[fajl]
                        else:
                            recnik_za_izraz[fajl] = recnik_za_rec[fajl]

                #sortiran_recnik = formiranje_grafa.sortiranje(recnik_za_izraz)
                #for fajl in sortiran_recnik:
                    #print(fajl[0] + " " + str(fajl[1]))

                sortiran_recnik = formiranje_grafa.sortiranje(recnik_za_izraz)  #lista skupova
                for i in range(0, len(sortiran_recnik)):
                    print(sortiran_recnik[i][0] + " " + str(sortiran_recnik[i][1]))
                    if i==(brojStranica-1):
                        break
                    if i == 0:
                        isecakRec = isecak_stranice_viseReci(sortiran_recnik[i][0], rec)
                        print("______________________________________________________________________________________________________")
                        print()
                        print(isecakRec)
                        print("______________________________________________________________________________________________________")
                        print()
        elif unos == 2:
            #path = input("Unesite putanju do fajla> ")
            path=validacija_direktorijuma()
            cvorovi, tries, graf = formiranje_grafa.prolazak_kroz_direktorijume(path)                
        default_menu()   
        unos = validacija_opcije()  
        #opcije(unos)   
        #if unos==3:
            #print("IZASLI STE IZ APLIKACIJE. DOVIĐENJA!")            
        #unos=input("Koju opciju zelite da izaberete")  
        #unos=int(unos)
    print("IZASLI STE IZ APLIKACIJE. DOVIDJENJA!")
        


def isecak_stranice(putanja, uneta_rec):
    parser = ParserParagraf()                
    linkovi, reci, paragrafs = parser.parse(putanja)
    parser = Parser()                
    linkovi, reci = parser.parse(putanja)
    isecak=" "
    for i in range (0,len(paragrafs)):
        rec=paragrafs[i]
        if rec==uneta_rec:
            isecak = isecak.join(paragrafs[i:i+30])
            #print(reci)
            break
    if isecak==" ":
        for i in range(0,len(reci)):
            rec=reci[i]
            if rec==uneta_rec:
                isecak = isecak.join(reci[i:(i+20)])
                #print()
                #print("kljucne reci linkova")
                break
    return isecak

    #for i in range(0,len(reci)):
        #rec=reci[i]
        #if rec==uneta_rec:
            #isecak = isecak.join(reci[i:(i+20)])
            #print(reci)
            #break
    #return isecak

def isecak_stranice_viseReci(putanja, uneta_rec):
    parser = ParserParagraf()                
    linkovi, reci, paragrafs = parser.parse(putanja)
    parser = Parser()                
    linkovi, reci = parser.parse(putanja)
    isecak=" "
    splitovan_string = uneta_rec.split()
    for i in range (0,len(paragrafs)):
        rec=paragrafs[i]
        if rec in splitovan_string:
            isecak = isecak.join(paragrafs[i:i+30])
            #print(reci)
            break
    if isecak==" ":
        for i in range(0,len(reci)):
            rec=reci[i]
            if rec in splitovan_string:
                isecak = isecak.join(reci[i:(i+20)])
                #print()
                #print("kljucne reci linkova")
                break
    return isecak

#def validacija_direktorijuma():  #putanje
    #pass
"""
def opcije(unos):
    if unos==3:
        print("IZASLI STE IZ APLIKACIJE. DOVIĐENJA!")
    elif unos==2:
        path=input("Unesite putanju do fajla> (izmena direktorijuma) ")

def opcija_dva(unos):   #promena direktorijuma bez prekida programa
    pass

def opcija_tri(unos):  #izlaz iz aplikacije (exit)
    if unos==3:
        print("IZASLI STE IZ APLIKACIJE. DOVIĐENJA!")
"""      

if __name__ == '__main__':
    poziv()
    
    
