
# Problema 5: Una universidad necesita un sistema para calcular el promedio de notas de estudiantes 
# y mostrar el ranking de los estudiantes basado en su rendimiento.
# Requisitos:
# 1. Solicitar al usuario el número de estudiantes a registrar.
# 2. Para cada estudiante, ingresar:
# о Nombre del estudiante.
# Tres notas (de 0 a 100).
# 3. Calcular el promedio de notas de cada estudiante y asignarlo a su registro.
# 4. Generar un ranking de los estudiantes en orden descendente según su promedio.
# 5. Mostrar:
# 。
# La lista de estudiantes con su promedio en orden descendente.
# El mejor estudiante (con el promedio más alto).
# El promedio general de todos los estudiantes.


def registrarCantidadEstudiantes():
    numeroEstudiantes = int(input("Ingrese el numero de estudiantes a registrar: "))
    
    return numeroEstudiantes


def registrarNotasEstudiantes(numeroEstudiantes):
    estudiantes = []
    
    for i in range(numeroEstudiantes):
        
        suma = 0
        nombre = input(f'Ingrese el nombre del estudiante {i+1} : ')
        
        nota1= float(input(f'Ingrese la primera nota para {nombre} : '))
        while nota1<0 or nota1>100:
            print("Nota Invalida. Debe de ser entre 0 y 100.")
            nota1= float(input(f'Ingrese la primera nota para {nombre} : '))
        
        nota2= float(input(f'Ingrese la segunda nota para {nombre} : '))
        while nota2<0 or nota2>100:
            print("Nota Invalida. Debe de ser entre 0 y 100.")
            nota2= float(input(f'Ingrese la segunda nota para {nombre} : '))
        
        nota3= float(input(f'Ingrese la tercera nota para {nombre} : '))
        while nota3<0 or nota3>100:
            print("Nota Invalida. Debe de ser entre 0 y 100.")
            nota3= float(input(f'Ingrese la tercera nota para {nombre} : '))
          
        
        for j in range(3):
            nota = float(input(f'Ingrese la nota {j+1} : '))
            while nota < 0 or nota > 100:
                print("Nota Invalida. Debe de ser entre 0 y 100.")
                nota = float(input(f'Ingrese la nota {j+1} : '))
            
            #suma = suma+nota
            suma += nota  
           

           
        promedio = (nota1+ nota2+ nota3) /3
        promedio2= suma/3
        
        print (f'Promedio 1: {promedio:.2f}')
        print(f'Promedio 2: {promedio2:.2f}')
        
        estudiantes.append((nombre, promedio))             
        
    
    return estudiantes


def ranking():
    print ("=====RANKING=====")
    estudiantes.sort(key=lambda x: x[1], reverse=True)
    for i, (nombre, promedio) in enumerate (estudiantes, start=1):
        print(f'{i}. {nombre} - Promedio: {promedio:.2f}')

def ordenarEstudiantes(estudiantes):
    n = len(estudiantes)
    
    for i in range(n):
        
        for j in range(0, n-i-1):
            if (estudiantes[j] < estudiantes[j+1]):
                estudiantes[j], estudiantes[j+1] = estudiantes[j+1], estudiantes[j]
    
    print(estudiantes)    
    for i, (nombre, promedio) in enumerate (estudiantes, start=1):
        print(f'{i}. {nombre} - Promedio: {promedio:.2f}')

    return estudiantes


def mejorEstudiante(estudiantes):
    estudiantes.sort(key=lambda x: x[1], reverse= True)
    mejorEstudiante = estudiantes[0]
    print(f'Mejor estudiantes  es: {mejorEstudiante[0]} con un promedio de {mejorEstudiante[1]}')


def promedioGeneral(estudiantes, n):
    promGeneral = sum([estudiante[1] for estudiante in estudiantes]) / cantEstudiantes
    print(f'El promedio general de todos los estudiantes es : {promGeneral}')
    
if __name__ == "__main__":
    cantEstudiantes = registrarCantidadEstudiantes()
    estudiantes = registrarNotasEstudiantes(cantEstudiantes)
    ranking()
    estudiantesOrdenados = ordenarEstudiantes(estudiantes.copy())
    mejorEstudiante(estudiantes)
    promedioGeneral(estudiantes, cantEstudiantes)
    

