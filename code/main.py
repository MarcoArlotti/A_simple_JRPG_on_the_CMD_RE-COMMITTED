import os
from random import choice
from funzioni_jrpg import Alleato,Nemico,Set_magia,Magia,Entita,turno

from sys import platform

if platform == "linux":
    clear = "clear"   
elif platform == "win32":
    clear = "cls"

def main():
    #creazione classe OSUBA
    vita_massima = 200
    magia6 = Magia("SIGILLO",999,"bho",True,False,vita_massima - 1) #TODO DA NON LASCIARE

    magia1 = Magia("BOMBA",1,"fuoco",True,True,12)
    magia2 = Magia("FRECCIA INFUOCATA",2,"fuoco",False,True,6)
    magia3 = Magia("TESTATA",2,"bho",False,False,12) #TODO cambiare il tipo di magia
    magia4 = Magia("PUGNO",1,"bho",False,True,6)
    magia5 = Magia("INSTAKILL",19,"bho",False,True,1) #TODO DA NON LASCIARE
    
    magia7 = Magia("PERFORAZIONE",3,"osserva",False,True,20)
    
    osuba_lista_magie1 = [magia1,magia2,magia7,magia5,magia6]
    osuba_lista_magie2 = [magia3,magia4]
    osuba_lista_magie3 = [magia5]
    
    osuba_set1 = Set_magia("TECNICHE \"OSSERVA\"",osuba_lista_magie1,[],[]) #TODO
    osuba_set2 = Set_magia("CORPO A CORPO",osuba_lista_magie2,[],[]) #TODO
    osuba_set3 = Set_magia("SET MOLTO BILANCIATO",osuba_lista_magie3,[],[]) #TODO

    lista_set_osuba = [
        osuba_set1,
        osuba_set2,
        osuba_set3
    ]
    
    osuba = Alleato(
        NOME = "OSUBA",
        COLORE = "GIALLO", #TODO
        vita_massima = 200,
        AGILITA = 20,
        POSSIBILITA_CRIT = 20,
        potenza_magie = 15,
        DIFESA = 10,
        lista_set = lista_set_osuba,
        sp_massimi = 40,
    )
    #creazione classe ...#TODO
    magia6 = Magia("SIGILLO",999,"bho",True,False,osuba._vita_massima - 1) #TODO DA NON LASCIARE
    osuba_lista_magie3 = [magia5,magia6]
    osuba_set3 = Set_magia("SET MOLTO BILANCIATO",osuba_lista_magie3,[],[])

    lista_set_osuba = [
        osuba_set1,
        osuba_set2,
        osuba_set3
    ]
    osuba._lista_set = lista_set_osuba

    lista_giocatori = [osuba] #TODO
    continuare = True
    while continuare:
        continuare = False
        turno(lista_giocatori)
        non_valido = True
        x = input("\n")#così facendo le statistiche si possono leggere
        while non_valido:
            os.system(clear)
            risposta = str(input("VUOI INIZIARE UN ALTRA BATTAGLIA?\n\nyes\nno\n"))
            if risposta == "yes" or risposta == "no":
                non_valido = False

        if risposta == "yes":
            continuare = True
        elif risposta == "no":
            continuare = False
            os.system(clear)
            print("Grazie per aver giocato,\n\nspero che la DEMO sia stata a priva di BUG!\n\nArlo.")

main()