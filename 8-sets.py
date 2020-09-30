# los set son una coleccion que no tienen indice se usan con {} como no tienen indice debes acceder a ellos de otra forma

colors = {"red","green","black"}

print(type(colors)) # esto imprime que la var colors es un dato tipo set

print("red" in colors) # esto nos muestra en la consola si red es un valor que esta dentro de colors con un true o false

colors.add("violet") # esto agrega violet al set colors

print(colors) # imprime colors con el nuevo valor violet

colors.remove("red") # esto elimina el valor red dentro del set colors

print(colors) # esto imprime colors con el valor red eliminado

colors.clear() # esto elimina todo el set

print(colors) # esto imprime en la consola el set totalmente eliminado

del colors # elimina la var colors

print(colors) # te saltara un error ya que no la var colors fue eliminada con del

# este tipo de dato lo usaras cuando quieras tener un conjunto de datos que no necesitas organizar de ninguna manera pero quizas si deseas agregar mas datos en el futuro o eliminarlos