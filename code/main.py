# importazione delle varie funzioni per far funzionare il gioco
from funzioni_jrpg import turno
import os

# importazione dei personaggi;
from giocatori.osuba import osuba
from giocatori.galo import galo

# libreria che rende compatibile il codice sia per linux che per windows
from sys import platform

if platform == "linux":
    clear = "clear"
elif platform == "win32":
    clear = "cls"


def main():
    global lista_giocatori

    lista_giocatori = [osuba, galo]  # TODO

    continuare = True
    while continuare:
        continuare = False
        partita_vinta = turno(lista_giocatori)
        if partita_vinta == True:
            non_valido = True
            while non_valido:
                os.system(clear)
                risposta = str(input("VUOI INIZIARE UN ALTRA BATTAGLIA?\n\nyes\nno\n"))
                if risposta == "yes" or risposta == "no":
                    non_valido = False
        else:
            print("\ \ \ HAI PERSO \ \ \\")

            risposta = "no"

        if risposta == "yes":
            continuare = True

        elif risposta == "no":
            continuare = False
            os.system(clear)
            print(
                "Grazie per aver giocato,\n\nspero che la DEMO sia stata a priva di BUG!\n\nArlo."
            )


main()
