#import py_cui
from function.funzioni_jrpg import Entita, Magia, Set_magia




test_magia1 = Magia("bomba",2,"esplosivo",True,True,10) #TODO
test_magia2 = Magia("bomba",3,"esplosivo",True,True,14) #TODO

test_lista_magie = [test_magia1,test_magia2]

test_debolezze = ["acqua"]
test_cosa_annulla = []

#set_magia
test_set_magia1 = Set_magia(test_lista_magie,test_debolezze,test_cosa_annulla) #TODO
test_set_magia2 = Set_magia(test_lista_magie,test_debolezze,test_cosa_annulla) #TODO
#lista_set
test_lista_set = [test_set_magia1,test_set_magia2]

test_entita = Entita("osuba","giallo",200,20,10,10,20,test_lista_set)
test_entita.cambia_set(test_set_magia1)
print(test_entita._set_in_uso)
test_entita.cambia_set(test_set_magia2)
print(test_entita._set_in_uso)