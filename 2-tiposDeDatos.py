#para saber que tipo de dato es un elemento escribe en la consola type(y aqui el dato que quieres analizar)

#strings (cadenas)
print("se puede asi")
print("""asi tambien""")
print('asi')
print('''asi tambien''')

print(type("hello world")) #imprimira en la consola que es un valor de clase "str" osea string

print("bye "+"world") #imprime en la consola el texto by y world juntos como unico texto esto se llama concatenacion gracias al signo +

#numbers (numeros)
print(30) #numero entero (integer)
print(30.5) #numero decimal (float)

print(type(30)) #imprime en la consola que es un dato tipo int (integer o entero)
print(type(30.5)) #imprime en la consola que es un dato tipo float (decimal)

#boolean o booleano
#los booleanos son valores de si y no o de 0 y 1
#supongamos que tenemos un programa que enciende y apaga un bombillo
True # indicaria que el bombillo se encienda
False # indicaria que el bombillo se apague

print(type(True)) #imprime "bool" (booleano)

#list o lista
#basicamente son listas de cualquier tipo de dato
[10,20,30]
["hello","bye",]
[20 ,"hello",True]

print(type([20,50])) #imprime que es un dato tipo "list"

#tuples o tuplas
# es como una lista pero se usa para datos que no se pueden cambiar (inmutable)

(10,20,30)
print(type((10,20,30))) #imprime que es un dato tipo "tuple"

#dictionaries o diccionarios
# te permiten agrupar datos que pertenecen a una misma entidad con un nombre y un valor
# por ejemplo los apodos de una sola persona irian asi
{
    "primer apodo":"mojo",
    "segundo apodo":"lion",
    "tercer apodo":"pepe"
}
#puede ser cualquier dato incluso juntos
{
    "edad":25,
    "estatura":22
}

print(type({
    "key":"valor"
})) #imprime que es un dato de clase "dict" (diccionario)

#none o ninguno
#es para indicar que lo vamos a usar no esta definido aun por ningun tipo de dato

None
print(type(None)) #imprime que es un dato de clase "noneType"