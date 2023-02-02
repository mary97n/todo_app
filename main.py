import functions, time

print(f"Today is {time.strftime('%b %d, %Y %H:%M:%S')}")
while True:
    # Ask user
    user_action = input("Type add, complete, edit, exit or show: ").lower().strip()

    # add
    if user_action.startswith("add") or user_action.startswith("new"):
        todos = functions.get_todos()

        # Adding the todos
        todos.append(user_action[4:].title() + '\n')

        functions.write_todos(todos)
    # show
    elif user_action.startswith("show") or user_action.startswith("display"):
        todos = functions.get_todos()

        # Printing each todos
        for n, i in enumerate(todos):
            i = i.replace('\n', '', 1)
            print(f"{n + 1}. {i}")
    # edit
    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()

            # Asking for the new todos and adding them
            index = int(user_action[5:])
            todos[index] = input("Enter new todo: ").title() + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    # complete
    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            # Deleting the todos
            index = int(user_action[9:])
            todo = todos[index].replace('\n', '', 1)
            print(f"Todo '{todo}' completed")
            todos.pop(index)

            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue
    # exit
    elif user_action.startswith("exit"):
        print("Bye!")
        break
    else:
        print("Command is not valid")