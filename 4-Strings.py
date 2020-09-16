myStr = "soy un string"

print(dir(myStr)) #imprime en la terminal las propiedades y metodos del dato string de la variable myStr que puedes alterar

print(myStr.upper()) #aqui ejecutamos un metodo en la variable que convierte todo el texto en mayuscula puedes verlo en la terminal notese las () indicadas despues de escribir el metodo asi se activan los metodos

print(myStr.lower()) #este metodo convierte todo en minuscula

print(myStr.swapcase()) #este metodo le da la vuelta a los cases por ejemplo si algo estaba en minuscula estara haora en mayuscula y visceversa

print(myStr.capitalize()) #este metodo convierte la primera del inicio en mayuscula y el resto en minuscula

print(myStr.replace("string","remplazo")) #este metodo toma una palabra del string y la remplaza por otra en este caso cambia string por remplazo

print(myStr.count("s")) #este metodo te cuenta cuantas veces se usa el caracter que se le ponga dentro de las () en este caso la s

print(myStr.startswith("soy")) #este metodo muestra si la variable empieza con cierta palabra o caracter si es asi te soltara un true si no es asi te soltara un false en este caso es true ya que si es verdad

print(myStr.endswith("string")) #este metodo te muestra si la variable termina con cierta palabra o caracter mostrandote si es falso o verdadero

print(myStr.split()) #es un metodo que separa la variable a partir del caracter puesto dentro de las () si lo dejas vacio separara a partir de los espacios en este caso separando soy , un , strting en la consola en una lista

print(myStr.find("y")) #este metodo busca en que posicion esta el caracter ubicado dentro de las () en este caso imprime el numero 2 debido que la y de soy esta en el segundo espacio contando desde la s como 0

print(myStr.index("y")) #este metodo te muestra en que posicion esta el caracter indicado muy parecido a .find

print(myStr.isnumeric()) #este metodo te muestra si un dato es numerico con false o true

print(myStr.isalpha()) #este metodo te muestra si un dato es alfanumerico



#puedes tener metodos dentro de metodos llamados metodos encadenados por ejemplo

print(myStr.replace("string","remplazo").upper()) #aqui primero remplazamos una palabra y luego convertimos todo a mayuscula

print(len(myStr)) #esto es una funcion que imprime la cantidad de caracteres que tiene un dato

#puedes elegir un caracter de un string a travez de [aqui pones una posicion] por ejemplo

print(myStr[2]) #imprime la letra y que es la que esta en la posicion 2
print(myStr[-1]) #con el - te devuelves en los caracteres por ejemplo aqui -1 seria la letra g del string

#concatenacion esto ya lo vimos pero veamos otro ejemplo con una variable y un string nuevo

print("hola " + myStr) #esto imprimira en la consola hola soy un string gracias a la concatenacion

print(f"hola {myStr}") #esto es otra forma de concatenar la f indica que dentro de un string va ir una variable dentro de {}