user_prompt = "Type add, show or exit: "
todos = []

while True:
    user_action = input(user_prompt)

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for todo in todos:
                print(todo)
        case 'exit':
            print('Bye!')
            break
        case _:
            print("Hey, you've entered a wrong command")
