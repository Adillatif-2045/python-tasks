'''this is about if a key is already exist in list then print list already has this key
 so choose another otherwise append that key and value in list.'''
#take range and item of list from user
print("Enter your list range :")
list_rng =int(input())
list=[]
for i in range(list_rng):

    enterd_list = input("Enter first no #{}: ".format(i + 1))
    list.append(enterd_list)

print("Your enterd list :",list)
#check if length of list is less than 10
if len(list)<10:

    key=input("Enter key :")
    value=input("Enter value :")
#check if key is in list
    if key in list :
        print("This key is already filled in list please choose another one!! ")

    else:

        list.append((key,value))

        print("list with key and value: ",list)
#it will print if len of list is >= 10
else:
    print("list is already full you can not add more items")


#end of code.













