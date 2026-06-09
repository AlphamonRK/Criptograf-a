def mostrar_menu():

    print("\n==================== ROT13 ======================")
    print(f"      (Consultas realizadas: {len(historial)})")
    print("===================================================")
    print("1. Transformar mensaje")
    print("2. Destransformar mensaje")
    print("3. Historial")
    print("4. guardar historial")
    print("5. Limpiar historial")
    print("6. Salir")

historial = []

def rot13(texto):
    resultado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            resultado += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            resultado += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif '0' <= char <= '9':
            resultado += chr((ord(char) - ord('0') + 5) % 10 + ord('0'))
        elif char in [' ', '.', ',', '!', '?']:
            resultado += char
        else:
            resultado += char
    return resultado

def desrot13(texto):
    return rot13(texto) 

def mostrar_historial(historial):
    if not historial:
        print("\nNo hay mensajes en el historial.")
    else:
        print("\n===== HISTORIAL =====")
        for i, mensaje in enumerate(historial, 1):
            print(f"{i}. {mensaje}")

def limpiar_historial():
    historial.clear()
    print("\nHistorial limpiado.")

def guardar_historial():
    with open("historial.txt", "w") as archivo:
        for mensaje in historial:
            archivo.write(mensaje + "\n")

def principal():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                mensaje = input("Ingrese el mensaje a transformar: ")
                resultado = rot13(mensaje)
                print(f"Mensaje transformado: {resultado}")
                historial.append(resultado)
                continuar = input("¿Desea transformar otro mensaje? (s/n): ").lower()
                if continuar == 'n':
                    print("\nRegresando al menú principal...\n")
                    break
        elif opcion == "2":
            while True:
                mensaje = input("Ingrese el mensaje a destransformar: ")
                resultado = rot13(mensaje)
                print(f"Mensaje destransformado: {resultado}")
                historial.append(resultado)
                continuar = input("¿Desea destransformar otro mensaje? (s/n): ").lower()
                if continuar == 'n':
                    print("\nRegresando al menú principal...\n")
                    break
        elif opcion == "3":
            mostrar_historial(historial)
        elif opcion == "4":
            guardar_historial()
            print("historial guardado. ¡Hasta luego!")
        elif opcion == "5":
            limpiar_historial()
        elif opcion == "6":
            print("gracias por usar el programa. ¡Hasta luego!")
            break   
        else:
            print("Opción no válida. Intente de nuevo.")


principal()