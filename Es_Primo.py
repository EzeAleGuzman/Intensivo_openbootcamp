#creando una funcion que nos devuelñva los numeros primos
# hasta llegar al numero
#crear funcion verifica si es primo
def es_primo(num):
    #veridficamos que no sea divisible por ningun numero entre 2 y 1- que el numero
    for i in range(2,num-1):
        if num%i==0: return False
    #si no es divisible es primo
    return True

#definimos otra funcion de primos hasta el numero que ponemos
def primos_hasta(num):
    #creamos la lista de los numeros primos
    primos= []
    #buscamos todos los numeros primos desde el 3 hasta el numerop quie le tiramos
    for i in range(3,num+1):
        resultado = es_primo(i)
        #agregamos cada numero a la lista
        if resultado == True: primos.append(i)
    #devolvemos la lista
    return primos
    
#lo mostramos en la
resultado = primos_hasta(95)
print(resultado)