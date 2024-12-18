import py_cui
from art import text2art
import inizio_run
import combattimento
py_cui.WHITE_ON_RED
root = py_cui.PyCUI(7, 9)

#primo valore determina quanto spazio verso il basso
#secondo valore determina quanto spazio verso destra
#terzo valore determina di quanto fare alta la grandezza del widget
#quarto valore quanto largo il widget
#?????
#?????
inizio_run.inizio_run()
Art = text2art("KEKW",font="sub-zero")
#root.add_block_label("test fraidoo", 0,0,3,3,1,0)
root.add_button("test fraido",0,3,1,1,3,3)

#root.text_block.add_text_color_rule('+', py_cui.GREEN_ON_BLACK, 'startswith')
root.start()
