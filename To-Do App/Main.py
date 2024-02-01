# from Functions import get_todos, write_todos

import Functions
import time


prompt = "Type add, show, edit, complete, or exit: "

# 'A','B','C','D','E' - for list generation
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:

    user_action = input(prompt).lower()

    if user_action.startswith('add'):

        todo = user_action[4:] + "\n"
        todos = Functions.get_todos()
        todos.append(todo.capitalize())

        Functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = Functions.get_todos()

        for index, i in enumerate(todos):
            i = i.title().strip('\n')
            row = f"{index + 1}-{i}"
            print(row)

    elif user_action.startswith('edit'):

        todos = Functions.get_todos()

        print("Your current todos are:")
        for index, i in enumerate(todos):
            i = i.title().strip('\n')
            row = f"{index+1}-{i}"
            print(row)

        number = int(input("What is the number of the item you want to edit?"))
        number = number - 1
        existing_todo = todos[number].strip('\n')
        new_todo = input(f"What do you want to change {existing_todo} to?").capitalize() + '\n'
        todos[number] = new_todo

        print("Your Todo list is now:")
        for index, i in enumerate(todos):
            i = i.title().strip('\n')
            row = f"{index + 1}-{i}"
            print(row)

        Functions.write_todos(todos)

    elif user_action.startswith('complete'):
        print("Your current list of Todos is:")

        todos = Functions.get_todos()

        for index, i in enumerate(todos):
            i = i.title().strip('\n')
            row = f"{index + 1}-{i}"
            print(row)

        item_delete = int(input("What number Todo do you want to delete?"))

        try:
            todos.pop(item_delete-1)
        except IndexError:
            print("That's an invalid command")
            continue

        print("Your Todo list is now:")

        for index, i in enumerate(todos):
            i = i.title().strip('\n')
            row = f"{index + 1}-{i}"
            print(row)

        print("Keep it up!")

        Functions.write_todos(todos)

    elif user_action.startswith('exit'):
        break

    else:
        print("Entered an invalid command")

print("Bye!")
