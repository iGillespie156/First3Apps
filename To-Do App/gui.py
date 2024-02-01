import Functions

import PySimpleGUI as pg

label = pg.Text("Type in a to-do:")
input_box = pg.InputText(tooltip="Enter to-do")
add_button = pg.Button("Add")

window = pg.Window('My To-Do App', layout=[[label], [input_box, add_button]])

window.read()
print("hello")
window.close()





