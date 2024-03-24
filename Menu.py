import pyxel
from time import sleep

class MenuEngine:
    #Everything related to the menu
    def __init__(self):
        self.screensize=[256,128]#List of the size of the screen (arg 0: width, arg 1: height)
        self.in_shop=False#Boolean true if the player is in the shop interface and false otherwise
        self.in_popup=False#Boolean true if the player is in the shop interface and wanrts to buy a new item and false otherwise
        self.in_settings=False#Boolean true if the player is in the settings interface and false otherwise
        self.coo_case_shop=[]#List of all the coordinates of the item's case in the shop interface (now not full but after contains lists of coordinates (x and y))
        self.shop_selected_cases_skins=[[81, 33]]#List of list of the coordinates (x and y) of the selected case in the skins line
        self.shop_selected_cases_skis=[[81, 48]]#List of list of the coordinates (x and y) of the selected case in the skis line
        self.shop_selected_cases_scarfs=[[81, 65]]#List of list of the coordinates (x and y) of the selected case in the scarfs line
        self.shop_selected_cases_objects=[]#List of list of the coordinates (x and y) of the selected case in the objects line (empty at the beginning, need money to unlock objects)
        self.cases_shop=[["skin_1",0,True],["skin_2",100,False],["skin_3",100,False],["skin_4",100,False],["skin_5",100,False],["skin_6",100,False],["skin_7",100,False],["ski_1",0,True],["ski_2",100,False],["ski_3",100,False],["ski_4",100,False],["ski_5",100,False],["ski_6",100,False],["ski_7",100,False],["scarf_1",0,True],["scarf_2",100,False],["scarf_3",100,False],["scarf_4",100,False],["scarf_5",False],["scarf_6",100,False],["scarf_7",100,False],["object_1",0,False],["object_2",100,False],["object_3",100,False],["object_4",100,False],["object_5",100,False],["object_6",100,False],["object_7",100,False]]##List of list with info on every shop cases (arg 0: name(str), arg 1: price(int), arg 2: boolean(true if unlocked, false otherwise))
 

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
        """Draws the shop interface with its logic"""
        if self.in_popup==False:
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
                        if self.cases_shop[self.coo_case_shop.index(i)][2]==True:
                            if i[1]==33 and i not in self.shop_selected_cases_skins:
                                self.shop_selected_cases_skins.append(i)
                            elif i[1]==48 and i not in self.shop_selected_cases_skis:
                                self.shop_selected_cases_skis.append(i)
                            elif i[1]==65 and i not in self.shop_selected_cases_scarfs:
                                self.shop_selected_cases_scarfs.append(i)
                            elif i[1]==82 and i not in self.shop_selected_cases_objects:
                                self.shop_selected_cases_objects.append(i)
                        else: self.in_popup=i
                            
                    
            #highlighting the selected cases using coordinates in the lists in relation + suppression of old selected cases when more than one case per line is selected
            #first line, skins
            if len(self.shop_selected_cases_skins)>0:
                if len(self.shop_selected_cases_skins)>1:
                    del (self.shop_selected_cases_skins[0:-1])
                pyxel.rectb(self.shop_selected_cases_skins[0][0],self.shop_selected_cases_skins[0][1],12,13,6)
            
            #second line, skis
            if len(self.shop_selected_cases_skis)>0:
                if len(self.shop_selected_cases_skis)>1:
                    del (self.shop_selected_cases_skis[0:-1])
                pyxel.rectb(self.shop_selected_cases_skis[0][0],self.shop_selected_cases_skis[0][1],12,13,6)
            
            #third line, scarfs
            if len(self.shop_selected_cases_scarfs)>0:
                if len(self.shop_selected_cases_scarfs)>1:
                    del (self.shop_selected_cases_scarfs[0:-1])
                pyxel.rectb(self.shop_selected_cases_scarfs[0][0],self.shop_selected_cases_scarfs[0][1],12,13,6)
            
            #fourth line, objects
            if len(self.shop_selected_cases_objects)>0:
                if len(self.shop_selected_cases_objects)>1:
                    del (self.shop_selected_cases_objects[0:-1])
                pyxel.rectb(self.shop_selected_cases_objects[0][0],self.shop_selected_cases_objects[0][1],12,13,6)
        else: self.shop_interface_popup_price_item(self.coo_case_shop.index(self.in_popup))

    def shop_interface_popup_price_item(self,ncase):
        """Draws a popup notifying the player of the price of the item he wants to purchase.
        If the player is ok and has the money needed, it will substract the price to his coins.
        Else it will simply close the popup

        Arg :
            ncase (int): the number of the item's case (0 to 27)"""
        pyxel.line(109,48,147,48,1)#line up
        pyxel.line(109,48,109,77,1)#line left
        pyxel.line(147,48,147,77,1)#line right
        pyxel.line(110,77,111,77,1)#1st part line down
        pyxel.line(127,77,129,77,1)#second part line down
        pyxel.line(145,77,146,77,1)#third part line down

        pyxel.text(109+2,48+2,self.cases_shop[ncase][0]+" :",1)
        pyxel.text(109+2,50+8,str(self.cases_shop[ncase][1])+" coins",1)

        pyxel.rectb(112,73,15,9,1)#disagree rectangle
        pyxel.text(112+2,73+2,"No",1)
        pyxel.rectb(130,73,15,9,1)#agree rectangle
        pyxel.text(130+2,73+2,"Yes",1)

        if 112 <= pyxel.mouse_x <= 126 and 73 <= pyxel.mouse_y <= 81:
            pyxel.rectb(112,73,15,9,0)
            pyxel.text(112+2,73+2,"No",0)
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.in_popup=False
        
        if 130 <= pyxel.mouse_x <= 144 and 73 <= pyxel.mouse_y <= 81:
            pyxel.rectb(130,73,15,9,0)
            pyxel.text(130+2,73+2,"Yes",0)
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):###and check if the number of coins is superior or equal to the item price
                ###need to substract the price of the item to the number of coins of the player
                self.cases_shop[ncase][2]=True
                self.in_popup=False




    def settings_interface(self):
        """Draws the grphics of the settings interface with its logic"""
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