#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------     Plantilla para diseño de un menú ----------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

#Funciones

#Funcion que imprime el menu por pantalla
#Se agregan las opciones necesarias segun el programa de cada uno.
def imprimirMenu():
    print()
    print("********************************************")
    print("Debe elegir una opcion, solo numeros enteros")
    print("1 - Elige la opcion 1")   
    print("2 - Elige la opcion 2")
    print("3 - Elige la opcion 3")
    print("0 - Salir")
    print("********************************************")
    print()
    
    return


#Funcion que valida que las opciones elegidas del menu sean las correctas.
#Solo valida numeros. Si se ingresa letras se corta el programa.
#Agregar las opciones necesarias segun el programa de cada uno.

def validarOpcionMenu(opcion):
    flag=True
    if opcion!=1 and opcion!=2 and opcion!=3 and opcion!=0: #Se ha ingresado un valor invalido por menu
        flag=False
    
    return flag
    
#************************   
#Programa principal
#************************   


print("Bienvenido al programa")
print()

#Leer la primera vez la opcion del menu
imprimirMenu()
opcion=int(input("Ingrese la opcion elegida del menu principal: "))

#Comienzo del proceso de las opciones del menu elegidas.

while opcion!=0:

    flagMenu=validarOpcionMenu(opcion)
    while flagMenu == False:
        print("Opcion de menu invalida, vuelva a ingresar...")
        print()
        opcion=int(input("Ingrese la opcion elegida del menu principal: "))
        flagMenu=validarOpcionMenu(opcion)

    #Analizamos las opciones validas del menú
    if opcion==1:
        #Instrucciones para la opcion 1
        print("Has elegido la opcion 1")
        #ingreso de datos para opcion 1
        #proceso de datos para opcion 1
        #impresion de datos para opcion 1
    elif opcion==2:
        print("Has elegido la opcion 2")
        #ingreso de datos para opcion 2
        #proceso de datos para opcion 2
        #impresion de datos para opcion 2
    elif opcion==3:
        print("Has elegido la opcion 3")
        #ingreso de datos para opcion 3
        #proceso de datos para opcion 3
        #impresion de datos para opcion 3

    #Luego de procesar la opcion del menu elegida
    #Vuelvo a invocar al menu
    imprimirMenu()   
    opcion=int(input("Ingrese la opcion elegida del menu principal: "))

else:
    print("FIN DEL PROGRAMA")
    
    

#Fin del programa
