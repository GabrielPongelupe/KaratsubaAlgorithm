from karatsuba import karatsuba 

numberOne = int(input('Digite o primeiro número '))
numberTwo = int(input('Digite o segundo número '))

result = karatsuba(numberOne, numberTwo)
print(f'Resultado: {numberOne} * {numberTwo} = {result}')
