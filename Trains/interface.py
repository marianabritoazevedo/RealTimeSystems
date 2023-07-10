import pygame
import pygame_gui
from pygame.locals import *
import tkinter as tk
from tkinter import ttk
from constants import *

# Função para atualizar a velocidade do trem 1
def update_speed1(value, train1):
    global train1_speed
    train1_speed = int(float(value))
    #train1.speed = train1_speed
    train1.setSpeed(int(float(value)))

# Função para atualizar a velocidade do trem 2
def update_speed2(value, train2):
    global train2_speed
    train2_speed = int(float(value))
    #train2.speed = train2_speed
    train2.setSpeed(int(float(value)))

def update_speed3(value, train3):
    global train3_speed
    train3_speed = int(float(value))
    #train3.speed = train3_speed
    train3.setSpeed(int(float(value)))
    

def update_speed4(value, train4):
    global train4_speed
    train4_speed = int(float(value))
    train4.setSpeed(int(float(value)))
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

    # Criação da interface de usuário
    manager = pygame_gui.UIManager((screen_width, screen_height))

    # Definição das coordenadas dos retângulos da pista
    #train1.x = (screen_width - track_width * 2 - border_thickness) // 2
    #train1.x = train1.x
    #train1.y = (screen_height - track_height * 2 - border_thickness * 3) // 2
    #train1.y = train1.y

    #train2.x = train1.x + track_width + border_thickness
    #train2.x = train2.x
    #train2.y = train1.y
    #train2.y = train2.y

    # Definição das coordenadas das pistas inferiores
    #train3.x = train1.x
    #train3.x = train3.x
    #train3.y = train2.y + track_height + border_thickness
    #train3.y = train3.y

    #train4.x = train2.x
    #train4.x = train4.x

    #train4.y = train2.y + track_height + border_thickness
    #train4.y = train4.y

    '''# Definição das coordenadas e velocidades iniciais dos trens
    train1.x = train1.x
    train1_y = train1.y
    train1_direction = train1.direction
    #train1_speed = train1.speed  
    #train1_speed = 1

    train2_x = train2.x
    train2_y = train2.y
    train2_direction = train2.direction
    #train2_speed = train2.speed
    #train2_speed = 1 

    train3_x = train3.x
    train3_y = train3.y
    train3_direction = train3.direction
    #train3_speed = train3.speed
    #train3_speed = 1

    train4_x = train4.x
    train4_y = train4.y
    train4_direction = train4.direction
    #train4_speed = train4.speed 
    #train4_speed = 1'''

    '''# Inicialização do Tkinter
    root = tk.Tk()
    root.title("Controle de Velocidade")
    root.geometry("300x350")'''

    '''#label1 = tk.Label(root, text="Velocidade do Trem 1")
    #label1.pack()
    create_colored_label("Velocidade do Trem 1", "#ffbb00", root)
    slider1 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=lambda value: update_speed1(value, train1))
    #slider1 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=update_speed1)
    slider1.pack(pady=10)

    create_colored_label("Velocidade do Trem 2", "#2781db", root)
    slider2 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=lambda value: update_speed2(value, train2))
    #slider2 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=update_speed2)
    slider2.pack(pady=10)

    create_colored_label("Velocidade do Trem 3", "#d1320a", root)
    slider3 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=lambda value: update_speed3(value, train3))
    #slider3 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=update_speed3)
    slider3.pack(pady=10)

    create_colored_label("Velocidade do Trem 4", "#0db537", root)
    slider4 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=lambda value: update_speed4(value, train4))
    #slider4 = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=update_speed4)
    slider4.pack(pady=10)'''

    # Criação dos controles deslizantes
    slider1rec = pygame.Rect(300, 500, 200, 15)
    slider1 = pygame_gui.elements.UIHorizontalSlider(slider1rec, 1.0, (1.0, 50.0), manager=manager)

    slider2rec = pygame.Rect(300, 520, 200, 15)
    slider2 = pygame_gui.elements.UIHorizontalSlider(slider2rec, 1.0, (1.0, 50.0), manager=manager)

    slider3rec = pygame.Rect(300, 540, 200, 15)
    slider3 = pygame_gui.elements.UIHorizontalSlider(slider3rec, 1.0, (1.0, 50.0), manager=manager)

    slider4rec = pygame.Rect(300, 560, 200, 15)
    slider4 = pygame_gui.elements.UIHorizontalSlider(slider4rec, 1.0, (1.0, 50.0), manager=manager)

    # Loop principal do jogo
    running = True
    clock = pygame.time.Clock()
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            manager.process_events(event)

        manager.update(time_delta)

        # Atualiza a velocidade dos trens com base nos sliders
        train1.setSpeed(slider1.get_current_value())
        train2.setSpeed(slider2.get_current_value())
        train3.setSpeed(slider3.get_current_value())
        train4.setSpeed(slider4.get_current_value())

        # Preencher a tela com a cor branca
        screen.fill(white)

        # Desenhar quadrado
        pygame.draw.rect(screen, gray, (200,50,400,400))

        # Desenhar a borda dos quatro retângulos da pista
        pygame.draw.rect(screen, lightgray, (220, 70, track_width, track_height))
        pygame.draw.rect(screen, lightgray, (410, 70, track_width, track_height))
        pygame.draw.rect(screen, lightgray, (220, 260, track_width, track_height))
        pygame.draw.rect(screen, lightgray, (410, 260, track_width, track_height))

        '''# Atualizar as coordenadas dos trens
        if train1_direction == "right":
            train1.x += train1.speed
            if train1.x >= train1.x + track_width - train_width:
                train1_direction = "down"
        elif train1_direction == "down":
            train1_y += train1.speed
            if train1_y >= train1.y + track_height - train_height:
                train1_direction = "left"
        elif train1_direction == "left":
            train1.x -= train1.speed
            if train1.x <= train1.x:
                train1_direction = "up"
        elif train1_direction == "up":
            train1_y -= train1.speed
            if train1_y <= train1.y:
                train1_direction = "right"

        if train2_direction == "right":
            train2_x += train2.speed
            if train2_x >= train2.x + track_width - train_width:
                train2_direction = "down"
        elif train2_direction == "down":
            train2_y += train2.speed
            if train2_y >= train2.y + track_height - train_height:
                train2_direction = "left"
        elif train2_direction == "left":
            train2_x -= train2.speed
            if train2_x <= train2.x:
                train2_direction = "up"
        elif train2_direction == "up":
            train2_y -= train2.speed
            if train2_y <= train2.y:
                train2_direction = "right"

        if train3_direction == "right":
            train3_x += train3.speed
            if train3_x >= train3.x + track_width - train_width:
                train3_direction = "down"
        elif train3_direction == "down":
            train3_y += train3.speed
            if train3_y >= train3.y + track_height - train_height:
                train3_direction = "left"
        elif train3_direction == "left":
            train3_x -= train3.speed
            if train3_x <= train3.x:
                train3_direction = "up"
        elif train3_direction == "up":
            train3_y -= train3.speed
            if train3_y <= train3.y:
                train3_direction = "right"

        if train4_direction == "right":
            train4_x += train4.speed
            if train4_x >= train4.x + track_width - train_width:
                train4_direction = "down"
        elif train4_direction == "down":
            train4_y += train4.speed
            if train4_y >= train4.y + track_height - train_height:
                train4_direction = "left"
        elif train4_direction == "left":
            train4_x -= train4.speed
            if train4_x <= train4.x:
                train4_direction = "up"
        elif train4_direction == "up":
            train4_y -= train4.speed
            if train4_y <= train4.y:
                train4_direction = "right"'''

        # Desenhar os retângulos dos trens
        pygame.draw.rect(screen, train1.color, (train1.x, train1.y, train_width, train_height))
        pygame.draw.rect(screen, train2.color, (train2.x, train2.y, train_width, train_height))
        pygame.draw.rect(screen, train3.color, (train3.x, train3.y, train_width, train_height))
        pygame.draw.rect(screen, train4.color, (train4.x, train4.y, train_width, train_height))

        # Desenha alavancas de velocidade
        pygame.draw.rect(screen, gray, (250,490,270,95))

        pygame.draw.rect(screen, train1.color, (260, 500, 15, 15))
        pygame.draw.rect(screen, train2.color, (260, 520, 15, 15))
        pygame.draw.rect(screen, train3.color, (260, 540, 15, 15))
        pygame.draw.rect(screen, train4.color, (260, 560, 15, 15))

        '''# Atualizar a tela
        pygame.display.flip()

        # Atraso de 10 milissegundos
        pygame.time.delay(10)

        # Atualizar o Tkinter
        root.update()'''
        manager.draw_ui(screen)
        pygame.display.update()

    # Encerramento do Pygame
    pygame.quit()
