# Taking multiple inputs from the user
user = input('>').split(" ")  # splitting the inputs with spaces by 'split'

# Assigning lists
list1 = []  # for user input
list2 = []  # for the output


for i in user:
    list1.append(i)  # appending the inputs into list1

# Checking for the symmetry
for i in list1:
    if i == i[::-1]:
        list2.append(True)
    else:
        list2.append(False)

# Printing outputs
if True in list2:
    print("True")
else:
    print("False")