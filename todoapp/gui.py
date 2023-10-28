import functions_todo as ft
import PySimpleGUI as pg

# create a label for your window
label = pg.Text("my todo app")

# create an input box for window
input_box = pg.InputText(tooltip="enter todo",key="todo")

# create a button in the todoapp window
button = pg.Button("Add")

# the window of todoapp, as you put values inside the layout put it in the list such a way that elements together must be kept together
window = pg.Window("my to do app", layout=[[[label], input_box,button]],font=("Helvetica",15))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = ft.read_text()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            ft.write_lines(todos)
        case pg.WIN_CLOSED:
            break
    print(event)
    print(values)
window.close() 