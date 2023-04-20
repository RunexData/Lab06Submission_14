import sys 
import pygame as pg
    
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.R = r
        self.G = g
        self.B = b
    def draw(self,screen):
        pg.draw.rect(screen,(self.R,self.G,self.B),(self.x,self.y,self.w,self.h))
        
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def hover(self):
        xpos, ypos = pg.mouse.get_pos()
        if xpos >= self.x and xpos <= self.x + self.w and ypos >= self.y and ypos <= self.y + self.h:
            return True
        else:
            return False
    def click(self):
        if pg.mouse.get_pressed()[0]:
            return True
        else:
            return False
        
pg.init()
run = True
win_x, win_y = 1920, 1080
screen = pg.display.set_mode((win_x, win_y))
btn = Button(win_x // 2 -50 ,win_y // 2 -50,100,100) # สร้าง Object จากคลาส Button ขึ้นมา
Left = False
Right = False
Up = False
Down = False
Stop = False

while(run):
    screen.fill((255, 255, 255))
    btn.draw(screen)
    # EX2
    if Stop :
        pass
    elif Up :
        btn.y -= 0.5
        pg.time.delay(1)
    elif Down :
        btn.y += 0.5
        pg.time.delay(1)
    elif Left :
        btn.x -= 0.5
        pg.time.delay(1)
    elif Right :
        btn.x += 0.5
        pg.time.delay(1)
        

    
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            pg.quit()
            run = False
            
        if event.type == pg.KEYUP:
            Stop = True
            print("STOP")
            pg.time.delay(3)
            Right = False
            Left = False 
            Up = False
            Down = False
            pass
        if event.type == pg.KEYDOWN and event.key == pg.K_d: 
            Right = True
            Stop = False
            pg.time.delay(3)
            print("D")
        if event.type == pg.KEYDOWN and event.key == pg.K_a: 
            Left = True
            Stop = False
            pg.time.delay(3)
            print("A")
        if event.type == pg.KEYDOWN and event.key == pg.K_s: 
            Down = True
            Stop = False
            pg.time.delay(3)
            print("S")
        if event.type == pg.KEYDOWN and event.key == pg.K_w: 
            Up = True
            Stop = False
            pg.time.delay(3)
            print("W")
