from time import sleep
from datetime import datetime
def relogio():
  while True:
    print("Hora:", end=" ")
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time)
    sleep(1)
relogio()