import os
from random import choice
from funzioni_jrpg import Alleato,Nemico,Set_magia,Magia,Entita,turno
#importazione dei personaggi;
from osuba import osuba

from sys import platform

if platform == "linux":
    clear = "clear"   
elif platform == "win32":
    clear = "cls"

def main():
    lista_giocatori = [osuba] #TODO

    continuare = True
    while continuare:
        continuare = False
        turno(lista_giocatori)

        non_valido = True
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