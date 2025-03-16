import os
from test_py_cui import main
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


main()