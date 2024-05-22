import pyxel
import random

class textures:
    def __init__(self):
        self.textures_infos={
            "ship":{"coo_x":0, "coo_y":0, "width":0, "height":0},
            "player":{
                "standing":{"coo_x":2, "coo_y":26, "width":11, "height":19},
                "swimming_down":{"coo_x":0, "coo_y":0, "width":5, "height":11},
                "swimming_right":{"coo_x":0, "coo_y":0, "width":11, "height":5},
                "swimming_up":{"coo_x":0, "coo_y":0, "width":5, "height":11},
                "swimming_left":{"coo_x":0, "coo_y":0, "width":11, "height":5}},
            "rocks":{
                "left":{
                    "small":{"coo_x":0, "coo_y":0, "width":0, "height":0},
                    "mid":{"coo_x":0, "coo_y":0, "width":0, "height":0},
                    "bigga":{"coo_x":0, "coo_y":0, "width":0, "height":0}},
                "right":{
                    "small":{"coo_x":0, "coo_y":0, "width":0, "height":0},
                    "mid":{"coo_x":0, "coo_y":0, "width":0, "height":0},
                    "bigga":{"coo_x":0, "coo_y":0, "width":0, "height":0}}},
            "kelp":{"coo_x":0, "coo_y":0, "width":0, "height":0}
        }

    def ship(self, x, y):
        pyxel.blt(x, y, self.textures_infos["ship"]["coo_x"], self.textures_infos["ship"]["coo_y"], self.textures_infos["ship"]["width"], self.textures_infos["ship"]["height"], 0)
    
    def player(self, x, y, mode):
        if mode=="standing": pyxel.blt(x, y, 0, self.textures_infos["player"]["standing"]["coo_x"], self.textures_infos["player"]["standing"]["coo_y"], self.textures_infos["player"]["standing"]["width"], self.textures_infos["player"]["standing"]["height"], 0)
        elif mode=="swimming_down": pyxel.blt(x, y, 0, self.textures_infos["player"]["swimming_down"]["coo_x"], self.textures_infos["player"]["swimming_down"]["coo_y"], self.textures_infos["player"]["swimming_down"]["width"], self.textures_infos["player"]["swimming_down"]["height"], 0)
        elif mode=="swimming_right": pyxel.blt(x, y, 0, self.textures_infos["player"]["swimming_right"]["coo_x"], self.textures_infos["player"]["swimming_right"]["coo_y"], self.textures_infos["player"]["swimming_right"]["width"], self.textures_infos["player"]["swimming_right"]["height"], 0)
        elif mode=="swimming_up": pyxel.blt(x, y, 0, self.textures_infos["player"]["swimming_up"]["coo_x"], self.textures_infos["player"]["swimming_up"]["coo_y"], self.textures_infos["player"]["swimming_up"]["width"], self.textures_infos["player"]["swimming_up"]["height"], 0)
        elif mode=="swimming_left": pyxel.blt(x, y, 0, self.textures_infos["player"]["swimming_left"]["coo_x"], self.textures_infos["player"]["swimming_left"]["coo_y"], self.textures_infos["player"]["swimming_left"]["width"], self.textures_infos["player"]["swimming_left"]["height"], 0)

    def rocks(self, x, y, side, size):
        if side=="left":
            if size=="small": pyxel.blt(x, y, self.textures_infos["rocks"]["left"]["small"]["coo_x"], self.textures_infos["rocks"]["left"]["small"]["coo_y"], self.textures_infos["rocks"]["left"]["small"]["width"], self.textures_infos["rocks"]["left"]["small"]["height"], 0)
            elif size=="mid": pyxel.blt(x, y, self.textures_infos["rocks"]["left"]["mid"]["coo_x"], self.textures_infos["rocks"]["left"]["mid"]["coo_y"], self.textures_infos["rocks"]["left"]["mid"]["width"], self.textures_infos["rocks"]["left"]["mid"]["height"], 0)
            elif size=="bigga": pyxel.blt(x, y, self.textures_infos["rocks"]["left"]["bigga"]["coo_x"], self.textures_infos["rocks"]["left"]["bigga"]["coo_y"], self.textures_infos["rocks"]["left"]["bigga"]["width"], self.textures_infos["rocks"]["left"]["bigga"]["height"], 0)
        elif side=="right":
            if size=="small": pyxel.blt(x, y, self.textures_infos["rocks"]["right"]["small"]["coo_x"], self.textures_infos["rocks"]["right"]["small"]["coo_y"], self.textures_infos["rocks"]["right"]["small"]["width"], self.textures_infos["rocks"]["right"]["small"]["height"], 0)
            elif size=="mid": pyxel.blt(x, y, self.textures_infos["rocks"]["right"]["mid"]["coo_x"], self.textures_infos["rocks"]["right"]["mid"]["coo_y"], self.textures_infos["rocks"]["right"]["mid"]["width"], self.textures_infos["rocks"]["right"]["mid"]["height"], 0)
            elif size=="bigga": pyxel.blt(x, y, self.textures_infos["rocks"]["right"]["bigga"]["coo_x"], self.textures_infos["rocks"]["right"]["bigga"]["coo_y"], self.textures_infos["rocks"]["right"]["bigga"]["width"], self.textures_infos["rocks"]["right"]["bigga"]["height"], 0)
    
    def kelp(self, x, y):
        pyxel.blt(x, y, self.textures_infos["kelp"]["coo_x"], self.textures_infos["kelp"]["coo_y"], self.textures_infos["kelp"]["width"], self.textures_infos["kelp"]["height"], 0)




class Bubbles:
    def __init__(self):
        self.bublist=[]
    def update(self):
        self.add_bubbles([random.randint(0,128),random.randint(0,128)+10],2)
        #self.add_bubbles([pyxel.mouse_x,pyxel.mouse_y],1)
    def add_bubbles(self,pos,maxsize):
        self.bublist.append([pos[0],pos[1],random.randint(10*maxsize,25*maxsize)])
    def draw(self):
        pyxel.cls(8)
        for bi in range(len(self.bublist)-1,0,-1):
            self.bublist[bi][1]-=(50-self.bublist[bi][2])/25
            self.bublist[bi][0]+=random.random()-0.5
            pyxel.circb(self.bublist[bi][0],self.bublist[bi][1],self.bublist[bi][2]/20,12-int(self.bublist[bi][2]/10))
            self.bublist[bi][2]-=1
            if self.bublist[bi][2]<=0:
                self.bublist.pop(bi)


class game:
    def __init__(self):
        self.screensize=[128, 128]
        pyxel.init(self.screensize[0],self.screensize[1], "Lost in the deep", 30)
        self.buble=Bubbles()
        pyxel.load("theme2.pyxres")
        pyxel.run(self.game_draw, self.game_update)
        
    def game_draw(self):
        self.buble.draw()
        textures.player(self, 0, 0, "swimming_down")

    def game_update(self):
        self.buble.update()

game()
