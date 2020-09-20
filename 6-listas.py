# recordemos que en las listas se pueden guardar cualquier tipo de datos e incluso tener sublistas y guardarlas en una variable por ejemplo

lista = [1 ,"hello",1.34,True,[1,2,"tres"]]

# otra forma de crear listas es con la funcion constructora list()

listaDeNumeros = list((1,2,3,4)) #nota que vienen dentro de una tupla () por que la funcion list solo acepta un dato a menos de que usemos la tupla para adentro ingresar los datos que queramos y seguir siendo una lista
print(listaDeNumeros) #imprime en la consola la lista de numeros
print(type(listaDeNumeros)) #imprime en la consola que es un dato tipo list

# otra forma es crear una lista rango que basicamente es decir de donde empieza y hasta donde termina esa lista

l = list(range(1,10))
print(l) #imprime la lista del 1 al 9 ya que el ultimo no se cuenta si quieres que lo cuente debes poner el range hasta 11 de esta forma contara del 1 al 10