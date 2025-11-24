texto = "***hola***"

# strip() con caracteres específicos
print(texto.strip("*"))  # "hola"

# lstrip() - elimina izquierda
print(texto.lstrip("*"))  # "hola***"

# rstrip() - elimina derecha
print(texto.rstrip("*"))  # "***hola"