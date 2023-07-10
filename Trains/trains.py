import threading
import time
from constants import *

# Criação do semáforo
semaphore = threading.Semaphore(1)

# Criação dos mutexes
mutex1 = threading.Lock()
mutex2 = threading.Lock()
mutex3 = threading.Lock()
mutex4 = threading.Lock()

class Train(threading.Thread):
    def __init__(self, name, color, x, y, event):
        threading.Thread.__init__(self)
        self.color = color
        self.name = name
        self.x = x
        self.y = y
        self.xStart = x
        self.yStart = y
        self.xEnd = self.xStart + 190
        self.yEnd = self.yStart + 190
        self.speed = 1
        self.event = event
        self.direction = "right"

    def run(self):
        while True:
            self.deal_critical()
            #self.move()
            if self.event.is_set():
                break

    def setSpeed(self, speed):
        self.speed = speed

    '''def move(self):
        if self.x < self.xEnd and self.y == self.yStart:
            self.x += STEP
        elif self.x == self.xEnd and self.y < self.yEnd:
            self.y += STEP
        elif self.x > self.xStart and self.y == self.yEnd:
            self.x -= STEP
        else:
            self.y -= STEP
        time.sleep(1/self.speed)'''

    def deal_critical(self):
        match self.name:
            case "T1":
                # Se T1 estiver entrando na região crítica 1
                if self.x == self.xEnd - train_width and self.y == self.yStart:
                    semaphore.acquire()
                    mutex1.acquire()
                
                # Quando T1 sair da região crítica 1
                if self.x == self.xEnd and self.y == self.yEnd:
                    semaphore.release()
                    mutex1.release()

                # Se T1 estiver entrando na região crítica 2
                if self.x == self.xEnd and self.y == self.yEnd - train_width:
                    mutex2.acquire()
                
                # Quando T1 sair da região crítica 2
                if self.x == self.xStart and self.y == self.yEnd:
                    mutex2.release()

            case "T2":
                # Se T2 estiver entrando na região crítica 1
                if self.x == self.xStart + train_width and self.y == self.yEnd:
                    mutex1.acquire()
                
                # Quando T2 sair da região crítica 1
                if self.x == self.xStart and self.y == self.yStart:
                    if mutex1.locked():
                        mutex1.release()
                
                # Se T2 estiver entrando na região crítica 3
                if self.x == self.xEnd and self.y == self.yEnd - train_width:
                    semaphore.acquire()
                    mutex3.acquire()

                # Quando T2 sair da região crítica 3
                if self.x == self.xStart and self.y == self.yEnd:
                    semaphore.release()
                    mutex3.release()
                
            case "T3":
                # Se T3 estiver entrando na região crítica 2
                if self.x == self.xStart and self.y == self.yStart + train_width:
                    semaphore.acquire()
                    mutex2.acquire()

                # Quando T3 sair da região crítica 2
                if self.x == self.xEnd and self.y == self.yStart:
                    semaphore.release()
                    if mutex2.locked():
                        mutex2.release()

                #  Se T3 estiver entrando na região crítica 4
                if self.x == self.xEnd -train_width and self.y == self.yStart:
                    mutex4.acquire()

                # Quando T3 sair da região crítica 4
                if self.x == self.xEnd and self.y == self.yEnd:
                    if mutex4.locked():
                        mutex4.release()
                
            case "T4":
                # Se T4 está entrando na região crítica 3
                if self.x == self.xStart and self.y == self.yStart + train_width:
                    mutex3.acquire()

                # Quando T4 sair da região crítica 3
                if self.x == self.xEnd and self.y == self.yStart:
                    if mutex3.locked():
                        mutex3.release()

                # Se T4 está entrando na região crítica 4
                if self.x == self.xStart + train_width and self.y == self.yEnd:
                    semaphore.acquire()
                    mutex4.acquire()
                
                # Quando T4 sair da região crítica 4
                if self.x == self.xStart and self.y == self.yStart:
                    semaphore.release()
                    if mutex4.locked():
                        mutex4.release()