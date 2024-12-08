from flask import Flask, render_template, request
from linked_list import LinkedList

app = Flask(__name__)
linked_list = LinkedList()

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/linked_list', methods=["POST", "GET"])
def linked_list_view():
    success_message = None
    # Handle POST request (form submission)
    if request.method == "POST":
        user_input = request.form.get('input') 
        action = request.form.get('action')  

        if action == 'insert_beginning':
            linked_list.insert_at_beginning(user_input)
            success_message = "Item successfully inserted at the beginning!"

        elif action == 'insert_end':
            linked_list.insert_at_end(user_input)
            success_message = "Item successfully inserted at the End!"

        elif action == 'remove_beginning':
            if linked_list.remove_beginning():
                success_message = "Successfully Removed from Beginning!"
            else:
                success_message = "Failed to Remove from Beginning. The list is empty."

        elif action == 'remove_end':
            if linked_list.remove_at_end():
                success_message = "Successfully Removed from End!"
            else:
                success_message = "Failed to Remove from End. The list is empty."

        elif action == 'remove_position':
            if linked_list.remove_at(user_input):
                success_message = f"Successfully Removed {user_input}!"
            else:
                success_message = f"Failed to Remove {user_input}. The item was not found."

        elif action == 'search':
            if linked_list.search(user_input):
                success_message = "Item Found"
            else:
                success_message = "Item Not Found"

        elif action == 'print':
            result = linked_list.print_linked_list()
            if result == False:
                success_message = "Linked list is Empty"
            else:
                success_message = f"{result}"       
            
    return render_template('LINKED LIST.html', success_message=success_message)



@app.route('/stack')
def stack():
    return render_template('STACK.html')

@app.route('/queue')
def queue():
    return render_template('QUEUE.html')

@app.route('/binary_tree')
def tree():
    return render_template('BINARY TREE.html')


if __name__ == '__main__':
    app.run(debug=True)