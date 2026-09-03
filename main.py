Real = True
nombre = ""

if Real == True:
    print("Estos es demasiado real.")

nombre = input("Bienvenido/a escriba su nombre: ")

while not nombre.isalpha():
    print("nombre incorrecto.")
    nombre = input("re escriba su nombre: ")

print(f"Hola {nombre}")

