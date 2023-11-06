# import necessary modules in the program
import traceback
import functions_todo as ft
import PySimpleGUI as pg
import time




pg.theme("light green 6")
# create a label for your window
label = pg.Text("death note")

# create an input box for window
input_box = pg.InputText(tooltip="enter todo", key="todo")

# create a button in the todoapp window
button = pg.Button("Add")

# create a list box to show the list box
# the size in pysimplegui works in a way that [w,h] w is width, h is height.
list_box = pg.Listbox(values=ft.read_text(), enable_events=True, size=(45, 10), key="todos_list")

# adding a clock on top of the app
clock = pg.Text('',key="clock")


# create an edit button to edit the contents in the todos
edit = pg.Button("Edit")
complete = pg.Button("completed")
clear = pg.Button("Clear")
exit = pg.Button('Exit')

# the window of todoapp, as you put values inside the layout put it in the list such a way that elements together must be kept together
window = pg.Window("my to do app", layout=[[clock],[[label], input_box], [list_box],[button,edit,complete,clear,exit]],
                   font=("Helvetica", 15))

# to keep the window open until we break the window that is close button.
while True:
    # tracking the event and values using two variables
    # adding time out in the read to refresh the app in every 200 milliseconds
    event, values = window.read(timeout=200)
    # adding the clock value in the loop.
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # now when each user action leads to value change in events so by using that we access the match case

    match event:

        # when the event is add we read the file and append the new data into the file
        # and this is only done when there is a value in the input box

        case "Add":
            if values['todo'] == '':
                continue
            else:
                todos = ft.read_text()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                ft.write_lines(todos)

                # this code is used to update our listbox in real time
                window['todos_list'].update(todos)

        # this case is used just to show our selection in the listbox in input box also
        case "todos_list":
            try:
                window['todo'].update(values['todos_list'][0])
            except:
                pg.popup('no todo present',font=('Helvetica',18))

        # this case edits the present todolist
        case "Edit":
            try:

                # we read the file and retrive the list
                todos = ft.read_text()

                # then select the value to edit from list box
                edit_todo = values['todos_list'][0]

                # take the index
                index = todos.index(edit_todo)

                # retrieve the value that is used to updata
                update_todo = values['todo'] +'\n'

                # update the todos list
                todos[index] = update_todo

                # write the todos list in the app
                ft.write_lines(todos)

                # update the list box
                window['todos_list'].update(todos)

            except IndexError as e:
                # to capture the error use traceback
                tb = traceback.format_exc()
                # to show a error information in the window use this.
                # pg.Print(f" an error happened .here is the info ", e,tb)
                pg.popup(f'choose a value to edit',font=('Helvetica',18))

        case "completed":
            try:
                todos = ft.read_text()
                completed_todo = values['todos_list'][0]
                todos.remove(completed_todo)
                ft.write_lines(todos)
                window['todos_list'].update(todos)
                window['todo'].update('')
            except IndexError as e:
                tb = traceback.format_exc()
                pg.popup("no element in the list \n try adding some !!!", font=('Helvetica',18))
        case "Clear":
            todos = ft.read_text()
            todos.clear()
            ft.write_lines(todos)
            window['todos_list'].update([''])
        case "Exit":
            break
        # this case is used to close the window if user clicks the close button.
        case pg.WIN_CLOSED:
            break
    #print(event)
   #print(values)
window.close()
