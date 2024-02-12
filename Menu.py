import pyxel
screensize=[256,128]
e=mousecol=mousex=mousey=0
#paramètres start menu :
coox=0#initial=0
cooy=int((screensize[1]-(screensize[1]/2))/2)#initial=29
width=screensize[0]-4#initial=124
height=int(screensize[1]/2)#initial=68
bgfroid=1#initial=1
colfondfroid=5#initial=5
colcontoursfroid=7#initial=7
btnfroid=3#initial=3
btncfroid=2#initial=2
bgchaud=10#initial=10
colfondchaud=9#initial=9
colcontourschaud=8#initial=8
btnchaud=10#initial=10
btncchaud=14#initial=14
colparamètres=13
colparamètresok=4
volume=3
musique=2
mode, bg, colfond, colcontours, btn, btnc, fenêtreskin, fenêtreniveaux, fenêtreparamètre="hiver", bgfroid, colfondfroid, colcontoursfroid, btnfroid, btncfroid, False, False, False
class MenuEngine:
    def __init__(self):
        pass

    def menu_update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        global pos, e, mode, bg, colfond, colcontours, bgchaud, colfondchaud, colcontourschaud, bgfroid, colfondfroid, colcontoursfroid, btn, btnc, btnfroid, btnchaud, btncfroid, btncchaud, fenêtreskin, fenêtreniveaux, fenêtreparamètre
        pos=[pyxel.mouse_x,pyxel.mouse_y]
        #Détéction clic bouton mode
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and mode=="hiver" and pos[0]>=coox+width-5 and pos[0]<=coox+width-4+3 and pos[1]>=cooy+height-7 and pos[1]<=cooy+height-3 and fenêtreniveaux==False and fenêtreparamètre==False and fenêtreskin==False:
            mode, bg, colfond, colcontours, btn, btnc="été", bgchaud, colfondchaud, colcontourschaud, btnchaud, btncchaud
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and mode=="été" and pos[0]>=coox+width-6 and pos[0]<=coox+width and pos[1]>=cooy+height-8 and pos[1]<=cooy+height-2 and fenêtreniveaux==False and fenêtreparamètre==False and fenêtreskin==False:
            mode, bg, colfond, colcontours, btn, btnc="hiver", bgfroid, colfondfroid, colcontoursfroid, btnfroid, btncfroid
        #Détection clic bouton paramètre
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pos[0]>=coox+width-7 and pos[0]<=coox+width+1 and pos[1]>=cooy+2 and pos[1]<=cooy+10:
            if fenêtreparamètre==False:fenêtreparamètre=True
            else:fenêtreparamètre=False
    def menu_draw(self):
        #self.terrain()
        #self.draw_scarf(8)
        self.start_menu()
        self.cursor()

    def cursor(self):
        global mousecol, mousex, mousey, mode, bgfroid, bgchaud
        if pos[0]!=mousex or pos[1]!=mousey:
            pyxel.pset(mousex,mousey,mousecol)
            mousecol=pyxel.pget(pos[0],pos[1])
            mousex=pos[0]
            mousey=pos[1]
        if mode=="hiver":bg=bgfroid
        else:bg=bgchaud
        pyxel.pset(pos[0],pos[1],8)
        pyxel.rect(0,0,20,20,bg)
        pyxel.text(0,0,str(pos[0]),7)
        pyxel.text(0,10,str(pos[1]),7)

    def start_menu(self):
        global mode, coox, cooy, width, height, bg, colfond, colcontours, btn, btnc
        
        #fond
        pyxel.cls(bg)

        #fond menu
        self.bg_menu()

        #contours blancs
        self.outlines_menu()
        
        #bouton start
        if fenêtreniveaux==False and fenêtreparamètre==False and fenêtreskin==False:
            start="START"
            if pos[0]>=coox+(width+2)/2-int((len(start)*3)/2+len(start)/2-1) and pos[0]<=coox+(width+2)/2+int((len(start)*3)/2+len(start)/2-1) and pos[1]>=cooy+height/2-2 and pos[1]<=cooy+height/2+3:
                self.start_button_menu(start, btnc)
            else: self.start_button_menu(start, btn)

        #bouton skin
        if fenêtreniveaux==False and fenêtreparamètre==False and fenêtreskin==False:
            skin="Skins"
            if pos[0]>=coox+4 and pos[0]<coox+4+len(skin)*3+len(skin)-1 and pos[1]>=cooy+4 and pos[1]<cooy+4+5:
                self.skin_button_menu(skin, btnc)
            else:self.skin_button_menu(skin, btn)

        #bouton niveaux
        if fenêtreniveaux==False and fenêtreparamètre==False and fenêtreskin==False:
            level="Level"
            if pos[0]>=coox+4 and pos[0]<coox+4+len(level)*3+len(level)-1 and pos[1]>=cooy+height+1-4-5 and pos[1]<cooy+height+1-4:
                self.level_button_menu(level, btnc)
            else:self.level_button_menu(level, btn)

        #bouton paramètre
        if fenêtreniveaux==False and fenêtreparamètre==False and fenêtreskin==False:
            if pos[0]>=coox+width-3-4 and pos[0]<=coox+width-3+4 and pos[1]>=cooy+6-4 and pos[1]<=cooy+6+4:
                self.settings_button_menu(btnc)
            else: self.settings_button_menu(btn)

        #bouton modes (lune pour hiver & soleil pour été)
        if fenêtreniveaux==False and fenêtreparamètre==False and fenêtreskin==False:
            if pos[0]>=coox+width-5 and pos[0]<=coox+width-4+3 and pos[1]>=cooy+height-7 and pos[1]<=cooy+height-3:
                self.mode_button_menu(mode, btnc)
            else: self.mode_button_menu(mode, btn)

        #affichage des différents paramètres
        if fenêtreparamètre==True:
            self.settings_button_menu(btnc)

            #bouton volume
            if volume !=0: self.volume_sound_settings_menu(colparamètresok)
            else: self.volume_sound_settings_menu(colparamètres)

            if volume>=1:
                pyxel.line(coox+10,cooy+5,coox+10,cooy+8,colparamètresok)
            else: pyxel.line(coox+10,cooy+5,coox+10,cooy+8,colparamètres)
            if volume>=3:
                pyxel.line(coox+12,cooy+5,coox+12,cooy+8,colparamètresok)
            else: pyxel.line(coox+12,cooy+5,coox+12,cooy+8,colparamètres)
            if volume>=5:
                pyxel.line(coox+14,cooy+5,coox+14,cooy+8,colparamètresok)
            else: pyxel.line(coox+14,cooy+5,coox+14,cooy+8,colparamètres)
            if volume==7:
                pyxel.line(coox+16,cooy+5,coox+16,cooy+8,colparamètresok)
            else: pyxel.line(coox+16,cooy+5,coox+16,cooy+8,colparamètres)

            #bouton musique
            if musique!=0: self.volume_music_settings_menu(colparamètresok)
            else: self.volume_music_settings_menu(colparamètres)

            if musique>=1:
                pyxel.line(coox+10,cooy+16,10,cooy+19,colparamètresok)
            else: pyxel.line(coox+10,cooy+16,10,cooy+19,colparamètres)
            if musique>=3:
                pyxel.line(coox+12,cooy+16,12,cooy+19,colparamètresok)
            else: pyxel.line(coox+12,cooy+16,12,cooy+19,colparamètres)
            if musique>=5:
                pyxel.line(coox+14,cooy+16,14,cooy+19,colparamètresok)
            else: pyxel.line(coox+14,cooy+16,14,cooy+19,colparamètres)
            if musique==7:
                pyxel.line(coox+16,cooy+16,16,cooy+19,colparamètresok)
            else: pyxel.line(coox+16,cooy+16,16,cooy+19,colparamètres)


        

    def bg_menu(self):
        pyxel.rect(coox+2, cooy+1, width, height,colfond)#rectangle principal
        pyxel.line(coox+1,cooy+2,coox+1,cooy-1+height,colfond)#ligne gauche
        pyxel.line(coox+2+width,cooy+2,coox+2+width,cooy-1+height,colfond)#ligne droite

    def outlines_menu(self):
        pyxel.line(coox+2,cooy,coox+width+1,cooy,colcontours)#ligne haut
        pyxel.line(coox+2,cooy+1+height,coox+width+1,cooy+1+height,colcontours)#ligne bas
        pyxel.line(coox,cooy+2,coox,cooy+height-1,colcontours)#ligne gauche
        pyxel.line(coox+3+width,cooy+2,coox+3+width,cooy+height-1,colcontours)#ligne droite
        pyxel.pset(coox+1,cooy+1,colcontours)#coin supérieur gauche
        pyxel.pset(coox+2+width,cooy+1,colcontours)#coin supérieur droit
        pyxel.pset(coox+1,cooy+height,colcontours)#coin inférieur gauche
        pyxel.pset(coox+2+width,cooy+height,colcontours)#coin inférieur droit

    def start_button_menu(self, text, col):
        pyxel.text(coox+(width+2)/2-int((len(text)*3)/2+len(text)/2-1),cooy+height/2-2,text,col)
    
    def skin_button_menu(self, text, col):
        pyxel.text(coox+4,cooy+4,text,col)
    
    def level_button_menu(self, text, col):
        pyxel.text(coox+4,cooy+height+1-4-5,text,col)
    
    def settings_button_menu(self, col):
            pyxel.circb(coox+width-3,cooy+6,2,col)
            pyxel.circb(coox+width-3,cooy+6,4,col)
    
    def mode_button_menu(self, mode, col):
        if mode=="hiver":
            pyxel.line(coox+width-4,cooy+height-3,coox+width-4+3,cooy+height-3,col)
            pyxel.line(coox+width-5,cooy+height-7,coox+width-5,cooy+height-4,col)
            pyxel.pset(coox+width-4,cooy+height-5,col)
            pyxel.pset(coox+width-4,cooy+height-4,col)
            pyxel.pset(coox+width-3,cooy+height-4,col)
        else:
            pyxel.rect(coox+width-5,cooy+height-7,5,5,col)
            pyxel.line(coox+width-7,cooy+height-5,coox+width-6,cooy+height-5,col)
            pyxel.line(coox+width,cooy+height-5,coox+width+1,cooy+height-5,col)
            pyxel.line(coox+width-3,cooy+height-9,coox+width-3,cooy+height-8,col)
            pyxel.line(coox+width-3,cooy+height-2,coox+width-3,cooy+height-1,col)
            pyxel.line(coox+width-5,cooy+height-7,coox+width-6,cooy+height-8,col)
            pyxel.line(coox+width-1,cooy+height-7,coox+width,cooy+height-8,col)
            pyxel.line(coox+width-5,cooy+height-3,coox+width-6,cooy+height-2,col)
            pyxel.line(coox+width-1,cooy+height-3,coox+width,cooy+height-2,col)
    
    def volume_sound_settings_menu(self, col):
        pyxel.rect(coox+5,cooy+5,2,4,col)
        pyxel.line(coox+7,cooy+4,coox+7,cooy+9,col)
        pyxel.line(coox+8,cooy+3,coox+8,cooy+10,col)

    def volume_music_settings_menu(self, col):
        pyxel.line(coox+2,cooy+19,coox+2,cooy+20,col)
        pyxel.rect(coox+3,cooy+18,2,4,col)
        pyxel.line(coox+5,cooy+20,coox+5,cooy+12,col)
        pyxel.line(coox+6,cooy+13,coox+7,cooy+14,col)
        pyxel.line(coox+6,cooy+14,coox+8,cooy+16,col)
