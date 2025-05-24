import pygame
import sys

# Inicialización
pygame.init()
pygame.mixer.init()

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
morado_puro = (131, 0, 255)




# Crear ventana
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dream stellar")

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()


# Variables del movimiento de los jugadores
XX1 = 200
YY1 = 280
XX2 = 600
YY2 = 280
YY3 = 295
XX3 = 410
YY4 = 0
XX4 = 0
YY5 = -100
XX5 = 300
YY6 = -100
YY7 = -100
YY8 = -100
YY9 = -100
YY10 = -100
YY11 = -100
YY12 = -100
movimientoX = 0
movimientoY = 1 

# varibales de puntos
puntos_1 = 0
puntos_2 = 0
tiempo = 0
tiempo2 = 0
tiempo3 = 0
velocidad = 0

# sonido de fondo
musica = pygame.mixer.music.load("sounds/musica.ogg")
pygame.mixer.music.play(1,0,0)

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

    pygame.draw.rect(ventana,blanco,(500,100,600,20))
    pygame.draw.line(ventana, blanco, (410,150),(410,450),4)

    # Dibujar elementos
    pygame.draw.rect(ventana,gris,(5,480,300,150))
    pygame.draw.rect(ventana,gris,(5,0,300,100))
    pygame.draw.rect(ventana,gris,(520,0,300,100))
    pygame.draw.rect(ventana,gris,(520,500,300,100))
    pygame.draw.rect(ventana, blanco, (800, 20, 0, 250))
    pygame.draw.line(ventana, blanco, (0, 150), (800, 150), 3)
    pygame.draw.line(ventana, blanco, (0, 450), (800, 450), 3)
    pygame.draw.line(ventana, blanco, (0,450),(800,450),3)    
    pygame.draw.rect(ventana, blanco, (500,500,20,100,))
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
    pygame.draw.rect(ventana, blanco , ( 300,0,20,100  ))
    pygame.draw.rect(ventana, blanco , ( 500,0,20,100  ))
    pygame.draw.rect(ventana, blanco , ( 780,0,20,100  ))
    pygame.draw.rect(ventana,blanco,(1,100,319,20))
    pygame.draw.rect(ventana,blanco,(500,100,600,20))

    # se carga el logo del juego y se pone en mitad de la cancha
    logo = pygame.image.load("img/logo.png")
    logo = pygame.transform.scale(logo, (150,150))
    ventana.blit(logo, (338 , 230))

    # cargamos el publico
    
    mictiano = pygame.image.load("img/mictiano.png")
    mictiano = pygame.transform.scale(mictiano,(70,70))
    ventana.blit(mictiano, (700,510))

    mictiano2 = pygame.image.load("img/mictiano.png")
    mictiano2 = pygame.transform.scale(mictiano2,(70,70))
    ventana.blit(mictiano2, (30,10))

    mictiano3 = pygame.image.load("img/mictiano.png")
    mictiano3 = pygame.transform.scale(mictiano3,(70,70))
    ventana.blit(mictiano3, (530,10))

    mictiano4 = pygame.image.load("img/mictiano.png")
    mictiano4 = pygame.transform.scale(mictiano4,(70,70))
    ventana.blit(mictiano4, (120,510))
    
    cualquierpersona = pygame.image.load("img/cualquierpersona.png")
    cualquierpersona = pygame.transform.scale(cualquierpersona,(130,130))
    ventana.blit(cualquierpersona,(5,490))

    aquino = pygame.image.load("img/aquino.png")
    aquino = pygame.transform.scale(aquino,(100,100))
    ventana.blit(aquino,(100,-7))

    pepe = pygame.image.load("img/pepe.png")
    pepe = pygame.transform.scale(pepe,(200,200))
    ventana.blit(pepe, (580,-50))
    
    panterarosa = pygame.image.load("img/panterarosa.png")
    panterarosa = pygame.transform.scale(panterarosa,(100,100))
    ventana.blit(panterarosa,(520,500))
    
    # esterek de la primera version de los personajes
    pygame.draw.rect(ventana, rojo, (XX1, YY1, 20, 60))
    pygame.draw.rect(ventana, azul, (XX2, YY2, 20, 60))

    # se carga el jugador 1
    rojo_player = pygame.image.load("img/rojo.png")
    rojo_player = pygame.transform.scale(rojo_player, (50,60))
    ventana.blit(rojo_player, (XX1 , YY1))

    # se carga el jugador 2
    azul_player = pygame.image.load("img/azul.png")
    azul_player = pygame.transform.scale(azul_player, (60, 60))
    ventana.blit(azul_player, (XX2, YY2))

    # generamos la pelota
    pygame.draw.circle(ventana, morado,(XX3,YY3),11,11)
    # Movimiento de los personajes con teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Tecla W (arriba)
        YY1 -= 5
    if keys[pygame.K_s]:  # Tecla S (abajo)
        YY1 += 5
    if keys[pygame.K_a]:  # Tecla A (izquierda)
        XX1 -= 5
    if keys[pygame.K_d]:  # Tecla D (derecha)
        XX1 += 5
    if keys[pygame.K_UP]:  # Flecha arriba
        YY2 -= 5
    if keys[pygame.K_DOWN]:  # Flecha abajo
        YY2 += 5
    if keys[pygame.K_LEFT]:  # Flecha izquierda
        XX2 -= 5
    if keys[pygame.K_RIGHT]:  # Flecha derecha
        XX2 += 5

    # pantalla de carga
    tiempo = tiempo + 1
    tiempo2 = tiempo2 + 2
    
    if keys[pygame.K_RETURN]:
        tiempo2 = 20
        YY4 = -600
        XX5 = -300
        movimientoX = 17
        velocidad = 1000

    if tiempo2 >= 50:
        # movimiento de la pelota
        XX3 = XX3 + movimientoX   
        YY3 =  movimientoY + YY3

    # puntuaciones    
    if XX3 >= 790:
        puntos_1 = puntos_1 + 1

    if XX3 <= 0:
        puntos_2 = puntos_2 + 1

    velocidad = velocidad + 1
    

    # texto de la version del juego
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("version 1.11.0",3, gris_mas_oscuro)
    ventana.blit(texto,(560,450))

    # texto de los puntos del jugador 1
    fuente_arial = pygame.font.SysFont("Arial", 50, 1, 1)
    texto = fuente_arial.render(str(puntos_1),3, negro)
    ventana.blit(texto,(390,510))

    # texto de los puntos del jugador 2
    fuente_arial = pygame.font.SysFont("Arial", 50, 1, 1)
    texto = fuente_arial.render(str(puntos_2),3, negro)
    ventana.blit(texto,(390,50))
    
    # cargamos la imagen de la pantalla del inicio
    carga = pygame.image.load("img/carga2.png")
    carga = pygame.transform.scale(carga,(800,600) )
    ventana.blit(carga, (XX4, YY4))

    # texto que sale en la pantalla de inicio
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("press Enter",3, blanco)
    ventana.blit(texto,(XX5,450))
    
    # hitbox de los personajes    
    XX23 = XX2 + 50
    YY23 = YY2 + 50

    if XX3 >= XX2 and XX3 <= XX23 and YY3 >= YY2 and YY3 <= YY23:
        if keys[pygame.K_SPACE]:
            movimientoX = -19
    
    XX24 = XX1 + 50
    YY24 = YY1 + 50

    if XX3 >= XX1 and XX3 <= XX24 and YY3 >= YY1 and YY3 <= YY24:
        if keys[pygame.K_e]:
            movimientoX = 19
 
    # condiciones utilizadas para que los personajes y la pelota no se salgan del mapa
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

    if XX2 >= 740:
        XX2 = XX2 - 5

    if XX1 >= 290:
        XX1 = XX1 - 5

    if XX2 <= 480:
        XX2 = XX2 + 5

    if XX3 >= 790 or XX3 <= 0:
            XX3 = 410
            YY3 = 295
            tiempo = 800
    

    
    if YY3 >= 430:
        movimientoY = -1

    if YY3 <= 170:
        movimientoY = 1
        
    # condicion para que el juego finalice cuando un jugador llegue a los 5 puntos
    if puntos_1 >= 8:
        texto = fuente_arial.render("VICTORIA DEL JUGADOR 1",3, amarillo)
        ventana.blit(texto,(180,200))
        movimientoX = 0
        movimientoY = 0
        
    if puntos_2 >= 8:
        texto = fuente_arial.render("VICTORIA DEL JUGADOR 2",3, amarillo)
        ventana.blit(texto,(180,200))       
        movimientoX = 0
        movimientoY = 0



    # Actualizar la pantalla
    pygame.display.flip()