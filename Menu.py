import pyxel
from time import sleep

class MenuEngine:
    #Everything related to the menu
    def __init__(self):
        self.screensize=[256,128]
        self.in_shop=False
        self.in_settings=False
        self.coo_case_shop=[]
        self.shop_selected_cases_skins=[]
        self.shop_selected_cases_skis=[]
        self.shop_selected_cases_=[]
        self.shop_selected_cases_objects=[]

    def menu_draw(self):
        #set camera to coordinates (0;0)
        pyxel.camera(0,0)

        #draws the mouse
        pyxel.mouse(True)

        #reveal the mouse coordinates if the key "b" is pressed
        if pyxel.btn(pyxel.KEY_B):
            pyxel.text(240,self.screensize[1]-15,str(pyxel.mouse_x),1)
            pyxel.text(240,self.screensize[1]-7,str(pyxel.mouse_y),1)

        #draws the menu borders
        for i in range(0,3,2):
            pyxel.rectb(70+i,27+i,self.screensize[0]-140,self.screensize[1]-47,1)
        
        #Title
        text_border("Ski Adventure",self.screensize[0]/2-26,10,1,11)
        
        #Menu design
        if self.in_shop==False and self.in_settings==False:
            
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
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): self.in_settings=True
            else:
                text_border("Settings",self.screensize[0]-106,self.screensize[1]-30,1,3)


        #detection of selected interface
        elif self.in_shop==True: self.shop_interface()
        elif self.in_settings==True: self.settings_interface()
        
    #Shop interface
    def shop_interface(self):
        #clicked shop button
        text_border("Shop",77,self.screensize[1]-29,1,11)

        #detection of the mouse to leave the shop interface
        if self.screensize[0]-179 <= pyxel.mouse_x <= self.screensize[0]-164 and self.screensize[1]-31 <= pyxel.mouse_y <= self.screensize[1]-24 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.in_shop=False

        #boxes of selection
        for y in range(33,49,15):
            for x in range(81,166,14):
                if len(self.coo_case_shop)!=28: self.coo_case_shop.append([x,y])
                pyxel.rectb(x,y,12,13,1)
        for y in range(65,83,17):
            for x in range(81,166,14):
                if len(self.coo_case_shop)!=28: self.coo_case_shop.append([x,y])
                pyxel.rectb(x,y,12,13,1)

        #detection of the mouse for shop selection + add the coordinates of the selected case to the list in relation
        for i in self.coo_case_shop:
            if i[0] <= pyxel.mouse_x <= i[0]+12 and i[1] <= pyxel.mouse_y <= i[1]+13:
                pyxel.rectb(i[0]-1,i[1]-1,14,15,11)
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    if i[1]==33 and i not in self.shop_selected_cases_skins:
                        self.shop_selected_cases_skins.append(i)
                        #print("shop_selected_cases_skins v0=",self.shop_selected_cases_skins)
                    elif i[1]==48 and i not in self.shop_selected_cases_skis:
                        self.shop_selected_cases_skis.append(i)
                        #print("shop_selected_cases_skis v0=",self.shop_selected_cases_skis)
                    elif i[1]==65 and i not in self.shop_selected_cases_:
                        self.shop_selected_cases_.append(i)
                        #print("shop_selected_cases_ v0=",self.shop_selected_cases_)
                    elif i[1]==82 and i not in self.shop_selected_cases_objects:
                        self.shop_selected_cases_objects.append(i)
                        #print("shop_selected_cases_objects v0=",self.shop_selected_cases_objects)
                else:pass
                
        #highlighting the selected cases using coordinates in the lists in relation + suppression of old selected cases when more than one case per line is selected
        #first line, skins
        if len(self.shop_selected_cases_skins)>0:
            #print("condition 1 ok, longueur +0")
            if len(self.shop_selected_cases_skins)>1:
                #print("condition 2 ok, longueur +1")
                del (self.shop_selected_cases_skins[0:-1])
            #print("dessination rect")
            pyxel.rectb(self.shop_selected_cases_skins[0][0],self.shop_selected_cases_skins[0][1],12,13,6)
        
        #second line, skis
        if len(self.shop_selected_cases_skis)>0:
            #print("condition 1 ok, longueur +0")
            if len(self.shop_selected_cases_skis)>1:
                #print("condition 2 ok, longueur +1")
                del (self.shop_selected_cases_skis[0:-1])
            #print("dessination rect")
            pyxel.rectb(self.shop_selected_cases_skis[0][0],self.shop_selected_cases_skis[0][1],12,13,6)
        
        #third line, ?
        if len(self.shop_selected_cases_)>0:
            #print("condition 1 ok, longueur +0")
            if len(self.shop_selected_cases_)>1:
                #print("condition 2 ok, longueur +1")
                del (self.shop_selected_cases_[0:-1])
            #print("dessination rect")
            pyxel.rectb(self.shop_selected_cases_[0][0],self.shop_selected_cases_[0][1],12,13,6)
        
        #fourth line, objects
        if len(self.shop_selected_cases_objects)>0:
            #print("condition 1 ok, longueur +0")
            if len(self.shop_selected_cases_objects)>1:
                #print("condition 2 ok, longueur +1")
                del (self.shop_selected_cases_objects[0:-1])
            #print("dessination rect")
            pyxel.rectb(self.shop_selected_cases_objects[0][0],self.shop_selected_cases_objects[0][1],12,13,6)
    
    def settings_interface(self):
        #clicked settings button
        text_border("Settings",self.screensize[0]-106,self.screensize[1]-29,1,11)

        #detection of the mouse to leave the settings interface
        if self.screensize[0]-107 <= pyxel.mouse_x <= self.screensize[0]-75 and self.screensize[1]-31 <= pyxel.mouse_y <= self.screensize[1]-24 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.in_settings=False
        
        #global volume design
        pyxel.rect(77,34,2,4,3)
        pyxel.line(79,33,79,38,3)
        pyxel.line(80,32,80,39,3)

        #music volume design
        pyxel.line(74,48,74,49,3)
        pyxel.rect(75,47,2,4,3)
        pyxel.line(77,41,77,49,3)#barre principale
        pyxel.line(78,42,79,43,3)
        pyxel.line(78,43,80,45,3)

    def menu_update(self):
        if (pyxel.btnp(pyxel.KEY_SPACE) or (self.screensize[0]/2-10 <= pyxel.mouse_x <= self.screensize[0]/2+10 and self.screensize[1]/2-4 <= pyxel.mouse_y <= self.screensize[1]/2+3 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT))) and (self.in_shop==False and self.in_settings==False):
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