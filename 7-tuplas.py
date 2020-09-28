# las tuplas son parecidas a las listas la principal diferencia es que las tuplas son inmutables quiere decir que las usaras con datos que no podras cambiar despues.

x = (1,2,3) # las tuplas se abren con ()

print(type(x)) # imprime que x es un elemento de tipo "tuple" tupla

meses = ("enero","febrero","marzo") # un ejemplo de datos que nunca cambian

s = tuple((1,2,3)) # otra forma de crear tuplas con una funcion constructora muy similar a la de las listas donde debes poner todo dentro de otra tupla para que te acepete todos los valores

print(s) # imprime la tupla de la variable s

# como toda funcion o elemento puedes ver sus metodos con dir

print(dir(s)) # imprime en la consola los metodos disponible para la tupla de la var s

f = (1,2,3,4,5)

print(f[1]) # imprime el valor 2 gracias a que lo seleccionamos con el [1] para ubicar su posicion en la tupla

# las tuplas para ser considerada tuplas debe tener mas de un dato o bien una coma , veamos un ejemplo

a = (1)

print(type(a)) # imprime en la consola que es un valor de tipo entero

a = (1,)

print(type(a)) # imprime en la consola que es un valor de tipo tupla

# una forma muy comun de usar las tuplas es junto con otras formas de contener valores por ejemplo en un diccionario

locaciones = {
    (14.24242, 45.2455) : "tokyo",  # mira como las locaciones que nunca cambian van dentro de una tupla dentro del diccionario
    (52.4545, 58.64685) : "new york"
}