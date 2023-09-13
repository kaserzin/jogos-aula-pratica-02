
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

lar, alt = 860, 480
tela = pygame.display.set_mode((lar, alt))

bola = 'bola.png'
mexer = pygame.image.load(bola).convert_alpha()
mexer = pygame.transform.scale(mexer, (40, 40))
imagem_de_fundo = 'imagem_de_fundo.png'
imagem = pygame.image.load(imagem_de_fundo).convert()
imagem = pygame.transform.scale(imagem, (lar, alt))
3

x, y = lar // 2, alt // 2
ligeresa = 0.5

ta_chei = False
if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_f]:
            ta_chei = not ta_chei
            if ta_chei:
                tela = pygame.display.set_mode((lar, alt), FULLSCREEN)
            else:
                tela = pygame.display.set_mode((lar, alt), 0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= ligeresa
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += ligeresa
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= ligeresa
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += ligeresa

        tela.blit(imagem, (0,0))

        tela.blit(mexer, (x, y))

        pygame.display.flip()