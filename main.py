import sys
import os
import time
import random
import math
#import pygame

# Installing pygame if it's not insstaled
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    print("[GAME] Trying to import pygame")
    import pygame
except:
    print("[EXCEPTION] Pygame not installed")

    try:
        print("[GAME] Trying to install pygame via pip")
        import pip
        install("pygame")
        print("[GAME] Pygame has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install pygame")
            import pip
            install("pygame")
            print("[GAME] Pygame has been installed")
        except:
            print("[ERROR 1] Pygame could not be installed")

    import pygame

# Center the window the best it can
os.environ["SDL_VIDEO_CENTERED"]='1'

# pygame configurations
pygame.init()
clock = pygame.time.Clock()
width,height = 1300, 700 
fps= 60
pygame.display.set_caption("Fourier Series Visualization!")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((width,height))

# Fonts
big_font = pygame.font.Font("myfont.ttf", 50)
small_font = pygame.font.Font("myfont.ttf", 20)
medium_font = pygame.font.Font("myfont.ttf", 35)
copy_right_font = pygame.font.SysFont("arials.ttf", 20)


# colors
white = (255, 255, 255)
black = (0, 0, 0)
navy = (0,0,128)
green = (32,178,170)
navy2 = (0,0,139)
screen.fill(white)	

# Function to draw text on screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)



# loop of square wave
def square():
	N = 1
	time= 0
	radius = 0
	pos_x = 400
	pos_y = 300
	wave_list = []
	offset = 300

	ITERATIONS = 5

	run=True
	while run:
	    clock.tick(fps)
	    screen.fill(white)

	    # Drawing Texts
	    draw_text("Press esc to return to main menu!", big_font, black, screen, 15, 620)	
	    draw_text("Press UP to increase number of itterations", small_font, black, screen, 15, 20)	
	    draw_text(" ©2021 | Created By DKHISSI AYOUB", copy_right_font, black, screen, 1065, 680)
	    draw_text("Number of iterations: "+ str(ITERATIONS), small_font, black, screen, 15, 50)	

	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            sys.exit()
	        if event.type == pygame.KEYDOWN:
	        	if event.key == pygame.K_ESCAPE:
	        		whoosh_SE.play()
	        		run = False
	        	if event.key == pygame.K_UP:
	        		tin_SE.play()
	        		ITERATIONS = ITERATIONS + 1
	        	if event.key == pygame.K_DOWN:
	        		tin_SE.play()
	        		if(ITERATIONS > 1):
	        			ITERATIONS = ITERATIONS - 1
	    x = pos_x
	    y = pos_y
	    for i in range(ITERATIONS):
	        old_x = x
	        old_y = y

	        N = i * 2 + 1
	        radius = 150 * (4/ (N * math.pi))
	        x += int( radius * math.cos(N * time))
	        y +=  int( radius * math.sin(N * time))


	        pygame.draw.circle(screen, navy, (old_x, old_y), int(radius) ,2)

	        pygame.draw.line(screen, black, (old_x, old_y), (x,y) , 3)
	        pygame.draw.circle(screen, green, (x,y), 5)

	    wave_list.insert(0, y)
	    if len(wave_list) > 1000:
	        wave_list.pop()

	    pygame.draw.line(screen, navy, (x,y), (pos_x+offset, wave_list[0]), 3)

	    for index in range(len(wave_list)):
	        pygame.draw.circle(screen, navy2, (index + pos_x + offset, wave_list[index]), 3)
	    time += 0.01

	    pygame.display.update()


# loop of Triangle wave
def triangle():
	N = 1
	time= 0
	radius = 0
	pos_x = 400
	pos_y = 300
	wave_list = []
	offset = 300

	ITERATIONS = 2
	run=True
	while run:
	    clock.tick(fps)
	    screen.fill(white)
	    # Drawing the text help
	    draw_text("Press esc to return to main menu!", big_font, black, screen, 15, 620)
	    draw_text("Press UP to increase number of itterations", small_font, black, screen, 15, 20)	
	    draw_text(" ©2021 | Created By DKHISSI AYOUB", copy_right_font, black, screen, 1065, 680)
	    draw_text("Number of iterations: "+ str(ITERATIONS), small_font, black, screen, 15, 50)

	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            sys.exit()
	        if event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_ESCAPE:
	            	whoosh_SE.play()
	            	run = False
	            if event.key == pygame.K_UP:
              	  	ITERATIONS = ITERATIONS + 1
              	  	tin_SE.play()
	            if event.key == pygame.K_DOWN:
	            	tin_SE.play()
	            	if(ITERATIONS > 1):
	                    ITERATIONS = ITERATIONS - 1
	    x = pos_x
	    y = pos_y
	    k = 1
	    for i in range(ITERATIONS):
	        old_x = x
	        old_y = y

	        N = i * 2 + 1
	        radius = 150*(8/ (N*math.pi)**2)
	        x += int( radius * math.sin(N * time))
	        y += int( radius * math.cos(N * time))


	        pygame.draw.circle(screen, navy, (old_x, old_y), int(radius) ,2)

	        pygame.draw.line(screen, black, (old_x, old_y), (x,y) , 3)
	        pygame.draw.circle(screen, green, (x,y), 2)

	    wave_list.insert(0, y)
	    if len(wave_list) > 1000:
	        wave_list.pop()

	    pygame.draw.line(screen, navy, (x,y), (pos_x+offset, wave_list[0]), 3)

	    for index in range(len(wave_list)):
	        pygame.draw.circle(screen, navy2, (index + pos_x + offset, wave_list[index]), 3)
	    time += 0.01

	    pygame.display.update()


# loop of sawTooth function
def sawTooth():
	N = 1
	time= 0
	radius = 0
	pos_x = 400
	pos_y = 300
	wave_list = []
	offset = 300

	ITERATIONS = 5
	run=True
	while run:
	    clock.tick(fps)
	    screen.fill(white)

	    # Drawing the text help
	    draw_text("Press esc to return to main menu!", big_font, black, screen, 15, 620)
	    draw_text("Press UP to increase the number of itterations", small_font, black, screen, 15, 20)
	    draw_text(" ©2021 | Created By DKHISSI AYOUB", copy_right_font, black, screen, 1065, 680)
	    draw_text("Number of iterations: "+ str(ITERATIONS), small_font, black, screen, 15, 50)
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            sys.exit()
	        if event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_ESCAPE:
	            	whoosh_SE.play()
	            	run = False
	            if event.key == pygame.K_UP:
              	  	tin_SE.play()
              	  	ITERATIONS = ITERATIONS + 1
	            if event.key == pygame.K_DOWN:
	            	tin_SE.play()
	            	if(ITERATIONS > 1):
	                    ITERATIONS = ITERATIONS - 1

	    x = pos_x
	    y = pos_y
	    for i in range(ITERATIONS):
	        old_x = x
	        old_y = y

	        N = i + 1
	        radius = 120 * (3/ (N * math.pi))
	        x -= int( radius * math.cos(N * time*2))
	        y -= int( radius * math.sin((N*time)*2))


	        pygame.draw.circle(screen, navy, (old_x, old_y), int(radius) ,2)

	        pygame.draw.line(screen, black, (old_x, old_y), (x,y) , 3)
	        pygame.draw.circle(screen, green, (x,y), 5)

	    wave_list.insert(0, y)
	    if len(wave_list) > 1000:
	        wave_list.pop()

	    pygame.draw.line(screen, navy, (x,y), (pos_x+offset, wave_list[0]), 3)

	    for index in range(len(wave_list)):
	        pygame.draw.circle(screen, navy2, (index + pos_x + offset, wave_list[index]), 3)
	    time += 0.01

	    pygame.display.update()


# IMAGES
img_square = pygame.image.load("square.png")
img_triangle = pygame.image.load("triangle.png")
img_sawtooth = pygame.image.load("sawtooth.png")


# Square button properties
square_button_x = 200
square_button_y = 200
square_button_width = 300
square_button_height = 180


button_square = pygame.Rect(square_button_x, square_button_y, square_button_width, square_button_height)

# Triangle button properties
triangle_button_x = 800
triangle_button_y = 200
triangle_button_width = 300
triangle_button_height = 180
button_triangle = pygame.Rect(triangle_button_x, triangle_button_y, triangle_button_width, triangle_button_height)

# SawTooth button properties
sawTooth_button_x = 500
sawTooth_button_y = 450
sawTooth_button_width = 300
sawTooth_button_height = 180
button_sawTooth = pygame.Rect(sawTooth_button_x, sawTooth_button_y, sawTooth_button_width, sawTooth_button_height)

# Sound effects
click_SE = pygame.mixer.Sound('click1.wav')
tin_SE = pygame.mixer.Sound('tin.wav')
whoosh_SE = pygame.mixer.Sound('whoosh.wav')



# Main Game Loop
run=True
click = False
while run:
    clock.tick(fps)
    screen.fill(white)

    # Text drawings
    draw_text("Fourier Series Visualization!", big_font, black, screen, 320, 20)
    draw_text("Choose a function to Visualize:", big_font, black, screen, 10, 100)
    draw_text("Square Wave", medium_font, black, screen, 255, 380)
    draw_text("Triangle Wave", medium_font, black, screen, 852, 380)
    draw_text("SawTooth Wave", medium_font, black, screen, 545, 630)
    draw_text(" ©2021 | Created By DKHISSI AYOUB", copy_right_font, black, screen, 1065, 680)



    # Drawing buttons:
    pygame.draw.rect(screen, navy, button_square, border_radius = 15)
    screen.blit(img_square, (square_button_x, square_button_y))

    pygame.draw.rect(screen, navy, button_triangle, border_radius = 15)
    screen.blit(img_triangle, (triangle_button_x, triangle_button_y))

    pygame.draw.rect(screen, navy, button_sawTooth, border_radius = 15)
    screen.blit(img_sawtooth, (sawTooth_button_x, sawTooth_button_y))



    # Handling events

    # Get mouse position:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

    if button_square.collidepoint((mouse_x, mouse_y)):
    	pygame.draw.rect(screen, (0, 100, 255), button_square, 3 , border_radius = 15) # Hover-over 
    	if click:
        	click_SE.play()
        	square()
    elif button_triangle.collidepoint((mouse_x, mouse_y)):
    	pygame.draw.rect(screen, (0, 100, 255), button_triangle, 3 , border_radius = 15) # Hover-over
    	if click:
    		click_SE.play() 
    		triangle()
    elif button_sawTooth.collidepoint((mouse_x, mouse_y)):
    	pygame.draw.rect(screen, (0, 100, 255), button_sawTooth, 3 , border_radius = 15) # Hover-over
    	if click:
    		click_SE.play()
    		sawTooth()

    

    pygame.display.update()








pygame.quit()