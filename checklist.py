
checklist = list()

#create
def create(item):
    checklist.append(item)

#read
def read(index):
    item = checklist[int(index)]
    print(item)
    return item

#update 
def update(index, item):
    checklist[index] = item

#destroy
def destroy(index):
    checklist.pop(index)

#list all items
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

#mark completed
def mark_completed(index):
    checklist[index] = "√ {}".format(checklist[index])
    print(checklist[index])
    return checklist[index]

def select(function_code):
    function_code = function_code.upper()
    #create item
    if function_code == "A":
        input_item = user_input("Input Item: ")
        create(input_item)
    #read item
    elif function_code == "R":
        item_index = user_input("Index Number? -> ")
        read(item_index)
    #Update item
    elif function_code == "U":
        index = user_input("Index Number: ")
        item = user_input("Input Item: ")
        update(int(index), item)
    #mark as complete 
    elif function_code == "C":
        index = user_input("Index Number: ")
        mark_completed(int(index))
    #print all items
    elif function_code == "P":
        list_all_items()
    #stops the loop
    elif function_code == "Q":
        return False
    #catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

running = True
while running:
    selection = user_input(
        "Press A to add to list, R to Read from list, U to update list, C to mark as completed, and P to display list and Q to quit -> ")
    running = select(selection)