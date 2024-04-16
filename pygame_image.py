import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    fbg_ing = pg.transform.flip(bg_img, True, False)#練習７
    kk_img = pg.image.load("fig/3.png") #練習２
    kk_ing = pg.transform.flip(kk_img, True, False)#練習２
    kk_ing = pg.transform.rotozoom(kk_ing,10,1.0)#練習２
    kk_rct = kk_ing.get_rect()#練習８
    kk_rct.center = 300, 200#練習８
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_rct.move_ip([0,-1])
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip([0,1])
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip([-1,0])
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip([1,0])
        x=tmr%3200#練習６
        screen.blit(bg_img, [-x, 0])#練習６
        screen.blit(fbg_ing,[-x+1600, 0])#練習７
        screen.blit(bg_img, [-x+3200, 0])#練習７
        screen.blit(fbg_ing,[-x+4800, 0])#練習７
        screen.blit(kk_ing, kk_rct)#練習８
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()