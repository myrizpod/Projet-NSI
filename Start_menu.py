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
volume=3
musique=2
mode, bg, colfond, colcontours, btn, btnc, fenêtreskin, fenêtreniveaux, fenêtreparamètre, volumemusic, volumesons="hiver", bgfroid, colfondfroid, colcontoursfroid, btnfroid, btncfroid, False, False, False, 3, 3
class Game:
    def __init__(self):
        pyxel.init(screensize[0], screensize[1])
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        global pos, e, mode, bg, colfond, colcontours, bgchaud, colfondchaud, colcontourschaud, bgfroid, colfondfroid, colcontoursfroid, btn, btnc, btnfroid, btnchaud, btncfroid, btncchaud, fenêtreskin, fenêtreniveaux, fenêtreparamètre
        pos=[pyxel.mouse_x,pyxel.mouse_y]
        #Détéction clic bouton mode
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and mode=="hiver" and pos[0]>=coox+width-5 and pos[0]<=coox+width-4+3 and pos[1]>=cooy+height-7 and pos[1]<=cooy+height-3:
            mode, bg, colfond, colcontours, btn, btnc="été", bgchaud, colfondchaud, colcontourschaud, btnchaud, btncchaud
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and mode=="été" and pos[0]>=coox+width-6 and pos[0]<=coox+width and pos[1]>=cooy+height-8 and pos[1]<=cooy+height-2:
            mode, bg, colfond, colcontours, btn, btnc="hiver", bgfroid, colfondfroid, colcontoursfroid, btnfroid, btncfroid
        #Détection clic bouton paramètre
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pos[0]>=coox+width-7 and pos[0]<=coox+width+1 and pos[1]>=cooy+2 and pos[1]<=cooy+10:
            if fenêtreparamètre==False:
                fenêtreparamètre=True
            else:fenêtreparamètre=False
    def draw(self):
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
        
        pyxel.cls(bg)#fond
        #fond menu
        self.bg_menu()
        #contours blancs
        self.outlines_menu()
        
        #bouton start
        self.start_button_menu()

        #bouton skin
        self.skin_button_menu()

        #bouton niveaux
        self.level_button_menu()

        #bouton paramètre
        #graphique + détection de la souris
        if fenêtreskin==False and fenêtreniveaux==False:
            self.settings_button_menu()
            #affichage des différents paramètres
            if fenêtreparamètre==True:
                #bouton volume
                self.volume_sound_settings_menu()
                
                pyxel.line(coox+10,cooy+5,coox+10,cooy+8,colparamètres)
                pyxel.line(coox+12,cooy+5,coox+12,cooy+8,colparamètres)
                pyxel.line(coox+14,cooy+5,coox+14,cooy+8,colparamètres)
                pyxel.line(coox+16,cooy+5,coox+16,cooy+8,colparamètres)
                #bouton musique
                self.volume_music_settings_menu()

                pyxel.line(10,45,10,48,colparamètres)
                pyxel.line(12,45,12,48,colparamètres)
                pyxel.line(14,45,14,48,colparamètres)
                pyxel.line(16,45,16,48,colparamètres)


        #bouton modes (lune pour hiver & soleil pour été)
        if fenêtreskin==False and fenêtreniveaux==False and fenêtreparamètre==False:
            self.mode_button_menu()

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

    def start_button_menu(self):
        start="START"
        if pos[0]>=coox+(width+2)/2-int((len(start)*3)/2+len(start)/2-1) and pos[0]<=coox+(width+2)/2+int((len(start)*3)/2+len(start)/2-1) and pos[1]>=cooy+height/2-2 and pos[1]<=cooy+height/2+3:
            pyxel.text(coox+(width+2)/2-int((len(start)*3)/2+len(start)/2-1),cooy+height/2-2,start,btnc)
        else:pyxel.text(coox+(width+2)/2-int((len(start)*3)/2+len(start)/2-1),cooy+height/2-2,start,btn)
    
    def skin_button_menu(self):
        skin="Skins"
        if pos[0]>=coox+4 and pos[0]<coox+4+len(skin)*3+len(skin)-1 and pos[1]>=cooy+4 and pos[1]<cooy+4+5:
            pyxel.text(coox+4,cooy+4,skin,btnc)
        else: pyxel.text(coox+4,cooy+4,skin,btn)
    
    def level_button_menu(self):
        level="Level"
        if pos[0]>=coox+4 and pos[0]<coox+4+len(level)*3+len(level)-1 and pos[1]>=cooy+height+1-4-5 and pos[1]<cooy+height+1-4:
            pyxel.text(coox+4,cooy+height+1-4-5,level,btnc)
        else:pyxel.text(coox+4,cooy+height+1-4-5,level,btn)
    
    def settings_button_menu(self):
        if pos[0]>=coox+width-3-4 and pos[0]<=coox+width-3+4 and pos[1]>=cooy+6-4 and pos[1]<=cooy+6+4:
            pyxel.circb(coox+width-3,cooy+6,2,btnc)
            pyxel.circb(coox+width-3,cooy+6,4,btnc)
        else:
            pyxel.circb(coox+width-3,cooy+6,2,btn)
            pyxel.circb(coox+width-3,cooy+6,4,btn)
    
    def mode_button_menu(self):
        if mode=="hiver":
            if pos[0]>=coox+width-5 and pos[0]<=coox+width-4+3 and pos[1]>=cooy+height-7 and pos[1]<=cooy+height-3:
                pyxel.line(coox+width-4,cooy+height-3,coox+width-4+3,cooy+height-3,btnc)
                pyxel.line(coox+width-5,cooy+height-7,coox+width-5,cooy+height-4,btnc)
                pyxel.pset(coox+width-4,cooy+height-5,btnc)
                pyxel.pset(coox+width-4,cooy+height-4,btnc)
                pyxel.pset(coox+width-3,cooy+height-4,btnc)
            else:
                pyxel.line(coox+width-4,cooy+height-3,coox+width-4+3,cooy+height-3,btn)
                pyxel.line(coox+width-5,cooy+height-7,coox+width-5,cooy+height-4,btn)
                pyxel.pset(coox+width-4,cooy+height-5,btn)
                pyxel.pset(coox+width-4,cooy+height-4,btn)
                pyxel.pset(coox+width-3,cooy+height-4,btn)
        else:
            if pos[0]>=coox+width-6 and pos[0]<=coox+width and pos[1]>=cooy+height-8 and pos[1]<=cooy+height-2:
                pyxel.rect(coox+width-5,cooy+height-7,5,5,btnc)
                pyxel.line(coox+width-7,cooy+height-5,coox+width-6,cooy+height-5,btnc)
                pyxel.line(coox+width,cooy+height-5,coox+width+1,cooy+height-5,btnc)
                pyxel.line(coox+width-3,cooy+height-9,coox+width-3,cooy+height-8,btnc)
                pyxel.line(coox+width-3,cooy+height-2,coox+width-3,cooy+height-1,btnc)
                pyxel.line(coox+width-5,cooy+height-7,coox+width-6,cooy+height-8,btnc)
                pyxel.line(coox+width-1,cooy+height-7,coox+width,cooy+height-8,btnc)
                pyxel.line(coox+width-5,cooy+height-3,coox+width-6,cooy+height-2,btnc)
                pyxel.line(coox+width-1,cooy+height-3,coox+width,cooy+height-2,btnc)
            else:
                pyxel.rect(coox+width-5,cooy+height-7,5,5,10)
                pyxel.line(coox+width-7,cooy+height-5,coox+width-6,cooy+height-5,9)
                pyxel.line(coox+width,cooy+height-5,coox+width+1,cooy+height-5,9)
                pyxel.line(coox+width-3,cooy+height-9,coox+width-3,cooy+height-8,9)
                pyxel.line(coox+width-3,cooy+height-2,coox+width-3,cooy+height-1,9)
                pyxel.line(coox+width-5,cooy+height-7,coox+width-6,cooy+height-8,9)
                pyxel.line(coox+width-1,cooy+height-7,coox+width,cooy+height-8,9)
                pyxel.line(coox+width-5,cooy+height-3,coox+width-6,cooy+height-2,9)
                pyxel.line(coox+width-1,cooy+height-3,coox+width,cooy+height-2,9)
    
    def volume_sound_settings_menu(self):
        pyxel.rect(coox+5,cooy+5,2,4,13)
        pyxel.line(coox+7,cooy+4,coox+7,cooy+9,colparamètres)
        pyxel.line(coox+8,cooy+3,coox+8,cooy+10,colparamètres)

    def volume_music_settings_menu(self):
        pyxel.line(2,48,2,49,colparamètres)
        pyxel.rect(3,47,2,4,colparamètres)
        pyxel.line(5,49,5,41,colparamètres)
        pyxel.line(6,42,7,43,colparamètres)
        pyxel.line(6,43,8,45,colparamètres)

Game()
