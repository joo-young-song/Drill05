from pico2d import *

open_canvas()

grass = load_image('grass.png')
character_run = load_image('animation_sheet.png')

def run_203_to_132():
    x,y,frame = 203,535,0
    while y > 243:
        if x > 132:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= 2
            delay(0.05)
        else:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            y -= 2
            delay(0.05)

def run_132_to_535():
    pass
def run_535_to_477():
    pass
def run_477_to_715():
    pass
def run_715_to_316():
    pass
def run_316_to_510():
    pass
def run_510_to_692():
    pass
def run_692_to_682():
    pass
def run_682_to_712():
    pass
def run_712_to_203():
    pass

while True:
    run_203_to_132()
    run_132_to_535()
    run_535_to_477()
    run_477_to_715()
    run_715_to_316()
    run_316_to_510()
    run_510_to_692()
    run_692_to_682()
    run_682_to_712()
    run_712_to_203()
    
close_canvas()
