#numeros enteros (int)
10
print(type(10)) #imprime en la consola que es un numero tipo entero

#numeros decimales o flotantes (floats)
10.5
print(type(10.5)) #imprime en la consola que es un numero tipo flotante

#con estos numeros puedes realizar cualquier operacion matematica *,/,-,+

print(85/5) #imprime el resultado de esta operacion

print(4 + 1.5) #imprime el resultado de esta operacion con numeros flotantes

#tambien se pueden hacer operaciones mas complejas por ejemplo

print(2**3) #con doble multiplicacion se eleva al cubo

print(3//2) #con este operador doble // te devuelve el numero entero y no uno decimal como suele hacerlo la division

print(10%3) #esto se conoce como operador de modulo funciona para ver el residuo de una division

#tambien funciona la tabla de presedencias matematicas donde primero se resuelve las exponenciasiones luego multiplicaciones divisiones y porcentajes y luego las sumas y restas por ejemplo

print(20-10/5*3**2) #3**2 = 9, 10/5 =2, 2 * 9 = 28, 20 -18 = 2.0

#tambien puedes especificar el orden en que quieres que baya primero por ejemplo

print((20-10)/(5*3**2)) #al cambiar el orden el resultado sera totalmente distinto

#es muy comun que cuando trabajemos con numeros los numeros usados los proporcione el usuario por ejemplo cuando creamos una calculadora para esto usaremos mucho una funcion llamada input que basicamente toma un caracter que el usuario mande a la consola

edad = input("inserte su edad: ") #lo que pasa aqui es que el usuario va proporcionar un numero (edad) en la consola que se ejecuto y se guardara en la variable edad, quedando edad con el valor del usuario

print(edad) # imprimira la edad proporcionada por el usuario antes

#tambien podemos agregarle a esa variable mas datos con los operadores y guardarlo en otra variable por ejemplo

nueva_edad = int(edad) + 5 #aqui le suma a la variable edad + 5 y lo guarda en una nueva variable nueva_edad el int es para convertir la variable edad a numero entero ya que por default es un string y no se pueden sumar strings con numeros tambien puedes usar la funcion float y lo convierte en un numero flotante

print(nueva_edad) # aqui imprime el nuevo resultado