
#  input from user for number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

#  multidimensional array with the given number of rows and columns
multi_array = [[0 for x in range(cols)] for i in range(rows)]

# Print the multi array
for i in range(rows):
    for x in range(cols):
        print(multi_array[i][x], end=" ")
    print()
   