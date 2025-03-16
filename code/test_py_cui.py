import py_cui

import os
from funzioni_jrpg import *


from nemici.cavaliere_nero import cavaliere_nero
from nemici.cavaliere_normale import cavaliere_normale
from nemici.goblin import goblin

#importazione dei personaggi;
from giocatori.osuba import osuba
from giocatori.galo import galo

#importazione dei nemici

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
    # while continuare:
        # continuare = False
        # partita_vinta = turno(lista_giocatori,lista_nemici_tutti)
        # if partita_vinta == True:
            # non_valido = True
            # while non_valido:
                # os.system(clear)
                # risposta = str(input("VUOI INIZIARE UN ALTRA BATTAGLIA?\n\nyes\nno\n"))
                # if risposta == "yes" or risposta == "no":
                    # non_valido = False
        # else:
            # print("\ \ \ HAI PERSO \ \ \\")
            # x = input("\n")
            # risposta = "no"
# 
        # if risposta == "yes":
            # continuare = True
        # elif risposta == "no":
            # continuare = False
            # os.system(clear)
            # print("Grazie per aver giocato,\n\nspero che la DEMO sia stata a priva di BUG!\n\nArlo.")

main()

class Menu:

    def __init__(self, master: py_cui.PyCUI):

        self.master = master

        # The scrolled list cells that will contain our tasks in each of the three categories
        self.todo_scroll_cell = self.master.add_scroll_menu('INVENTORY', 0, 0, row_span=5, column_span=1)
        self.in_progress_scroll_cell = self.master.add_scroll_menu('BATTLE FIELD', 0, 1, row_span=2, column_span=2)
        
        
        self.add_block_lable = self.master.add_scroll_menu("osuba", 0, 1, row_span = 1, column_span = 1, padx = 1, pady = 0)

        self.add_block_lable.add_text_color_rule('I', py_cui.GREEN_ON_BLACK, 'startswith')
        
        

# Create the CUI with 7 rows 6 columns, pass it to the wrapper object, and start it
root = py_cui.PyCUI(7, 6)
root.set_title('A_simple_JRPG_on_the_CMD_RE-COMMITTED')
s = Menu(root)

root.start()