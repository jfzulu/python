'''
Problema 1: Un peaje de la ciudad quiere que usted sistematice el 
control del pago de los peajes, por este pasan tres tipos de 
automotores: 
1. Vehículos 
2. Camiones 
3. Tracto mulas  
No se sabe cuántos de estos pasan al día por el peaje, pero cuando el 
día finaliza se registra un tipo de automotor cero 0. 
 
El cobro por cada tipo de automotor es el siguiente: 
 
Tipo Valor 
   1. Vehículo $ 3.500 
   2. Camión $ 12.000 
   3. Tracto mula $ 16.000 
 
Desarrolle un programa en Python donde conociendo el tipo de 
automotor determinar: 
• El valor a pagar por cada automotor que pase por el peaje 
• Total recaudado en el peaje en ese día. 
• Total recaudado por cada tipo de automotor. 
• Cuál es el tipo de Automotor que más transita por el peaje 
(Asumiendo que no hay empates).
'''

automotores = [{'tipo': 1, 'valor': 3500},
               {'tipo': 2, 'valor': 12000},
               {'tipo': 3, 'valor': 16000}]

# Inicializar variables
total_recaudado = 0
total_vehiculos = 0
total_camiones = 0
total_tracto_mulas = 0
tipo_mas_frecuente = None
cantidad_total = 0






# Bucle para registrar los automotores que pasan por el peaje
while(True):
    print('''
    ╔══════════════════════════════════════════════════╗
    ║                 PEAJES DE LA CIUDAD              ║
    ╚══════════════════════════════════════════════════╝
    ║                                                  ║
    ║                Estimado usuario                  ║
    ║      Sea bienvenido a nuestro peaje              ║
    ║                                                  ║
    ║                Tipos de automotores:             ║
    ║               1. Vehículo                        ║
    ║               2. Camión                          ║
    ║               3. Tracto mula                     ║
    ║               0. Salir                           ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝    
    ''')
    try:
        tipo_automotor = int(input("Ingrese el tipo de automotor (0 para salir): "))
        if tipo_automotor == 0:
            break
        elif tipo_automotor < 0 or tipo_automotor > 3:
            print("Tipo de automotor inválido. Intente nuevamente.")
            continue

        # Calcular el valor a pagar
        for automotor in automotores:
            if automotor['tipo'] == tipo_automotor:
                valor_a_pagar = automotor['valor']
                total_recaudado += valor_a_pagar
                cantidad_total += 1

                # Actualizar totales por tipo de automotor
                if tipo_automotor == 1:
                    total_vehiculos += 1
                elif tipo_automotor == 2:
                    total_camiones += 1
                elif tipo_automotor == 3:
                    total_tracto_mulas += 1

                # Mostrar el valor a pagar
                print(f"Valor a pagar por el automotor tipo {tipo_automotor}: ${valor_a_pagar}")
                break

    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")


# Determinar recaudación total
print(f'\nTotal recaudado en el peaje: ${total_recaudado}')
totalRecaudo= 23124123
print(f'\nTotal recaudo en el peaje: ${totalRecaudo}')
print(f"\nTotal recaudado en el peaje: ${total_recaudado}")
# Mostrar recaudación por tipo de automotor
print(f"Total recaudado por vehículos: ${total_vehiculos * automotores[0]['valor']}")
print(f"Total recaudado por camiones: ${total_camiones * automotores[1]['valor']}")
print(f"Total recaudado por tracto mulas: ${total_tracto_mulas * automotores[2]['valor']}")
# Mostrar cantidad total de automotores
print(f"Cantidad total de automotores que pasaron por el peaje: {cantidad_total}")
# Mostrar cantidad total de automotores por tipo
print(f"Cantidad total de vehículos: {total_vehiculos}")
print(f"Cantidad total de camiones: {total_camiones}")
print(f"Cantidad total de tracto mulas: {total_tracto_mulas}")
# Determinar el tipo de automotor que más transita
if total_vehiculos > total_camiones and total_vehiculos > total_tracto_mulas:
    tipo_mas_frecuente = "Vehículo"
elif total_camiones > total_vehiculos and total_camiones > total_tracto_mulas:
    tipo_mas_frecuente = "Camión"  
elif total_tracto_mulas > total_vehiculos and total_tracto_mulas > total_camiones:
    tipo_mas_frecuente = "Tracto mula"
else:
    tipo_mas_frecuente = "No hay un tipo de automotor que más transite, no hay automoteres o transitan en la misma frecuencia."
print(f"Tipo de automotor que más transita por el peaje: {tipo_mas_frecuente}")
# Fin del programa
