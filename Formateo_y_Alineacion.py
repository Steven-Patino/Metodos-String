texto = "python"

# center() - centra texto
print(texto.center(10, "*"))  # "**python**"

# ljust() - alinea a izquierda
print(texto.ljust(10, "-"))  # "python----"

# rjust() - alinea a derecha
print(texto.rjust(10, "+"))  # "++++python"

# zfill() - rellena con ceros a izquierda
print("42".zfill(5))  # "00042"