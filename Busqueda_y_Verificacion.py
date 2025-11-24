texto = "Hola Mundo Python"

# find() - busca subcadena y devuelve posición
print(texto.find("Mundo"))  # 5

# index() - similar a find pero lanza excepción si no encuentra
print(texto.index("Python"))  # 12

# count() - cuenta ocurrencias
print(texto.count("o"))  # 3

# startswith() - verifica si empieza con
print(texto.startswith("Hola"))  # True

# endswith() - verifica si termina con
print(texto.endswith("Python"))  # True

# isalpha() - verifica si todos son letras
print("abc".isalpha())  # True

# isnumeric() - verifica si todos son números
print("123".isnumeric())  # True

# isalnum() - verifica si es alfanumérico
print("abc123".isalnum())  # True