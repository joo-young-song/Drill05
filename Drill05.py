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
    x, y, frame = 132, 243, 0
    while y < 470:
        if x < 535:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 2
            delay(0.05)
        else:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            y += 2
            delay(0.05)

def run_535_to_477():
    x, y, frame = 535, 470, 0
    while y > 203:
        if x > 477:
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

def run_477_to_715():
    x, y, frame = 477, 203, 0
    while y > 136:
        if x < 715:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 2
            delay(0.05)
        else:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            y -= 2
            delay(0.05)
def run_715_to_316():
    x, y, frame = 715, 136, 0
    while y < 225:
        if x > 316:
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
            y += 2
            delay(0.05)
def run_316_to_510():
    x, y, frame = 316, 225, 0
    while y > 92:
        if x < 510:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 2
            delay(0.05)
        else:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            y -= 2
            delay(0.05)
def run_510_to_692():
    x, y, frame = 510, 92, 0
    while y < 518:
        if x < 692:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 2
            delay(0.05)
        else:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            y += 2
            delay(0.05)
def run_692_to_682():
    x, y, frame = 692, 518, 0
    while y > 336:
        if x > 682:
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
def run_682_to_712():
    x, y, frame = 682, 336, 0
    while y < 349:
        if x < 712:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 2
            delay(0.05)
        else:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character_run.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            y += 2
            delay(0.05)
def run_712_to_203():
    pass

while True:
    #run_203_to_132()
    #run_132_to_535()
    #run_535_to_477()
    #run_477_to_715()
    #run_715_to_316()
    #run_316_to_510()
    #run_510_to_692()
    #run_692_to_682()
    run_682_to_712()
    run_712_to_203()
    
close_canvas()
