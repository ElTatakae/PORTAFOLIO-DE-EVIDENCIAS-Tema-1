#Funciones con argumentos nulos
def operacion (num1=None,num2=None,):
    if num1==None or num2==None:
        print("No se recibio uno o dos de los argumentos")
        return #se termina la funcion
    return n1+n2, n1-n2 #se asigna a suma y a resta
suma, resta= operaciones(20,10)
print("Suma=",suma)
print("Resta=", resta)

s,r=operaciones()
print("Suma=",s)
print("Resta=",r)

