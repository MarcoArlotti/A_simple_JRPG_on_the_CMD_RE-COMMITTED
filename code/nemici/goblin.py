from funzioni_jrpg import Nemico,Set_magia,Magia

magia3 = Magia("testata",2,"bho",False,True,1) #TODO cambiare il tipo di magia
magia4 = Magia("pugno",1,"bho",False,True,1)
magia5 = Magia("colpo con spada",3,"bho",True,True,1)
magia6 = Magia("carica",3,"bho",False,True,1)

lista_magie_goblin = [magia3,magia4]

set_goblin = Set_magia("",lista_magie_goblin,[],[])
lista_set_goblin = [set_goblin]

goblin = Nemico("Goblin",1,"red",86,30,10,10,20,lista_set_goblin,None,10)