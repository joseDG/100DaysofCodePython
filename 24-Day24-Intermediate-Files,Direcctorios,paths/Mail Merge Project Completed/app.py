import modulo_fichero

nombre_fichero = 'fichero.txt'
fichero = modulo_fichero.Fichero(nombre_fichero)

texto = 'Esta es la primera fila del fichero. \nEsta sera la segunda fila.'
fichero.grabar_fichero(texto)

texto = '\nEste es un texto incluido en la tercera fila'
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print(texto_leido)