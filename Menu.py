import pyxel

class MenuEngine:
    #Everything related to the menu
    def __init__(self):
        self.screensize=[256,128]
        self.in_shop=False

    def menu_draw(self):
        pyxel.camera(0,0)
        #Draws the mouse
        pyxel.mouse(True)

        #reveal the mouse coordinates if the key "b" is pressed
        if pyxel.btn(pyxel.KEY_B):
            pyxel.text(240,self.screensize[1]-15,str(pyxel.mouse_x),1)
            pyxel.text(240,self.screensize[1]-7,str(pyxel.mouse_y),1)

        #draws the menu borders
        for a in range(0,3,2):
            pyxel.rectb(70+a,27+a,self.screensize[0]-140,self.screensize[1]-47,1)
        
        #Title
        text_border("Ski Adventure",self.screensize[0]/2-26,10,1,11)
        
        #Menu design
        if self.in_shop==False:
            
            #start button
            if self.screensize[0]/2-10 <= pyxel.mouse_x <= self.screensize[0]/2+10 and self.screensize[1]/2-4 <= pyxel.mouse_y <= self.screensize[1]/2+3:
                text_border("START",self.screensize[0]/2-9,self.screensize[1]/2-1,1,11)
            else:
                text_border("START",self.screensize[0]/2-9,self.screensize[1]/2-2,1,3)
            #shop button
            if self.screensize[0]-179 <= pyxel.mouse_x <= self.screensize[0]-164 and self.screensize[1]-31 <= pyxel.mouse_y <= self.screensize[1]-24:
                text_border("Shop",77,self.screensize[1]-29,1,11)
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): self.in_shop=True
            else:
                text_border("Shop",77,self.screensize[1]-30,1,3)
            #settings button
            if self.screensize[0]-107 <= pyxel.mouse_x <= self.screensize[0]-75 and self.screensize[1]-31 <= pyxel.mouse_y <= self.screensize[1]-24:
                text_border("Settings",self.screensize[0]-106,self.screensize[1]-29,1,11)
            else:
                text_border("Settings",self.screensize[0]-106,self.screensize[1]-30,1,3)


        #detection of selected interface
        elif self.in_shop==True: self.shop_interface()
        
    #Shop interface
    def shop_interface(self):
        #clicked shop button
        text_border("Shop",77,self.screensize[1]-29,1,11)
        #detection of the mouse to leave the shop interface
        if self.screensize[0]-179 <= pyxel.mouse_x <= self.screensize[0]-164 and self.screensize[1]-31 <= pyxel.mouse_y <= self.screensize[1]-24 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.in_shop=False
        #boxes of selection
        for x in range(81,166,14):
            for y in range(33,49,15):
                pyxel.rectb(x,y,12,13,1)
        for x in range(81,166,14):
            pyxel.rectb(x,65,12,13,1)
        for x in range(81,166,14):
            pyxel.rectb(x,82,12,13,1)

    def menu_update(self):
        if pyxel.btnp(pyxel.KEY_SPACE) or (self.screensize[0]/2-10 <= pyxel.mouse_x <= self.screensize[0]/2+10 and self.screensize[1]/2-4 <= pyxel.mouse_y <= self.screensize[1]/2+3 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)):
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