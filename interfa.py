def mostrar_resultado(jugada_computadora, ganador, puntos_usuario, puntos_computadora):
    print(f"La computadora eligió: {jugada_computadora}")

    if ganador == "usuario":
        print("¡Ganaste esta ronda!")
    elif ganador == "computadora":
        print("La computadora ganó esta ronda.")
    else:
        print("Es un empate.")

    print(f"Puntos - Usuario: {puntos_usuario}, Computadora: {puntos_computadora}")

def mostrar_mensaje_final(puntos_usuario):
    if puntos_usuario == 3:
        print("¡Felicidades! Has ganado el juego.")
    else:
        print("La computadora ha ganado el juego.")
