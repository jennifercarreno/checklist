
checklist = list()
# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

# checklist[1] = 'Cats'
# checklist.pop(1)
# print(checklist)

#create
def create(item):
    checklist.append(item)

#read
def read(index):
    item = checklist[index]
    return item

#update 
def update(index, item):
    checklist[index] = item

#destroy
def destroy(index):
    checklist.pop(index)

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
   # print(read(1))

test()