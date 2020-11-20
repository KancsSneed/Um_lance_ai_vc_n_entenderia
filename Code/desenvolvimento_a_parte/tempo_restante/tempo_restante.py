from datetime import datetime, timedelta, time


while True:
    now = datetime.now().time()
    d1 = datetime(2020, 11, 19, now.hour, now.minute, now.second)
    d2 = d1 + timedelta(hours=20, minutes=50)
    print(d2.time())