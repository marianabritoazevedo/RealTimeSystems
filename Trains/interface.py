import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import ttk
from constants import *

# Função para atualizar a velocidade do trem 1
def update_speed1(value, train1):
    global train1_speed
    train1_speed = int(float(value))
    #train1.speed = train1_speed
    train1.setSpeed(train1_speed)

# Função para atualizar a velocidade do trem 2
def update_speed2(value, train2):
    global train2_speed
    train2_speed = int(float(value))
    #train2.speed = train2_speed
    train2.setSpeed(train2_speed)

def update_speed3(value, train3):
    global train3_speed
    train3_speed = int(float(value))
    #train3.speed = train3_speed
    train3.setSpeed(train3_speed)
    

def update_speed4(value, train4):
    global train4_speed
    train4_speed = int(float(value))
    train4.setSpeed(train4_speed)
    #train4.speed = train4_speed

def create_colored_label(text, color, root):
    label_frame = tk.Frame(root, bg=color)
    label_frame.pack(pady=5)
    label = tk.Label(label_frame, text=text, fg="black", bg=color)
    label.pack()

def interface(train1, train2, train3, train4):
    # Inicialização do Pygame
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pista")

    # Definição das coordenadas dos retângulos da pista
    #track1_x = (screen_width - track_width * 2 - border_thickness) // 2
    track1_x = train1.x
    #track1_y = (screen_height - track_height * 2 - border_thickness * 3) // 2
    track1_y = train1.y

    #track2_x = track1_x + track_width + border_thickness
    track2_x = train2.x
    #track2_y = track1_y
    track2_y = train2.y

    # Definição das coordenadas das pistas inferiores
    #track3_x = track1_x
    track3_x = train3.x
    #track3_y = track2_y + track_height + border_thickness
    track3_y = train3.y

    #track4_x = track2_x
    track4_x = train4.x

    #track4_y = track2_y + track_height + border_thickness
    track4_y = train4.y

    # Definição das coordenadas e velocidades iniciais dos trens
    train1_x = train1.x
    train1_y = train1.y
    train1_direction = train1.direction
    train1_speed = train1.speed  

    train2_x = train2.x
    train2_y = train2.y
    train2_direction = train2.direction
    train2_speed = train2.speed 

    train3_x = train3.x
    train3_y = train3.y
    train3_direction = train3.direction
    train3_speed = train3.speed

    train4_x = train4.x
    train4_y = train4.y
    train4_direction = train4.direction
    train4_speed = train4.speed 

    # Inicialização do Tkinter
    root = tk.Tk()
    root.title("Controle de Velocidade")
    root.geometry("300x350")

    #label1 = tk.Label(root, text="Velocidade do Trem 1")
    #label1.pack()
    create_colored_label("Velocidade do Trem 1", "#ffbb00", root)
    slider1 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=lambda value: update_speed1(value, train1))
    slider1.pack(pady=10)

    create_colored_label("Velocidade do Trem 2", "#2781db", root)
    slider2 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=lambda value: update_speed2(value, train2))
    slider2.pack(pady=10)

    create_colored_label("Velocidade do Trem 3", "#d1320a", root)
    slider3 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=lambda value: update_speed3(value, train3))
    slider3.pack(pady=10)

    create_colored_label("Velocidade do Trem 4", "#0db537", root)
    slider4 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=lambda value: update_speed4(value, train4))
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
        pygame.draw.rect(screen, train1.color, (train1_x, train1_y, train_width, train_height))
        pygame.draw.rect(screen, train2.color, (train2_x, train2_y, train_width, train_height))
        pygame.draw.rect(screen, train3.color, (train3_x, train3_y, train_width, train_height))
        pygame.draw.rect(screen, train4.color, (train4_x, train4_y, train_width, train_height))

        # Atualizar a tela
        pygame.display.flip()

        # Atraso de 10 milissegundos
        pygame.time.delay(10)

        # Atualizar o Tkinter
        root.update()

    # Encerramento do Pygame
    pygame.quit()
