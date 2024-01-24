def get_todos(filepath = "Sec12_App1_ToDo/todos.txt"):
    """ Read a text file and return the list of
    to-do items."""
    with open(filepath, "r") as local_file:
        todos_local = local_file.readlines()
    return todos_local

print(help(get_todos))

def write_todos(todos_arg, filepath = "Sec12_App1_ToDo/todos.txt"):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
print(help(write_todos))