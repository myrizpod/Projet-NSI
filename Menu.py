import pyxel

class MenuEngine:
    #Everything related to the menu
    def __init__(self):
        self.screensize=[256,128]

    def menu_draw(self):
        pyxel.camera(0,0)
        #draws the menu borders
        for a in range(0,3,2):
            pyxel.rectb(70+a,20+a,self.screensize[0]-140,self.screensize[1]-40,1)

        #Draws the mouse
        pyxel.mouse(True)
        #change the START button's color if the user hoover it with the mouse
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
    """draws text at position [x,y] of color color surrounded by a border of color borderColor. <-- Understandeable sentence

    Args:
        text (string): text to print
        x (int): x position of the text
        y (int): y position of the text
        borderColor (int [0,15]): color of the border line
        color (int [0,15]): color of the text
    """
    #border
    for modX in range(-1,2):
        for modY in range(-1,2):
            pyxel.text(x+modX,y+modY,text,borderColor)
    pyxel.text(x,y,text,color)