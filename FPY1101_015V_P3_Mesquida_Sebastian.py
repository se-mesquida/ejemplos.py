# Variable global
DataBase = {}

# Funciones para validar datos
def validar_nif():
    continuar = True
    while continuar:
        nif = input('NIF: ')
        # 1. Verificamos que NIF contenga una estructura separada por un guion
        if '-' in nif:
            primerosDigitos = nif.split('-')[0]
            segundosDigitos = nif.split('-')[1]
            # 2. Verificamos que el NIF ingresado contenga 8 y 3 caracteres en su estructura
            if len(primerosDigitos) == 8 and len(segundosDigitos) == 3:
                # 3. Verificamos que los primeros caracteres sean numéricos
                try:
                    primerosDigitosNumericos = int(primerosDigitos)
                    nif = str(primerosDigitosNumericos) + '-' + str(segundosDigitos).upper()
                    return nif
                except:
                    print('--------------------------------------------------------------------------------------------------------')
                    print('Error!, los primeros 8 caracteres deben ser numéricos.')
                    print('--------------------------------------------------------------------------------------------------------')
            else:
                print('--------------------------------------------------------------------------------------------------------')
                print('ERROR!, Ingrese un NIF con la siguiente estructura: 8 números, guion y 3 caracteres (EJ: 99999999-RTX).')
                print('--------------------------------------------------------------------------------------------------------')
        else:
            print('--------------------------------------------------------------------------------------------------------')
            print('ERROR!, Ingrese un NIF con la siguiente estructura: 8 números, guion y 3 caracteres (EJ: 99999999-RTX).')
            print('--------------------------------------------------------------------------------------------------------')

def validar_nombre():
    while True:
        nombre = input('Nombre: ')
        if len(nombre) >= 8:
            return nombre
        else:
            print('--------------------------------------------------------------------------------------------------------')
            print('ERROR!, El nombre debe contener mínimo 8 caracteres.')
            print('--------------------------------------------------------------------------------------------------------')

def validar_edad():
    while True:
        try:
            edad = int(input('Edad: '))
            if edad >= 15:
                return edad
            else:
                print('--------------------------------------------------------------------------------------------------------')
                print('Error!, este documento solo se puede emitir para personas mayores o iguales a 15 años de edad.')
                print('--------------------------------------------------------------------------------------------------------')
        except:
            print('--------------------------------------------------------------------------------------------------------')
            print('Error!, ingrese una edad numérica mayor o igual a 15.')
            print('--------------------------------------------------------------------------------------------------------')

def verificar_procedencia(nif):
    if nif[-2:] == 'SP':
    
        return 'España'
    else:
        return 'Unión Europea'

def verificar_numerico_entre(cotaInferior, cotaSuperior, nombreCertificado):
    while True:
        try:
            valor = int(input(f'Ingrese valor para Certificado de {nombreCertificado}: '))
            if cotaInferior <= valor <= cotaSuperior:
                return valor
            else:
                print(f'Ingrese un valor numérico entre {cotaInferior} y {cotaSuperior}.')
        except:
            print(f'Ingrese un valor numérico entre {cotaInferior} y {cotaSuperior}.')

# Funcionalidades del programa
def grabar():
    while True:
        print('--------------------------------------------------------------------------------------------------------')
        print('Para Grabar ingrese los datos solicitados')
        print('--------------------------------------------------------------------------------------------------------')
      
        nif = validar_nif()
        nombre = validar_nombre()
        edad = validar_edad()
        procedencia = verificar_procedencia(nif)
        
        if nif in DataBase:
            print('--------------------------------------------------------------------------------------------------------')
            print('El NIF ingresado ya existe en la Base de Datos, ingrese otro NIF.')
            print('--------------------------------------------------------------------------------------------------------')
        else:
            DataBase[nif] = {'nombre': nombre, 'edad': edad, 'procedencia': procedencia}
            print('--------------------------------------------------------------------------------------------------------')
            print(f'Datos guardados exitosamente para el NIF {nif}.')
            print('--------------------------------------------------------------------------------------------------------')
            break

def buscar():
    while True:
        nif = validar_nif()
        if nif in DataBase:
            print('--------------------------------------------------------------------------------------------------------') 
            print('Datos Encontrados')
            print(f'NIF: {nif}')
            print(f'Nombre: {DataBase[nif]["nombre"]}')
            print(f'Edad: {DataBase[nif]["edad"]}')
            print(f'Procedencia: {DataBase[nif]["procedencia"]}')
            print('--------------------------------------------------------------------------------------------------------') 
            break
        else:
            print('--------------------------------------------------------------------------------------------------------') 
            print('El NIF ingresado no se encuentra registrado en la Base de Datos.')
            print('--------------------------------------------------------------------------------------------------------') 

def buscarParaCertificado(nombreCertificado):
    while True:
        nif = validar_nif()
        if nif in DataBase:
            print('--------------------------------------------------------------------------------------------------------') 
            print(f'{nombreCertificado}')
            print(f'NIF: {nif}')
            print(f'Nombre: {DataBase[nif]["nombre"]}')
            print(f'Edad: {DataBase[nif]["edad"]}')
            print(f'Procedencia: {DataBase[nif]["procedencia"]}')
            print('--------------------------------------------------------------------------------------------------------') 
            break
        else:
            print('--------------------------------------------------------------------------------------------------------') 
            print('El NIF ingresado no se encuentra registrado en la Base de Datos.')
            print('--------------------------------------------------------------------------------------------------------') 

def imprimirCertificados(valor_nacimiento, valor_conyugal, valor_unionEuropea):
    while True:
        print('--------------------------------------------------------------------------------------------------------')
        print('Ingrese qué certificado desea imprimir')
        print(f'1 <- Certificado de Nacimiento                      valor: {valor_nacimiento}')
        print(f'2 <- Certificado de Estado Conyugal                 valor: {valor_conyugal}')
        print(f'3 <- Certificado de Pertenencia a la Unión Europea  valor: {valor_unionEuropea}')
        print(f'4 <- Volver al menu principal')
        print('--------------------------------------------------------------------------------------------------------')
        try:
            opcion = int(input('Ingrese opción:'))
            
            if opcion == 1:
                buscarParaCertificado('Certificado de Nacimiento')
            elif opcion == 2:
                buscarParaCertificado('Certificado de Estado Conyugal')
            elif opcion == 3:
                buscarParaCertificado('Certificado de Pertenencia a la Unión Europea')
            elif opcion == 4:
                print('volver al menu principal') 
                break
            else:
                print('Error!, ingrese una opción numérica disponible.')
        except:
            print('Error!, ingrese una opción numérica disponible.')

# Función principal para ejecutar el programa
def EjecutarPrograma():
    print('Antes de comenzar con el programa ingrese los valores de los siguientes certificados...')
    valor_certificadoNacimiento = verificar_numerico_entre(1500, 5000, 'Nacimiento')
    valor_estadoConyugal = verificar_numerico_entre(1500, 5000, 'Estado Conyugal')
    valor_pertenenciaUnionEuropea = verificar_numerico_entre(1500, 5000, 'Pertenencia a la Unión Europea')
    
    while True:
        print('--------------------------------------------------------------------------------------------------------')
        print('Programa NIF Registros App 1.0')
        print('--------------------------------------------------------------------------------------------------------')
        print('Seleccione una de las opciones del siguiente menú...')
        print('1 -> Grabar datos de una persona (NIF, nombre, edad)')
        print('2 -> Buscar personas por su NIF')
        print('3 -> Imprimir certificados')
        print('4 -> Salir')
        
        opcion = input('Ingrese opción: ')
        try:
            opcionNumerica = int(opcion)
            if opcionNumerica == 1:
                grabar()
            elif opcionNumerica == 2:
                buscar()
            elif opcionNumerica == 3:
                imprimirCertificados(valor_certificadoNacimiento, valor_estadoConyugal, valor_pertenenciaUnionEuropea)
            elif opcionNumerica == 4:
                print('--------------------------------------------------------------------------------------------------------')
                print('Saliendo del programa creado por Sebastian Mesquida.')
                print('Programa NIF Registros App 1.0')
                print('--------------------------------------------------------------------------------------------------------')
                break
            else:
                print('--------------------------------------------------------------------------------------------------------')
                print('Opción no válida, por favor ingrese un número del 1 al 4.')
                print('--------------------------------------------------------------------------------------------------------')
        except:
            print('--------------------------------------------------------------------------------------------------------')
            print('Error!, ingrese una opción numérica disponible en el menú.')
            print('--------------------------------------------------------------------------------------------------------')

# Ejecutar el programa
EjecutarPrograma()

input()