import random as r
import time,subprocess
note = ["A ","A#","B ","C ","C#","D ","D#","E ","F ","F#","G ","G#"]

while True:
    print(f"{note[round(r.randrange(12))]} ： {r.randint(1,6)}弦")
    time.sleep(10)
    subprocess.call("clear")