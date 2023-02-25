'''about to add random list and then ask user do you want to add new item if yes then
see if item is in list then show that its already in the list and show the list if not then
show the list with new item '''

print("Enter range for random list :")
list_rng =int(input())
list=[]
for i in range(list_rng):
    enterd_list = input("Enter first no #{}: ".format(i + 1))
    list.append(enterd_list)

print("Your enterd list :",list)

print("Do you want to add an item y/n ")
x=input()

if x=="y":
    print("Add new item in list")
    new_item=input()

    if new_item in list:
            print("This item already exist in the list")
    else:
        list.append(new_item)
        print("list with new item : ",list)
else:
    print("please enter y for continue")

