import random

categorias = {
    "lenguajes" : ["python", "javascript"], 
    "programacion" : ["programa", "variable", "funcion", "bucle"],
    "tipos de datos" : ["entero", "lista", "cadena"]
}

guessed = []
attempts = 6
score = 0 # Puntuacion

print("¡Bienvenido al Ahorcado!")
print()

# Imprime en pantalla las categorias
for clave in categorias:
    print(f"{clave}")
print()
opcion = input("Ingrese una categoria: ")
# En caso de Opcion invalida
while opcion not in categorias: 
    opcion = input("Esa opcion no es valida. Por favor ingresar otra: ")
word = random.choice(categorias[opcion])

while attempts > 0:
    # Mostrar progreso actual -> (letras correctas y guiones para las pendientes o faltantes)
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el usuario ya adivinó la palabra por completo
    if "_" not in progress:
        score+= 6
        print("¡Ganaste!")
        print(f"Puntuación: {score}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")
    while not letter.isalpha():
        letter = input("Entrada no válida. Vuelve a ingresar: ")
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
        score-=1
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0
    print(f"Puntuación: {score}")