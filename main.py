user_prompt = "Type add, show, edit, complete or exit: "
todos = []

while True:
    user_action = input(user_prompt)

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, todo in enumerate(todos):
                print(f"{index+1}. {todo}")
        case 'edit':
            number_to_edit = int(input("What number of todo you want to edit? "))
            todos[number_to_edit - 1] = input(f"Reenter number {number_to_edit} todo: ")
        case 'complete':
            number_to_complete = int(input("What number of todo you want to complete? "))
            todos.remove(todos[number_to_complete - 1])
        case 'exit':
            print('Bye!')
            break
        case _:
            print("Hey, you've entered a wrong command")
