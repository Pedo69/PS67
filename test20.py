# Python program to demonstrate
# Adding Elements to a Array
# importing "array" for array creations
import array as arr
# array with int type
a = arr.array('i', [1, 2, 3])
print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
# inserting array using
# insert() function
a.insert(1, 4)
a.append(5)
a.remove(2)
print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()