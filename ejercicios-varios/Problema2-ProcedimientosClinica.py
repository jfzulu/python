'''
Problema 2: El valor de un procedimiento en una clínica se hace con 
base en su código. El código consiste en un número entero de 5 dígitos, 
el cual permite calcular el total a pagar además de conocer el tipo de 
paciente, el procedimiento a realizar, su costo y el descuento (o 
recargo) a que tenga derecho. 
• El primer dígito (de izquierda a derecha) indica sí es afiliado (1) o 
particular (2). 
• El segundo dígito determina el servicio que solicita el paciente y 
su costo: 
Tabla 1  
Valores de procedimientos 
Digito 
1 
Procedimiento Costo 
Radiografía 
2 Ecografía $35.000 
3 
Laboratorio 
$30.000 
$25.000 
4 Consulta Externa $40.000 
5 
Consulta Especializada 
$80.000 
Nota. Esta tabla muestra la información de los valores de 
procedimientos, digito, procedimiento y costo. Fuente. Autor 
La suma del tercero, cuarto y quinto dígito determinara el descuento 
o recargo que se aplicara al paciente, así: 
• Sí la suma es par y el paciente es afiliado tendrá un descuento 
del 15% 
• Sí la suma es par y el paciente es particular tendrá un recargo 
del 15% 
• Sí la suma es impar y el paciente es afiliado tendrá un descuento 
del 25% 
• Sí la suma es impar y el paciente es particular tendrá un recargo 
2 
del 25% 
Funciones a implementar: 
• Función validar: Recibe como parámetro un número entero, 
retorna 1 sí el número tiene 5 dígitos, en caso de no cumplir 
retorna 0, para indicar que no es válido. 
• Función tipo: Recibe como parámetro un número entero, sí el 
primer dígito es 1 retorna "AFILIADO", pero sí es 2 retorna 
"PARTICULAR", dato de tipo string. 
• Función servicio: Recibe como parámetro un número entero, el 
segundo dígito permite retornar el nombre del procedimiento a 
realizar. Ejemplo: sí el dígito es 3 retorna "LABORATORIO" 
• Función costo: Recibe como parámetro un dato de tipo string 
con el nombre del servicio a realizar, con base a este se 
determinar el costo base. Ejemplo: sí recibe "LABORATORIO" se 
retorna 25000. 
• Función descuReca: Recibe como parámetro un número entero 
(el código), un dato de tipo string con el tipo de paciente y un 
dato de tipo entero con el costo del procedimiento, y calcula el 
valor del descuento o recargo. 
• Función pago: Recibe como parámetro un número entero 
correspondiente al costo base del servicio y un número float 
correspondiente al descuento o recargo que se aplicara, la 
función retorna el valor final a pagar por el servicio. 
• Función principal: Captura el código del paciente, verifica su 
validez y determina los datos del paciente, haciendo el llamado 
a las diferentes funciones para mostrar en pantalla el costo final 
del servicio.
'''
valores_procedimientos = [
    {'digito': 1, 'procedimiento': 'Radiografía', 'costo': 30000},
    {'digito': 2, 'procedimiento': 'Ecografía', 'costo': 35000},
    {'digito': 3, 'procedimiento': 'Laboratorio', 'costo': 30000},
    {'digito': 4, 'procedimiento': 'Consulta Externa', 'costo': 40000},
    {'digito': 5, 'procedimiento': 'Consulta Especializada', 'costo': 80000}
]


def validarNumero():
    while True:
        try:
            numero = int(input("Ingrese el código del paciente (5 dígitos): "))
            if 10000 <= numero <= 99999:
                return numero
            else:
                print("El número debe tener 5 dígitos. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

def tipoPaciente(numero):
    if str(numero)[0] == '1':
        return "AFILIADO"
    elif str(numero)[0] == '2':
        return "PARTICULAR"
    else:
        return None


def servicio(numero):
    digito = int(str(numero)[1])
    for procedimiento in valores_procedimientos:
        if procedimiento['digito'] == digito:
            return procedimiento['procedimiento']
    return None

def costo(procedimiento):
    for servicio in valores_procedimientos:
        if servicio['procedimiento'] == procedimiento:
            return servicio['costo']
    return None

def descuReca(numero, tipo, costo):
    suma_digitos = sum(int(d) for d in str(numero)[2:])
    if suma_digitos % 2 == 0:  # Suma par
        if tipo == "AFILIADO":
            return costo * 0.15  # Descuento del 15%
        else:
            return costo * 0.15  # Recargo del 15%
    else:  # Suma impar
        if tipo == "AFILIADO":
            return costo * 0.25  # Descuento del 25%
        else:
            return costo * 0.25  # Recargo del 25%

def pago(costo_base, descuento_recargo):
    return costo_base - descuento_recargo if descuento_recargo < 0 else costo_base + descuento_recargo

if __name__ == "__main__":
    numero = validarNumero()
    tipo = tipoPaciente(numero)
    print(f"Tipo de paciente: {tipo}")
    procedimiento = servicio(numero)
    print(f"Procedimiento: {procedimiento}")
    costo_base = costo(procedimiento)
    print(f"Costo base: ${costo_base}")
    descuento_recargo = descuReca(numero, tipo, costo_base)
    print(f"Descuento/Recargo: ${descuento_recargo}")
    total_a_pagar = pago(costo_base, descuento_recargo)
    print(f"Total a pagar: ${total_a_pagar}")
    


