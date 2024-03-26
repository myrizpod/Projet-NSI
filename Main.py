from Game import *
from Menu import *
import pyxel
import Save
#Global variables

class App:
    

    def __init__(self):
        global game,menu
        self.p_inGame=False
        self.inGame=False
        self.total_coins=0
        self.best_score=0
        self.unlocked_items=[[],[],[]]
        self.screen_size=[256,128]
        pyxel.init(self.screen_size[0], self.screen_size[1],"Ski Game",30)
        pyxel.load("textures.pyxres")
        #wierd place to initialise game and menu but needed otherwise pyxel gets mad
        game=GameEngine(self.screen_size,show_player=False,pieces=self.total_coins) 
        menu=MenuEngine()
        Save.load()
        pyxel.run(self.update, self.draw)

    def draw(self):
        global game,menu
        #choose wether or not menu should be shown
        game.game_draw()
        if not self.inGame:
            menu.menu_draw()  

    def update(self):
        global menu,game
        #switch between runing the menu and the game
        if self.p_inGame==False and self.inGame==True:
            game.__init__(self.screen_size,show_player=True)
        self.p_inGame=self.inGame
        


        #used properly quit the game (gonna use it for save files)
        if pyxel.btnp(pyxel.KEY_Q):
            print("Quitting")
            self.total_coins+=game.getstats()[0]
            self.best_score=game.getstats()[1] if game.getstats()[1]>self.best_score else self.best_score
            Save.save(self.best_score,self.total_coins,self.unlocked_items)
            pyxel.quit()

        if self.inGame:
            game.game_update()
        else:
            self.inGame=menu.menu_update()
        
App()