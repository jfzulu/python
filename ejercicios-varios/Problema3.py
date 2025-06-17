'''
Problema 3: Una biblioteca desea sistematizar el manejo de los libros, 
usando el siguiente menú. 
Encabezado Menú: Biblioteca LEXUS 
Opción 1. Prestamos. 
Opción 2. Recolección. 
Opción 3. Salir. 
Mensaje en pantalla para ingresar la selección: ¿Cuál es su opción? 
Implementar las siguientes funciones: 
3 
• Menú (): Utilizado en el main (), funcionara hasta que el usuario 
de la opción 3. 
• ValidarCódigo (): Debe recibir el código del libro y este debe 
cumplir: ser un número de 6 dígitos, el primer dígito corresponde 
al tipo (1. General 2. Colección 3. Reserva) los 3 siguientes al área 
que debe estar entre 101 y 108. Si cumple debe retornar un 
1(uno), si no cumple debe retornar un 0 (cero). 
• Préstamo (): La función debe recibir el código del libro, y sí es 
válido retorna la cantidad de días que puede ser prestado, siendo 8 
días para los del área General, 3 para los de Colección y 1 para los 
de Reserva, sí no es válido retorna 0.  
• Recolección (): La función debe recibir el código del libro, y sí es 
válido retorna el valor a pagar por el usuario, así: $500 por los 
del área General, $1.000 por los de Colección y $5.000 por los de 
Reserva, sí no es válido retorna 0. 
Al final del día se debe indicar cuántos libros se prestaron y cuánto 
dinero se recolecto.
'''



def menu():
    print("=====BIBLIOTECA LEXUS=====")
    print("1. Préstamos")
    print("2. Recolección")
    print("3. Salir")
    print("===========================")
    opcion = int(input("¿Cuál es su opción? "))
    while opcion < 1 or opcion > 3:
        print("Opción inválida. Intente nuevamente.")
        opcion = int(input("¿Cuál es su opción? "))
    
    return opcion

def validar_codigo(codigo):
    if len(str(codigo)) != 6:
        return 0
    tipo = int(str(codigo)[0])
    area = int(str(codigo)[1:4])
    if tipo not in [1, 2, 3] or area < 101 or area > 108:
        return 0
    return 1

if __name__ == "__main__":
    opcion = menu()
    while opcion != 3:
        
        if opcion == 1:

            # Lógica para préstamos
            pass
        elif opcion == 2:
            # Lógica para recolección
            pass
        opcion = menu()
    
    print("Gracias por visitar la Biblioteca LEXUS. ¡Hasta luego!")


