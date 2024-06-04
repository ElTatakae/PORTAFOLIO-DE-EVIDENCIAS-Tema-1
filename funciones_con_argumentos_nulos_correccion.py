#Funciones con argumentos nulos
def operacion (num1=None,num2=None,):
    if num1==None or num2==None:
        print("No se recibio uno o dos de los argumentos")
        return #se termina la funcion
    return num1+num2, num1-num2 #se retorna la suma y la resta

suma, resta= operacion(20,10) #cambió de operaciones a operacion
print("Suma=",suma)
print("Resta=", resta)

resultado=operacion()#cambio operaciones a operacion
if resultado is not None:
    s,r=resultado
    print("Suma=",s)
    print("Resta=",r)
else:
    print("No se recibio uno o dos de los argumentos")



