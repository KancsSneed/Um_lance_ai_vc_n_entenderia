from pygame import mixer
import time
sound = 'Yamete.mp3'

mixer.init()
mixer.music.load('sounds/' + sound)
mixer.music.play()
time.sleep(3)