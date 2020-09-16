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

#puedes tener metodos dentro de metodos llamados metodos encadenados por ejemplo

print(myStr.replace("string","remplazo").upper()) #aqui primero remplazamos una palabra y luego convertimos todo a mayuscula