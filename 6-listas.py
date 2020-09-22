# recordemos que en las listas se pueden guardar cualquier tipo de datos e incluso tener sublistas y guardarlas en una variable por ejemplo

lista = [1 ,"hello",1.34,True,[1,2,"tres"]]

# otra forma de crear listas es con la funcion constructora list()

listaDeNumeros = list((1,2,3,4)) #nota que vienen dentro de una tupla () por que la funcion list solo acepta un dato a menos de que usemos la tupla para adentro ingresar los datos que queramos y seguir siendo una lista

print(listaDeNumeros) #imprime en la consola la lista de numeros

print(type(listaDeNumeros)) #imprime en la consola que es un dato tipo list

# otra forma es crear una lista rango que basicamente es decir de donde empieza y hasta donde termina esa lista

l = list(range(1,10))

print(l) #imprime la lista del 1 al 9 ya que el ultimo no se cuenta si quieres que lo cuente debes poner el range hasta 11 de esta forma contara del 1 al 10

# recuerda que con dir puedes ver que metodos puedes usar con una funcion o elemento vamos a ver algunos

print(dir(lista)) # imprime en la consola todos los metodos que se puede hacer con una lista

print(len(lista)) # este metodo imprime en la consola la longitud de una lista

print(lista[1]) # imprime la posicion designada de una lista en este caso devuelve "hello" en la consola

print(1.34 in lista) # este metodo es para ver si un valor esta dentro de un elemento en este caso una lista devolviendo true o false

listaDeNumeros.append(5) # este metodo agrega un nuevo valor a la lista

print(listaDeNumeros) # imprime la lista con el nuevo valor 5

listaDeNumeros.extend([6,7,8]) # este metodo extiende la lista con varios valores mas

print(listaDeNumeros) # imprime la lista con los nuevos valores extendidos

listaDeNumeros.insert(2,"me infiltre") # este metodo inserta un nuevo valor segun la posicion designada en este caso la posicion 2

print(listaDeNumeros) # imprime la lista con el nuevo valor insertado "me infiltre"

listaDeNumeros.pop(2) # este metodo elimina un dato de la lista en la posicion 2

print(listaDeNumeros) # imprime la lista con el dato eliminado de la posicion 2 por defecto elimina el ultimo

listaDeNumeros.remove(4) # este metodo elimina un dato especificado en este caso elimina el numero 4

print(listaDeNumeros) # imprime la lista con el numero 4 eliminado

listaDeNumeros.sort() # ordena los datos de la lista en orden alfabetico

print(listaDeNumeros) # imprime los datos ordenados en orden alfabetico

print(listaDeNumeros.index(3)) # este metodo te dice en que posicion se ubica el dato requerido en este caso el numero 3

print(lista.count(1)) # este metodo te dice cuantas veces esta repetido el numero 1 en la lista

listaDeNumeros.clear() # este metodo limpia la lista completamente dejandola vacia

print(listaDeNumeros) #imprime la lista vacia

# tambien puedes cambiar un valor de una lista de la siguiente manera

lista[1] = "bye" # aqui cambias el valor de la posicion 1 por el string "bye"

print(lista) # imprime la lista con el nuevo string "bye"