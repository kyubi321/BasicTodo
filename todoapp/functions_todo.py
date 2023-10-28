def read_text():
    with open('text.txt', 'r') as f:
        todos = f.readlines()

    return todos


def write_lines(todos):
    with open('text.txt', 'w+') as f:
        f.writelines(todos)
    return todos


if __name__ == '__main__':
    print("welcome to the todo app")