#  Que es un subprograma? 
# un subprograma es un bloque de codigo independiente, con su propio nombre, que realiza iuna tarea especifica y puede ser invicado (llamdo) desde cualquier parte del programa principal, las veces que necesite. 

#funciones y procedimientos
# Funcion: subprograma que SIEMPRE regresa un valor al punto deonde fue llamado usando la sentencia return. se usa cuando necesitas un resultado para seguir trabajando con el.

#el procedimento: subprograma que realiza una accion ( mostrar algo, modificar datos, guardar informacion), pero no necesita regrasar un valor utilizable. se usa cuando el objetivo un dato de vuelve 

# def 

#ejercicio 1 : Funcion vs procedimiento 

def calcular_area_rectangulo(base, altura):
    area = base * altura
    #return area # <-------- regresa un valor 

def mostrar_resultado(nombre, area):
    print(f'El area de {nombre} es {area} m2') # <--- no regresa nada 

resultado = calcular_area_rectangulo (5,5)

mostrar_resultado("el terreno", resultado)

#tu turno escribe un proceso llamado saludar  (nombre ) qu eimprima un saludo perosnalizado funcion llamda es mayor de edad que regrese true o false, usa ambos en un mini programa 



def es_mayorde_edad(edad):
   return edad >= 18

def saludar(nombre):
   print(f"Hola {nombre}")

nombre_alumno = input("Ingresa nombre: ")
edad = int(input("Ingresa tu edad: "))


saludar(nombre_alumno)
if es_mayorde_edad(edad):
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

#ejercicio 2: el error de no usar return 

def calcular_doble(numero):
    doble = numero * 2
    return doble

resultado = calcular_doble(10)
print(resultado)

#Tu turno: Corrige el Ejercicio 2 para que calcular_doble regrese el valor correctamente con return, y que sea el print(resultado) el que se encargue de mostrarlo.

