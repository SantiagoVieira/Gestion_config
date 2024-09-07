def pedir_datos():
    nombre = input("¿Cuál es tu nombre? ")
    edad = input("¿Cuántos años tienes? ")
    
    # Verificar que la edad sea un número entero
    try:
        edad = int(edad)
        print(f"Hola, {nombre}. Tienes {edad} años.")
    except ValueError:
        print("Por favor, ingresa un número válido para la edad.")

# Llamar a la función
pedir_datos()
