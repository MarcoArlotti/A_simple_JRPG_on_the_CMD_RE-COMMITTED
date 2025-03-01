from funzioni_jrpg import *

vita_massima = 200
#creazione delle varie magie di osuba (un personaggio)
magia6 = Magia("SIGILLO",999,"bho",True,False,vita_massima - 1) #TODO DA NON LASCIARE
magia1 = Magia("BOMBA",1,"fuoco",True,True,12)
magia2 = Magia("FRECCIA INFUOCATA",2,"fuoco",False,True,6)
magia3 = Magia("TESTATA",2,"bho",False,False,12) #TODO cambiare il tipo di magia
magia4 = Magia("PUGNO",1,"bho",False,True,6)
magia5 = Magia("INSTAKILL",19,"bho",False,True,1) #TODO DA NON LASCIARE

magia7 = Magia("PERFORAZIONE",3,"osserva",False,True,20)

#creazione delle varie liste di magie da mettere nei set
magia_s_1 = Magia_speciale("salta_turno",2,"SPECIALE",False,True,10,1)
magia_s_2 = Magia_speciale("attacco_2_turni",2,"SPECIALE",False,True,10,2)

osuba_lista_magie1 = [magia1,magia2,magia7,magia5,magia6,magia_s_1,magia_s_2]
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
#per colpa della magia "SIGILLO" osuba si può creare solo verso la fine
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

magia6 = Magia("SIGILLO",999,"bho",True,False,osuba._vita_massima - 1) #TODO DA NON LASCIARE (POSSIBILE MECCANICA END GAME)

osuba_lista_magie3 = [magia5,magia6]

osuba_set3 = Set_magia("SET MOLTO BILANCIATO",osuba_lista_magie3,[],[])

lista_set_osuba = [
    osuba_set1,
    osuba_set2,
    osuba_set3
]

#assegnazione dek set creati a osuba
osuba._lista_set = lista_set_osuba