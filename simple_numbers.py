def calc():
    num_a = int(input('Input number a:'))
    num_b = int(input('Input number b:'))
    for i in range(num_a, num_b + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0 and i != j and j != 1:
                count += 1
        if count == 0:
            print(f'Simple numbers from {num_a} to {num_b}: {i}')


calc()