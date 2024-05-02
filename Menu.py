import pyxel
"""
To do:
    - optimize the popup graphics /
    - replace the coordinates with variables /
    - make the popup show the effect of the wanted item (if there is one) /
    - create the mode button of desert/snow with its logic /
    - replace the colors of the graphics with variables depending on the game's mode /
"""
class MenuEngine:
    #Everything related to the menu
    def __init__(self,app):
        self.app=app
        self.screensize=[256,128]#List of the size of the screen (arg 0: width, arg 1: height)
        self.all_colours={"snowy":
                          {"basic text color":1,
                           "outlines color":1,
                           "title":{"bordercolor":1, "text color":11},
                           "main buttons":{"clicked":{"bordercolor":1, "text color":11}, "normal":{"bordercolor":1, "text color":3}},
                           "money text":{"shadow color":1, "text color":10},
                           "shop cases":{"shop cases color":1, "selected shop cases color":11,"shop cases mouseover":12},
                           "price popup":{"popup background color":5, "popup text item's name color":7, "popup text item's price color":10, "popup text item's effect color":1, "normal":{"popup buttons's outlines color":1, "popup buttons's text color":1}, "clicked":{"popup buttons's outlines color":0, "popup buttons's text color":0}},
                           "settings graphics":{"settings outline color":1, "global volume logo color":3, "music volume logo color":3, "empty volume lines color":0, "volume lines color":3, "volume buttons color":1, "clicked volume buttons color":0},
                           "effect popup":{"popup background color":5, "popup text item's effect color":0, "normal":{"popup buttons's outlines color":1, "popup buttons's text color":1}, "clicked":{"popup buttons's outlines color":0, "popup buttons's text color":0}}},
                        "desert":
                          {"basic text color":0,
                           "outlines color":10,
                           "title":{"bordercolor":8, "text color":10},
                           "main buttons":{"clicked":{"bordercolor":8, "text color":14}, "normal":{"bordercolor":8, "text color":10}},
                           "money text":{"shadow color":10, "text color":1},
                           "shop cases":{"shop cases color":8, "selected shop cases color":14,"shop cases mouseover":10},
                           "price popup":{"popup background color":1, "popup text item's name color":7, "popup text item's price color":10, "popup text item's effect color":8, "normal":{"popup buttons's outlines color":10, "popup buttons's text color":10}, "clicked":{"popup buttons's outlines color":9, "popup buttons's text color":9}},
                           "settings graphics":{"settings outline color":2, "global volume logo color":8, "music volume logo color":8, "empty volume lines color":14, "volume lines color":2, "volume buttons color":8, "clicked volume buttons color":2},
                           "effect popup":{"popup background color":5, "popup text item's effect color":7, "normal":{"popup buttons's outlines color":10, "popup buttons's text color":10}, "clicked":{"popup buttons's outlines color":8, "popup buttons's text color":8}}}}#Dictionnary of dictionnary of... with the colors (int (0 to 15)) of all graphical element of the start menu depending on the game mode
        self.global_volume=3#Global volume of all game's sounds (int: (0 to 7))
        self.music_volume=2#Volume of the game's music (int: (0 to 7))
        self.mode="snowy"#The mode of the game (str: "snowy" or "desert")
        self.target_coins=self.app.total_coins#The amount of money, decreasing after a purchase of the player in the shop allowing the animation of -5coins until correct amount (int)
        self.in_shop=False#Boolean true if the player is in the shop interface and false otherwise
        self.in_popup=False#Boolean true if the player is in the shop interface and wanrts to buy a new item and false otherwise
        self.in_effect_popup=False#Boolean true if player right click on a shop item already purchase allowing the apparition of a popup with infos about the item's effect
        self.in_settings=False#Boolean true if the player is in the settings interface and false otherwise
        self.coo_case_shop=[]#List of all the coordinates of the item's case in the shop interface (now not full but after contains lists of coordinates (x and y))
        self.shop_selected_cases_skins=[[81, 33]]#List of list of the coordinates (x and y) of the selected case in the skins line
        self.shop_selected_cases_skis=[[81, 48]]#List of list of the coordinates (x and y) of the selected case in the skis line
        self.shop_selected_cases_scarfs=[[81, 65]]#List of list of the coordinates (x and y) of the selected case in the scarfs line
        self.shop_selected_cases_objects=[]#List of list of the coordinates (x and y) of the selected case in the objects line (empty at the beginning, need money to unlock objects)
        self.selected_skin="The Duck"#Name of the selected skin (str)
        self.selected_ski="Black skis"#Name of the selected ski (str)
        self.selected_scarf="Black scarf"#Name of the selected scarf (str)
        self.selected_object=""#Name of the selected object (str)
        self.cases_shop=[["The Duck",0,True,"No effect"],["Donald",100,False,"effet a specifier"],["Pika pika",3,False,"effet a specifier"],["Golden Duck",100,False,"effet a specifier"],["Maskass",100,False,"effet a specifier"],["Songoku",100,False,"effet a specifier"],["Ninja turtle",100,False,"effet a specifier"],["Black skis",0,True],["Blue skis",100,False],["Electric skis",100,False],["Yellow skis",100,False],["Red skis",100,False],["Snowy skis",100,False],["Green skis",100,False],["Black scarf",0,True],["Blue scarf",100,False],["Electric scarf",100,False],["Yellow_scarf",100,False],["Red scarf",100,False],["Green_and_white_scarf",100,False],["Green scarf",100,False],["Shield",0,False,"effet a specifier"],["Chest",100,False,"effet a specifier"],["Bomb",100,False,"effet a specifier"],["Froggy",100,False,"effet a specifier"],["Magnet",100,False,"effet a specifier"],["Coins x2",100,False,"effet a specifier"],["Trophy",100,False,"effet a specifier"]]##List of list with info on every shop cases (arg 0: name(str), arg 1: price(int), arg 2: boolean(true if unlocked, false otherwise), arg 3(if available): str(object'effect))
        #Reading the already acquired items and changing the value of the boolean of self.cases_shop according to it
        for i in range(len(app.unlocked_items)-1):
            if not self.cases_shop[i][2]==True:
                self.cases_shop[i][2]=app.unlocked_items[i]


    def menu_draw(self):
        #set camera to coordinates (0;0)
        pyxel.camera(0,0)

        #reveal the mouse coordinates if the key "b" is pressed
        if pyxel.btn(pyxel.KEY_B):
            pyxel.text(240,self.screensize[1]-15,str(pyxel.mouse_x),self.all_colours[self.mode]["basic text color"])
            pyxel.text(240,self.screensize[1]-7,str(pyxel.mouse_y),self.all_colours[self.mode]["basic text color"])

        #draws the menu borders
        for i in range(0,3,2):
            pyxel.rectb(70+i,27+i,self.screensize[0]-140,self.screensize[1]-47,self.all_colours[self.mode]["outlines color"])

        #Title
        text_border("Ski Adventure",self.screensize[0]/2-26,10,self.all_colours[self.mode]["title"]["bordercolor"],self.all_colours[self.mode]["title"]["text color"])
        
        #Menu design
        if self.in_shop==False:
            pyxel.text(4,3,"Best score: "+str(self.app.best_score),self.all_colours[self.mode]["basic text color"])
            #start button
            if self.screensize[0]/2-10 <= pyxel.mouse_x <= self.screensize[0]/2+10 and self.screensize[1]/2-4 <= pyxel.mouse_y <= self.screensize[1]/2+3:
                text_border("START",self.screensize[0]/2-9,self.screensize[1]/2-1,self.all_colours[self.mode]["main buttons"]["clicked"]["bordercolor"],self.all_colours[self.mode]["main buttons"]["clicked"]["text color"])#the start button if the mouse is over
            else:
                text_border("START",self.screensize[0]/2-9,self.screensize[1]/2-2,self.all_colours[self.mode]["main buttons"]["normal"]["bordercolor"],self.all_colours[self.mode]["main buttons"]["normal"]["text color"])#the start button if the mouse is not over
            #mode button
            if self.mode=="snowy":
                if self.screensize[0]-23 <= pyxel.mouse_x <= self.screensize[0]-5 and 4 <= pyxel.mouse_y <= 22:
                    pyxel.blt(self.screensize[0]-23,4,0,32,32,19,19,0)#the flake button graphics if the mouse is over
                else:
                    pyxel.blt(self.screensize[0]-23,4,0,0,32,19,19,0)#the flake button graphics if the mouse is not over
            if self.mode=="desert":
                if self.screensize[0]-29 <= pyxel.mouse_x <= self.screensize[0]-5 and 4 <= pyxel.mouse_y <= 28:
                    pyxel.blt(self.screensize[0]-29,4,0,43,68,25,25,13)#the sun button graphics if the mouse is over
                else:
                    pyxel.blt(self.screensize[0]-29,4,0,11,68,25,25,13)#the sun button graphics if the mouse is not over
            #shop button
            if 76 <= pyxel.mouse_x <= 92 and self.screensize[1]-31 <= pyxel.mouse_y <= self.screensize[1]-24:
                text_border("Shop",77,self.screensize[1]-29,self.all_colours[self.mode]["main buttons"]["clicked"]["bordercolor"],self.all_colours[self.mode]["main buttons"]["clicked"]["text color"])#the shop button if the mouse is over
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.in_settings==False: self.in_shop=True
            else:
                text_border("Shop",77,self.screensize[1]-30,self.all_colours[self.mode]["main buttons"]["normal"]["bordercolor"],self.all_colours[self.mode]["main buttons"]["normal"]["text color"])#the shop button if the mouse is not over
            #settings button
            if self.screensize[0]-107 <= pyxel.mouse_x <= self.screensize[0]-75 and self.screensize[1]-31 <= pyxel.mouse_y <= self.screensize[1]-24:
                text_border("Settings",self.screensize[0]-106,self.screensize[1]-29,self.all_colours[self.mode]["main buttons"]["clicked"]["bordercolor"],self.all_colours[self.mode]["main buttons"]["clicked"]["text color"])#the settings button if the mouse is over
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): self.in_settings=not self.in_settings
            elif self.in_settings==False:
                text_border("Settings",self.screensize[0]-106,self.screensize[1]-30,self.all_colours[self.mode]["main buttons"]["normal"]["bordercolor"],self.all_colours[self.mode]["main buttons"]["normal"]["text color"])#the settings button if the mouse is not over
            else:
                text_border("Settings",self.screensize[0]-106,self.screensize[1]-29,self.all_colours[self.mode]["main buttons"]["clicked"]["bordercolor"],self.all_colours[self.mode]["main buttons"]["clicked"]["text color"])#the settings button if the player is in the settings
            
            #detection of the necessity of settings appearence
            if self.in_settings==True: self.settings_interface()

        #detection of the necessity of shop appearence
        else: self.shop_interface()

        #draws the mouse
        if self.mode=="snowy": pyxel.blt(pyxel.mouse_x,pyxel.mouse_y,0,24,0,8,8,0)
        else: pyxel.blt(pyxel.mouse_x,pyxel.mouse_y,0,32,0,8,8,0)

    #Shop interface
    def shop_interface(self):
        """Draws the shop graphics with its logic"""
        #clicked shop button
        text_border("Shop",77,self.screensize[1]-29,self.all_colours[self.mode]["main buttons"]["clicked"]["bordercolor"],self.all_colours[self.mode]["main buttons"]["clicked"]["text color"])

        #detection of the mouse to leave the shop interface
        if 76 <= pyxel.mouse_x <= 92 and self.screensize[1]-31 <= pyxel.mouse_y <= self.screensize[1]-24 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.in_popup==False and self.in_effect_popup==False:
            self.in_shop=False

        if self.in_effect_popup==False:

            #showing the actual amount of money with an animation decreasing it if the player bought something in the shop
            if self.app.total_coins>self.target_coins:
                if self.app.total_coins-self.target_coins>=5: self.app.total_coins-=5
                else: self.app.total_coins-=self.app.total_coins-self.target_coins
            pyxel.text(4,3,"Coins: "+str(self.app.total_coins),self.all_colours[self.mode]["money text"]["shadow color"])#shadow of the text of the amount of money
            pyxel.text(3,3,"Coins: "+str(self.app.total_coins),self.all_colours[self.mode]["money text"]["text color"])#text of the amount of money

            #graphics of the boxes of selection
            for y in range(33,49,15):
                for x in range(81,166,14):
                    if len(self.coo_case_shop)!=28: self.coo_case_shop.append([x,y])
                    pyxel.rectb(x,y,12,13,self.all_colours[self.mode]["shop cases"]["shop cases color"])#the two first lines of cases for shop's items
                    pyxel.blt(x+2,y+3,2,((x-81)/14)*16,((y-33)/15)*32,8,8,0)#skins and skis graphics
            for y in range(65,83,17):
                for x in range(81,166,14):
                    if len(self.coo_case_shop)!=28: self.coo_case_shop.append([x,y])
                    pyxel.rectb(x,y,12,13,self.all_colours[self.mode]["shop cases"]["shop cases color"])#the two last lines of cases for shop's items
                    pyxel.blt(x+2,y+3,2,((x-81)/14)*16,64+((y-65)/17)*32,8,8,0)#scarfs and objects graphics
        
        #detection of the mouse for shop selection + add the coordinates of the selected case to the list in relation
        if self.in_popup==False and self.in_effect_popup==False:
            for i in self.coo_case_shop:
                if i[0] <= pyxel.mouse_x <= i[0]+12 and i[1] <= pyxel.mouse_y <= i[1]+13:
                    pyxel.rectb(i[0]-1,i[1]-1,14,15,self.all_colours[self.mode]["shop cases"]["shop cases mouseover"])#rectangle appearing whenever the mouse is over a case of a shop's item
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
                        else: self.in_popup=i#Saving the value of the case to buy
                    elif pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT) and self.cases_shop[self.coo_case_shop.index(i)][2]==True and len(self.cases_shop[self.coo_case_shop.index(i)])>3:
                        self.in_effect_popup=i

        #highlighting the selected cases using coordinates in the lists in relation + suppression of old selected cases when more than one case per line is selected + add the name of the selected item per line in the related variable to be used in the game file
        #first line, skins
        if self.in_effect_popup==False:
            if len(self.shop_selected_cases_skins)>0:
                if len(self.shop_selected_cases_skins)>1:
                    del (self.shop_selected_cases_skins[0:-1])
                pyxel.rectb(self.shop_selected_cases_skins[0][0],self.shop_selected_cases_skins[0][1],12,13,self.all_colours[self.mode]["shop cases"]["selected shop cases color"])#drawing a rectangle to reveal the selected skin in the shop
                self.selected_skin=self.cases_shop[self.coo_case_shop.index(self.shop_selected_cases_skins[0])][0]
            
            #second line, skis
            if len(self.shop_selected_cases_skis)>0:
                if len(self.shop_selected_cases_skis)>1:
                    del (self.shop_selected_cases_skis[0:-1])
                pyxel.rectb(self.shop_selected_cases_skis[0][0],self.shop_selected_cases_skis[0][1],12,13,self.all_colours[self.mode]["shop cases"]["selected shop cases color"])#drawing a rectangle to reveal the selected ski in the shop
                self.selected_ski=self.cases_shop[self.coo_case_shop.index(self.shop_selected_cases_skis[0])][0]
            
            #third line, scarfs
            if len(self.shop_selected_cases_scarfs)>0:
                if len(self.shop_selected_cases_scarfs)>1:
                    del (self.shop_selected_cases_scarfs[0:-1])
                pyxel.rectb(self.shop_selected_cases_scarfs[0][0],self.shop_selected_cases_scarfs[0][1],12,13,self.all_colours[self.mode]["shop cases"]["selected shop cases color"])#drawing a rectangle to reveal the selected scarf in the shop
                self.selected_scarf=self.cases_shop[self.coo_case_shop.index(self.shop_selected_cases_scarfs[0])][0]
            
            #fourth line, objects
            if len(self.shop_selected_cases_objects)>0:
                if len(self.shop_selected_cases_objects)>1:
                    del (self.shop_selected_cases_objects[0:-1])
                pyxel.rectb(self.shop_selected_cases_objects[0][0],self.shop_selected_cases_objects[0][1],12,13,self.all_colours[self.mode]["shop cases"]["selected shop cases color"])#drawing a rectangle to reveal the selected object in the shop
                self.selected_object=self.cases_shop[self.coo_case_shop.index(self.shop_selected_cases_objects[0])][0]

        if self.in_popup!=False: self.shop_interface_popup_price_item(self.coo_case_shop.index(self.in_popup))#Drawing a popup with the info about the wanting item to purchase
        if self.in_effect_popup!=False: self.effect_popup(self.coo_case_shop.index(self.in_effect_popup))#Drawing a popup with effect infos about the selecte item


    def effect_popup(self, ncase):
        """Draws a popup with the item's effect that the player right click on (if already purchased).
        Arg :
            ncase (int): the number of the item's case (0 to 27)"""
        pyxel.rectb(95,48,68,17,self.all_colours[self.mode]["effect popup"]["normal"]["popup buttons's outlines color"])#pricipal popup's rectangle outlines
        pyxel.rect(96,49,66,15,self.all_colours[self.mode]["effect popup"]["popup background color"])#background of the main window
        pyxel.rect(123,61,12,7,self.all_colours[self.mode]["effect popup"]["popup background color"])#background of 'ok' button
        pyxel.text(96,49+2,self.cases_shop[ncase][3],self.all_colours[self.mode]["effect popup"]["popup text item's effect color"])#text with item's effect

        if 122 <= pyxel.mouse_x <= 135 and 60 <= pyxel.mouse_y <= 68:
            pyxel.rectb(122,60,14,9,self.all_colours[self.mode]["effect popup"]["clicked"]["popup buttons's outlines color"])#outline of 'ok' button if mouse is over
            pyxel.text(125,62,"Ok",self.all_colours[self.mode]["effect popup"]["clicked"]["popup buttons's text color"])#text of the 'ok' button if mouse is over
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.in_effect_popup=False
        else:
            pyxel.rectb(122,60,14,9,self.all_colours[self.mode]["effect popup"]["normal"]["popup buttons's outlines color"])#outline of 'ok' button
            pyxel.text(125,62,"Ok",self.all_colours[self.mode]["effect popup"]["normal"]["popup buttons's text color"])#text of the 'ok' button


    def shop_interface_popup_price_item(self,ncase):
        """Draws a popup notifying the player of the price of the item he wants to purchase.
        If the player is ok and has the money needed, it will substract the price to his coins and unlock the selected item.
        Else it will simply close the popup

        Arg :
            ncase (int): the number of the item's case (0 to 27)"""
        #popup graphics
        pyxel.rectb(95,48,68,30,self.all_colours[self.mode]["price popup"]["normal"]["popup buttons's outlines color"])#principal popup's rectangle outlines
        pyxel.rect(96,49,66,28,self.all_colours[self.mode]["price popup"]["popup background color"])#background of the main window
        pyxel.rect(113,77,13,4,self.all_colours[self.mode]["price popup"]["popup background color"])#background no button
        pyxel.rect(131,77,14,4,self.all_colours[self.mode]["price popup"]["popup background color"])#background yes button

        pyxel.text(96+1,48+2,self.cases_shop[ncase][0]+" :",self.all_colours[self.mode]["price popup"]["popup text item's name color"])#show the name of the item to buy in the popup
        pyxel.text(96+1,48+9,str(self.cases_shop[ncase][1])+" coins",self.all_colours[self.mode]["price popup"]["popup text item's price color"])#show the price of the item to buy in the popup
        if len(self.cases_shop[ncase])==4:
            pyxel.text(96,48+16,self.cases_shop[ncase][3],self.all_colours[self.mode]["price popup"]["popup text item's effect color"])#revealing the item's special effect if it has one

        #Detection of the mouse coordinates to leave the popup interface
        if 112 <= pyxel.mouse_x <= 126 and 73 <= pyxel.mouse_y <= 81:
            pyxel.rectb(112,73,15,9,self.all_colours[self.mode]["price popup"]["clicked"]["popup buttons's outlines color"])#disagree rectangle's graphics if mouse is over
            pyxel.text(112+2,73+2,"No",self.all_colours[self.mode]["price popup"]["clicked"]["popup buttons's text color"])#disagree rectangle's text if mouse is over
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.in_popup=False
        else:
            pyxel.rectb(112,73,15,9,self.all_colours[self.mode]["price popup"]["normal"]["popup buttons's outlines color"])#disagree rectangle's graphics
            pyxel.text(112+2,73+2,"No",self.all_colours[self.mode]["price popup"]["normal"]["popup buttons's text color"])#disagree rectangle's text

        #Detection of the mouse coordinates to purchase (if the player has the correct amount of money) the item to buy
        if 130 <= pyxel.mouse_x <= 144 and 73 <= pyxel.mouse_y <= 81:
            pyxel.rectb(131,73,15,9,self.all_colours[self.mode]["price popup"]["clicked"]["popup buttons's outlines color"])#agree rectangle's graphics if mouse is over
            pyxel.text(131+2,73+2,"Yes",self.all_colours[self.mode]["price popup"]["clicked"]["popup buttons's text color"])#agree rectangle's text if mouse i over
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.app.total_coins>=self.cases_shop[ncase][1]:
                self.target_coins-=self.cases_shop[ncase][1]
                self.cases_shop[ncase][2],self.app.unlocked_items[ncase]=True,True
                self.in_popup=False
        else:
            pyxel.rectb(131,73,15,9,self.all_colours[self.mode]["price popup"]["normal"]["popup buttons's outlines color"])#agree rectangle's graphics
            pyxel.text(131+2,73+2,"Yes",self.all_colours[self.mode]["price popup"]["normal"]["popup buttons's text color"])#agree rectangle's text


    def settings_interface(self):
        """Draws the graphics of the settings interface with its logic"""
        #rectangle of settings
        pyxel.rectb(self.screensize[0]-122,self.screensize[1]-57,50,25,self.all_colours[self.mode]["settings graphics"]["settings outline color"])
        
        #global volume design
        pyxel.rect(self.screensize[0]-118,self.screensize[1]-53,2,4,self.all_colours[self.mode]["settings graphics"]["global volume logo color"])
        pyxel.line(self.screensize[0]-116,self.screensize[1]-54,self.screensize[0]-116,self.screensize[1]-49,self.all_colours[self.mode]["settings graphics"]["global volume logo color"])
        pyxel.line(self.screensize[0]-115,self.screensize[1]-55,self.screensize[0]-115,self.screensize[1]-48,self.all_colours[self.mode]["settings graphics"]["global volume logo color"])
        #lines of the global volume with colors changing with the actual global volume (self.global_volume)
        for x in range(self.screensize[0]-113,self.screensize[0]-113+13,2):
            pyxel.line(x,self.screensize[1]-53,x,self.screensize[1]-50,self.all_colours[self.mode]["settings graphics"]["empty volume lines color"])#global volume lines if not attein
        for v in range(self.screensize[0]-113,self.screensize[0]-113+2*(self.global_volume),2):
            pyxel.line(v,self.screensize[1]-53,v,self.screensize[1]-50,self.all_colours[self.mode]["settings graphics"]["volume lines color"])#global volume lines if attein
        #design of the global volume button
        #"+" button
        if self.screensize[0]-98 <= pyxel.mouse_x <= self.screensize[0]-93 and self.screensize[1]-54 <= pyxel.mouse_y <= self.screensize[1]-49:
            pyxel.rect(self.screensize[0]-96,self.screensize[1]-54,2,6,self.all_colours[self.mode]["settings graphics"]["clicked volume buttons color"])#vertical line of the "+"
            pyxel.rect(self.screensize[0]-98,self.screensize[1]-52,6,2,self.all_colours[self.mode]["settings graphics"]["clicked volume buttons color"])#horyzontal line of the "+"
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.global_volume<7: self.global_volume+=1
        else:
            pyxel.rect(self.screensize[0]-96,self.screensize[1]-54,2,6,self.all_colours[self.mode]["settings graphics"]["volume buttons color"])#vertical line of the "+"
            pyxel.rect(self.screensize[0]-98,self.screensize[1]-52,6,2,self.all_colours[self.mode]["settings graphics"]["volume buttons color"])#horyzontal line of the "+"
        #"-" button
        if self.screensize[0]-88 <= pyxel.mouse_x <= self.screensize[0]-85 and self.screensize[1]-52 <= pyxel.mouse_y <= self.screensize[1]-51:
            pyxel.rect(self.screensize[0]-88,self.screensize[1]-52,4,2,self.all_colours[self.mode]["settings graphics"]["clicked volume buttons color"])#line of the "-"
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.global_volume>0: self.global_volume-=1
        else:
            pyxel.rect(self.screensize[0]-88,self.screensize[1]-52,4,2,self.all_colours[self.mode]["settings graphics"]["volume buttons color"])#line of the "-"

        #music volume design
        pyxel.line(self.screensize[0]-120,self.screensize[1]-39,self.screensize[0]-120,self.screensize[1]-38,self.all_colours[self.mode]["settings graphics"]["music volume logo color"])#first part left of the 'ball' 
        pyxel.rect(self.screensize[0]-119,self.screensize[1]-40,2,4,self.all_colours[self.mode]["settings graphics"]["music volume logo color"])#major part of the 'ball'
        pyxel.line(self.screensize[0]-117,self.screensize[1]-46,self.screensize[0]-117,self.screensize[1]-38,self.all_colours[self.mode]["settings graphics"]["music volume logo color"])#principal line
        pyxel.line(self.screensize[0]-116,self.screensize[1]-45,self.screensize[0]-115,self.screensize[1]-44,self.all_colours[self.mode]["settings graphics"]["music volume logo color"])#first part of the head
        pyxel.line(self.screensize[0]-116,self.screensize[1]-44,self.screensize[0]-114,self.screensize[1]-42,self.all_colours[self.mode]["settings graphics"]["music volume logo color"])#second part of the head
        #lines of the music volume with colors changing with the actual music volume (self.music_volume)
        for x in range(self.screensize[0]-112,self.screensize[0]-112+13,2):
            pyxel.line(x,self.screensize[1]-42,x,self.screensize[1]-39,self.all_colours[self.mode]["settings graphics"]["empty volume lines color"])#music's volume lines if not attein
        for v in range(self.screensize[0]-112,self.screensize[0]-112+(2*self.music_volume),2):
            pyxel.line(v,self.screensize[1]-42,v,self.screensize[1]-39,self.all_colours[self.mode]["settings graphics"]["volume lines color"])#music's volume lines if attein
        #design of the music volume button
        #"+" button
        if self.screensize[0]-97 <= pyxel.mouse_x <= self.screensize[0]-92 and self.screensize[1]-43 <= pyxel.mouse_y <= self.screensize[1]-38:
            pyxel.rect(self.screensize[0]-95,self.screensize[1]-43,2,6,self.all_colours[self.mode]["settings graphics"]["clicked volume buttons color"])#vertical line of the "+"
            pyxel.rect(self.screensize[0]-97,self.screensize[1]-41,6,2,self.all_colours[self.mode]["settings graphics"]["clicked volume buttons color"])#horyzontal line of the "+"
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.music_volume<7: self.music_volume+=1
        else:
            pyxel.rect(self.screensize[0]-95,self.screensize[1]-43,2,6,self.all_colours[self.mode]["settings graphics"]["volume buttons color"])#vertical line of the "+"
            pyxel.rect(self.screensize[0]-97,self.screensize[1]-41,6,2,self.all_colours[self.mode]["settings graphics"]["volume buttons color"])#horyzontal line of the "+"
        #"-" button
        if self.screensize[0]-87 <= pyxel.mouse_x <= self.screensize[0]-84 and self.screensize[1]-41 <= pyxel.mouse_y <= self.screensize[1]-40:
            pyxel.rect(self.screensize[0]-87,self.screensize[1]-41,4,2,self.all_colours[self.mode]["settings graphics"]["clicked volume buttons color"])#line of the "-"
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.music_volume>0: self.music_volume-=1
        else:
            pyxel.rect(self.screensize[0]-87,self.screensize[1]-41,4,2,self.all_colours[self.mode]["settings graphics"]["volume buttons color"])#line of the "-"


    def menu_update(self):
        if self.screensize[0]-23 <= pyxel.mouse_x <= self.screensize[0]-5 and 4 <= pyxel.mouse_y <= 22 and self.mode=="snowy" and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.mode="desert"
        elif self.screensize[0]-29 <= pyxel.mouse_x <= self.screensize[0]-5 and 4 <= pyxel.mouse_y <= 28 and self.mode=="desert" and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.mode="snowy"
        if (pyxel.btnp(pyxel.KEY_SPACE) or (self.screensize[0]/2-10 <= pyxel.mouse_x <= self.screensize[0]/2+10 and self.screensize[1]/2-4 <= pyxel.mouse_y <= self.screensize[1]/2+3 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT))) and (self.in_shop==False and self.in_settings==False):
            return True
        else:
            return False


def text_border(text,x,y,borderColor,color):
    """draws text at position [x,y] of color color surrounded by a border of color borderColor. <-- Understandeable sentence

    Args:
        text (string): text to show
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