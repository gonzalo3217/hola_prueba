def factorial(n):
    if n == 0:
        return 1
    else:
         return n * factorial(n - 1)
         
number = 5
result = factorial(number)
print(f"El factorial de {number} es {result}."             
	
