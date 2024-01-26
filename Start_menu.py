import pyxel
e=mousecol=mousex=mousey=0
#paramètres start menu :
coox=0#initial=0
cooy=29#initial=29
width=124#initial=124
height=68#initial=68
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
mode, bg, colfond, colcontours, btn, btnc, fenêtreskin, fenêtreniveaux, fenêtreparamètre, volumemusic, volumesons="hiver", bgfroid, colfondfroid, colcontoursfroid, btnfroid, btncfroid, False, False, False, 3, 3
class Game:
    def __init__(self):
        pyxel.init(128, 128)
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


    def draw_scarf(self,col1):
        global pos,e
        e=min(e+pyxel.rndi(0,1),3)
        e=max(e-pyxel.rndi(0,1),-3)
        spos=[pos[0]+pyxel.rndi(-5,-8),pos[1]+e]
        pyxel.line(pos[0],pos[1],spos[0],spos[1],col1)
        
    def terrain(self):
        ppos=[0,10]
        p0=0
        r=0
        pn=0
        while pn<1280:
            ppos[0]+=1
            if ppos[0]>=pn:  
                n=rndi(100,500)
                p1=p0+r
                r=rndi(10,100)
                p0=p1+r
                for x in range(n):
                    ppos[0]+=1 
                    s=(p0-p1)*cos(x/(n/pi))
                    y=p0-s+30
                    pyxel.rect(int((x+pn)/10),int(y/10),1,50,1)
                pn+=n
    
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
        
        pyxel.rect(0,0,128,128,bg)#fond
        #fond menu
        pyxel.rect(coox+2, cooy+1, width, height,colfond)
        pyxel.line(coox+1,cooy+2,coox+1,cooy-1+height,colfond)#ligne gauche
        pyxel.line(coox+2+width,cooy+2,coox+2+width,cooy-1+height,colfond)#ligne droite
        #contours blancs
        pyxel.line(coox+2,cooy,coox+width+1,cooy,colcontours)#ligne haut
        pyxel.line(coox+2,cooy+1+height,coox+width+1,cooy+1+height,colcontours)#ligne bas
        pyxel.line(coox,cooy+2,coox,cooy+height-1,colcontours)#ligne gauche
        pyxel.line(coox+3+width,cooy+2,coox+3+width,cooy+height-1,colcontours)#ligne droite
        pyxel.pset(coox+1,cooy+1,colcontours)#coin supérieur gauche
        pyxel.pset(coox+2+width,cooy+1,colcontours)#coin supérieur droit
        pyxel.pset(coox+1,cooy+height,colcontours)#coin inférieur gauche
        pyxel.pset(coox+2+width,cooy+height,colcontours)#coin inférieur droit
        
        #bouton start
        #graphique + détection de la souris
        if fenêtreskin==False and fenêtreniveaux==False and fenêtreparamètre==False:
            start="START"
            if pos[0]>=coox+(width+2)/2-int((len(start)*3)/2+len(start)/2-1) and pos[0]<=coox+(width+2)/2+int((len(start)*3)/2+len(start)/2-1) and pos[1]>=cooy+height/2-2 and pos[1]<=cooy+height/2+3:
                pyxel.text(coox+(width+2)/2-int((len(start)*3)/2+len(start)/2-1),cooy+height/2-2,start,btnc)
            else:
                pyxel.text(coox+(width+2)/2-int((len(start)*3)/2+len(start)/2-1),cooy+height/2-2,start,btn)

        #bouton perso
        #graphique + détection de la souris
        if fenêtreniveaux==False and fenêtreparamètre==False:
            shop="Skins"
            if pos[0]>=coox+4 and pos[0]<coox+4+len(shop)*3+len(shop)-1 and pos[1]>=cooy+4 and pos[1]<cooy+4+5:
                pyxel.text(coox+4,cooy+4,shop,btnc)
            else:
                pyxel.text(coox+4,cooy+4,shop,btn)

        #bouton niveaux
        #graphique + détection de la souris
        if fenêtreskin==False and fenêtreparamètre==False:
            niveaux="Niveaux"
            if pos[0]>=coox+4 and pos[0]<coox+4+len(niveaux)*3+len(niveaux)-1 and pos[1]>=cooy+height+1-4-5 and pos[1]<cooy+height+1-4:
                pyxel.text(coox+4,cooy+height+1-4-5,niveaux,btnc)
            else:
                pyxel.text(coox+4,cooy+height+1-4-5,niveaux,btn)

        #bouton paramètre
        #graphique + détection de la souris
        if fenêtreskin==False and fenêtreniveaux==False:
            if pos[0]>=coox+width-3-4 and pos[0]<=coox+width-3+4 and pos[1]>=cooy+6-4 and pos[1]<=cooy+6+4:
                pyxel.circb(coox+width-3,cooy+6,2,btnc)
                pyxel.circb(coox+width-3,cooy+6,4,btnc)
            else:
                pyxel.circb(coox+width-3,cooy+6,2,btn)
                pyxel.circb(coox+width-3,cooy+6,4,btn)
            #affichage des différents paramètres
            if fenêtreparamètre==True:
                #bouton volume
                pyxel.rect(coox+4,cooy+5,2,4,13)
                pyxel.line(coox+6,cooy+4,coox+6,cooy+9,colparamètres)
                pyxel.line(coox+7,cooy+3,coox+7,cooy+10,colparamètres)
                pyxel.line(coox+9,cooy+5,coox+9,cooy+8,colparamètres)
                pyxel.line(coox+11,cooy+5,coox+11,cooy+8,colparamètres)
                pyxel.line(coox+13,cooy+5,coox+13,cooy+8,colparamètres)
                pyxel.line(coox+15,cooy+5,coox+15,cooy+8,colparamètres)
                #bouton musique
                pyxel.circ(5,42,2,colparamètres)


        #bouton modes (lune pour hiver & soleil pour été)
        if fenêtreskin==False and fenêtreniveaux==False and fenêtreparamètre==False:
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

        
        

Game()
