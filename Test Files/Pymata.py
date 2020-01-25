from PyMata.pymata import PyMata
board=PyMata('COM6')
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(board.get_analog_mapping_request_results())