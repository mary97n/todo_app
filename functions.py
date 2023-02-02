TODOS_PATH = "todos.txt"

def get_todos(path=TODOS_PATH):
    """ Gets the todos form the file "files/todos.text" """
    with open(path, 'r') as file:
        todos_def = file.readlines()
    return todos_def


def write_todos(todos_arg, path=TODOS_PATH):
    """ Writes the todos in the file "files/todos.text" """
    with open(path, 'w') as file:
        file.writelines(todos_arg)