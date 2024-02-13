import pyxel

class MenuEngine:
    def __init__(self):
        self.screensize=[256,128]
        self.mousecol, self.mousex, self.mousey=0, 0, 0
        #paramètres start menu :
        self.coox=0#initial=0
        self.cooy=int((self.screensize[1]-(self.screensize[1]/2))/2)#initial=29
        self.width=self.screensize[0]-4#initial=124
        self.height=int(self.screensize[1]/2)#initial=68
        self.bgfroid=1#initial=1
        self.colfondfroid=5#initial=5
        self.colcontoursfroid=7#initial=7
        self.btnfroid=3#initial=3
        self.btncfroid=2#initial=2
        self.bgchaud=10#initial=10
        self.colfondchaud=9#initial=9
        self.colcontourschaud=8#initial=8
        self.btnchaud=10#initial=10
        self.btncchaud=14#initial=14
        self.colparamètres=13
        self.colparamètresok=4
        self.volume=3
        self.musique=2
        self.mode, self.bg, self.colfond, self.colcontours, self.btn, self.btnc, self.fenêtreskin, self.fenêtreniveaux, self.fenêtreparamètre="hiver", self.bgfroid, self.colfondfroid, self.colcontoursfroid, self.btnfroid, self.btncfroid, False, False, False

    def menu_update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.pos=[pyxel.mouse_x,pyxel.mouse_y]
        #Détéction clic bouton self.mode
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.mode=="hiver" and self.pos[0]>=self.coox+self.width-5 and self.pos[0]<=self.coox+self.width-4+3 and self.pos[1]>=self.cooy+self.height-7 and self.pos[1]<=self.cooy+self.height-3 and self.fenêtreniveaux==False and self.fenêtreparamètre==False and self.fenêtreskin==False:
            self.mode, self.bg, self.colfond, self.colcontours, self.btn, self.btnc="été", self.bgchaud, self.colfondchaud, self.colcontourschaud, self.btnchaud, self.btncchaud
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.mode=="été" and self.pos[0]>=self.coox+self.width-6 and self.pos[0]<=self.coox+self.width and self.pos[1]>=self.cooy+self.height-8 and self.pos[1]<=self.cooy+self.height-2 and self.fenêtreniveaux==False and self.fenêtreparamètre==False and self.fenêtreskin==False:
            self.mode, self.bg, self.colfond, self.colcontours, self.btn, self.btnc="hiver", self.bgfroid, self.colfondfroid, self.colcontoursfroid, self.btnfroid, self.btncfroid
        #Détection clic bouton paramètre
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.pos[0]>=self.coox+self.width-7 and self.pos[0]<=self.coox+self.width+1 and self.pos[1]>=self.cooy+2 and self.pos[1]<=self.cooy+10:
            if self.fenêtreparamètre==False:self.fenêtreparamètre=True
            else:self.fenêtreparamètre=False
    def menu_draw(self):
        #self.terrain()
        #self.draw_scarf(8)
        self.start_menu()
        self.cursor()

    def cursor(self):
        if self.pos[0]!=self.mousex or self.pos[1]!=self.mousey:
            pyxel.pset(self.mousex,self.mousey,self.mousecol)
            self.mousecol=pyxel.pget(self.pos[0],self.pos[1])
            self.mousex=self.pos[0]
            self.mousey=self.pos[1]
        if self.mode=="hiver":self.bg=self.bgfroid
        else:self.bg=self.bgchaud
        pyxel.pset(self.pos[0],self.pos[1],8)
        pyxel.rect(0,0,20,20,self.bg)
        pyxel.text(0,0,str(self.pos[0]),7)
        pyxel.text(0,10,str(self.pos[1]),7)

    def start_menu(self):        
        #fond
        pyxel.cls(self.bg)

        #fond menu
        self.bg_menu()

        #contours blancs
        self.outlines_menu()
        
        #bouton start
        if self.fenêtreniveaux==False and self.fenêtreparamètre==False and self.fenêtreskin==False:
            start="START"
            if self.pos[0]>=self.coox+(self.width+2)/2-int((len(start)*3)/2+len(start)/2-1) and self.pos[0]<=self.coox+(self.width+2)/2+int((len(start)*3)/2+len(start)/2-1) and self.pos[1]>=self.cooy+self.height/2-2 and self.pos[1]<=self.cooy+self.height/2+3:
                self.start_button_menu(start, self.btnc)
            else: self.start_button_menu(start, self.btn)

        #bouton skin
        if self.fenêtreniveaux==False and self.fenêtreparamètre==False and self.fenêtreskin==False:
            skin="Skins"
            if self.pos[0]>=self.coox+4 and self.pos[0]<self.coox+4+len(skin)*3+len(skin)-1 and self.pos[1]>=self.cooy+4 and self.pos[1]<self.cooy+4+5:
                self.skin_button_menu(skin, self.btnc)
            else:self.skin_button_menu(skin, self.btn)

        #bouton niveaux
        if self.fenêtreniveaux==False and self.fenêtreparamètre==False and self.fenêtreskin==False:
            level="Level"
            if self.pos[0]>=self.coox+4 and self.pos[0]<self.coox+4+len(level)*3+len(level)-1 and self.pos[1]>=self.cooy+self.height+1-4-5 and self.pos[1]<self.cooy+self.height+1-4:
                self.level_button_menu(level, self.btnc)
            else:self.level_button_menu(level, self.btn)

        #bouton paramètre
        if self.fenêtreniveaux==False and self.fenêtreparamètre==False and self.fenêtreskin==False:
            if self.pos[0]>=self.coox+self.width-3-4 and self.pos[0]<=self.coox+self.width-3+4 and self.pos[1]>=self.cooy+6-4 and self.pos[1]<=self.cooy+6+4:
                self.settings_button_menu(self.btnc)
            else: self.settings_button_menu(self.btn)

        #bouton modes (lune pour hiver & soleil pour été)
        if self.fenêtreniveaux==False and self.fenêtreparamètre==False and self.fenêtreskin==False:
            if self.pos[0]>=self.coox+self.width-5 and self.pos[0]<=self.coox+self.width-4+3 and self.pos[1]>=self.cooy+self.height-7 and self.pos[1]<=self.cooy+self.height-3:
                self.mode_button_menu(self.mode, self.btnc)
            else: self.mode_button_menu(self.mode, self.btn)

        #affichage des différents paramètres
        if self.fenêtreparamètre==True:
            self.settings_button_menu(self.btnc)

            #bouton self.volume
            if self.volume !=0: self.volume_sound_settings_menu(self.colparamètresok)
            else: self.volume_sound_settings_menu(self.colparamètres)

            if self.volume>=1:
                pyxel.line(self.coox+10,self.cooy+5,self.coox+10,self.cooy+8,self.colparamètresok)
            else: pyxel.line(self.coox+10,self.cooy+5,self.coox+10,self.cooy+8,self.colparamètres)
            if self.volume>=3:
                pyxel.line(self.coox+12,self.cooy+5,self.coox+12,self.cooy+8,self.colparamètresok)
            else: pyxel.line(self.coox+12,self.cooy+5,self.coox+12,self.cooy+8,self.colparamètres)
            if self.volume>=5:
                pyxel.line(self.coox+14,self.cooy+5,self.coox+14,self.cooy+8,self.colparamètresok)
            else: pyxel.line(self.coox+14,self.cooy+5,self.coox+14,self.cooy+8,self.colparamètres)
            if self.volume==7:
                pyxel.line(self.coox+16,self.cooy+5,self.coox+16,self.cooy+8,self.colparamètresok)
            else: pyxel.line(self.coox+16,self.cooy+5,self.coox+16,self.cooy+8,self.colparamètres)

            #bouton self.musique
            if self.musique!=0: self.volume_music_settings_menu(self.colparamètresok)
            else: self.volume_music_settings_menu(self.colparamètres)

            if self.musique>=1:
                pyxel.line(self.coox+10,self.cooy+16,10,self.cooy+19,self.colparamètresok)
            else: pyxel.line(self.coox+10,self.cooy+16,10,self.cooy+19,self.colparamètres)
            if self.musique>=3:
                pyxel.line(self.coox+12,self.cooy+16,12,self.cooy+19,self.colparamètresok)
            else: pyxel.line(self.coox+12,self.cooy+16,12,self.cooy+19,self.colparamètres)
            if self.musique>=5:
                pyxel.line(self.coox+14,self.cooy+16,14,self.cooy+19,self.colparamètresok)
            else: pyxel.line(self.coox+14,self.cooy+16,14,self.cooy+19,self.colparamètres)
            if self.musique==7:
                pyxel.line(self.coox+16,self.cooy+16,16,self.cooy+19,self.colparamètresok)
            else: pyxel.line(self.coox+16,self.cooy+16,16,self.cooy+19,self.colparamètres)


        

    def bg_menu(self):
        pyxel.rect(self.coox+2, self.cooy+1, self.width, self.height,self.colfond)#rectangle principal
        pyxel.line(self.coox+1,self.cooy+2,self.coox+1,self.cooy-1+self.height,self.colfond)#ligne gauche
        pyxel.line(self.coox+2+self.width,self.cooy+2,self.coox+2+self.width,self.cooy-1+self.height,self.colfond)#ligne droite

    def outlines_menu(self):
        pyxel.line(self.coox+2,self.cooy,self.coox+self.width+1,self.cooy,self.colcontours)#ligne haut
        pyxel.line(self.coox+2,self.cooy+1+self.height,self.coox+self.width+1,self.cooy+1+self.height,self.colcontours)#ligne bas
        pyxel.line(self.coox,self.cooy+2,self.coox,self.cooy+self.height-1,self.colcontours)#ligne gauche
        pyxel.line(self.coox+3+self.width,self.cooy+2,self.coox+3+self.width,self.cooy+self.height-1,self.colcontours)#ligne droite
        pyxel.pset(self.coox+1,self.cooy+1,self.colcontours)#coin supérieur gauche
        pyxel.pset(self.coox+2+self.width,self.cooy+1,self.colcontours)#coin supérieur droit
        pyxel.pset(self.coox+1,self.cooy+self.height,self.colcontours)#coin inférieur gauche
        pyxel.pset(self.coox+2+self.width,self.cooy+self.height,self.colcontours)#coin inférieur droit

    def start_button_menu(self, text, col):
        pyxel.text(self.coox+(self.width+2)/2-int((len(text)*3)/2+len(text)/2-1),self.cooy+self.height/2-2,text,col)
    
    def skin_button_menu(self, text, col):
        pyxel.text(self.coox+4,self.cooy+4,text,col)
    
    def level_button_menu(self, text, col):
        pyxel.text(self.coox+4,self.cooy+self.height+1-4-5,text,col)
    
    def settings_button_menu(self, col):
            pyxel.circb(self.coox+self.width-3,self.cooy+6,2,col)
            pyxel.circb(self.coox+self.width-3,self.cooy+6,4,col)
    
    def mode_button_menu(self, mode, col):
        if self.mode=="hiver":
            pyxel.line(self.coox+self.width-4,self.cooy+self.height-3,self.coox+self.width-4+3,self.cooy+self.height-3,col)
            pyxel.line(self.coox+self.width-5,self.cooy+self.height-7,self.coox+self.width-5,self.cooy+self.height-4,col)
            pyxel.pset(self.coox+self.width-4,self.cooy+self.height-5,col)
            pyxel.pset(self.coox+self.width-4,self.cooy+self.height-4,col)
            pyxel.pset(self.coox+self.width-3,self.cooy+self.height-4,col)
        else:
            pyxel.rect(self.coox+self.width-5,self.cooy+self.height-7,5,5,col)
            pyxel.line(self.coox+self.width-7,self.cooy+self.height-5,self.coox+self.width-6,self.cooy+self.height-5,col)
            pyxel.line(self.coox+self.width,self.cooy+self.height-5,self.coox+self.width+1,self.cooy+self.height-5,col)
            pyxel.line(self.coox+self.width-3,self.cooy+self.height-9,self.coox+self.width-3,self.cooy+self.height-8,col)
            pyxel.line(self.coox+self.width-3,self.cooy+self.height-2,self.coox+self.width-3,self.cooy+self.height-1,col)
            pyxel.line(self.coox+self.width-5,self.cooy+self.height-7,self.coox+self.width-6,self.cooy+self.height-8,col)
            pyxel.line(self.coox+self.width-1,self.cooy+self.height-7,self.coox+self.width,self.cooy+self.height-8,col)
            pyxel.line(self.coox+self.width-5,self.cooy+self.height-3,self.coox+self.width-6,self.cooy+self.height-2,col)
            pyxel.line(self.coox+self.width-1,self.cooy+self.height-3,self.coox+self.width,self.cooy+self.height-2,col)
    
    def volume_sound_settings_menu(self, col):
        pyxel.rect(self.coox+5,self.cooy+5,2,4,col)
        pyxel.line(self.coox+7,self.cooy+4,self.coox+7,self.cooy+9,col)
        pyxel.line(self.coox+8,self.cooy+3,self.coox+8,self.cooy+10,col)

    def volume_music_settings_menu(self, col):
        pyxel.line(self.coox+2,self.cooy+19,self.coox+2,self.cooy+20,col)
        pyxel.rect(self.coox+3,self.cooy+18,2,4,col)
        pyxel.line(self.coox+5,self.cooy+20,self.coox+5,self.cooy+12,col)
        pyxel.line(self.coox+6,self.cooy+13,self.coox+7,self.cooy+14,col)
        pyxel.line(self.coox+6,self.cooy+14,self.coox+8,self.cooy+16,col)
