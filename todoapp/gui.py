import functions_todo
import PySimpleGUI as pg

# create a label for your window
label = pg.Text("my todo app")

# create an input box for window
input_box = pg.InputText(tooltip="enter todo")

# create a button in the todoapp window
button = pg.Button("Add")

# the window of todoapp, as you put values inside the layout put it in the list such a way that elements together must be kept together
window = pg.Window("my to do app", layout=[[[label], input_box,button],])
window.read()
window.close()