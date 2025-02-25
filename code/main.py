import os
from funzioni_jrpg import *


from nemici.cavaliere_nero import cavaliere_nero
from nemici.cavaliere_normale import cavaliere_normale
from nemici.goblin import goblin

#importazione dei personaggi;
from giocatori.osuba import osuba
#from giocatori.galo import galo

#importazione dei nemici

from sys import platform

if platform == "linux":
    clear = "clear"   
elif platform == "win32":
    clear = "cls"

def main():
    lista_giocatori = [osuba] #TODO
    lista_nemici_tutti = [goblin,cavaliere_nero,cavaliere_normale] #TODO

    continuare = True
    while continuare:
        continuare = False
        partita_vinta = turno(lista_giocatori,lista_nemici_tutti)
        if partita_vinta == True:
            non_valido = True
            while non_valido:
                os.system(clear)
                risposta = str(input("VUOI INIZIARE UN ALTRA BATTAGLIA?\n\nyes\nno\n"))
                if risposta == "yes" or risposta == "no":
                    non_valido = False
        else:
            print("\ \ \ HAI PERSO \ \ \\")
            x = input("\n")
            risposta = "no"

        if risposta == "yes":
            continuare = True
        elif risposta == "no":
            continuare = False
            os.system(clear)
            print("Grazie per aver giocato,\n\nspero che la DEMO sia stata a priva di BUG!\n\nArlo.")
main()