import time
import os
def agenda(): 
    contactos = {}
    salir = True
    while(salir):

        print(' BIENVENIDO A MI AGENDA\n')
        print(' 1.) ver Contactos\n 2.) Agregar Contacto\n 3.) Buscar Contacto\n 4.) Modificar Contacto\n 5.) Eliminar Contato\n 6.) salir\n')

        opcion = input('Digite el numero de la opcion que desea ver:')
        os.system('clear')
        if opcion == '1': #<-----------Muestra los Contactos ----------------
                for Contacto in contactos:
                        for numero in contactos:
                                print('Contacto \ Numero')
                                print(numero,contactos[Contacto])
                time.sleep(5)
                os.system('clear')

        elif opcion == '2': #<-----------------Registra los contactos ----------
                nombre = input('Nombre :')
                if nombre in contactos:
                        print('Error el cotacto ya existe')
                        time .sleep(4)
                        os.system('clear')
                        continue
                try:
                        numero = int(input('Numero:'))
                        if numero>9999999999:
                                print('El numero es demaciado largo')
                                time.sleep(4)
                                os.system('clear')
                                continue
                        elif numero<1000000000:
                                print('El numero es demaciado corto \n Debe de ser de 10 digitos')
                                time.sleep(4)
                                os.system('clear')
                                continue     
                except:
                        print('valor no valido')
                        time.sleep(4)
                        os.system('clear')
                contactos[(nombre)]=numero
                print('Contacto Agregado')
                print(contactos)
                time.sleep(4)
                os.system('clear')
        
        elif opcion == '3':  #<----------Busca los contactos-----------
                buscar = input('Contacto a Buscar : ')
                print(contactos[buscar])
                time.sleep(4)
                os.system('clear')
                if buscar not in contactos:
                        print('El contacto no existe..Agreguelo desde el Menu')
                        continue

        elif opcion == '4': #<---------Modifica los contactos-------------
                contacto = input('Contacto a Modificar')
                if contacto not in contactos:
                        print('El contacto no existe..Agreguelo desde el Menu')
                        continue

                try:
                        nuevo=int(input('Nuevo Numero:'))
                        contactos[contacto] = nuevo
                        if numero>9999999999:
                                print('El numero es demaciado largo')
                                time.sleep(4)
                                os.system('clear')
                                continue
                        elif numero<1000000000:
                                print('El numero es muy corto, Debe de ser de 10 Digitos')
                        print('Contacto modificado con exito')
                        time.sleep(4)
                        os.system('clear')  
                        continue

                except:
                        print('¡Dato no valido!')
                        time.sleep(4)
                        os.system('clear')  
                        continue

        elif opcion == '5': #<------------Elimina los contactos---------
                eliminar = input('Contacto a Eliminar:')
                if eliminar not in contactos:
                        print('El contacto no existe')
                        continue
                del(contactos[eliminar])
                print('contacto',eliminar,'eliminado con exito')
                time.sleep(4)
                os.system('clear')
                continue                                                    

        elif opcion == '6': #<---------Regresar al Menu Principal --------
                os.system('exit')

        else:
                 print('opcion no valida,\n Elija una opcion')
                 time.sleep(3)
                 os.system('clear')

agenda()                                       
