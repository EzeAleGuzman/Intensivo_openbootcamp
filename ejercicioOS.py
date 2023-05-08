#importo la libreria os
import os

#"Me posisciono en la carpeta descargas"
os.chdir("/Users/ezeal/Downloads/")

#obtengo todos los directorios dentro de la carpeta descargas y lo convierto en una lista
lista = os.listdir()
 
#recorro la lista de y muestro cada directorio
for directorio in lista:
    print(directorio)
    
#muestro en pantalla solo los resultados que sean ficheros
for elemento in lista:
    ruta_elemento = os.path.join(os.getcwd(), elemento) 
    if os.path.isfile(ruta_elemento): 
        #compruebo el tamañio del fichero y los paso a GB 
        tamaño = os.stat(ruta_elemento).st_size
        #convierto el tamaño de bytes a Mega Bytes
        tamaño_mb = tamaño / (1024 ** 2)
        #muestro los ficheros y los paso a Mega bytes
        print("Archivo:", elemento, "({:.2f} MB)".format(tamaño_mb)) 
    elif os.path.isdir(ruta_elemento):  
        print("Fichero:", elemento)  


