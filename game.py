import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 675
screen_height = 732

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Flappy Bird')
#game - variables
ground_scroll = 0
scroll_speed = 4
flying =False
over=False
#loading images
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for n in range(1,4):
            img=pygame.image.load(f'img/bird{n}.png')
            self.images.append(img)
        self.image = self.images[self.index] 
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.velocity=0
        self.clicked=False
    def update(self):
        if flying==True:
            self.velocity+=0.6
            if self.velocity>5:
                self.vel=5
            print(self.velocity)    
            if self.rect.bottom<600:
                self.rect.y+=int(self.velocity)
        if over==False:
            keys=pygame.key.get_pressed()  
            if (keys[K_SPACE] or pygame.mouse.get_pressed()[0]==1) and self.clicked==False:
                self.clicked=True
                self.velocity=-6
            if keys[K_SPACE]==0 and pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
            self.counter+=1
            flap_cooldown=10
            if self.counter>flap_cooldown:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
            self.image=self.images[self.index]  
            self.image=pygame.transform.rotate(self.images[self.index],-2*self.velocity) 
        else:
            self.image=pygame.transform.rotate(self.images[self.index],-90)

bird_group=pygame.sprite.Group()
flappy= Bird(100,int(screen_height/2))
bird_group.add(flappy)






run = True
while run:

    clock.tick(fps)

    screen.blit(bg,(0,0))
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(ground_img,(ground_scroll,600))
    if flappy.rect.bottom>600:
        over=True
        flying=False
    if over==False:
        ground_scroll-=scroll_speed
        if abs(ground_scroll)>35:
            ground_scroll=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys=pygame.key.get_pressed()
        if over==False and flying==False and (keys[K_SPACE] or pygame.MOUSEBUTTONDOWN==event.type) :
            flying=True    
    pygame.display.update()

pygame.quit()