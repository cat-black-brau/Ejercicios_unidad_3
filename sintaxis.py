#sintaxis de una funcion 

#Encabezado - def nombre_de_la_funcion(parametros): - define el nombre y que recibe. 

#cuerpo de la funcion - son las lineas del codigo inventados que ejecutan la logica de la funcion.

# parametros - los datos que la funcion recibe para trabajo (puede ser cero, uno o verios)

#Retorno - la sentencia return valor que entrega el resultado de vuelta 

#ejercicio 

def calcular_promedio(nota1,nota2,nota3,nota4): #encabezado de la funcion
    sumar = nota1 + nota2 + nota3 + nota4 # cuerpo
    promedio = sumar /4
    return promedio


resultado = calcular_promedio(8.0,9.0,7.0,9.0)
print(f'Promedio: {resultado:.2f}')

#tu turno modifica la funcion paraq que reciba 4 calificaciones en lugar de 3 y ajusta el caculo del promedio correctamente 


def mostrar_bienvenida():
    print('=== sistema de calificaciones ====') # sin parametros


def calcular_iva(precio, tasa = 0.16): #parametro con valor por defecto
    return precio * (1 + tasa)

mostrar_bienvenida()

total1 = calcular_iva(100)
print(f'Total con iva por defecto: $ {total1:.2f}')# usando valor por defecto de taza

total2 = calcular_iva(100, 0.08)
print(f'Total con iva por defecto: $ {total2:.2f}')

#Tu turno: Escribe una función calcular_descuento(precio, porcentaje=10) que calcule el precio final con descuento. Pruébala una vez sin especificar el porcentaje y otra vez con un porcentaje distinto.

def calcular_descuento(precio, porcentaje = 0.10):
    descuento = precio * porcentaje
    precio_final =  precio - descuento
    return precio_final

caso_1 = calcular_descuento(100)
print(f'Total con descuento: $ {caso_1:.2f}')

caso_2 = calcular_descuento(100, 0.50)
print(f'Total con descuento: $ {caso_2:.2f}')


