import threading
from trains import *
from interface import *
from constants import *

event = threading.Event()

# Criação dos trens
train_1 = Train("trem1", yellow, 200, 50, event)
train_2 = Train("trem2", blue, 390, 50, event)
train_3 = Train("trem3", red, 200, 240, event)
train_4 = Train("trem4", green, 390, 240, event)

# Criação da Thread de visualização
viewer = threading.Thread(target=interface, args=(train_1, train_2, train_3, train_4))

# Início da thread gráfica
viewer.start()

# Início das threads dos trens
train_1.start()
train_2.start()
train_3.start()
train_4.start()

# Finalização das threads
while True:
    if not viewer.is_alive():
        event.set()
        train_1.join()
        train_2.join()
        train_3.join()
        train_4.join()
        break
