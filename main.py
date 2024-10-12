from time import sleep
from datetime import datetime

def relogio():
    """
    Exibe a hora atual a cada segundo até que o usuário interrompa o programa.
    """
    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"\rHora: {current_time}", end="", flush=True)
            sleep(1)
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")

if __name__ == "__main__":
    relogio()