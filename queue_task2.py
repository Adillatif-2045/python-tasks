# fixed size list
size=5
list=[]
for i in range(size):
    fixed_list = input("Enter list item #{} : ".format(i + 1))
    list.append(fixed_list)
print("your list is :", list)

#ask user to add item

print("Do you want to add an item y/n ")
x=input()
if x=="y":

#if user say y then  ask him to add item
    print("Add item in list")
    new_item=int(input())

# pop last item from list
    list.pop()

#insert item at 0 index of list

    list.insert(0,int(new_item))
    print("your new list with new item : ",list)
else:

#if user dont say y then show this msg

    print("invalid input please try again with y ")

#end of code



















