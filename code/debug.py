import py_cui
from art import text2art
from termcolor import colored
py_cui.WHITE_ON_RED
root = py_cui.PyCUI(7, 8)

#primo valore determina quanto spazio verso il basso
#secondo valore determina quanto spazio verso destra
#terzo valore determina di quanto fare alta la grandezza del widget
#quarto valore quanto largo il widget
#?????
#?????
def attacca():
    pass
#Art = text2art("osuba",font="sub-zero")
#root.add_block_label(Art,row=0,column=0,row_span=2,column_span= 2,padx= 0,pady= 0,center= False)
#
menu_item_list = ["Item1", "Item2", "dsadasdf","Item1", "Item2", "dsadasdf","Item1", "Item2", "dsadasdf","Item1", "Item2", "dsadasdf",]

menu = root.add_scroll_menu("fabio", row=4, column=4, row_span = 1, column_span = 1, padx = 1, pady = 0)
menu.add_item_list(menu_item_list)
menu.add_mouse_command()
#root.add_button("attacca",row=4,column=0,row_span=2,column_span= 2,padx= 0,pady= 0,command=attacca())
#root.add_block_label(Art2,row=0,column=0,row_span=2,column_span= 2,padx= 0,pady= 0,center= False)
#root.text_block.add_text_color_rule('+', py_cui.GREEN_ON_BLACK, 'startswith')
root.start()
