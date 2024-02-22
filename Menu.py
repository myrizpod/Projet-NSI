import pyxel

class MenuEngine:
    #Everything related to the menu
    def __init__(self):
        self.screensize=[256,128]

    def menu_draw(self):
        pyxel.camera(0,0)

        pyxel.text(240,110,str(pyxel.mouse_x),7)
        pyxel.text(240,120,str(pyxel.mouse_y),7)

        #draws the menu borders
        for a in range(0,3,2):
            pyxel.rectb(70+a,27+a,self.screensize[0]-140,self.screensize[1]-47,1)

        #Draws the mouse
        pyxel.mouse(True)

        #change the START button's color if the user hoover it with the mouse
        #start button
        if self.screensize[0]/2-10 <= pyxel.mouse_x <= self.screensize[0]/2+10 and self.screensize[1]/2-4 <= pyxel.mouse_y <= self.screensize[1]/2+3:
            text_border("START",self.screensize[0]/2-9,self.screensize[1]/2-1,1,11)
        else:
            text_border("START",self.screensize[0]/2-9,self.screensize[1]/2-2,1,3)
        #shop button
        if self.screensize[0]-179 <= pyxel.mouse_x <= self.screensize[0]-164 and self.screensize[1]-31 <= pyxel.mouse_y <= self.screensize[1]-24:
            text_border("Shop",77,self.screensize[1]-29,1,11)
        else:
            text_border("Shop",77,self.screensize[1]-30,1,3)
        #settings button
        if self.screensize[0]-107 <= pyxel.mouse_x <= self.screensize[0]-75 and self.screensize[1]-31 <= pyxel.mouse_y <= self.screensize[1]-24:
            text_border("Settings",self.screensize[0]-106,self.screensize[1]-29,1,11)
        else:
            text_border("Settings",self.screensize[0]-106,self.screensize[1]-30,1,3)



    def menu_update(self):
        if pyxel.btnp(pyxel.KEY_SPACE) or (self.screensize[0]/2-10 <= pyxel.mouse_x <= self.screensize[0]/2+10 and self.screensize[1]/2-11 <= pyxel.mouse_y <= self.screensize[1]/2-4 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)):
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