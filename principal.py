from figuras import obtener_jugada_usuario, obtener_jugada_computadora, determinar_ganador
from interfa import mostrar_resultado, mostrar_mensaje_final

def jugar():
    puntos_usuario = 0
    puntos_computadora = 0

    while puntos_usuario < 3 and puntos_computadora < 3:
        jugada_usuario = obtener_jugada_usuario()
        jugada_computadora = obtener_jugada_computadora()

        ganador = determinar_ganador(jugada_usuario, jugada_computadora)

        if ganador == "usuario":
            puntos_usuario += 1
        elif ganador == "computadora":
            puntos_computadora += 1

        mostrar_resultado(jugada_computadora, ganador, puntos_usuario, puntos_computadora)

    mostrar_mensaje_final(puntos_usuario)

if __name__ == "__main__":
    jugar()
