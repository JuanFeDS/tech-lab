# -------------------
# OPCION 1
# -------------------
# Abrir el archivo
file = open('./Datos/text.txt')

print(file.read())

# Cerrar el archivo
file.close()

# -------------------
# OPCION 2
# -------------------
# Abrir el archivo
with open('./Datos/text.txt', mode='a') as file:
    # print(file.read())
    file.write('\n')
    file.write('Hola, mundo!')






