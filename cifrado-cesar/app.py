def mostrar_menu():
    print("\n===== CIFRADO DE CESAR =====")
    print("1. Cifrar un mensaje")
    print("2. Descifrar un mensaje")
    print("3. Ver historial de cifrados y descifrados")
    print("4. Salir")

historial = []


def cifrar_cesar(texto, clave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            desplazamiento = clave % 26
            if char.islower():
                resultado += chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
            else:
                resultado += chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
        else:
            resultado += char
    return resultado
             

def descifrar_cesar(texto, clave):
    return cifrar_cesar(texto, -clave)

def mostrar_historial():
    print("\n===== HISTORIAL DE CIFRADOS Y DESCIFRADOS =====")
    for mensaje, clave in historial:
        print(f"Mensaje: {mensaje}, Clave: {clave}")

def principal():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            while True:
                if opcion == '1':
                 mensaje = input("Ingrese el mensaje a cifrar: ")
                 clave = int(input("Ingrese la clave de cifrado (número entero): "))
                 mensaje_cifrado = cifrar_cesar(mensaje, clave)
                 print(f"Mensaje cifrado: {mensaje_cifrado}")
                 historial.append((mensaje_cifrado, clave))
                 continuar = input("¿Desea cifrar otro mensaje? (s/n): ").lower()
                if continuar == 'n':
                    print("\nRegresando al menú principal...\n")
                    break
                

        elif opcion == '2':
            while True:
                mensaje = input("Ingrese el mensaje a descifrar: ")
                clave = int(input("Ingrese la clave de descifrado (número entero): "))
                mensaje_descifrado = descifrar_cesar(mensaje, clave)
                print(f"Mensaje descifrado: {mensaje_descifrado}")
                historial.append((mensaje_descifrado, clave))
                continuar = input("¿Desea descifrar otro mensaje? (s/n): ").lower()
                if continuar == 'n':
                    print("\nRegresando al menú principal...\n")
                    break

        elif opcion == '3':
            mostrar_historial()

        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

principal()

    