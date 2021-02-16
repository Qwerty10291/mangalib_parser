import pygame
import sys
import os
DIRECTORY = '/home/ferret/manga/тирания_вооружённых/1'


glava_now, image_now = open('data.txt', 'r').read().replace('\n', '').split()
glava_now, image_now = int(glava_now), int(image_now)

file_now = open('data.txt', 'w')
print(pygame.init())

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

os.chdir(DIRECTORY)
glav = sorted(os.listdir(), key=lambda x: float(x))
images_now = []
slice_now = 0


def load_images(glava):
    global images_now
    images_now = [pygame.image.load(f'{DIRECTORY}/{glava}/{i}') for i in sorted(os.listdir(
        f'{DIRECTORY}/{glava}'), key=lambda x: os.path.getmtime(f'{DIRECTORY}/{glava}/{x}')) 
        if '.png' in i or '.jpg' in i or '.jpeg' in i]
    images_now = [pygame.transform.scale(i, (WIDTH, i.get_rect().height)) for i in images_now]


def re_draw():
    screen.fill((0, 0, 0))
    screen.blit(image, (x, y))
    pygame.display.update()


load_images(glava_now)
image_now = 0
image = images_now[image_now]
screen = pygame.display.set_mode((WIDTH, HEIGHT))

time = pygame.time.get_ticks()

pygame.display.set_caption(f'глава {glava_now} страница {image_now + 1}')
x, y = 0, 0
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            file_now.write(f'{glava_now} {image_now}')
            file_now.close()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and time + 500 < pygame.time.get_ticks():
        if image_now == 0:
            glava_now -= 1
            load_images(glava_now)
            image_now = len(images_now) - 1
        else:
            image_now -= 1
            image = images_now[image_now]
        print(glava_now, image_now)
        y = 0
        time = pygame.time.get_ticks()
        pygame.display.set_caption(
            f'глава {glava_now} страница {image_now + 1}')
        re_draw()
    elif key[pygame.K_RIGHT] and time + 500 < pygame.time.get_ticks():
        print('right')
        if image_now == len(images_now) - 1:
            if glava_now < len(glav):
                glava_now += 1
                load_images(glava_now)
                image_now = 0
        else:
            image_now += 1
            image = images_now[image_now]
        y = 0
        time = pygame.time.get_ticks()
        pygame.display.set_caption(
            f'глава {glava_now} страница {image_now + 1}')
        re_draw()
    elif key[pygame.K_UP]:
        y += 100
        re_draw()
    elif key[pygame.K_DOWN]:
        screen.blit(image, (x, y))
        y -= 100
        re_draw()
    pygame.time.delay(60)
