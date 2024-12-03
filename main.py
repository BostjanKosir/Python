numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
operations = [ '*' ]

for num1 in numbers:
    for num2 in numbers:
        for operation in operations:
            if operation == '/' and num2 == 0:

                continue
            result = eval(f'{num1}{operation}{num2}')
            if 0 < result <= 99:
                print(f"{num1}{operation}{num2} = {result}")