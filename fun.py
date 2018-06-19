import random
import pygame

pygame.init
width = 1000
height = 700
s = pygame.display.set_mode((width,height))
#wowzers
running = True
class base_sprite(pygame.sprite.Sprite):
        def __init__(self, color=(0,0,0), width=0, height=0, image=None,x=0,y=0, scale=None, surface=False):
            pygame.sprite.Sprite.__init__(self)
            if "Surface" in type(image).__name__ or surface:
                self.image = image
            else:
                self.image = pygame.image.load(image)
            if scale != None:
                self.image = pygame.transform.scale(self.image, (scale[0], scale[1]))
            pygame.draw.rect(self.image, color, [5000000,5000000,width,height])
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def blit(self, screen):
            self.image.blit(self.image, screen)
sptW = 50
sptH = 100
yPos = height/2
xPos = width/2
sprite = base_sprite(image = 'sprite.png', width = sptW, height = sptH)
home = pygame.sprite.Group()

while running:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_LEFT):
                                xPos += 3
                        if (event.key == pygame.K_RIGHT):
                                xPos -= 3
                        if (event.key == pygame.K_UP):
                                yPos += 1
                        if (event.key == pygame.K_DOWN):
                                yPos -= 1
                if xPos >=  width:
                        xPos -= sptW
                        


        
        home.add(sprite)
        home.draw(s)
        pygame.display.update()
        pygame.display.flip()
        
    
    




