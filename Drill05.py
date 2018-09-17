from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_from_center_to_right():
    x,y = 800 // 2, 90
    while x < 800 - 25 :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 2
        delay(0.01)

def move_up():
    x, y = 800 - 25 , 90
    while y < 600 - 25:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)

def move_left():
    x, y = 800 - 25, 600 - 25
    while x > 0 + 2:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)

def move_down():
    x, y = 2, 600 - 25
    while y > 0 + 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)

def move_from_left_to_center():
    x, y = 2, 90
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

import math

def move_circle():
    cx, cy, r = 800 // 2, 600 // 2, (600-180)//2
    degree = -90
    while degree < 270:
        radian = math.radians(degree)
        x = cx + r * math.cos(radian)
        y = cy + r * math.sin(radian)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        degree += 1
        delay(0.01)


def make_rectangle():
    move_from_center_to_right()
    move_up()
    move_left()
    move_down()
    move_from_left_to_center()

def make_circle():
    move_circle()

while True:
    make_rectangle()
    make_circle()

    
close_canvas()
