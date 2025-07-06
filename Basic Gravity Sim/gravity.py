import pygame
import time
import math

pygame.init()

#Function to update screen
def updateDisplay():
    #Updates Screen
    pygame.display.update()


#creating the screen - width and height tuple 
#Same as x and y axis, but (0,0) attop left then plus x and plus y as you go out from origin
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Gravity")

color = (68, 148, 8)

circleX = None
circleY = None

mousePressed = 0

def circle(x,y):
    pygame.draw.circle(screen, (0,0,0), (x, y), 10)


clock = pygame.time.Clock()

lastChecked = 0

mass = 10
circle_velocity = 0

gravityConst = 150

spacePressed = 0

def gravity(y, ti, vel, space):
    
    newY = y
    newCheck = ti
    newVel = vel
    
    newCheck = time.time()

    deltaT = newCheck - ti
    
    if space == 1 and y >= 530:
            
            newVel =  -275
    
    #Need to set
    if y < 540:
        
        newY = y + vel*deltaT + 0.5*gravityConst*(pow(deltaT, 2))
        
        newVel += gravityConst*deltaT
        
    elif y >= 540 and abs(vel) >= 20:
        
        newVel = -vel*0.75
        
        newY = 540 + newVel*deltaT + 0.5*gravityConst*(pow(deltaT, 2))
    
        if newY > 540:
            newY = 540
    else:
        newVel = 0
        newY = 540
    
    return newY, newCheck, newVel

xSpeed = 3
x_change = 0

running = True
while running:
    for event in pygame.event.get(): #makes sure all event are in pygame.event.get so that we can run through them and check if the close button is closed
        
        if event.type == pygame.QUIT: #changes running status when the close button is pressed
            
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            coords = pygame.mouse.get_pos()
            
            
            circleX, circleY = coords
            
            circle_velocity = 0
            
            mousePressed = 1
            
            #circleX = coords[0]
            
            #circleY = coords[1]
            lastChecked = time.time()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -xSpeed
            
            if event.key == pygame.K_RIGHT:
                x_change = xSpeed
            
            if event.key == pygame.K_SPACE:
                spacePressed = 1
            
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_SPACE:
                spacePressed = 0
    
    screen.fill((255,255,255))
    
    pygame.draw.rect(screen, color, pygame.Rect(0, 550, 800, 50))
    
    if mousePressed is 1:
        
        circleY, lastChecked, circle_velocity = gravity(circleY, lastChecked, circle_velocity, spacePressed)
        
        circleX += x_change
        
        circle(circleX,circleY)
        
        

    updateDisplay()

    clock.tick(60)
