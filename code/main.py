#importazione delle varie funzioni per far funzionare il gioco
from funzioni_jrpg import *

#importazione dei nemici
from nemici.cavaliere_nero import cavaliere_nero
from nemici.cavaliere_normale import cavaliere_normale
from nemici.goblin import goblin

#importazione dei personaggi;
from giocatori.osuba import osuba
from giocatori.galo import galo

#libreria che rende compatibile il codice sia per linux che per windows
from sys import platform

if platform == "linux":
    clear = "clear"   
elif platform == "win32":
    clear = "cls"

def main():
    global lista_giocatori
    global lista_nemici_tutti

    lista_giocatori = [osuba,galo] #TODO
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
            
            risposta = "no"

        if risposta == "yes":
            continuare = True
        elif risposta == "no":
            continuare = False
            os.system(clear)
            print("Grazie per aver giocato,\n\nspero che la DEMO sia stata a priva di BUG!\n\nArlo.")

# BUG SE UN NEMICO MUORE SE CE NE è UN ALTRO DELLO STESSO TIPO, MUOIONO ENTRAMBI
main()