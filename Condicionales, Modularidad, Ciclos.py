import os
#condicionales, Modularidad y ciclos 
def sumar ( v1,  v2):
    suma= v1 + v2
    return suma

def restar ( v1,  v2):
    resta= v1 - v2
    return resta

def producto ( v1,  v2):
    prod= v1 * v2
    return prod

def dividir ( v1,  v2):
    div= v1 / v2
    return div

#Se piden los dos valores
def menu():
    v1 = int(input("Primer Valor: "))
    v2 = int(input("Segundo Valor: "))

    while True: 
    

        #Se despliega menu
        os.system('cls')
        print("1 : Sumar")
        print("2 : Restar")
        print("3 : Multiplicar")
        print("4 : Dividir ")
        print("5 : Salir")
        opcion = int(print('Opcion'))
    
        #Se solicita una opcion
        opc=int("Opcion: ")
        
        
        
        if opcion == 1:
            print(sumar (v1, v2))
            print("Suma = ", s)

        elif opcion == 2:
            r= restar (v1, v2)
            print("Resta = ", r)

        elif opcion == 3:
            p= producto (v1, v2)
            print("Multiplicación = ", p)

        elif opcion == 4:
            d= dividir (v1, v2)
            print("División = ", d)

        elif opcion == 5:
            break

        else : print("Opcion no Valida")



    # Programa Principal
    menu()



    

