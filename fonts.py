import pygame

pygame.font.init()

font_list = pygame.font.get_fonts()

for font_name in font_list:
    print(font_name)