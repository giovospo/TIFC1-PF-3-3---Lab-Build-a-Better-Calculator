# Este es un ejemplo de una calculadora mejorada con funciones para sumar, multiplicar, verificar enteros y pares.

# Función para sumar una lista de números
# Recibe una lista de números y devuelve la suma total.
# Ejemplo: addmultiplenumbers([5, 7, 9]) devuelve 21

def addmultiplenumbers(numbers):
    """
    Recibe una lista de números y devuelve la suma total.
    """
    total = 0
    for n in numbers:
        total += n
    return total

# Función para multiplicar una lista de números
# Recibe una lista de números y devuelve el producto total.
# Ejemplo: multiplymultiplenumbers([4, 5, 6, 7]) devuelve 840

def multiplymultiplenumbers(numbers):
    """
    Recibe una lista de números y devuelve el producto total.
    """
    result = 1
    for n in numbers:
        result *= n
    return result

# Función para verificar si un número es un entero
# Devuelve True si num es un entero, incluyendo floats que representan enteros (ej. 7.0), y False para cualquier otro caso.

def isitaninteger(num):
    """
    Devuelve True si num es un entero.
    - True para int (ej. 3)
    - True para float que representa entero (ej. 7.0)
    - False para float con decimales (ej. 7.3)
    """
    # Evitar que True/False cuenten como enteros (bool hereda de int)
    if isinstance(num, bool):
        return False

    if isinstance(num, int):
        return True

    if isinstance(num, float):
        return num.is_integer()

    return False

# Función para verificar si un número es par

def isiteven(num):
    """
    Devuelve True si num es un número entero y par, False en cualquier otro caso.
    """
    if not isitaninteger(num):
        return False
    return int(num) % 2 == 0


def main():
    # Lógica interactiva (no la evalúa pytest, pero hace tu calculadora "usable")
    print("Hello learners!")
    print("Better Calculator (demo)")
    print("Ejemplos rápidos:")
    print("Suma:", addmultiplenumbers([5, 7, 9]))
    print("Multiplicación:", multiplymultiplenumbers([4, 5, 6, 7]))
    print("¿6 es par?:", isiteven(6))
    print("¿7.3 es entero?:", isitaninteger(7.3))


if __name__ == "__main__":
    main()