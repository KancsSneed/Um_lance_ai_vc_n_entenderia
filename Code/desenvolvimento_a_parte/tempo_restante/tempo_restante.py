from datetime import datetime, timedelta, time
from time import sleep




while True:
    def intervalo():
        agora = datetime.now()
        minutos = 60 - agora.minute
        segundos = minutos * 60
        print(segundos)
    intervalo()
    sleep(1)

