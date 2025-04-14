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

# def test():
    # print("test")
# 
# class Menu:
# 
    # def __init__(self, master: py_cui.PyCUI):
# 
        # self.master = master
# 
        # The scrolled list cells that will contain our tasks in each of the three categories
        # self.todo_scroll_cell = self.master.add_scroll_menu('INVENTORY', 0, 0, row_span=5, column_span=1)
        # self.in_progress_scroll_cell = self.master.add_scroll_menu('BATTLE FIELD', 0, 1, row_span=2, column_span=2)
        # 
        # 
        # self.add_block_lable = self.master.add_block_label("OSUBA", 3, 1, row_span = 1, column_span = 1, padx = 0, pady = 0)
# 
        # self.bottone = self.master.add_button("ATTACK",row=4,column=1,row_span=1,column_span=1,padx=1,pady=0,command=test)
        # 
        # 
# 
# Create the CUI with 7 rows 6 columns, pass it to the wrapper object, and start it
# root = py_cui.PyCUI(7, 6)
# root.set_title('A_simple_JRPG_on_the_CMD_RE-COMMITTED')
# s = Menu(root)
# 
# root.start()