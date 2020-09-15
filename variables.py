#las variables es un nombre simbolico para guardar cualquier tipo de valor/dato y usarlo en cualquier momento recuerda que las mayusculas son importantes (case sensitive) y no es valido empezar una variable con un numero solo con caracteres tipo letra o guiones

name = "cesar"
Name = "cesar en mayuscula" #como name empieza con N mayuscula es otra variable difetente al primer name
numero = 150
diccionario ={
    "libro":"fortaleza digital",
    "año":"1998"
}

print(name,Name,numero,diccionario) #imprime en la consola todas las variables anteriores

#puedes crear variables en una sola linea por ejemplo

var1,var2 = 100,"string" #aqui hay dos variables en una sola linea

print(var1,var2)

#convenciones (la forma en que se escriben las variables para hacerlo mas legible)
#hay 3 formas principales para hacer mas legible una variable

book_name = "cleopatra" #separados con simbolos (snake case)
bookName = "cleopatra" #usando mayuscula en la primera letra de cada palabra nueva (camel case)
BookName = "cleopatra" #usando mayuscula en la primera letra de todas las palabras (pascal case)

#constantes
#para escribir variables constantes (que nunca cambian su valor) se escribe toda en mayuscula pero esto sigue siendo otra forma de convencion ya que python lo leera igual que una var pero nos sirve a nostros como coders leer una variable que sabemos que sera constante gracias a que esta toda en mayuscula otros lenguajes tendran reglas distintas por ejemplo en js para crear constantes se usa la palabra const

PI = 3.1416
MY_NAME = "cesar"

#python es de tipadoDinamico osea que puedes reasignar valores a una variable por ejemplo

Numero = 12
Numero = 13

print(Numero) #imprimira el numero 13 ya que el 12 fue cambiado