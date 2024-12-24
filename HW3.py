import time  # big o มีค่า O(1)

last_num = int(input("Enter your number 'N':"))   

start = time.time()

k = last_num // 2  
sum_of_evens = k * (k + 1)  

m = (last_num + 1) // 2  
sum_of_odds = m * m  

end = time.time()

print(f'Time taken: {(end - start) * 1000:.2f} ms')
print(f'sum of odd number = {sum_of_odds}')
print(f'sum of even number = {sum_of_evens}')
