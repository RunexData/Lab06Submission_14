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
class InputBox:
    def __init__(self, x, y, w, h,check, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.check = check
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                txt = event.unicode
                if event.key == pg.K_RETURN:
                    pass
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.check:
                        if txt.isnumeric():
                            self.text += txt
                        else:
                            pass
                    else:
                        self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
                
    def ans(self):
        return self.text
    
    def reset(self):
        self.text = ''
        self.txt_surface = FONT.render('', True,(255,255,255))
        
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5,))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2,10)
        
pg.init()
win_x, win_y = 1920, 1080
screen = pg.display.set_mode((win_x, win_y))

font = pg.font.Font('BAUHS93.ttf', 100) # font and fontsize
fontS = pg.font.Font('BAUHS93.ttf', 30)
login = font.render('LOGIN', True, (0,0,0), (255,255,255))# (text,is smooth?,letter color,background color)
first = fontS.render('FIRSTNAME', True, (0,0,0), (255,255,255))
last = fontS.render('LASTNAME', True, (0,0,0), (255,255,255))
age = fontS.render('AGE', True, (0,0,0), (255,255,255))
submitt = fontS.render('SUBMIT', True, (255,255,255))
submittt = fontS.render('SUBMIT', True, (0,0,0))
resett= fontS.render('RESET', True, (255,0,0))
resettt = fontS.render('RESET', True, (0,0,0))
loginRect = login.get_rect() # text size
firstRect = first.get_rect() # text size
lastRect = last.get_rect() # text size
ageRect = age.get_rect() # text size
submitRect = submitt.get_rect() # text size
submit2Rect = submittt.get_rect()
resetRect = resett.get_rect()
loginRect.center = (win_x // 2, 250)
submitRect.center = (win_x // 2, 700)

resetRect.center = (win_x // 2, 775)
COLOR_INACTIVE = (0,0,0)# ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = (148,148,148)    # ^^^
FONT = pg.font.Font('BAUHS93.ttf', 32)
val = 0
r = 0
input_box1 = InputBox(win_x // 2 - 100, 350, 140, 45,False) # สร้าง InputBox1
input_box2 = InputBox(win_x // 2 - 100, 450, 140, 45,False) # สร้าง InputBox2
input_box3 = InputBox(win_x // 2 - 100, 550, 140, 45,True) # สร้าง InputBox2
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

submit = Button(win_x // 2-65 ,675,130,50)
reset = Button(win_x // 2-65 ,750,130,50)
        
while run:
    screen.fill((255, 255, 255))
    
    screen.blit(login,loginRect)
    screen.blit(first,(win_x // 2 - 100,320))
    screen.blit(last,(win_x // 2 - 100,420))
    screen.blit(age,(win_x // 2 - 100,520))
    submit.draw(screen)
    screen.blit(submitt,submitRect)
    reset.draw(screen)
    screen.blit(resett,resetRect)
    
    pg.draw.rect(screen,(0,0,0),(0,900,1920,100))
   
    if val == 1:
        screen.blit(ans,ansRect)
    if r == 1:
        input_box1.reset()
        input_box2.reset()
        input_box3.reset()
        ans = fontS.render('', True, (255,255,255))
        r = 0
    if submit.hover():
        if submit.click():
            submit.R = 255
            submit.G = 255
            submit.B = 255
            screen.blit(submittt,submitRect)
            ans = fontS.render('Hello '+ input_box1.ans() + '  ' + input_box2.ans() + " ! You are " + input_box3.ans() + ' years old.', True, (255,255,255))
            ansRect = ans.get_rect()
            ansRect.center=(win_x//2,940)
            val = 1
        else :
            submit.R = 0
            submit.G = 0
            submit.B = 0
    else:
        submit.R = 0
        submit.G = 0
        submit.B = 0
        
    if reset.hover():
        if reset.click():
            reset.R = 255
            reset.G = 255
            reset.B = 255
            r = 1
        else :
            reset.R = 0
            reset.G = 0
            reset.B = 0
    else:
        reset.R = 0
        reset.G = 0
        reset.B = 0
    
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            pg.quit()
            run = False
            
    pg.time.delay(1)
    pg.display.update()