from Game import *
from Menu import *
import pyxel
import Save
import music
#Global variables

class App:

    def __init__(self):
        global game
        self.p_inGame=False
        self.inGame=False
        tmp=Save.load()
        self.mode="snowy"
        music.play_music(2)
        self.total_coins=int(tmp["coins"])
        self.best_score=int(tmp["best_score"])
        tmp=tmp["unlocked_items"][1:-1].split(",")#Selection of the list (trunc to get the useful part) with the unlocked items and split it
        self.unlocked_items=[False if x==" False" else True for x in tmp]#Conversion of the str elements in tmp to boolean to get used after in the menu file
        self.screen_size=[256,128]
        pyxel.init(self.screen_size[0], self.screen_size[1],"Ski Game",30)
        pyxel.load("textures.pyxres")
        #wierd place to initialise game and menu but needed otherwise pyxel gets mad
        self.menu=MenuEngine(self)
        game=GameEngine(self.screen_size,self,not_in_menu=False) 
        pyxel.run(self.update, self.draw)  

    def draw(self):
        
        #choose wether or not menu should be shown
        game.game_draw()
        if not self.inGame:
            self.menu.menu_draw()

    def update(self):
        global game
        #switch between runing the menu and the game
        if self.p_inGame==False and self.inGame==True:
            self.mode=self.menu.mode
            effects=[]
            for i in range(len(self.menu.cases_shop)):
                if self.menu.cases_shop[i][0]==self.menu.selected_skin or self.menu.cases_shop[i][0]==self.menu.selected_ski:
                    effects+=self.menu.cases_shop[i][3].split("/")
                if self.menu.cases_shop[i][0]==self.menu.selected_object:
                    effects.append(self.menu.cases_shop[i][0])
            print(effects)
            game.__init__(self.screen_size,self,skin=self.menu.selected_skin,scarf=self.menu.selected_scarf,ski=self.menu.selected_ski,theme=self.mode,effects=effects,not_in_menu=True)
        self.p_inGame=self.inGame

        #used properly quit the game (gonna use it for save files)
        if pyxel.btnp(pyxel.KEY_Q):
            print("Quitting")
            Save.save(self.best_score,self.total_coins,self.unlocked_items)
            Save.load()
            pyxel.quit()

        if self.inGame:
            game.game_update()
        else:
            self.inGame=self.menu.menu_update()
            self.mode=self.menu.mode
            game.theme=self.menu.mode
            game.colors=game.global_colors[self.mode]


App()
