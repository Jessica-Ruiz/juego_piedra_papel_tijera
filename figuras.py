import random

def obtener_jugada_usuario():
    jugada = input("Elige piedra, papel o tijera: ").lower()
    while jugada not in ['piedra', 'papel', 'tijera']:
        print("Opción inválida. Intenta de nuevo.")
        jugada = input("Elige piedra, papel o tijera: ").lower()
    return jugada

def obtener_jugada_computadora():
    return random.choice(['piedra', 'papel', 'tijera'])

def determinar_ganador(jugada_usuario, jugada_computadora):
    if jugada_usuario == jugada_computadora:
        return "empate"
    elif (jugada_usuario == 'piedra' and jugada_computadora == 'tijera') or (jugada_usuario == 'papel' and jugada_computadora == 'piedra') or (jugada_usuario == 'tijera' and jugada_computadora == 'papel'):
        return "usuario"
    else:
        return "computadora"