import multiprocessing
from playsound import playsound
import time

t_min = int(input("Enter No. of minutes after which user has to be notified: "))
t_sec = int(input("Enter No. of seconds after which user has to be notified: "))
sec=t_min*60+t_sec
current_time = int(time.time())
while(current_time+sec != int(time.time())):
    continue

p = multiprocessing.Process(target=playsound, args=("your-audio-file-name",))
p.start()
input("press ENTER to stop playback")
p.terminate()