import pygame
import sys

# Inicialización
pygame.init()

# Colores
amarillo = (187, 173, 4)
rojo = (255, 0, 0)
azul = (0, 0, 255)
blanco = (255, 255, 255)
negro = (0, 0, 0)
amarilo_oscuro = (142, 130, 10 )
verde = (0, 255, 255)
rosado = (255, 195, 203)
naranja = (194, 88, 0)
cian = (0, 255, 255)
gris = (118, 120, 119)
gris_oscuro = (80, 81, 81)
gris_mas_oscuro = (58,59,58)
gris_claro = (198, 200, 199)
rosadito = (197, 71, 56)
morado = (145, 74, 201 )
cafe = (91, 10, 10 )
# Crear ventana
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dream stellar")

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Variables del movimiento de los jugadores
XX1, YY1 = 200, 280
XX2, YY2 = 600, 280

# Bucle principal
while True:
    clock.tick(50)  # Limita los FPS a 50

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar pantalla con color negro
    ventana.fill(negro)
    
    # Dibujar elementos
    pygame.draw.rect(ventana, blanco, (800, 20, 0, 250))
    pygame.draw.line(ventana, blanco, (0, 150), (800, 150), 3)
    pygame.draw.line(ventana, blanco, (0, 450), (800, 450), 3)
    pygame.draw.rect(ventana, rojo, (XX1, YY1, 20, 60))
    pygame.draw.rect(ventana, azul, (XX2, YY2, 20, 60))
    pygame.draw.line(ventana, blanco, (0,450),(800,450),3)    
    pygame.draw.rect(ventana, blanco, (100,500,20,100 ))
    pygame.draw.rect(ventana, blanco, (200,500,20,100,))
    pygame.draw.rect(ventana, blanco, (300,500,20,100,))
    pygame.draw.rect(ventana, blanco, (500,500,20,100,))
    pygame.draw.rect(ventana, blanco, (600,500,20,100,))
    pygame.draw.rect(ventana, blanco, (700,500,20,100,))
    pygame.draw.rect(ventana, blanco, (1,500,20,100,))
    pygame.draw.rect(ventana, blanco, (780,500,20,100,))
    pygame.draw.rect(ventana, blanco, (1,480,319,20))
    pygame.draw.rect(ventana, blanco, (500,480,400,20))
    pygame.draw.rect(ventana, blanco, (335,590,150,20,))
    pygame.draw.rect(ventana, rojo, (335,479,150,100,))
    pygame.draw.rect(ventana, blanco, (335,1,150,10,))
    pygame.draw.rect(ventana, azul, (335,20,150,100,))
    pygame.draw.rect(ventana, blanco, (300,500,20,100,))
    pygame.draw.rect(ventana, blanco , ( 1,0,20,100  ))
    pygame.draw.rect(ventana, blanco , ( 100,0,20,100  ))
    pygame.draw.rect(ventana, blanco , ( 200,0,20,100  ))
    pygame.draw.rect(ventana, blanco , ( 300,0,20,100  ))
    pygame.draw.rect(ventana, blanco , ( 500,0,20,100  ))
    pygame.draw.rect(ventana, blanco , ( 600,0,20,100  ))
    pygame.draw.rect(ventana, blanco , ( 700,0,20,100  ))
    pygame.draw.rect(ventana, blanco , ( 800,0,20,100  ))
    pygame.draw.rect(ventana, blanco , ( 780,0,20,100  ))
    pygame.draw.rect(ventana,blanco,(1,100,319,20))
    pygame.draw.rect(ventana,blanco,(500,100,600,20))
    pygame.draw.line(ventana, blanco, (410,150),(410,450),4)
    pygame.draw.circle(ventana, morado,(410,315),11,11)
    # Movimiento de las palas con teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Tecla W (arriba)
        YY1 -= 3
    if keys[pygame.K_s]:  # Tecla S (abajo)
        YY1 += 3
    if keys[pygame.K_a]:  # Tecla A (izquierda)
        XX1 -= 3
    if keys[pygame.K_d]:  # Tecla D (derecha)
        XX1 += 3
    if keys[pygame.K_UP]:  # Flecha arriba
        YY2 -= 3
    if keys[pygame.K_DOWN]:  # Flecha abajo
        YY2 += 3
    if keys[pygame.K_LEFT]:  # Flecha izquierda
        XX2 -= 3
    if keys[pygame.K_RIGHT]:  # Flecha derecha
        XX2 += 3

    # texto de la version del juego
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("version 1.2.0",3, gris_mas_oscuro)
    ventana.blit(texto,(580,450))


    if YY1 >= 390:
        YY1 = YY1 - 5

    if YY2 >= 390:
        YY2 = YY2 - 5

    if YY1 <= 150:
        YY1 = YY1 + 5

    if YY2 <=  150:
        YY2 = YY2 + 5

    if XX1 <= 0:
        XX1 = XX1 + 5

    if XX2 >= 780:
        XX2 = XX2 - 5

    if XX1 >= 390:
        XX1 = XX1 - 5

    if XX2 <= 410:
        XX2 = XX2 + 5
    # Actualizar la pantalla
    pygame.display.flip()