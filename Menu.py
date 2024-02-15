import pyxel

class MenuEngine:
    def __init__(self):
        self.screensize=[256,128]



    def menu_draw(self):
        pyxel.camera(0,0)
        x,y = 70,20
        for i in range(2):
            pyxel.rectb(x,y,self.screensize[0]-140,self.screensize[1]-40,1)
            x,y=x+2,y-2

        pyxel.mouse(True)
        if self.screensize[0]/2-10 <= pyxel.mouse_x <= self.screensize[0]/2+10 and self.screensize[1]/2-11 <= pyxel.mouse_y <= self.screensize[1]/2-4:
            text_border("START",self.screensize[0]/2-9,self.screensize[1]/2-10,1,11)
        else:
            text_border("START",self.screensize[0]/2-9,self.screensize[1]/2-10,1,3)






    def menu_update(self):
        if self.screensize[0]/2-10 <= pyxel.mouse_x <= self.screensize[0]/2+10 and self.screensize[1]/2-11 <= pyxel.mouse_y <= self.screensize[1]/2-4 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return True
        else:
            return False
    
def text_border(text,x,y,borderColor,color):
    pyxel.text(x+1,y+1,text,borderColor)
    pyxel.text(x+1,y-1,text,borderColor)
    pyxel.text(x-1,y-1,text,borderColor)
    pyxel.text(x-1,y+1,text,borderColor)
    pyxel.text(x+1,y,text,borderColor)
    pyxel.text(x,y+1,text,borderColor)
    pyxel.text(x-1,y,text,borderColor)
    pyxel.text(x,y-1,text,borderColor)
    pyxel.text(x,y,text,color)