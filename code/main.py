import os
from random import choice
from funzioni_jrpg import Alleato,Nemico,Set_magia,Magia,Entita

def main():
    #creazione classe OSUBA
    magia1 = Magia("bomba esplosiva",1,"fuoco",True,True,12)
    magia2 = Magia("freccia infuocata",2,"fuoco",False,True,6)
    magia3 = Magia("testata",2,"bho",False,False,12) #TODO cambiare il tipo di magia
    magia4 = Magia("pugno",1,"bho",False,True,6)
    magia5 = Magia("ISTAKILL",19,"bho",False,True,1) #TODO DA NON LASCIARE
    magia6 = Magia("SIGILLO",999,"bho",True,False,osuba._vita_massima - 1) #TODO DA NON LASCIARE
    magia7 = Magia("PERFORAZIONE",3,"osserva",False,True,20)

    osuba_lista_magie1 = [magia1,magia2,magia7]
    osuba_lista_magie2 = [magia3,magia4]
    osuba_lista_magie3 = [magia5,magia6]
    
    osuba_set1 = Set_magia(osuba_lista_magie1,[],[]) #TODO
    osuba_set2 = Set_magia(osuba_lista_magie2,[],[]) #TODO
    osuba_set3 = Set_magia(osuba_lista_magie3,[],[]) #TODO

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
        lista_set = lista_set_osuba
    )
    #creazione classe ...#TODO

    lista_giocatori = [osuba] #TODO

main()