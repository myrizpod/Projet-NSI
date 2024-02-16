from Game import *
from Menu import *
import pyxel
import Save
#Global variables
inGame=False
total_coins=0
best_score=0
unlocked_items=[[],[],[]]
screen_size=[256,128]
class App:
    global game,menu
    def __init__(self):
        global game,menu,screen_size
        pyxel.init(screen_size[0], screen_size[1],"Ski Game",30)
        pyxel.load("textures.pyxres")
        #wierd place to initialise game and menu but needed otherwise pyxel gets mad
        game=GameEngine()
        menu=MenuEngine()
        Save.load()
        pyxel.run(self.update, self.draw)

    def draw(self):
        #choose wether or not menu should be shown
        global inGame,menu,game
        game.game_draw()
        if not inGame:
            menu.menu_draw()   

    def update(self):
        
        #switch between runing the menu and the game
        global inGame,menu,game


        #used properly quit the game (gonna use it for save files)
        if pyxel.btnp(pyxel.KEY_Q):
            print("Quitting")
            Save.save()
            pyxel.quit()

        if inGame:
            game.game_update()
        else:
            inGame=menu.menu_update()
        
App()