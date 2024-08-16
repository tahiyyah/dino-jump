import pygame
from pygame import *
import random

#initialising pygame
pygame.init()

#defining dimensions for screen
screen_width = 1000
screen_height = 700

score = 0
music = True

#defining colours using RGB
lightpink = (255, 218, 252)
pink = (253, 141, 242)
lightgrey = (224, 224, 224)
grey = (172, 172, 172)
darkgrey = (92, 92, 92)
blue = (134, 138, 255)
lightblue = (186, 219, 253)
orange = (255, 188, 28)
green = (182, 218, 169)
lightgreen = (219, 255, 191)
lightdarkgreen = (127, 255, 112)
darkgreen = (101, 206, 80)
yellow = (255, 227, 82)
beige = (255, 237, 161)
darkbeige = (206, 194, 143)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("dino jump") #game name

#loading/transforming images
bg_image = pygame.image.load('background.jpg')
bg_image = pygame.transform.scale(bg_image, (1000,700))
go_bg = pygame.image.load('explosion.png')
win_bg = pygame.image.load('win.png')
lava_pit = pygame.image.load('lava pit.png')
lava_pit = pygame.transform.scale(lava_pit, (1000, 200))
portal_image = pygame.image.load('portal.png')
portal_image = pygame.transform.scale(portal_image, (60, 70))
heart = pygame.image.load('heart.png')
heart = pygame.transform.scale(heart, (30, 25))
instructions_bg = pygame.image.load('instructions scroll.png')
instructions_bg = pygame.transform.scale(instructions_bg, (700, 700))
back_button_img = pygame.image.load('back button.png')
back_button_img = pygame.transform.scale(back_button_img, (50, 50))
next_button_img = pygame.image.load('next button.png')
next_button_img = pygame.transform.scale(next_button_img, (50, 50))
sound_on = pygame.image.load('sound on.png')
sound_on = pygame.transform.scale(sound_on, (150, 150))
sound_off = pygame.image.load('sound off.png')
sound_off = pygame.transform.scale(sound_off, (150, 150))

#platform images
platform_img_1 = pygame.image.load('platform .jpg')
platform_img_1 = pygame.transform.scale(platform_img_1, (90, 40))
platform_img_2 = pygame.transform.scale(platform_img_1, (170, 40))
platform_img_3 = pygame.transform.scale(platform_img_1, (40,40))

blue_button_img = pygame.image.load('character buttons/blue dino button.png')
blue_button_img = pygame.transform.scale(blue_button_img, (100, 100))
brown_button_img = pygame.image.load('character buttons/brown dino button.png')
brown_button_img = pygame.transform.scale(brown_button_img, (100, 100))
darkgreen_button_img = pygame.image.load('character buttons/dark green dino button.png')
darkgreen_button_img = pygame.transform.scale(darkgreen_button_img, (100, 100))
darkgrey_button_img = pygame.image.load('character buttons/dark grey dino button.png')
darkgrey_button_img = pygame.transform.scale(darkgrey_button_img, (100, 100))
lightgrey_button_img = pygame.image.load('character buttons/light grey dino button.png')
lightgrey_button_img = pygame.transform.scale(lightgrey_button_img, (100, 100))
lightgreen_button_img = pygame.image.load('character buttons/light green dino button.png')
lightgreen_button_img = pygame.transform.scale(lightgreen_button_img, (100, 100))
pink_button_img = pygame.image.load('character buttons/pink dino button.png')
pink_button_img = pygame.transform.scale(pink_button_img, (100, 100))

#images for jumping animation
#blue dino jumping right
blue_jump1 = pygame.image.load('blue jumping/jump 1.png')
blue_jump1 = pygame.transform.scale(blue_jump1, (50, 50))
blue_jump2 = pygame.image.load('blue jumping/jump 2.png')
blue_jump2 = pygame.transform.scale(blue_jump2, (50, 50))
blue_jump3 = pygame.image.load('blue jumping/jump 3.png')
blue_jump3 = pygame.transform.scale(blue_jump3, (50, 50))
blue_jump4 = pygame.image.load('blue jumping/jump 4.png')
blue_jump4 = pygame.transform.scale(blue_jump4, (50, 50))
blue_jumping_r = [blue_jump1, blue_jump2, blue_jump3, blue_jump4]

#blue dino jumping left
blue_jump5 = pygame.image.load('blue jumping/jump 5.png')
blue_jump5 = pygame.transform.scale(blue_jump5, (50, 50))
blue_jump6 = pygame.image.load('blue jumping/jump 6.png')
blue_jump6 = pygame.transform.scale(blue_jump6, (50, 50))
blue_jump7 = pygame.image.load('blue jumping/jump 7.png')
blue_jump7 = pygame.transform.scale(blue_jump7, (50, 50))
blue_jump8 = pygame.image.load('blue jumping/jump 8.png')
blue_jump8 = pygame.transform.scale(blue_jump8, (50, 50))
blue_jumping_l = [blue_jump5, blue_jump6, blue_jump7, blue_jump8]

#brown dino jumping right
brown_jump1 = pygame.image.load('brown jumping/jump 1.png')
brown_jump1 = pygame.transform.scale(brown_jump1, (50, 50))
brown_jump2 = pygame.image.load('brown jumping/jump 2.png')
brown_jump2 = pygame.transform.scale(brown_jump2, (50, 50))
brown_jump3 = pygame.image.load('brown jumping/jump 3.png')
brown_jump3 = pygame.transform.scale(brown_jump3, (50, 50))
brown_jump4 = pygame.image.load('brown jumping/jump 4.png')
brown_jump4 = pygame.transform.scale(brown_jump4, (50, 50))
brown_jumping_r = [brown_jump1, brown_jump2, brown_jump3, brown_jump4]

#brown dino jumping left
brown_jump5 = pygame.image.load('brown jumping/jump 5.png')
brown_jump5 = pygame.transform.scale(brown_jump5, (50, 50))
brown_jump6 = pygame.image.load('brown jumping/jump 6.png')
brown_jump6 = pygame.transform.scale(brown_jump6, (50, 50))
brown_jump7 = pygame.image.load('brown jumping/jump 7.png')
brown_jump7 = pygame.transform.scale(brown_jump7, (50, 50))
brown_jump8 = pygame.image.load('brown jumping/jump 8.png')
brown_jump8 = pygame.transform.scale(brown_jump8, (50, 50))
brown_jumping_l = [brown_jump5, brown_jump6, brown_jump7, brown_jump8]

#darkgreen dino jumping right
darkgreen_jump1 = pygame.image.load('darkgreen jumping/jump 1.png')
darkgreen_jump1 = pygame.transform.scale(darkgreen_jump1, (50, 50))
darkgreen_jump2 = pygame.image.load('darkgreen jumping/jump 2.png')
darkgreen_jump2 = pygame.transform.scale(darkgreen_jump2, (50, 50))
darkgreen_jump3 = pygame.image.load('darkgreen jumping/jump 3.png')
darkgreen_jump3 = pygame.transform.scale(darkgreen_jump3, (50, 50))
darkgreen_jump4 = pygame.image.load('darkgreen jumping/jump 4.png')
darkgreen_jump4 = pygame.transform.scale(darkgreen_jump4, (50, 50))
darkgreen_jumping_r = [darkgreen_jump1, darkgreen_jump2, darkgreen_jump3, darkgreen_jump4]

#darkgreen dino jumping left
darkgreen_jump5 = pygame.image.load('darkgreen jumping/jump 5.png')
darkgreen_jump5 = pygame.transform.scale(darkgreen_jump5, (50, 50))
darkgreen_jump6 = pygame.image.load('darkgreen jumping/jump 6.png')
darkgreen_jump6 = pygame.transform.scale(darkgreen_jump6, (50, 50))
darkgreen_jump7 = pygame.image.load('darkgreen jumping/jump 7.png')
darkgreen_jump7 = pygame.transform.scale(darkgreen_jump7, (50, 50))
darkgreen_jump8 = pygame.image.load('darkgreen jumping/jump 8.png')
darkgreen_jump8 = pygame.transform.scale(darkgreen_jump8, (50, 50))
darkgreen_jumping_l = [darkgreen_jump5, darkgreen_jump6, darkgreen_jump7, darkgreen_jump8]

#darkgrey dino jumping right
darkgrey_jump1 = pygame.image.load('darkgrey jumping/jump 1.png')
darkgrey_jump1 = pygame.transform.scale(darkgrey_jump1, (50, 50))
darkgrey_jump2 = pygame.image.load('darkgrey jumping/jump 2.png')
darkgrey_jump2 = pygame.transform.scale(darkgrey_jump2, (50, 50))
darkgrey_jump3 = pygame.image.load('darkgrey jumping/jump 3.png')
darkgrey_jump3 = pygame.transform.scale(darkgrey_jump3, (50, 50))
darkgrey_jump4 = pygame.image.load('darkgrey jumping/jump 4.png')
darkgrey_jump4 = pygame.transform.scale(darkgrey_jump4, (50, 50))
darkgrey_jumping_r = [darkgrey_jump1, darkgrey_jump2, darkgrey_jump3, darkgrey_jump4]

#darkgrey dino jumping left
darkgrey_jump5 = pygame.image.load('darkgrey jumping/jump 5.png')
darkgrey_jump5 = pygame.transform.scale(darkgrey_jump5, (50, 50))
darkgrey_jump6 = pygame.image.load('darkgrey jumping/jump 6.png')
darkgrey_jump6 = pygame.transform.scale(darkgrey_jump6, (50, 50))
darkgrey_jump7 = pygame.image.load('darkgrey jumping/jump 7.png')
darkgrey_jump7 = pygame.transform.scale(darkgrey_jump7, (50, 50))
darkgrey_jump8 = pygame.image.load('darkgrey jumping/jump 8.png')
darkgrey_jump8 = pygame.transform.scale(darkgrey_jump8, (50, 50))
darkgrey_jumping_l = [darkgrey_jump5, darkgrey_jump6, darkgrey_jump7, darkgrey_jump8]

#lightgrey dino jumping right
lightgrey_jump1 = pygame.image.load('lightgrey jumping/jump 1.png')
lightgrey_jump1 = pygame.transform.scale(lightgrey_jump1, (50, 50))
lightgrey_jump2 = pygame.image.load('lightgrey jumping/jump 2.png')
lightgrey_jump2 = pygame.transform.scale(lightgrey_jump2, (50, 50))
lightgrey_jump3 = pygame.image.load('lightgrey jumping/jump 3.png')
lightgrey_jump3 = pygame.transform.scale(lightgrey_jump3, (50, 50))
lightgrey_jump4 = pygame.image.load('lightgrey jumping/jump 4.png')
lightgrey_jump4 = pygame.transform.scale(lightgrey_jump4, (50, 50))
lightgrey_jumping_r = [lightgrey_jump1, lightgrey_jump2, lightgrey_jump3, lightgrey_jump4]

#lightgrey dino jumping left
lightgrey_jump5 = pygame.image.load('lightgrey jumping/jump 5.png')
lightgrey_jump5 = pygame.transform.scale(lightgrey_jump5, (50, 50))
lightgrey_jump6 = pygame.image.load('lightgrey jumping/jump 6.png')
lightgrey_jump6 = pygame.transform.scale(lightgrey_jump6, (50, 50))
lightgrey_jump7 = pygame.image.load('lightgrey jumping/jump 7.png')
lightgrey_jump7 = pygame.transform.scale(lightgrey_jump7, (50, 50))
lightgrey_jump8 = pygame.image.load('lightgrey jumping/jump 8.png')
lightgrey_jump8 = pygame.transform.scale(lightgrey_jump8, (50, 50))
lightgrey_jumping_l = [lightgrey_jump5, lightgrey_jump6, lightgrey_jump7, lightgrey_jump8]

#pink dino jumping right
pink_jump1 = pygame.image.load('pink jumping/jump 1.png')
pink_jump1 = pygame.transform.scale(pink_jump1, (50, 50))
pink_jump2 = pygame.image.load('pink jumping/jump 2.png')
pink_jump2 = pygame.transform.scale(pink_jump2, (50, 50))
pink_jump3 = pygame.image.load('pink jumping/jump 3.png')
pink_jump3 = pygame.transform.scale(pink_jump3, (50, 50))
pink_jump4 = pygame.image.load('pink jumping/jump 4.png')
pink_jump4 = pygame.transform.scale(pink_jump4, (50, 50))
pink_jumping_r = [pink_jump1, pink_jump2, pink_jump3, pink_jump4]

#pink dino jumping left
pink_jump5 = pygame.image.load('pink jumping/jump 5.png')
pink_jump5 = pygame.transform.scale(pink_jump5, (50, 50))
pink_jump6 = pygame.image.load('pink jumping/jump 6.png')
pink_jump6 = pygame.transform.scale(pink_jump6, (50, 50))
pink_jump7 = pygame.image.load('pink jumping/jump 7.png')
pink_jump7 = pygame.transform.scale(pink_jump7, (50, 50))
pink_jump8 = pygame.image.load('pink jumping/jump 8.png')
pink_jump8 = pygame.transform.scale(pink_jump8, (50, 50))
pink_jumping_l = [pink_jump5, pink_jump6, pink_jump7, pink_jump8]

#lightgreen dino jumping right
lightgreen_jump1 = pygame.image.load('lightgreen jumping/jump 1.png')
lightgreen_jump1 = pygame.transform.scale(lightgreen_jump1, (50, 50))
lightgreen_jump2 = pygame.image.load('lightgreen jumping/jump 2.png')
lightgreen_jump2 = pygame.transform.scale(lightgreen_jump2, (50, 50))
lightgreen_jump3 = pygame.image.load('lightgreen jumping/jump 3.png')
lightgreen_jump3 = pygame.transform.scale(lightgreen_jump3, (50, 50))
lightgreen_jump4 = pygame.image.load('lightgreen jumping/jump 4.png')
lightgreen_jump4 = pygame.transform.scale(lightgreen_jump4, (50, 50))
lightgreen_jumping_r = [lightgreen_jump1, lightgreen_jump2, lightgreen_jump3, lightgreen_jump4]

#lightgreen dino jumping left
lightgreen_jump5 = pygame.image.load('lightgreen jumping/jump 5.png')
lightgreen_jump5 = pygame.transform.scale(lightgreen_jump5, (50, 50))
lightgreen_jump6 = pygame.image.load('lightgreen jumping/jump 6.png')
lightgreen_jump6 = pygame.transform.scale(lightgreen_jump6, (50, 50))
lightgreen_jump7 = pygame.image.load('lightgreen jumping/jump 7.png')
lightgreen_jump7 = pygame.transform.scale(lightgreen_jump7, (50, 50))
lightgreen_jump8 = pygame.image.load('lightgreen jumping/jump 8.png')
lightgreen_jump8 = pygame.transform.scale(lightgreen_jump8, (50, 50))
lightgreen_jumping_l = [lightgreen_jump5, lightgreen_jump6, lightgreen_jump7, lightgreen_jump8]

#images for walking animation
#blue dino moving right
blue_move_r_initial = pygame.image.load('blue move right/blue initial.png')
blue_move_r_initial = pygame.transform.scale(blue_move_r_initial, (50, 50))
blue_move_r1 = pygame.image.load('blue move right/move right 1.png')
blue_move_r1 = pygame.transform.scale(blue_move_r1, (50, 50))
blue_move_r2 = pygame.image.load('blue move right/move right 2.png')
blue_move_r2 = pygame.transform.scale(blue_move_r2, (50, 50))
blue_move_r3 = pygame.image.load('blue move right/move right 3.png')
blue_move_r3 = pygame.transform.scale(blue_move_r3, (50, 50))
blue_move_r4 = pygame.image.load('blue move right/move right 4.png')
blue_move_r4 = pygame.transform.scale(blue_move_r4, (50, 50))
blue_move_r5 = pygame.image.load('blue move right/move right 5.png')
blue_move_r5 = pygame.transform.scale(blue_move_r5, (50, 50))
blue_move_r6 = pygame.image.load('blue move right/move right 6.png')
blue_move_r6 = pygame.transform.scale(blue_move_r6, (50, 50))
blue_moving_r = [blue_move_r_initial, blue_move_r1, blue_move_r2, blue_move_r3, blue_move_r4, blue_move_r5, blue_move_r6]

#blue dino moving left
blue_move_l_initial = pygame.image.load('blue move left/blue initial.png')
blue_move_l_initial = pygame.transform.scale(blue_move_l_initial, (50, 50))
blue_move_l1 = pygame.image.load('blue move left/move left 1.png')
blue_move_l1 = pygame.transform.scale(blue_move_l1, (50, 50))
blue_move_l2 = pygame.image.load('blue move left/move left 2.png')
blue_move_l2 = pygame.transform.scale(blue_move_l2, (50, 50))
blue_move_l3 = pygame.image.load('blue move left/move left 3.png')
blue_move_l3 = pygame.transform.scale(blue_move_l3, (50, 50))
blue_move_l4 = pygame.image.load('blue move left/move left 4.png')
blue_move_l4 = pygame.transform.scale(blue_move_l4, (50, 50))
blue_move_l5 = pygame.image.load('blue move left/move left 5.png')
blue_move_l5 = pygame.transform.scale(blue_move_l5, (50, 50))
blue_move_l6 = pygame.image.load('blue move left/move left 6.png')
blue_move_l6 = pygame.transform.scale(blue_move_l6, (50, 50))
blue_moving_l = [blue_move_l_initial, blue_move_l1, blue_move_l2, blue_move_l3, blue_move_l4, blue_move_l5, blue_move_l6]

#brown dino moving right
brown_move_r_initial = pygame.image.load('brown move right/brown initial.png')
brown_move_r_initial = pygame.transform.scale(brown_move_r_initial, (50, 50))
brown_move_r1 = pygame.image.load('brown move right/move right 1.png')
brown_move_r1 = pygame.transform.scale(brown_move_r1, (50, 50))
brown_move_r2 = pygame.image.load('brown move right/move right 2.png')
brown_move_r2 = pygame.transform.scale(brown_move_r2, (50, 50))
brown_move_r3 = pygame.image.load('brown move right/move right 3.png')
brown_move_r3 = pygame.transform.scale(brown_move_r3, (50, 50))
brown_move_r4 = pygame.image.load('brown move right/move right 4.png')
brown_move_r4 = pygame.transform.scale(brown_move_r4, (50, 50))
brown_move_r5 = pygame.image.load('brown move right/move right 5.png')
brown_move_r5 = pygame.transform.scale(brown_move_r5, (50, 50))
brown_move_r6 = pygame.image.load('brown move right/move right 6.png')
brown_move_r6 = pygame.transform.scale(brown_move_r6, (50, 50))
brown_moving_r = [brown_move_r_initial, brown_move_r1, brown_move_r2, brown_move_r3, brown_move_r4, brown_move_r5, brown_move_r6]

#brown dino moving left
brown_move_l_initial = pygame.image.load('brown move left/brown initial.png')
brown_move_l_initial = pygame.transform.scale(brown_move_l_initial, (50, 50))
brown_move_l1 = pygame.image.load('brown move left/move left 1.png')
brown_move_l1 = pygame.transform.scale(brown_move_l1, (50, 50))
brown_move_l2 = pygame.image.load('brown move left/move left 2.png')
brown_move_l2 = pygame.transform.scale(brown_move_l2, (50, 50))
brown_move_l3 = pygame.image.load('brown move left/move left 3.png')
brown_move_l3 = pygame.transform.scale(brown_move_l3, (50, 50))
brown_move_l4 = pygame.image.load('brown move left/move left 4.png')
brown_move_l4 = pygame.transform.scale(brown_move_l4, (50, 50))
brown_move_l5 = pygame.image.load('brown move left/move left 5.png')
brown_move_l5 = pygame.transform.scale(brown_move_l5, (50, 50))
brown_move_l6 = pygame.image.load('brown move left/move left 6.png')
brown_move_l6 = pygame.transform.scale(brown_move_l6, (50, 50))
brown_moving_l = [brown_move_l_initial, brown_move_l1, brown_move_l2, brown_move_l3, brown_move_l4, brown_move_l5, brown_move_l6]

#darkgreen dino moving right
darkgreen_move_r_initial = pygame.image.load('darkgreen move right/darkgreen initial.png')
darkgreen_move_r_initial = pygame.transform.scale(darkgreen_move_r_initial, (50, 50))
darkgreen_move_r1 = pygame.image.load('darkgreen move right/move right 1.png')
darkgreen_move_r1 = pygame.transform.scale(darkgreen_move_r1, (50, 50))
darkgreen_move_r2 = pygame.image.load('darkgreen move right/move right 2.png')
darkgreen_move_r2 = pygame.transform.scale(darkgreen_move_r2, (50, 50))
darkgreen_move_r3 = pygame.image.load('darkgreen move right/move right 3.png')
darkgreen_move_r3 = pygame.transform.scale(darkgreen_move_r3, (50, 50))
darkgreen_move_r4 = pygame.image.load('darkgreen move right/move right 4.png')
darkgreen_move_r4 = pygame.transform.scale(darkgreen_move_r4, (50, 50))
darkgreen_move_r5 = pygame.image.load('darkgreen move right/move right 5.png')
darkgreen_move_r5 = pygame.transform.scale(darkgreen_move_r5, (50, 50))
darkgreen_move_r6 = pygame.image.load('darkgreen move right/move right 6.png')
darkgreen_move_r6 = pygame.transform.scale(darkgreen_move_r6, (50, 50))
darkgreen_moving_r = [darkgreen_move_r_initial, darkgreen_move_r1, darkgreen_move_r2, darkgreen_move_r3, darkgreen_move_r4, darkgreen_move_r5, darkgreen_move_r6]

#darkgreen dino moving left
darkgreen_move_l_initial = pygame.image.load('darkgreen move left/darkgreen initial.png')
darkgreen_move_l_initial = pygame.transform.scale(darkgreen_move_l_initial, (50, 50))
darkgreen_move_l1 = pygame.image.load('darkgreen move left/move left 1.png')
darkgreen_move_l1 = pygame.transform.scale(darkgreen_move_l1, (50, 50))
darkgreen_move_l2 = pygame.image.load('darkgreen move left/move left 2.png')
darkgreen_move_l2 = pygame.transform.scale(darkgreen_move_l2, (50, 50))
darkgreen_move_l3 = pygame.image.load('darkgreen move left/move left 3.png')
darkgreen_move_l3 = pygame.transform.scale(darkgreen_move_l3, (50, 50))
darkgreen_move_l4 = pygame.image.load('darkgreen move left/move left 4.png')
darkgreen_move_l4 = pygame.transform.scale(darkgreen_move_l4, (50, 50))
darkgreen_move_l5 = pygame.image.load('darkgreen move left/move left 5.png')
darkgreen_move_l5 = pygame.transform.scale(darkgreen_move_l5, (50, 50))
darkgreen_move_l6 = pygame.image.load('darkgreen move left/move left 6.png')
darkgreen_move_l6 = pygame.transform.scale(darkgreen_move_l6, (50, 50))
darkgreen_moving_l = [darkgreen_move_l_initial, darkgreen_move_l1, darkgreen_move_l2, darkgreen_move_l3, darkgreen_move_l4, darkgreen_move_l5, darkgreen_move_l6]

#darkgrey dino moving right
darkgrey_move_r_initial = pygame.image.load('darkgrey move right/darkgrey initial.png')
darkgrey_move_r_initial = pygame.transform.scale(darkgrey_move_r_initial, (50, 50))
darkgrey_move_r1 = pygame.image.load('darkgrey move right/move right 1.png')
darkgrey_move_r1 = pygame.transform.scale(darkgrey_move_r1, (50, 50))
darkgrey_move_r2 = pygame.image.load('darkgrey move right/move right 2.png')
darkgrey_move_r2 = pygame.transform.scale(darkgrey_move_r2, (50, 50))
darkgrey_move_r3 = pygame.image.load('darkgrey move right/move right 3.png')
darkgrey_move_r3 = pygame.transform.scale(darkgrey_move_r3, (50, 50))
darkgrey_move_r4 = pygame.image.load('darkgrey move right/move right 4.png')
darkgrey_move_r4 = pygame.transform.scale(darkgrey_move_r4, (50, 50))
darkgrey_move_r5 = pygame.image.load('darkgrey move right/move right 5.png')
darkgrey_move_r5 = pygame.transform.scale(darkgrey_move_r5, (50, 50))
darkgrey_move_r6 = pygame.image.load('darkgrey move right/move right 6.png')
darkgrey_move_r6 = pygame.transform.scale(darkgrey_move_r6, (50, 50))
darkgrey_moving_r = [darkgrey_move_r_initial, darkgrey_move_r1, darkgrey_move_r2, darkgrey_move_r3, darkgrey_move_r4, darkgrey_move_r5, darkgrey_move_r6]

#darkgrey dino moving left
darkgrey_move_l_initial = pygame.image.load('darkgrey move left/darkgrey initial.png')
darkgrey_move_l_initial = pygame.transform.scale(darkgrey_move_l_initial, (50, 50))
darkgrey_move_l1 = pygame.image.load('darkgrey move left/move left 1.png')
darkgrey_move_l1 = pygame.transform.scale(darkgrey_move_l1, (50, 50))
darkgrey_move_l2 = pygame.image.load('darkgrey move left/move left 2.png')
darkgrey_move_l2 = pygame.transform.scale(darkgrey_move_l2, (50, 50))
darkgrey_move_l3 = pygame.image.load('darkgrey move left/move left 3.png')
darkgrey_move_l3 = pygame.transform.scale(darkgrey_move_l3, (50, 50))
darkgrey_move_l4 = pygame.image.load('darkgrey move left/move left 4.png')
darkgrey_move_l4 = pygame.transform.scale(darkgrey_move_l4, (50, 50))
darkgrey_move_l5 = pygame.image.load('darkgrey move left/move left 5.png')
darkgrey_move_l5 = pygame.transform.scale(darkgrey_move_l5, (50, 50))
darkgrey_move_l6 = pygame.image.load('darkgrey move left/move left 6.png')
darkgrey_move_l6 = pygame.transform.scale(darkgrey_move_l6, (50, 50))
darkgrey_moving_l = [darkgrey_move_l_initial, darkgrey_move_l1, darkgrey_move_l2, darkgrey_move_l3, darkgrey_move_l4, darkgrey_move_l5, darkgrey_move_l6]

#lightgrey dino moving right
lightgrey_move_r_initial = pygame.image.load('lightgrey move right/lightgrey initial.png')
lightgrey_move_r_initial = pygame.transform.scale(lightgrey_move_r_initial, (50, 50))
lightgrey_move_r1 = pygame.image.load('lightgrey move right/move right 1.png')
lightgrey_move_r1 = pygame.transform.scale(lightgrey_move_r1, (50, 50))
lightgrey_move_r2 = pygame.image.load('lightgrey move right/move right 2.png')
lightgrey_move_r2 = pygame.transform.scale(lightgrey_move_r2, (50, 50))
lightgrey_move_r3 = pygame.image.load('lightgrey move right/move right 3.png')
lightgrey_move_r3 = pygame.transform.scale(lightgrey_move_r3, (50, 50))
lightgrey_move_r4 = pygame.image.load('lightgrey move right/move right 4.png')
lightgrey_move_r4 = pygame.transform.scale(lightgrey_move_r4, (50, 50))
lightgrey_move_r5 = pygame.image.load('lightgrey move right/move right 5.png')
lightgrey_move_r5 = pygame.transform.scale(lightgrey_move_r5, (50, 50))
lightgrey_move_r6 = pygame.image.load('lightgrey move right/move right 6.png')
lightgrey_move_r6 = pygame.transform.scale(lightgrey_move_r6, (50, 50))
lightgrey_moving_r = [lightgrey_move_r_initial, lightgrey_move_r1, lightgrey_move_r2, lightgrey_move_r3, lightgrey_move_r4, lightgrey_move_r5, lightgrey_move_r6]

#lightgrey dino moving left
lightgrey_move_l_initial = pygame.image.load('lightgrey move left/lightgrey initial.png')
lightgrey_move_l_initial = pygame.transform.scale(lightgrey_move_l_initial, (50, 50))
lightgrey_move_l1 = pygame.image.load('lightgrey move left/move left 1.png')
lightgrey_move_l1 = pygame.transform.scale(lightgrey_move_l1, (50, 50))
lightgrey_move_l2 = pygame.image.load('lightgrey move left/move left 2.png')
lightgrey_move_l2 = pygame.transform.scale(lightgrey_move_l2, (50, 50))
lightgrey_move_l3 = pygame.image.load('lightgrey move left/move left 3.png')
lightgrey_move_l3 = pygame.transform.scale(lightgrey_move_l3, (50, 50))
lightgrey_move_l4 = pygame.image.load('lightgrey move left/move left 4.png')
lightgrey_move_l4 = pygame.transform.scale(lightgrey_move_l4, (50, 50))
lightgrey_move_l5 = pygame.image.load('lightgrey move left/move left 5.png')
lightgrey_move_l5 = pygame.transform.scale(lightgrey_move_l5, (50, 50))
lightgrey_move_l6 = pygame.image.load('lightgrey move left/move left 6.png')
lightgrey_move_l6 = pygame.transform.scale(lightgrey_move_l6, (50, 50))
lightgrey_moving_l = [lightgrey_move_l_initial, lightgrey_move_l1, lightgrey_move_l2, lightgrey_move_l3, lightgrey_move_l4, lightgrey_move_l5, lightgrey_move_l6]

#pink dino moving right
pink_move_r_initial = pygame.image.load('pink move right/pink initial.png')
pink_move_r_initial = pygame.transform.scale(pink_move_r_initial, (50, 50))
pink_move_r1 = pygame.image.load('pink move right/move right 1.png')
pink_move_r1 = pygame.transform.scale(pink_move_r1, (50, 50))
pink_move_r2 = pygame.image.load('pink move right/move right 2.png')
pink_move_r2 = pygame.transform.scale(pink_move_r2, (50, 50))
pink_move_r3 = pygame.image.load('pink move right/move right 3.png')
pink_move_r3 = pygame.transform.scale(pink_move_r3, (50, 50))
pink_move_r4 = pygame.image.load('pink move right/move right 4.png')
pink_move_r4 = pygame.transform.scale(pink_move_r4, (50, 50))
pink_move_r5 = pygame.image.load('pink move right/move right 5.png')
pink_move_r5 = pygame.transform.scale(pink_move_r5, (50, 50))
pink_move_r6 = pygame.image.load('pink move right/move right 6.png')
pink_move_r6 = pygame.transform.scale(pink_move_r6, (50, 50))
pink_moving_r = [pink_move_r_initial, pink_move_r1, pink_move_r2, pink_move_r3, pink_move_r4, pink_move_r5, pink_move_r6]

#pink dino moving left
pink_move_l_initial = pygame.image.load('pink move left/pink initial.png')
pink_move_l_initial = pygame.transform.scale(pink_move_l_initial, (50, 50))
pink_move_l1 = pygame.image.load('pink move left/move left 1.png')
pink_move_l1 = pygame.transform.scale(pink_move_l1, (50, 50))
pink_move_l2 = pygame.image.load('pink move left/move left 2.png')
pink_move_l2 = pygame.transform.scale(pink_move_l2, (50, 50))
pink_move_l3 = pygame.image.load('pink move left/move left 3.png')
pink_move_l3 = pygame.transform.scale(pink_move_l3, (50, 50))
pink_move_l4 = pygame.image.load('pink move left/move left 4.png')
pink_move_l4 = pygame.transform.scale(pink_move_l4, (50, 50))
pink_move_l5 = pygame.image.load('pink move left/move left 5.png')
pink_move_l5 = pygame.transform.scale(pink_move_l5, (50, 50))
pink_move_l6 = pygame.image.load('pink move left/move left 6.png')
pink_move_l6 = pygame.transform.scale(pink_move_l6, (50, 50))
pink_moving_l = [pink_move_l_initial, pink_move_l1, pink_move_l2, pink_move_l3, pink_move_l4, pink_move_l5, pink_move_l6]

#lightgreen dino moving right
lightgreen_move_r_initial = pygame.image.load('lightgreen move right/lightgreen initial.png')
lightgreen_move_r_initial = pygame.transform.scale(lightgreen_move_r_initial, (50, 50))
lightgreen_move_r1 = pygame.image.load('lightgreen move right/move right 1.png')
lightgreen_move_r1 = pygame.transform.scale(lightgreen_move_r1, (50, 50))
lightgreen_move_r2 = pygame.image.load('lightgreen move right/move right 2.png')
lightgreen_move_r2 = pygame.transform.scale(lightgreen_move_r2, (50, 50))
lightgreen_move_r3 = pygame.image.load('lightgreen move right/move right 3.png')
lightgreen_move_r3 = pygame.transform.scale(lightgreen_move_r3, (50, 50))
lightgreen_move_r4 = pygame.image.load('lightgreen move right/move right 4.png')
lightgreen_move_r4 = pygame.transform.scale(lightgreen_move_r4, (50, 50))
lightgreen_move_r5 = pygame.image.load('lightgreen move right/move right 5.png')
lightgreen_move_r5 = pygame.transform.scale(lightgreen_move_r5, (50, 50))
lightgreen_move_r6 = pygame.image.load('lightgreen move right/move right 6.png')
lightgreen_move_r6 = pygame.transform.scale(lightgreen_move_r6, (50, 50))
lightgreen_moving_r = [lightgreen_move_r_initial, lightgreen_move_r1, lightgreen_move_r2, lightgreen_move_r3, lightgreen_move_r4, lightgreen_move_r5, lightgreen_move_r6]

#lightgreen dino moving left
lightgreen_move_l_initial = pygame.image.load('lightgreen move left/lightgreen initial.png')
lightgreen_move_l_initial = pygame.transform.scale(lightgreen_move_l_initial, (50, 50))
lightgreen_move_l1 = pygame.image.load('lightgreen move left/move left 1.png')
lightgreen_move_l1 = pygame.transform.scale(lightgreen_move_l1, (50, 50))
lightgreen_move_l2 = pygame.image.load('lightgreen move left/move left 2.png')
lightgreen_move_l2 = pygame.transform.scale(lightgreen_move_l2, (50, 50))
lightgreen_move_l3 = pygame.image.load('lightgreen move left/move left 3.png')
lightgreen_move_l3 = pygame.transform.scale(lightgreen_move_l3, (50, 50))
lightgreen_move_l4 = pygame.image.load('lightgreen move left/move left 4.png')
lightgreen_move_l4 = pygame.transform.scale(lightgreen_move_l4, (50, 50))
lightgreen_move_l5 = pygame.image.load('lightgreen move left/move left 5.png')
lightgreen_move_l5 = pygame.transform.scale(lightgreen_move_l5, (50, 50))
lightgreen_move_l6 = pygame.image.load('lightgreen move left/move left 6.png')
lightgreen_move_l6 = pygame.transform.scale(lightgreen_move_l6, (50, 50))
lightgreen_moving_l = [lightgreen_move_l_initial, lightgreen_move_l1, lightgreen_move_l2, lightgreen_move_l3, lightgreen_move_l4, lightgreen_move_l5, lightgreen_move_l6]

#enemy images
enemy_r = pygame.image.load('stone golem.PNG')
enemy_r = pygame.transform.scale(enemy_r, (50, 50))
enemy_l = pygame.image.load('stone golem 2.PNG')
enemy_l = pygame.transform.scale(enemy_l, (50, 50))

#coin images
coin1 = pygame.image.load('coin sprites/coin1.png')
coin1 = pygame.transform.scale(coin1, (17, 17))
coin2 = pygame.image.load('coin sprites/coin2.png')
coin2 = pygame.transform.scale(coin2, (17, 17))
coin3 = pygame.image.load('coin sprites/coin3.png')
coin3 = pygame.transform.scale(coin3, (17, 17))
coin4 = pygame.image.load('coin sprites/coin4.png')
coin4 = pygame.transform.scale(coin4, (17, 17))
coin_sprites = [coin1, coin2, coin3, coin4]

#apple images
redapple = pygame.image.load('red apple.PNG')
redapple = pygame.transform.scale(redapple, (25, 25))
rainbowapple = pygame.image.load('rainbow apple.PNG')
rainbowapple = pygame.transform.scale(rainbowapple, (25, 25))

#sound effects
bg_music = pygame.mixer.Sound('sfx/bg music.mp3')
bg_music.play(-1) #plays the music for as long as the game is running
bg_music.set_volume(0.3) #decreased the volume to 0.3
death_sfx = pygame.mixer.Sound('sfx/death sfx.mp3')
coin_sfx = pygame.mixer.Sound('sfx/coin sfx.mp3')
win_sfx = pygame.mixer.Sound('sfx/win sfx.mp3')
chomp_sfx = pygame.mixer.Sound('sfx/chomp sfx.mp3')
over_sfx = pygame.mixer.Sound('sfx/over sfx.mp3')
jump_sfx = pygame.mixer.Sound('sfx/jump sfx.mp3')
portal_sfx = pygame.mixer.Sound('sfx/portal sfx.mp3')

#leaderboard trophy images
gold = pygame.image.load('gold trophy.png')
gold = pygame.transform.scale(gold, (30, 30))
silver = pygame.image.load('silver trophy.png')
silver = pygame.transform.scale(silver, (30, 30))
bronze = pygame.image.load('bronze trophy.png')
bronze = pygame.transform.scale(bronze, (30, 30))

#classes
class Button: #creates button class
    def __init__(self, text, text_x_pos, text_y_pos, text_size, x_pos, y_pos, width, height, base_colour, hover_colour, enabled):
        self.text = text #all parameter values will be inputted later when a button object is instantiated
        self.text_x_pos = text_x_pos
        self.text_y_pos = text_y_pos
        self.text_size = text_size
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.base_colour = base_colour
        self.hover_colour = hover_colour
        self.enabled = enabled
        self.draw() #draws button to screen automatically

    def draw(self): #draws button to screen
        font = pygame.font.Font('font/OpenDyslexic-Bold.ttf', self.text_size)
        button_text = font.render(self.text, True, 'black') #creates text to go on button
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height)) #creates rectangle that is the button

        if self.enabled: #if enabled = True
            if self.hover():   
                pygame.draw.rect(screen, self.hover_colour, button_rect, 0, 3) #changes colour when clicked
            else:
                pygame.draw.rect(screen, self.base_colour, button_rect, 0, 3)
        else:
            pygame.draw.rect(screen, self.base_colour, button_rect, 0, 3) #if enabled is false, will not change colour when clicked

        screen.blit(button_text, (self.text_x_pos, self.text_y_pos))

    def hover(self):
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
            

    def clicked(self): #checks if button gets clicked
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
        
        
class ImageButton(): #creates a button class that can have buttons with images
    def __init__(self, image, image_x_pos, image_y_pos, x_pos, y_pos, width, height, base_colour, hover_colour, enabled):
        self.image = image
        self.image_x_pos = image_x_pos #the position of the image can be placed on the button at specific coordinates
        self.image_y_pos = image_y_pos
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.base_colour = base_colour
        self.hover_colour = hover_colour
        self.enabled = enabled
        self.draw()

    def draw(self): #draws button to screen
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height)) #creates rectangle that is the button

        if self.enabled: #if enabled = True
            if self.hover():   
                pygame.draw.rect(screen, self.hover_colour, button_rect, 0, 3) #changes colour when clicked
            else:
                pygame.draw.rect(screen, self.base_colour, button_rect, 0, 3)
        else:
            pygame.draw.rect(screen, self.base_colour, button_rect, 0, 3) #if enabled is false, will not change colour when clicked

        screen.blit(self.image, (self.image_x_pos, self.image_y_pos))
    
    def hover(self):
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
        
    def clicked(self): #checks if button gets clicked
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.dy = 0 #reset variables
        self.dx = 0
        self.threshold = 20
        self.lives = 3

        #sprites lists for animations
        self.jump_r_sprites = jumpinganimation_r
        self.jump_l_sprites = jumpinganimation_l
        self.move_r_sprites = movinganimationr
        self.move_l_sprites = movinganimationl

        #attributes for movement/ animations
        self.speed = 4
        self.vely = 0
        self.jumped = False
        self.index1 = 0
        self.counter1 = 0
        self.index2 = 0
        self.counter2 = 0
        self.direction = True #True for right, False for left

    #movement methods
    def moveLeft(self):
        self.dx = -self.speed
        self.counter1 += 1

        if self.counter1 > 2:
            self.counter1 = 0
            self.index1 += 1
            if self.index1 >= len(self.move_l_sprites):
                self.index1 = 0
            self.image = self.move_l_sprites[self.index1]
        self.direction = False

    def stopmoveLeft(self):
        self.dx = 0
        self.index1 = 0
        self.counter1 = 0
        self.image = self.move_l_sprites[self.index1]

    def moveRight(self):
        self.dx = self.speed
        self.counter2 += 1

        if self.counter2 > 2:
            self.counter2 = 0
            self.index2 += 1
            if self.index2 >= len(self.move_r_sprites):
                self.index2 = 0
            self.image = self.move_r_sprites[self.index2]
        self.direction = True

    def stopmoveRight(self):
        self.dx = 0
        self.index2 = 0
        self.counter2 = 0
        self.image = self.move_r_sprites[self.index2]

    def jump(self):
        if not self.jumped:
            self.vely = -17
            self.jumped = True 
            jump_sfx.play()

        #jumping animation (right)
        if self.jumped and self.direction == True:
            self.vely += 1
            for i in range(len(self.jump_r_sprites)):
                self.image = self.jump_r_sprites[i]

        #jumping animation (left)
        if self.jumped and self.direction == False:
            self.vely += 1
            for i in range(len(self.jump_l_sprites)):
                self.image = self.jump_l_sprites[i]

    def gravity(self):
        if self.vely > 17:
            self.vely = 17
            self.jumped = False

        self.dy += self.vely

    def update(self): 
        global score
        self.vely += 0.4  
        self.dy = self.vely 

        #collisions with stationary platforms
        for platform in platform_group:
            #collision in x axis
            if platform.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            #collisions in y axis
            if platform.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                #check if player is below platform
                if self.vely < 0:
                    self.dy = platform.rect.bottom - self.rect.top
                    self.vely = 0
                #check if player is above platform
                elif self.vely >= 0:
                    self.dy = platform.rect.top - self.rect.bottom

        #collisions with moving platforms
        for platform in movingplatform_group:
            #collision in x axis
            if platform.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            #collision in y axis
            if platform.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                #check if player is below platform
                if abs((self.rect.top + self.dy) - platform.rect.bottom) < self.threshold:
                    self.dy = platform.rect.bottom - self.rect.top
                    self.vely = 0
                #check if player is above platform
                elif abs((self.rect.bottom + self.dy) - platform.rect.top) < self.threshold:
                    self.rect.bottom = platform.rect.top - 1
                    self.dy = 0
                #move player sideways with the platforms
                if platform.move_x != 0:
                    self.rect.bottom = platform.rect.top
                    self.vely = 0
                    self.rect.x += platform.move
                    self.jumped = False

        #collisions with enemies
        if pygame.sprite.spritecollide(self, enemy_group, False):
            self.lives -= 1
            death_sfx.play()
            self.rect.x = 71
            self.rect.y = 400

        #collisions with lava
        if pygame.sprite.spritecollide(self, lava_group, False):
            self.lives -= 1
            death_sfx.play()
            self.rect.x = 71
            self.rect.y = 400

        if self.lives == 3:
            screen.blit(heart, (105, 27))
            screen.blit(heart, (70, 27))
            screen.blit(heart, (35, 27)) 
        if self.lives == 2:
            screen.blit(heart, (70, 27))
            screen.blit(heart, (35, 27)) 
        if self.lives == 1:
            screen.blit(heart, (35, 27))         

        if self.lives == 0:
            over_sfx.play()
            bg_music.set_volume(0)
            game_over()

        #collisions with portals
        if pygame.sprite.spritecollide(self, portal_group, False):
            portal_sfx.play()
            global result
            result = 4
            restart_game()

        #collisions with coins
        if pygame.sprite.spritecollide(self, coin_group, True):
            score += 1
            coin_sfx.play()

        #collision with red apples
        if pygame.sprite.spritecollide(self, redapple_group, True):
            score += 3
            chomp_sfx.play()

        #collision with rainbow apples
        if pygame.sprite.spritecollide(self, rainbowapple_group, True):
            score += 5
            chomp_sfx.play()
        
        # write('lives: ' + str(self.lives), 20, 'black', 40, 30)
        write('score: ' + str(score), 20, 'black', 40, 60)

        #updating player position
        self.rect.y += self.dy
        self.rect.x += self.dx

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MovingPlatform(pygame.sprite.Sprite):
    def __init__(self, image, x, y, move_x, move_y, move_speed, move_max):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move = 1
        self.move_speed = move_speed
        self.move_max = move_max
        self.move_count = 0
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move * self.move_x
        self.rect.y += self.move * self.move_y
        self.move_count += self.move_speed

        if self.move_count > self.move_max:
            self.move *= -1 #moves platform in opposite direction
            self.move_count *= -1
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, move_speed, move_max):
        super().__init__()
        self.image = enemy_r
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_speed = move_speed
        self.move_max = move_max
        self.move_count = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.dy = 0 #reset variables
        self.dx = 0
        self.vely = 0
        self.threshold = 20
       
    def update(self):
        self.rect.x += self.move_speed #increases x position of enemy
        self.move_count += 1

        if self.move_count > self.move_max:
            self.move_speed *= -1 #moves enemy in opposite direction
            self.move_count = 0

        #changes enemy image
        if self.move_speed > 0:
            self.image = enemy_r
        elif self.move_speed < 0:
            self.image = enemy_l

        self.vely += 0.5
        self.dy += self.vely

        #collisions with stationary platforms
        for platform in platform_group:
            #collision in x axis
            if platform.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            #collisions in y axis
            if platform.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                #check if player is below platform
                if self.vely < 0:
                    self.dy = platform.rect.bottom - self.rect.top
                    self.vely = 0
                #check if player is above platform
                elif self.vely >= 0:
                    self.dy = platform.rect.top - self.rect.bottom

        #collisions with moving platforms
        for platform in movingplatform_group:
            #collision in x axis
            if platform.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            #collision in y axis
            if platform.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                #check if enemy is below platform
                if abs((self.rect.top + self.dy) - platform.rect.bottom) < self.threshold:
                    self.vely = 0
                    self.dy = platform.rect.bottom - self.rect.top
                #check if enemy is above platform
                elif abs((self.rect.bottom + self.dy) - platform.rect.top) < self.threshold:
                    self.rect.bottom = platform.rect.top - 1
                    self.dy = 0
                #move enemy sideways with the platforms
                if platform.move_x != 0:
                    self.rect.bottom = platform.rect.top
                    self.vely = 0
                    self.rect.x += platform.move

        if self.vely > 17:
            self.vely = 17

        #update enemy position
        self.rect.y += self.dy
        self.rect.x += self.dx

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = lava_pit
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = portal_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = coin1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animation_sprites = coin_sprites
        self.index = 0  #keeps track of current frame

    def update(self):
        current_time = pygame.time.get_ticks()
        animation_speed = 150  #setting how fast the animation will be
        self.index = (current_time // animation_speed) % len(self.animation_sprites) #calculating index of current frame
        self.image = self.animation_sprites[self.index] #updating coin image

class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = redapple
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class RainbowApple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = rainbowapple
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def write(message, size, colour, x_pos, y_pos): #creates function for writing text to screen
    font = pygame.font.Font('font/OpenDyslexic-Bold.ttf', size)
    text = font.render(message, True, colour)
    screen.blit(text, (x_pos, y_pos))

#sprite groups
allSpritesList = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
movingplatform_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
redapple_group = pygame.sprite.Group()
rainbowapple_group = pygame.sprite.Group()

clock = pygame.time.Clock()

#generating lava
lava_bottom = Lava(0, 525)
lava_group.add(lava_bottom)

#game loops
def win():
    win_sfx.play()

    global result
    result = 0

    global score

    file = open('leaderboard.txt', 'a')
    if score < 10:
       score = ('0'+str(score))
    file.write(str(score)+': '+username+'\n')
    file.close()

    score = 0

    while True:

        #draw to screen
        screen.blit(win_bg, (0, 0))
        restart_button = Button('restart', 270, 609, 20, 260, 600, 100, 40, yellow, orange, True)
        menu_button = Button('menu', 481, 609, 20, 460, 600, 100, 40, yellow, orange, True)
        leaderboard_button = Button('leaderboard', 662, 609, 20, 650, 600, 150, 40, yellow, orange, True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if restart_button.clicked():
                    restart_game()
                    result = 1
                if menu_button.clicked():
                    restart_game()
                    result = 2
                if leaderboard_button.clicked():
                    restart_game()
                    result = 3
        pygame.display.update()

def restart_game():
    if music:
        bg_music.set_volume(0.3)

    # clear sprite groups
    allSpritesList.empty()
    platform_group.empty()
    movingplatform_group.empty()
    enemy_group.empty()
    lava_group.empty()
    portal_group.empty()
    coin_group.empty()
    redapple_group.empty()
    rainbowapple_group.empty()

    lava_bottom = Lava(0, 525)
    lava_group.add(lava_bottom)
    allSpritesList.add(lava_group)

    if result == 1:
        level1()
    if result == 2:
        menu_screen()
    if result == 3:
        leaderboard()
    if result == 4:
        if next_level == 2:
            level2()
        if next_level == 3:
            level3()
        if next_level == 4:
            win()

def game_over(): #title screen game loop
    global result
    result = 0

    global score
    display_score = score

    file = open('leaderboard.txt', 'a')
    if score < 10:
       score = ('0'+str(score))
    file.write(str(score)+': '+username+'\n')
    file.close()

    score = 0

    while True:

        #draw to screen
        screen.blit(go_bg, (0, 0))
        write(username+'\'s final score: '+str(display_score), 20, 'black', 400, 500)
        restart_button = Button('restart', 270, 559, 20, 260, 550, 100, 40, yellow, orange, True)
        menu_button = Button('menu', 481, 559, 20, 460, 550, 100, 40, yellow, orange, True)
        leaderboard_button = Button('leaderboard', 662, 559, 20, 650, 550, 150, 40, yellow, orange, True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if restart_button.clicked():
                    restart_game()
                    result = 1
                if menu_button.clicked():
                    restart_game()
                    result = 2
                if leaderboard_button.clicked():
                    restart_game()
                    result = 3
        pygame.display.update()

def level3():
    global next_level
    next_level = 4
    character = Player(playercharacter, 0, 400)
    allSpritesList.add(character)

    #generating platforms
    stationaryplatforms = (Platform(platform_img_2, 0, 450), #start platform
                           Platform(platform_img_3, 590, 480),
                           Platform(platform_img_3, 630, 440),
                           Platform(platform_img_3, 620, 300),
                           Platform(platform_img_1, random.randint(60, 130), 130),
                           Platform(platform_img_2, random.randint(720, 840), 130),
                           Platform(platform_img_1, 30, 270)) #end platform
    movingplatforms = (MovingPlatform(platform_img_2, 300, 200, 1, 0, 10, 500),
                       MovingPlatform(platform_img_2, 310, 480, 1, 0, 3, 50),
                       MovingPlatform(platform_img_3, 670, 280, 0, 1, 4, 500),
                       MovingPlatform(platform_img_3, 565, 190, 0, 1, 3, 190),
                       MovingPlatform(platform_img_2, 840, 380, 0, 1, random.randint(1, 5), random.randint(30, 100)))

    platform_group.add(stationaryplatforms)
    movingplatform_group.add(movingplatforms)

    #gnerating enemies
    enemies = (Enemy(290, 200, 3, 40),
               Enemy(830, 330, 3, 40),
               Enemy(350, 470, 1, 40),
               Enemy(840, 80, 1, 80))
    enemy_group.add(enemies)

    #generating portal
    portal3 = Portal(50, 190)
    portal_group.add(portal3)

    #generating coins
    coins = (Coin(400, 380), Coin(640, 400), Coin(640, 130), Coin(740, 90),
            Coin(170, 90), Coin(70, 90), Coin(120, 90))
    coin_group.add(coins)

    #generating random (apples/coin)
    type1 = random.randint(1,3)
    if type1 == 1:
        r_apples = Apple(845, 350)
        redapple_group.add(r_apples)
        allSpritesList.add(redapple_group)
    if type1 == 2:
        rb_apples = RainbowApple(845, 350)
        rainbowapple_group.add(rb_apples)
        allSpritesList.add(rainbowapple_group)
    if type1 == 3:
        extra_coin = Coin(845, 350)
        coin_group.add(extra_coin)

    type2 = random.randint(1,3)
    if type2 == 1:
        r_apples = Apple(315, 150)
        redapple_group.add(r_apples)
        allSpritesList.add(redapple_group)
    if type2 == 2:
        rb_apples = RainbowApple(315, 150)
        rainbowapple_group.add(rb_apples)
        allSpritesList.add(rainbowapple_group)
    if type2 == 3:
        extra_coin = Coin(315, 150)
        coin_group.add(extra_coin)

    allSpritesList.add(coin_group)
    allSpritesList.add(portal_group)
    allSpritesList.add(enemy_group)
    allSpritesList.add(movingplatform_group)
    allSpritesList.add(platform_group)

    while True:
        #draw to screen 
        screen.blit(bg_image, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.moveLeft()
        if keys[pygame.K_LEFT] == False and character.direction == False:
            character.stopmoveLeft()
        if keys[pygame.K_RIGHT]:
            character.moveRight()
        if keys[pygame.K_RIGHT] == False and character.direction == True:
            character.stopmoveRight()
        if keys[pygame.K_UP]:
            character.jump()

        character.update()
        character.gravity()
        allSpritesList.update()
        allSpritesList.draw(screen)

        pygame.display.update()
        clock.tick(60)

def level2():
    global next_level
    next_level = 3
    character = Player(playercharacter, 0, 400)
    allSpritesList.add(character)

    #generating platforms
    stationaryplatforms = (Platform(platform_img_2, 0, 450), #start platform
                           Platform(platform_img_1, random.randint(320, 430), 440),
                           Platform(platform_img_2, 630, 250),
                           Platform(platform_img_1, 870, 150)) #end platform
    movingplatforms = (MovingPlatform(platform_img_3, 260, 290, 0, 1, 6, 500),
                       MovingPlatform(platform_img_3, 600, 465, 1, 0, 7, 180),
                       MovingPlatform(platform_img_3, 700, 465, 1, 0, 7, 180),
                       MovingPlatform(platform_img_3, 840, 400, 0, 1, 3, 190),
                       MovingPlatform(platform_img_2, 30, 200, 0, 1, 1, 60),
                       MovingPlatform(platform_img_1, 390, 150, 1, 0, 1, 50))

    platform_group.add(stationaryplatforms)
    movingplatform_group.add(movingplatforms)

    #generating enemies
    enemies = (Enemy(15, 150, 3, 50), Enemy(620, 200, 1, 140))
    enemy_group.add(enemies)

    #generating portal
    portal2 = Portal(885, 70)
    portal_group.add(portal2)

    #generating coins
    coins = (Coin(400, 400), Coin(455, 400), Coin(600, 425), Coin(700, 425), Coin(850, 350),
             Coin(850, 280), Coin(640, 210), Coin(705, 210), Coin(760, 210), Coin(400, 110))
    coin_group.add(coins)

    #generating random (apples/coin)
    type = random.randint(1,3)
    if type == 1:
        r_apples = Apple(40, 200)
        redapple_group.add(r_apples)
        allSpritesList.add(redapple_group)
    if type == 2:
        rb_apples = RainbowApple(40, 200)
        rainbowapple_group.add(rb_apples)
        allSpritesList.add(rainbowapple_group)
    if type == 3:
        extra_coin = Coin(40, 200)
        coin_group.add(extra_coin)

    allSpritesList.add(coin_group)
    allSpritesList.add(portal_group)
    allSpritesList.add(enemy_group)
    allSpritesList.add(movingplatform_group)
    allSpritesList.add(platform_group)

    while True:
        #draw to screen 
        screen.blit(bg_image, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.moveLeft()
        if keys[pygame.K_LEFT] == False and character.direction == False:
            character.stopmoveLeft()
        if keys[pygame.K_RIGHT]:
            character.moveRight()
        if keys[pygame.K_RIGHT] == False and character.direction == True:
            character.stopmoveRight()
        if keys[pygame.K_UP]:
            character.jump()

        character.update()
        character.gravity()
        allSpritesList.update()
        allSpritesList.draw(screen)

        pygame.display.update()
        clock.tick(60)

def level1():
    global next_level
    next_level = 2
    character = Player(playercharacter, 71, 400)
    allSpritesList.add(character)

    #generating platforms
    platforms = (Platform(platform_img_1, 50, 400),
                 Platform(platform_img_1, 220, random.randint(270, 420)),
                Platform(platform_img_2, 390, 300),
                Platform(platform_img_1, 680, random.randint(270, 420)),
                Platform(platform_img_1, 870, 300))
    
    platform_group.add(platforms)

    #generating enemy
    enemy1 = Enemy(375, 250, 1, 150)
    enemy_group.add(enemy1)

    #creating the portal
    portal1 = Portal(890, 220)
    portal_group.add(portal1)

    #generating coins
    coins = (Coin(410, 260), Coin(465, 260), Coin(520, 260), Coin(910, 180))
    coin_group.add(coins)

    allSpritesList.add(coin_group)
    allSpritesList.add(portal_group)
    allSpritesList.add(platform_group)
    allSpritesList.add(enemy_group)
    allSpritesList.add(lava_group)

    while True:
        #draw to screen 
        screen.blit(bg_image, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.moveLeft()
        if keys[pygame.K_LEFT] == False and character.direction == False:
            character.stopmoveLeft()
        if keys[pygame.K_RIGHT]:
            character.moveRight()
        if keys[pygame.K_RIGHT] == False and character.direction == True:
            character.stopmoveRight()
        if keys[pygame.K_UP]:
            character.jump()

        character.update()
        character.gravity()
        enemy_group.update()
        allSpritesList.update()
        allSpritesList.draw(screen)

        pygame.display.update()
        clock.tick(60)

def choose_character():
    next_active = False
    global playercharacter #creating a global variable means it can be used outside this function
    global jumpinganimation_r
    global jumpinganimation_l
    global movinganimationl
    global movinganimationr
    movinganimationr = []
    movinganimationl = []
    jumpinganimation_r = []
    jumpinganimation_l = []
    playercharacter = '' #sets variable to empty string

    while True:

        #draw to screen 
        screen.blit(bg_image, (0, 0))
        blue_dino_button = ImageButton(blue_button_img, 70, 300, 60, 300, 100, 120, lightblue, blue, True)
        brown_dino_button = ImageButton(brown_button_img, 200, 300, 190, 300, 100, 120, beige, darkbeige, True)
        darkgreen_dino_button = ImageButton(darkgreen_button_img, 325, 300, 317, 300, 100, 120, lightdarkgreen, darkgreen, True)
        darkgrey_dino_button = ImageButton(darkgrey_button_img, 460, 300, 450, 300, 100, 120, grey, darkgrey, True)
        lightgrey_dino_button = ImageButton(lightgrey_button_img, 590, 300, 580, 300, 100, 120, lightgrey, grey, True)
        pink_dino_button = ImageButton(pink_button_img, 720, 300, 710, 300, 100, 120, lightpink, pink, True)
        lightgreen_dino_button = ImageButton(lightgreen_button_img, 850, 300, 840, 300, 100, 120, lightgreen, green, True)
        write('select the character you wish to play:', 25, 'black', 230, 220)
        next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)
        back_button = ImageButton(back_button_img, 17, 15, 10, 10, 60, 60, yellow, orange, True)
        

        for event in pygame.event.get():
                if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if blue_dino_button.clicked():
                        playercharacter = blue_button_img
                        jumpinganimation_r = blue_jumping_r
                        jumpinganimation_l = blue_jumping_l
                        movinganimationl = blue_moving_l
                        movinganimationr = blue_moving_r
                        next_active = True
                        next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)
                    if brown_dino_button.clicked():
                        playercharacter = brown_button_img
                        jumpinganimation_r = brown_jumping_r
                        jumpinganimation_l = brown_jumping_l
                        movinganimationl = brown_moving_l
                        movinganimationr = brown_moving_r
                        next_active = True
                        next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)
                    if darkgreen_dino_button.clicked():
                        playercharacter = darkgreen_button_img
                        jumpinganimation_r = darkgreen_jumping_r
                        jumpinganimation_l = darkgreen_jumping_l
                        movinganimationl = darkgreen_moving_l
                        movinganimationr = darkgreen_moving_r
                        next_active = True
                        next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)
                    if darkgrey_dino_button.clicked():
                        playercharacter = darkgrey_button_img
                        jumpinganimation_r = darkgrey_jumping_r
                        jumpinganimation_l = darkgrey_jumping_l
                        movinganimationl = darkgrey_moving_l
                        movinganimationr = darkgrey_moving_r
                        next_active = True
                        next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)
                    if lightgrey_dino_button.clicked():
                        playercharacter = lightgrey_button_img
                        jumpinganimation_r = lightgrey_jumping_r
                        jumpinganimation_l = lightgrey_jumping_l
                        movinganimationl = lightgrey_moving_l
                        movinganimationr = lightgrey_moving_r
                        next_active = True
                        next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)
                    if pink_dino_button.clicked():
                        playercharacter = pink_button_img
                        jumpinganimation_r = pink_jumping_r
                        jumpinganimation_l = pink_jumping_l
                        movinganimationl = pink_moving_l
                        movinganimationr = pink_moving_r
                        next_active = True
                        next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)
                    if lightgreen_dino_button.clicked():
                        playercharacter = lightgreen_button_img
                        jumpinganimation_r = lightgreen_jumping_r
                        jumpinganimation_l = lightgreen_jumping_l
                        movinganimationl = lightgreen_moving_l
                        movinganimationr = lightgreen_moving_r
                        next_active = True
                        next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)
                    if back_button.clicked():
                        naming()
                    if next_button.clicked():
                        level1()

        pygame.display.update()

def naming(): #one player username input screen
    font = pygame.font.Font('font/OpenDyslexic-Bold.ttf', 20)
    global username
    username = ''
    username_box = pygame.Rect(370, 300, 240, 32) #creating rectangle that username will be inputted in
    username_box_colour = yellow

    next_active = False
    active = False

    while True:

        #draw to screen 
        screen.blit(bg_image, (0, 0))
        write("enter a username 5 to 15 characters long:", 20, 'black', 265, 260)
        next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)
        back_button = ImageButton(back_button_img, 17, 15, 10, 10, 60, 60, yellow, orange, True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN: #checks if username_box is pressed or not
                if username_box.collidepoint(event.pos): 
                    active = True
                    username_box_colour = orange #changes input box colour to orange if pressed
                else: 
                    active = False
                    username_box_colour = yellow

                if next_button.clicked():
                    choose_character()
                if back_button.clicked():
                    menu_screen()

            if active == True:
                if event.type == pygame.KEYDOWN: #checks if keys are pressed
                    if event.key == pygame.K_BACKSPACE: #checks for backspaces and removes last character if backspace is pressed
                        username = username[:-1]
                    elif len(username) < 15: #only adds character if length is < 15
                        username += event.unicode

                if len(username) >= 5 and len(username) <= 15:
                    next_active = True #changing variable to 'True' allows the button to be activated
                    next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)
                elif len(username) <5:
                    next_active = False
                    next_button = ImageButton(next_button_img, 930, 635, 928, 630, 60, 60, yellow, orange, next_active)

        pygame.draw.rect(screen, username_box_colour, username_box) #drawing rectangle that username will be inputted in
        username_text_surface = font.render(username, True, 'black')
        screen.blit(username_text_surface, (username_box.x+5, username_box.y+5)) #displays text to the screen

        pygame.display.update()

def leaderboard(): #leaderboard game loop
    file = open('leaderboard.txt', 'r')
    read_file = file.readlines()
    sorted_data = sorted(read_file, reverse = True) #sorts scores into descending order

    while True:
        #draw to screen 
        screen.blit(bg_image, (0, 0))
        back_button = ImageButton(back_button_img, 17, 15, 10, 10, 60, 60, yellow, orange, True)

        #trophies
        screen.blit(gold, (360, 195))
        screen.blit(silver, (360, 245))
        screen.blit(bronze, (360, 295))

        y = 200
        for line in range(5):
            write(str(line+1)+'    '+str(sorted_data[line]), 20, 'black', 400, y)
            y += 50 #increases the position the text in the y direction

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if back_button.clicked():
                    menu_screen()

        pygame.display.update()

def settings(): #settings game loop
    global music
    while True:
        #draw to screen 
        screen.blit(bg_image, (0,0))

        back_button = ImageButton(back_button_img, 17, 15, 10, 10, 60, 60, yellow, orange, True)

        #buttons for bg music
        music_on = ImageButton(sound_on, 125, 300, 148, 327, 110, 110, yellow, orange, True)
        music_off = ImageButton(sound_off, 275, 300, 298, 327, 110, 110, yellow, orange, True)
        write('background music:', 20, 'black', 175, 250)

        #buttons for sfx
        sfx_on = ImageButton(sound_on, 525, 300, 548, 327, 110, 110, yellow, orange, True)
        sfx_off = ImageButton(sound_off, 674, 300, 698, 327, 110, 110, yellow, orange, True)
        write('sound effects:', 20, 'black', 600, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music_on.clicked():
                    #turns music on
                    music = True
                    bg_music.set_volume(0.3)
                if music_off.clicked():
                    #turns music off
                    music = False
                    bg_music.set_volume(0)
                if sfx_on.clicked():
                    #turns all sfx on
                    death_sfx.set_volume(1)
                    coin_sfx.set_volume(1)
                    win_sfx.set_volume(1)
                    chomp_sfx.set_volume(1)
                    over_sfx.set_volume(1)
                    jump_sfx.set_volume(1)
                    portal_sfx.set_volume(1)
                if sfx_off.clicked():
                    #turns all sfx off
                    death_sfx.set_volume(0)
                    coin_sfx.set_volume(0)
                    win_sfx.set_volume(0)
                    chomp_sfx.set_volume(0)
                    over_sfx.set_volume(0)
                    jump_sfx.set_volume(0)
                    portal_sfx.set_volume(0)
                if back_button.clicked():
                    menu_screen()

        pygame.display.update()

def menu_screen(): #menu screen game loop
    while True:

        #draw to screen
        screen.blit(bg_image, (0, 0))
        game_button = Button("start game", 425, 267, 18, 400, 255, 160, 40, yellow, orange, True) #creating all necessary buttons
        leaderboard_button = Button("leaderboard", 420, 338, 18, 400, 325, 160, 40, yellow, orange, True)
        settings_button = Button("settings", 440, 403, 18, 400, 390, 160, 40, yellow, orange, True)
        back_button = ImageButton(back_button_img, 17, 15, 10, 10, 60, 60, yellow, orange, True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if game_button.clicked():
                    naming()
                if leaderboard_button.clicked():
                    leaderboard()
                if settings_button.clicked():
                    settings()
                if back_button.clicked():
                    home_screen()

        pygame.display.update()

def instructions_screen(): #instructions screen game loop
    while True:

        #draw to screen
        screen.blit(bg_image, (0, 0))
        screen.blit(instructions_bg, (140, -13))
        write("how to play:", 50, 'black', 335, 50) #all text for instructions
        write("> use the arrow keys to control the character", 15, 'black', 300, 175)
        write("> collect as many coins and apples as you can", 15, 'black', 300, 235)
        write("> avoid enemies, they cost you lives :(", 15, 'black', 300, 295)
        write("> try to achieve the highest score and make it to ", 15, 'black', 300, 355)
        write("  the top of the leaderboard!!!", 15, 'black', 306, 380)
        write("and most importantly...", 25, 'black', 345, 440)
        write("have fun :D", 40, 'black', 380, 485)

        back_button = ImageButton(back_button_img, 17, 15, 10, 10, 60, 60, yellow, orange, True) #creates back button for instructions screen to go to home screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if back_button.clicked():
                    home_screen() #goes back to home screen if button is pressed

        pygame.display.update()

def home_screen(): #home screen game loop
    while True:

        #draw to screen
        screen.blit(bg_image, (0, 0))
        logo = pygame.image.load('game logo.PNG')
        logo = pygame.transform.scale(logo, (300, 300))
        screen.blit(logo, (330, 45))

        menu_button = Button("menu", 461, 339, 22, 420, 330, 150, 40, yellow, orange, True) #creating menu and instructions buttons
        instructions_button = Button("instructions", 426, 439, 22, 420, 430, 150, 40, yellow, orange, True) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if menu_button.clicked():
                    menu_screen()
                if instructions_button.clicked():
                    instructions_screen()

        pygame.display.update()

def title_screen(): #title screen game loop
    while True:

        #draw to screen
        screen.blit(bg_image, (0, 0))
        logo = pygame.image.load('game logo.PNG')
        logo = pygame.transform.scale(logo, (600, 600))
        screen.blit(logo, (170, 45))
        
        button1 = Button("click to begin!", 426, 641, 18, 420, 630, 150, 40, yellow, orange, True) #instantiates button object

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if button1.clicked():
                    home_screen()

        pygame.display.update()
title_screen()

pygame.quit()