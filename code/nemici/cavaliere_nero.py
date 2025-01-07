from funzioni_jrpg import Nemico,Set_magia,Magia

magia5 = Magia("colpo con spada",3,"bho",True,True,1)
lista_magie_cavaliere = [magia5]

set_cavaliere = Set_magia("",lista_magie_cavaliere,[],[])
lista_set_cavaliere = [set_cavaliere]

cavaliere_nero = Nemico("Cavaliere nero",3,"red",120,4,2,2,10,lista_set_cavaliere,None,15.5)