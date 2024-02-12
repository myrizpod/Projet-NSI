from Game import *
from Menu import *
game=GameEngine()
menu=MenuEngine()
import pyxel
import time
import math
import random
class App:
    def __init__(self):
        self.screen_size=[256,128]
        pyxel.init(self.screen_size[0], self.screen_size[1],"Ski Game",30)
        pyxel.load("textures.pyxres")
        pyxel.run(self.update, self.draw)

    def draw(self):
        global game
        if not pyxel.btn(pyxel.KEY_H):
            game.game_draw()
        else:
            menu.menu_draw()   

    def update(self):
        global game
        if not pyxel.btn(pyxel.KEY_H):
            game.game_update()
        else:
            menu.menu_update()
        
App()