FILEPATH = "/Users/iantgillespie/PycharmProjects/GetMyLifeTogether/To-Do App/todos.txt"


def get_todos(filepath=FILEPATH):
    """Opens the existing Todos
    1 arg which is the filepath, defaults to todos.txt
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """Writes to the existing Todos
      2 params which are a list to add to the todos file and
      the filepath which defaults to todos.txt
      """
    with open(filepath, "w") as file:
        file.writelines(todos_local)
