import py_cui
from art import text2art
py_cui.WHITE_ON_RED
root = py_cui.PyCUI(7, 9)


Art = text2art("KEKW",font="sub-zero")
root.add_block_label(Art, 0, 0, row_span = 3, column_span = 3, padx = 1, pady = 0)
root.text_block.add_text_color_rule('+', py_cui.GREEN_ON_BLACK, 'startswith')
root.start()
py_cui.WHITE_ON_RED