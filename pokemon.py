#Autores: Jose Antonio Adriano Munoz, Isabel Repetto Garcia-Plata
#Titulo: Palabras encadenadas por las letras de los extremos

"""FUNCIONES"""


"""Definimos la funcion para crear una lista cuyo elementos seran las 
palabras que componen el fichero .txt"""

def cargarFicheroEnLista(fichero):
    #Comenzamos abriendo el fichero que queremos analizar.
    archivo = open(fichero,'r')
    contenido = archivo.readlines()
    archivo.close()
    #Ahora separamos por palabras y las almacenamos cada una como elemento individual de la lista.
    for linea in contenido:
        for palabra in linea.split(' '):
            lista_pokemon.append(palabra)

"""Definimos la funcion que vamos a utilizar para comparar cada palabra 
con todas las demas para crear las listas de palabras encadenadas."""

def compara_palabras(lista_pokemon,pokemon_actual,cont,i):
    while cont <= len(lista_pokemon)-1:
        if pokemon_actual[-1] == lista_pokemon[cont][0]:
            resultados[i].append(lista_pokemon[cont])
            pokemon_actual = lista_pokemon[cont]
            lista_pokemon.pop(cont)
            cont=0
        else:
            cont += 1

"""Definimos la funcion que utilizaremos al final para comparar todas las 
listas de palabras encadenadas y devolver la lista con mayor numero de palabras"""

def compara_listas(lista_resultados):
    mayor = 0
    for numlista in range(0,len(lista_resultados)-1):
        if(len(lista_resultados[numlista])>mayor):
            del mayores[:]
            mayor = len(lista_resultados[numlista])
        if(len(lista_resultados[numlista])==mayor):
            mayores.append(numlista)


"""PROGRAMA PRINCIPAL"""

#Inicializacion de variables

"""Creamos una lista donde vamos a guardar los nombres de los pokemon de forma individual. 
Cada nombre sera un elemento de la lista."""
lista_pokemon = []

"""Creamos otra lista donde almacenaremos las listas generadas por la funcion 'compara'.
Cada palabra genera una lista de, al menos, una palabra (ella misma). Por lo tanto, cada 
elemento de esta lista 'resultados', sera una lista de palabras encadenadas.El numero de
listas resultantes debe coincidir con el numero de pokemon que aparecen en la lista_pokemon"""
resultados = []

"""Indice para ir almacenando las listas resultantes en la lista 'resultados'."""
numLista=0

"""Lista para guardar los indices de las listas resultantes con mayor num de elementos.
En el caso de que solo sea una, solo contendra un indice al finalizar."""
mayores = []

#Codigo de programa principal

"""Cargamos el fichero en la lista por primera vez"""
cargarFicheroEnLista("pokemon.txt")

"""Con este bucle que crea y recorre la lista de pokemon completa, mandaremos uno por uno
a la funcion 'compara' para crear con cada uno su lista de palabras encadenadas."""
for pokemon in lista_pokemon:
    #Agregamos una lista nueva vacia para la palabra pokemon correspondiente
    resultados.append([])
    #En dicha lista agregamos el nombre del pokemon que la inicializa
    resultados[numLista].append(lista_pokemon[numLista])
    #Mandamos la palabra a comparar para agregar sus palabras encadenadas (si las hay)
    compara_palabras(lista_pokemon,pokemon,0,numLista)
    numLista += 1
    #Reseteamos la lista de pokemon
    lista_pokemon = []
    cargarFicheroEnLista("pokemon.txt")


"""Por ultimo mandamos la lista de listas resultantes para ser comparadas."""
compara_listas(resultados)


"""Bucle para imprimir la/s lista/s con mayor numero de elementos."""
for indice in mayores:
    print "La lista  "+str(indice)+" contiene "+str(len(resultados[indice]))+" elementos:\n",resultados[indice],"\n"
