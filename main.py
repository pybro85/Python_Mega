import functions 
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    # .strip() method is used to remove any trailing space or whatsover in your input
    
    if user_action.startswith('add'):
        todo = user_action[4:]
                
        todos = functions.get_todos()
        
        todos.append(todo + '\n')
        
        
        functions.write_todos(todos, "Latest/todos.txt")
    
    elif user_action.startswith('show'): 

        todos = functions.get_todos()
        
        
        # Using list comprehension to get rid of backslashes
        # new_todos = [item.strip("\n") for item in todos]
        
        
        for index, item in enumerate(todos):
            item = item.title()
            item = item.strip("\n")
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            number = number - 1
            
            todos = functions.get_todos()
                    
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            
            functions.write_todos(todos, "Latest/todos.txt")
            
        except ValueError:
            print('Your command is not valid.')
            continue            
            
    
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            
            todos = functions.get_todos()
            
            index = number - 1            
            todo_to_remove = todos[index].strip("\n")
            
            todos.pop(index)
            
            functions.write_todos(todos, "Latest/todos.txt")
                    
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There's no item with that number")
            continue
        except ValueError:
            print("Please enter the number of the ToDo you want to complete")
            continue
        
    elif user_action.startswith('exit'):
        break
    
    # If you need to print a message in case that the user input is different from the ones that are in cases, then you can use a case with an underscore(Althoug it can be any name, underscore is the widely used coinventional form). It is called Match-case.
    else:
        print("Hey, you have entered an unknown command")

print('Bye!')
    

