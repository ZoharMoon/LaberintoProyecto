nombre = input("Escribe tu nombre: ")
print("Bienvenido a mi laberinto",nombre)

import readchar

print("El programa está en ejecución. Presiona la tecla '↑' para salir.")

while True:
    char = readchar.readkey()
    if char == readchar.key.UP:
        print("Tecla '↑' presionada. Saliendo del programa.")
        break
    print(f"Tecla '{char}' presionada.")