#La recursividad es cuando una función se llama a sí misma para resolver un problema, dividiéndolo en una versión más pequeña del mismo problema, hasta llegar a un punto tan simple que ya no necesita dividirse más.

def  contar_sinlimite(numero):
    print(numero)
    #contar_sinlimite(numero + 1 ) # se llam asi mismo siempre
    #NO HAY NINGUNA CONDICION QUE DETENGA ESTO


contar_sinlimite(1)

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

print(f'facrotial interativo de 6 : {factorial_iterativo(6)}')

#caso base = condicion que deteiene la recuersion , sin el, la funcion  se llamaria infinaitamente 
#caso recursion = donde la funcion se llama a si mima con un problema mas pequenio, acercandoce al caso base

def factporial_recursivo(n):
    if n==0 or n== 1:
        return 1
    else:
        return n * factporial_recursivo(n-1)
print(f'Factorial recursivo de 5: {factporial_recursivo(5)}')


# caracteristicas de los procesos recursivos 
#pila de llamada (call stack)

def factorial_visual(n, nivel = 0):
    sangria = ''* nivel
    print(f'{sangria}----> entrada con n={n}')
    if n==0 or n == 1:
        print(f'{sangria} <--- caso base, regresa 1')
        return 1 
    else:
        resultado= n *factorial_visual(n - 1, nivel +1)
        print(f'{sangria}<-- regresa {resultado} (n={n})')
        return resultado
factorial_visual(4)


def fibonacci(n):
    if n==0 : #caso base 1
        return 0 
    elif n == 1: #caso base 2
        return 1
    else: #caso recursivo 
        return fibonacci (n -1) + fibonacci (n -2)
    
for i in range(10):
    print(f'fibonacci({i}) = {fibonacci(i)}')

    