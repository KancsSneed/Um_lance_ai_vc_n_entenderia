from datetime import datetime

now = datetime.now()
semana = datetime.date(now).strftime("%V")

if int(semana) % 2 == 0:
    print('S')
else:
    print('N')