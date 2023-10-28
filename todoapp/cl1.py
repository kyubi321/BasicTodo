import time

from functions_todo import read_text, write_lines
import functions_todo
# now we want to add a time statement in our program so to do that we need ,
# the time module to be imported in the program
#now check out time functions, here we used strftime which returns time in string format
print(time.strftime("Data: %d-%m-%y , Time : %H:%M:%S  "))
print("stupid")
todos = []
while True:
    something = input("choose an option : \n"
                      "  1.add\n  2.show\n  3.exit\n  4.edit\n  5.replace\n  6.complete\n  7.clear\n :")
    # function integration
    todos = read_text()
    something = something.strip()

    if something.startswith('add'):
        value = something[4:] + "\n"
        todos.append(value)
        with open('text.txt', 'a+') as file:
            file.writelines(value)

    elif "show" in something or 'display' in something:
        file = read_text()

            # list comprehension methods
            # new_todo = [x.strip('\n') for x in file]

        for index, items in enumerate(file):
            items = items.strip('\n')
            print(f"{index + 1}.{items.title()}")

    elif "exit" in something:
        print("you have successfully exited from the app  ")
        break

    elif something.startswith('edit'):
        try:
            ethane = int(something[5:])
            ethane = ethane - 1
            puthiyea = input("matti addi vedalle :") + "\n"
            todos[ethane] = puthiyea

            todos = write_lines(todos)
            print("mattikne myrea nookiyum kandokke addi iniyenkilum")
        except ValueError:
            print("your command is not valid")
            # using continue because the continue statement exits ignores the rest of the lines under it then executes the while loop next
            continue

    elif "replace" in something:
        try:
            ethane = int(something[8:])
            ethane = ethane - 1
            repl = input("enter the string to be replaced")
            cont = input("enter the content to be replaced")
            todos[ethane] = todos[ethane].replace(repl, cont)
            todos = write_lines(todos)
        except ValueError:
            print("your command is not valid retype again ")
            continue
    elif "complete" in something:
        try:
            ethane = int(something[8:])
            ethane = ethane - 1
            value = todos[ethane].strip('\n')
            todos.pop(ethane)
            todos = write_lines(todos)
            print(f'{value} is removed')
        except IndexError:
            print("theres no such item in the list")

    elif "clear" in something:
        with open('text.txt', 'w+') as f:
            f.truncate(0)

    else:
        print("you have printed some shit retype it bitch :")

print("go die")
