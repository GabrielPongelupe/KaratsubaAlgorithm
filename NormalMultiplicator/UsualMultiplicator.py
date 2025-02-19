# Código de múltiplicação normal (usual aprendido nas escolas) feito APENAS para prática e exercício.


def multiply_numbers(U, V):
    n = len(U)
    product = [0] * (2 * n)  
    
    for i in range(n-1, -1, -1): 
        carry = 0  
        for j in range(n-1, -1, -1):  
            temp_product = U[i] * V[j] + product[i + j + 1] + carry
            product[i + j + 1] = temp_product % 10 
            carry = temp_product // 10 
        
        product[i + j] += carry  
    
    while len(product) > 1 and product[0] == 0:
        product.pop(0)

    return product


# Example usage:
U = [1, 2, 3]  
V = [4, 5, 6]  

result = multiply_numbers(U, V)
print("Multiplication result:", result)  # Output will be the list [5, 6, 0, 8, 8]
