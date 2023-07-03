import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import ttk

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pista")

# Definição das cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (209, 50, 10)
yellow = (255, 187, 0)
blue = (39, 129, 219)
green = (13, 181, 55)

# Definição das dimensões do retângulo da pista
track_width = 200
track_height = 200

# Definição da espessura da linha da borda do retângulo
border_thickness = 2

# Definição das coordenadas dos retângulos da pista
track1_x = (screen_width - track_width * 2 - border_thickness) // 2
track1_y = (screen_height - track_height * 2 - border_thickness * 3) // 2

track2_x = track1_x + track_width + border_thickness
track2_y = track1_y

# Definição das coordenadas das pistas inferiores
track3_x = track1_x
track3_y = track2_y + track_height + border_thickness

track4_x = track2_x
track4_y = track2_y + track_height + border_thickness

# Definição das coordenadas e velocidades iniciais dos trens
train1_x = track1_x
train1_y = track1_y
train1_direction = "right"
train1_speed = 1  

train2_x = track2_x
train2_y = track2_y
train2_direction = "right"
train2_speed = 1  

train3_x = track3_x
train3_y = track3_y
train3_direction = "right"
train3_speed = 1 

train4_x = track4_x
train4_y = track4_y
train4_direction = "right"
train4_speed = 1 

# Definição das dimensões dos trens
train_width = 30
train_height = 20

# Inicialização do Tkinter
root = tk.Tk()
root.title("Controle de Velocidade")
root.geometry("300x350")

# Função para atualizar a velocidade do trem 1
def update_speed1(value):
    global train1_speed
    train1_speed = int(float(value))

# Função para atualizar a velocidade do trem 2
def update_speed2(value):
    global train2_speed
    train2_speed = int(float(value))

def update_speed3(value):
    global train3_speed
    train3_speed = int(float(value))

def update_speed4(value):
    global train4_speed
    train4_speed = int(float(value))

def create_colored_label(text, color):
    label_frame = tk.Frame(root, bg=color)
    label_frame.pack(pady=5)
    label = tk.Label(label_frame, text=text, fg="black", bg=color)
    label.pack()

#label1 = tk.Label(root, text="Velocidade do Trem 1")
#label1.pack()
create_colored_label("Velocidade do Trem 1", "#ffbb00")
slider1 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=update_speed1)
slider1.pack(pady=10)

create_colored_label("Velocidade do Trem 2", "#2781db")
slider2 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=update_speed2)
slider2.pack(pady=10)

create_colored_label("Velocidade do Trem 3", "#d1320a")
slider3 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=update_speed3)
slider3.pack(pady=10)

create_colored_label("Velocidade do Trem 4", "#0db537")
slider4 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=update_speed4)
slider4.pack(pady=10)



# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher a tela com a cor branca
    screen.fill(white)

    # Desenhar a borda dos quatro retângulos da pista
    pygame.draw.rect(screen, black, (track1_x, track1_y, track_width, track_height), border_thickness)
    pygame.draw.rect(screen, black, (track2_x, track2_y, track_width, track_height), border_thickness)
    pygame.draw.rect(screen, black, (track3_x, track3_y, track_width, track_height), border_thickness)
    pygame.draw.rect(screen, black, (track4_x, track4_y, track_width, track_height), border_thickness)

    # Atualizar as coordenadas dos trens
    if train1_direction == "right":
        train1_x += train1_speed
        if train1_x >= track1_x + track_width - train_width:
            train1_direction = "down"
    elif train1_direction == "down":
        train1_y += train1_speed
        if train1_y >= track1_y + track_height - train_height:
            train1_direction = "left"
    elif train1_direction == "left":
        train1_x -= train1_speed
        if train1_x <= track1_x:
            train1_direction = "up"
    elif train1_direction == "up":
        train1_y -= train1_speed
        if train1_y <= track1_y:
            train1_direction = "right"

    if train2_direction == "right":
        train2_x += train2_speed
        if train2_x >= track2_x + track_width - train_width:
            train2_direction = "down"
    elif train2_direction == "down":
        train2_y += train2_speed
        if train2_y >= track2_y + track_height - train_height:
            train2_direction = "left"
    elif train2_direction == "left":
        train2_x -= train2_speed
        if train2_x <= track2_x:
            train2_direction = "up"
    elif train2_direction == "up":
        train2_y -= train2_speed
        if train2_y <= track2_y:
            train2_direction = "right"

    if train3_direction == "right":
        train3_x += train3_speed
        if train3_x >= track3_x + track_width - train_width:
            train3_direction = "down"
    elif train3_direction == "down":
        train3_y += train3_speed
        if train3_y >= track3_y + track_height - train_height:
            train3_direction = "left"
    elif train3_direction == "left":
        train3_x -= train3_speed
        if train3_x <= track3_x:
            train3_direction = "up"
    elif train3_direction == "up":
        train3_y -= train3_speed
        if train3_y <= track3_y:
            train3_direction = "right"

    if train4_direction == "right":
        train4_x += train4_speed
        if train4_x >= track4_x + track_width - train_width:
            train4_direction = "down"
    elif train4_direction == "down":
        train4_y += train4_speed
        if train4_y >= track4_y + track_height - train_height:
            train4_direction = "left"
    elif train4_direction == "left":
        train4_x -= train4_speed
        if train4_x <= track4_x:
            train4_direction = "up"
    elif train4_direction == "up":
        train4_y -= train4_speed
        if train4_y <= track4_y:
            train4_direction = "right"

    # Desenhar os retângulos dos trens
    pygame.draw.rect(screen, yellow, (train1_x, train1_y, train_width, train_height))
    pygame.draw.rect(screen, blue, (train2_x, train2_y, train_width, train_height))
    pygame.draw.rect(screen, red, (train3_x, train3_y, train_width, train_height))
    pygame.draw.rect(screen, green, (train4_x, train4_y, train_width, train_height))

    # Atualizar a tela
    pygame.display.flip()

    # Atraso de 10 milissegundos
    pygame.time.delay(10)

    # Atualizar o Tkinter
    root.update()

# Encerramento do Pygame
pygame.quit()
