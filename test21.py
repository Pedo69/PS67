import array as number
a = number.array('i', [50, 87, 65, 39])
print ("Array before insertion : ", end =" ")
for i in range (0, 4):
    print (a[i], end =" ")
print()
print(max(a), min(a))
print(f'sum = {sum(a)}, ave = {sum(a) / 4}')
print(sorted(a))
print(sorted(a)[::-1])
odd_num = [x for x in a if x % 2 != 0]
print(odd_num)
even_num = [x for x in a if x % 2 == 0]
print(even_num)