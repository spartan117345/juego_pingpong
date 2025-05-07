import pygame
import  sys

# Inicialización
pygame.init()

# Colores
amarillo = (187, 173, 4)
amarilo_oscuro = (142, 130, 10 )
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (52, 237, 11)
rosado = (255, 195, 203)
negro = (0,0,0)
naranja = (194, 88, 0)
blanco = (255, 255, 255)
cian = (0, 255, 255)
gris = (118, 120, 119)
gris_oscuro = (80, 81, 81)
gris_mas_oscuro = (58,59,58)
gris_claro = (198, 200, 199)
boca = (197, 71, 56)
morado = (145, 74, 201 )
cafe = (91, 10, 10 )

# Crear ventana
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("juego pingpong")
ventana.fill(negro)

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# variables del movimiento del player_1
XX1 = 200
YY1 = 300



# Bucle principal
while True:
    clock.tick(50)  # Limita los FPS a 50

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.draw.rect(ventana, blanco, (800, 20, 0,250))
    pygame.draw.line(ventana, blanco, (0,150),(800,150),3)
    pygame.draw.line(ventana, blanco, (0,450),(800,450),3)    
    pygame.draw.rect(ventana, rojo, (YY1,XX1,20,60 ))
    
    # Movimiento de la gallina con teclas (se usa get_pressed() para un movimiento más fluido)
    keys = pygame.key.get_pressed()  # Obtiene todas las teclas presionadas
    if keys[pygame.K_w]:  # Tecla W (arriba)
        YY1 = YY1 - 3
    if keys[pygame.K_s]:  # Tecla S (abajo)
        YY1 = YY1 + 3
    if keys[pygame.K_a]:  # Tecla A (izquierda)
        XX1 = XX1 - 3
    if keys[pygame.K_d]:  # Tecla D (derecha)
        XX1 = XX1 + 3
    
    
    
    
    
    # Actualizar la pantalla
    pygame.display.flip()















