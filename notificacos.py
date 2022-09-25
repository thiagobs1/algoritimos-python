
import time
from plyer import notification

arrayMessage = ["fazer lições do curso", "Terminar trabalho de modelagem", "enviar artigos"]
i = 0

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "TAREFA: ",
            message = arrayMessage[i],
            timeout = 10
        )
        time.sleep(7200)
        i = i + 1
        if i == 3:
            i = 0