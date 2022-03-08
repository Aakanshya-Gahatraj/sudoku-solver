import sys
import pygame as pg
import sudokuSolver as s

pg.init()

pg.display.set_caption("Sudoku")
screen_size = 390, 450
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 35)
text = pg.font.SysFont(None, 25)
bright_black = (34, 32, 36)


def draw_bg():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 360, 360), 3)
    i = 1
    while(i*40 < 360):
        line_width = 1 if i % 3 > 0 else 3
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(
                    (i*40)+15, 15), pg.Vector2((i*40)+15, 375), line_width)
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(
            15, (i*40)+15), pg.Vector2(375, (i*40)+15), line_width)
        i += 1


def draw_numbers():
    row = 0
    offset = 30
    while row < 9:
        col = 0
        while col < 9:
            output = s.board[row][col]
            numberText = font.render(str(output), True, pg.Color("black"))
            screen.blit(numberText, pg.Vector2(
                        (col*40)+offset, (row*40)+offset-4))
            col += 1
        row += 1


msg = "Solve"


def draw_button():

    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if click[0] == 1:
        s.sudokuSolver(s.board)
        draw_numbers()
        global msg
        msg = "Solved"

    if 145+100 > mouse[0] > 145 and 390+40 > mouse[1] > 390:
        pg.draw.rect(screen, pg.Color("black"),
                     pg.Rect(145, 390, 100, 40))
    else:
        pg.draw.rect(screen, pg.Color(bright_black),
                     pg.Rect(145, 390, 100, 40))

    text = font.render(str(msg), True, pg.Color("white"))
    screen.blit(text, pg.Vector2(160, 398))


def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    draw_bg()
    draw_numbers()
    draw_button()
    pg.display.flip()


while 1:
    game_loop()
