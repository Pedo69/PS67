import time
print('*****calculate sum of odd and even number between 1-N (Exit press 0)*****')
odd = 0
even = 0
while True:
    first_num = 1
    last_num = int(input("Enter you number 'N' (Exit press 0):"))
    
    start = time.time()
    for i in range(first_num, last_num + 1):
    
        if i % 2 == 0:
            even += i

        elif i % 2 != 0:
            odd += i

    if last_num == 0: 
        print('*****End Programe*****')
        break

    print(f'Time taken: { (time.time()-start) * 1000:.2f} ms')
    print(f'sum of odd number = {odd}')
    print(f'sum of even number = {even}')


