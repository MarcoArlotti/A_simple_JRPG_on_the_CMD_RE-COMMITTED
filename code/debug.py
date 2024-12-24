#import py_cui
from funzioni_jrpg import Entita, Magia, Set_magia




test_magia1 = Magia("bomba",2,"esplosivo",True,True,10)
test_magia2 = Magia("bomba",3,"esplosivo",True,True,14)
test_magia3 = Magia("dwdw",3,"esplosivo",True,True,14)
test_lista_magie = [test_magia1,test_magia2]

test_lista_magie2 = [test_magia3]

test_debolezze = ["acqua"]
test_debolezze2 = ["fuoco"]
test_cosa_annulla = []

#set_magia
test_set_magia1 = Set_magia(test_lista_magie,test_debolezze,test_cosa_annulla)
test_set_magia2 = Set_magia(test_lista_magie,test_debolezze2,test_cosa_annulla)
test_set_magia3 = Set_magia(test_lista_magie2,test_debolezze,test_cosa_annulla)
#lista_set
test_lista_set = [test_set_magia1,test_set_magia2]

test_entita = Entita("osuba","giallo",200,20,10,10,20,test_lista_set)
print(test_entita.cambia_set(test_set_magia3))

print(test_entita.cambia_set(test_set_magia1))
