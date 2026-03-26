# Mi interpretacion de este ultimo inciso:
# Cuando dice "al jugar varias rondas seguidas" hago que el juego quede en un loop constante
# y se termina cuando se juegan todas las palabras de una categoria (cualquiera)

import random

categorias = {
    "lenguajes" : ["python", "javascript"], 
    "programacion" : ["programa", "variable", "funcion", "bucle"],
    "tipos de datos" : ["entero", "lista", "cadena"]
}

words_played = {
    "lenguajes" : ["python", "javascript"], 
    "programacion" : ["programa", "variable", "funcion", "bucle"],
    "tipos de datos" : ["entero", "lista", "cadena"]
}

while True:
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

    # Cuando la categoria se quedo sin palabras corta el loop
    if not words_played[opcion]:
        print("Esta categoría se quedó sin palabras")
        break
    else:
        word = random.sample(words_played[opcion],1)
        words_played[opcion].remove(word[0])
        print(words_played[opcion])

    while attempts > 0:
        # Mostrar progreso actual -> (letras correctas y guiones para las pendientes o faltantes)
        progress = ""
        for letter in word[0]:
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
        elif letter in word[0]:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            score-=1
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word[0]}")
        score = 0
        print(f"Puntuación: {score}")