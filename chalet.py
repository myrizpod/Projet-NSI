# Pyxel Studio
import pyxel

class Game:
    def __init__(self):
        pyxel.init(128, 128)
        pyxel.run(self.update, self.draw)
        pyxel.load("res.pyxres")

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        global pos,e
        pos=[pyxel.mouse_x,pyxel.mouse_y]

    def draw(self):
        #self.terrain()
        #self.draw_scarf(8)
        #self.start_menu()
        #self.cursor()
        self.chalet()

    def chalet(self):
    
        pyxel.blt(0,0,0,0,72,23,22,0)



Game()

    
