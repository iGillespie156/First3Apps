import Functions as fun

import PySimpleGUI as pg

label = pg.Text("Type in a to-do:")
input_box = pg.InputText(tooltip="Enter to-do", key = "todo")
add_button = pg.Button("Add")

window = pg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button]],
                   font=('Helvetica', 20))


while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = fun.get_todos()
            new_todo = values["todo"] +'\n'
            todos.append(new_todo)
            fun.write_todos(new_todo)
        case pg.WIN_CLOSED:
            break



    print(todos)

    print(event)
window.close()





