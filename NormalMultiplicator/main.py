from UsualMultiplicator import multiply_numbers 

numberOne = int(input("Digite o primeiro número: "))
numberTwo = int(input("Digite o segundo número: "))

# Converte os números para listas de dígitos
digitsOne = [int(d) for d in str(numberOne)]
digitsTwo = [int(d) for d in str(numberTwo)]

# Multiplica os números e obtém a lista de dígitos do resultado
result = multiply_numbers(digitsOne, digitsTwo)

# Converte a lista de volta para um número inteiro
resultNumber = int("".join(map(str, result)))

print(f"Resultado: {numberOne} * {numberTwo} = {resultNumber}")