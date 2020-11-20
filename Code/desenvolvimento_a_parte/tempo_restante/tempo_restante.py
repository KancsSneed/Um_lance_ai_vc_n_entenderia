from datetime import datetime, timedelta, time
import time


def intervalo(horas):
    agora = datetime.now()
    tempo = horas - agora.hour
    tempo_minuto = tempo * 60
    print(horas)
    print(tempo)
    print(tempo_minuto)

intervalo(20)

