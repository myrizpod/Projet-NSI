from Game import *
from Menu import *
import pyxel

#Global variables
inGame=False


class App:
    global game,menu
    def __init__(self):
        global game,menu
        #initializing game window (yes screen_size should be shared between all parts of the code. but i cant find a way to do it)
        self.screen_size=[256,128]
        pyxel.init(self.screen_size[0], self.screen_size[1],"Ski Game",30)
        pyxel.load("textures.pyxres")
        #wierd place to initialise game and menu but needed otherwise pyxel gets mad
        game=GameEngine()
        menu=MenuEngine()
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
        if inGame:
            game.game_update()
        else:
            inGame=menu.menu_update()
        
App()