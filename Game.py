

"""
Notes about the project ( bugs and other...):
-there's an issue with obstacle generation whet the player is too fast


"""
#info and imports
print("Launched Ü")
print("Press Q to quit (and save info)")
print("Press E/R to slow down/speed up | debug only")
print("Press T to plop obstacle at the player | debug too")
import pyxel
import math
import random

#Variable setup
screen_size=[256,128] #constant, size of the screen [Height,Width]
terrain=list([[-500,0]]) #list of points that define the terrain, each point as [X,Y]
obstacle_list=[] #list of the obstacles present in the game. Should be obstacle class.
coin_list=[]
grounded=False #defines wether or not the player is grounded
cam=[0,-50] # position of the camera
e=0 #scarf end Y relative to player Y
dead=False #if player is dead (for death screen)
g=0 #used for first iteration
player_pos=[0,0,0,0,2] #player position info with [X,Y,indext of next closest point on terrain,downward momentum,forward momentum]
terrain_size_mult=70 #defines how zoomed in is the terrain
snow_flake_list=[] # liste de la neige
pdir=0 #direction of the player in range [0;8[ with 0/8=forward,2=up,4=backward and 6=down
obstacle_distance=0 #distance from the last obstacle
obstacle_distance_min=200 #minimum distance between two obstacles
score=0 #score of the player
snow_col=[None,12,6,7] #colors for different snowflake layers
coin_distance=0
coin_distance_min=100

#Main class
class Game:
  def __init__(self):
    """
    Setup of the pyxel screen
    """
    pyxel.init(screen_size[0], screen_size[1],"Ski Game",30)
    pyxel.load("textures.pyxres")
    pyxel.run(self.update, self.draw)

  def update(self):
      global player_pos,g,e,pdir,cam,screen_size,grounded,terrain,obstacle_distance,\
        obstacle_distance_min,dead,coin_distance,coin_distance_min
      cam_offset=(30,50) #offset of the camera with the player

      if g==0:
        g=1
        print("Starting Gen")
        self.gen_terrain(screen_size[0]*10)
        print("Added points")

      if terrain[1][0]+cam_offset[0]*10+100<player_pos[0]*10:
        terrain.pop(0)
        player_pos[2]-=1


      if terrain[-1][0]-screen_size[0]*10<=player_pos[0]*10:
        self.gen_terrain(1)

      if pyxel.btnp(pyxel.KEY_P):
        pyxel.pal()
        pyxel.dither(1)
        dead=False

      if pyxel.btnp(pyxel.KEY_Q):
          print("Quitting")
          pyxel.quit()

      obstacle_distance+=player_pos[4]
      if obstacle_distance>obstacle_distance_min and random.random()<0.02*player_pos[4]:
        obstacle_distance=0
        pointA,pointB=terrain[self.find_next_point(player_pos[0]+screen_size[0])-1],terrain[self.find_next_point(player_pos[0]+screen_size[0])]
        y=int(pointB[1]/10-self.terrain_y(pointB[0]-((player_pos[0]+screen_size[0])*10),pointA,pointB)/10)
        r=random.random()
        if r>1/2:
          obstacle_list.append(obstacle(player_pos[0]+246,y-8,'rock'))
        elif r<1/4:
          obstacle_list.append(obstacle(player_pos[0]+242,y-16,'tree'))
        else:  
          obstacle_list.append(obstacle(player_pos[0]+242,y-16,'tree_snowy'))

      coin_distance+=player_pos[4]
      if coin_distance>coin_distance_min and random.random()<0.02*player_pos[4]:
        coin_distance=0
        pointA,pointB=terrain[self.find_next_point(player_pos[0]+screen_size[0])-1],terrain[self.find_next_point(player_pos[0]+screen_size[0])]
        y=int(pointB[1]/10-self.terrain_y(pointB[0]-((player_pos[0]+screen_size[0])*10),pointA,pointB)/10)
        coin_list.append(coin(player_pos[0]+246,y-8))


      if pyxel.btn(pyxel.KEY_E):
        player_pos[4]=max(0,player_pos[4]-0.1)

      if pyxel.btn(pyxel.KEY_R):
        player_pos[4]=min(10,player_pos[4]+0.1)

      self.player_movement()

      self.update_player_points()
      cam=[player_pos[0]-cam_offset[0],player_pos[1]-cam_offset[1]]

      if pyxel.btn(pyxel.KEY_SPACE):
        if grounded:
          player_pos[3]=-2
        else:
          pdir=(pdir+0.15)%8  
      self.detect_collisions_obstacles()  

  def die(self):
    global dead,alpha
    alpha=3
    dead=True
    pyxel.pal(5,2)
    pyxel.pal(7,15)
    pyxel.pal(6,14)
    pyxel.pal(12,13)


  def detect_collisions_obstacles(self):
    global player_pos,obstacle_list,cam
    if not dead:
      for o in range(len(obstacle_list)):
        obs=obstacle_list[o]
        for i in range(0,9):
          if obs.hitbox[0]<player_pos[0]+i<obs.hitbox[2] and obs.hitbox[1]<player_pos[1]+i<obs.hitbox[3]:
            obstacle_list[o].__init__(obs.pos[0],obs.pos[1],obs.type)  
            obstacle_list[o].shiver_time=10
            pyxel.play(0, 0)
            player_pos[4]=0
            self.die()
            break


  def update_player_points(self):
    global terrain,player_pos
    if terrain[player_pos[2]][0]<=player_pos[0]*10:
      player_pos[2]+=1

  def find_next_point(self,x):
    global terrain
    for i in range(len(terrain)):
      if terrain[i][0]>=x*10:
        return i

  def terrain_y(self,x,pointA,pointB):
    return (pointB[1]-pointA[1])*((math.cos(((x/(pointB[0]-pointA[0]))*math.pi)-math.pi)+1)/2)  


  def player_movement(self):
    global player_pos,grounded,pdir
    player_pos[0]+=player_pos[4]
    pointA,pointB=terrain[player_pos[2]-1],terrain[player_pos[2]]
    if int(pointB[1]/10-self.terrain_y(pointB[0]-(player_pos[0]*10),pointA,pointB)/10)-8>player_pos[1]:
      grounded=False
      player_pos[3]+=0.1
    else:
      if not grounded:
        if pdir<1.5 or pdir>7.5:
          player_pos[4]+=1
          pdir=0
        elif not dead:
          self.die()      
      grounded=True
      player_pos[3]=min(0,player_pos[3])

    if int(pointB[1]/10-self.terrain_y(pointB[0]-(player_pos[0]*10),pointA,pointB)/10)-10<player_pos[1] and player_pos[3]>=0:
      player_pos[3]=0
      if not grounded:
        if pdir<1.5 or pdir>7.5:
          pdir=0
        elif not dead:
          self.die()      
      grounded=True
      player_pos[1]=(pointB[1]/10-self.terrain_y(pointB[0]-(player_pos[0]*10),pointA,pointB)/10)-8
    player_pos[1]+=player_pos[3]

  def draw(self):
      global player_pos,cam,dead,score,alpha
      pyxel.cls(5)
      pyxel.camera(cam[0],cam[1]) #update camera to the position stored in the variable cam[X,Y]
      self.draw_terrain()
      self.obstacles_draw()
      self.coins_draw()
      self.draw_scarf(8)
      self.draw_player()
      self.neige_draw()
     
      score+=player_pos[4]
      pyxel.text(cam[0]+screen_size[0]-19-len(str(int(score)))*4,cam[1],'Score:'+str(int(score/10)),1)
      pyxel.text(cam[0]+screen_size[0]-20-len(str(int(score)))*4,cam[1],'Score:'+str(int(score/10)),9)
      if grounded and pyxel.btn(pyxel.KEY_B):
        pyxel.text(cam[0],cam[1],'Grounded',8)
      if dead:
        alpha=max(0,alpha-0.05)
        player_pos[4]=max(0,player_pos[4]-0.05)
        pyxel.text(50+cam[0], 50+cam[1], 'U dead', 8)
        pyxel.dither(alpha)

 
  def obstacles_draw(self):
    """draws each obstacle at its position
    """    
    global obstacle_list
    for obs in obstacle_list:
      obs.shiver_time=max(obs.shiver_time-1,0)
      if obs.shiver_time==0:
        obs.is_shivering=False
      if obs.is_shivering:
        obs.shiver()
      pyxel.blt(obs.pos[0], obs.pos[1], 0, obs.texture_info[0], obs.texture_info[1], obs.texture_info[2], obs.texture_info[3], 0)
      pyxel.blt(obs.pos[0], obs.pos[1], 0, obs.texture_overlay[0], obs.texture_overlay[1], obs.texture_overlay[2], obs.texture_overlay[3], 0)
      if pyxel.btn(pyxel.KEY_B):  
        pyxel.rectb(obs.hitbox[0],obs.hitbox[1],obs.hitbox[2]-obs.hitbox[0],obs.hitbox[3]-obs.hitbox[1],8)


  def coins_draw(self):
      """draws each coin at its position
      """    
      global coin_list
      for coin in coin_list:
        pyxel.rect(coin.pos[0], coin.pos[1],4,4,8)
        pyxel.blt(coin.pos[0], coin.pos[1], 0, 24, 8, 4, 4, 0)


  def draw_player(self):
    """draws player at its position
    """    
    global pdir  
    rotframes=[[0, 32],[0, 40],[ 0, 48],[ 0, 56],[8, 32],[8, 40],[8, 48],[8, 56]] # sprites for player rotation range([0,7])
    pyxel.blt(player_pos[0], player_pos[1], 0, rotframes[int(pdir)][0], rotframes[int(pdir)][1], 8, 8, 0)
    if pyxel.btn(pyxel.KEY_B):  
        pyxel.rectb(player_pos[0],player_pos[1],8,8,11)
 
  def draw_scarf(self,col1):
      """draws the player's scarf
     
      !!To do:
        make the scarf use 2 colors

      Args:
          col1 (int [0,15]): scarf color
      """
      global player_pos,e,pdir
      scarf_dis=[[2,2],[0,3],[2,5],[7,3],[5,5],[7,4],[5,2],[4,0]] #scarf displacement depending on player rotation
      e=min(e+pyxel.rndi(0,1),player_pos[4])
      e=max(e-pyxel.rndi(0,1),-player_pos[4])
      spos=[player_pos[0]-3*player_pos[4],player_pos[1]+e]
      pyxel.line(player_pos[0]+scarf_dis[int(pdir)][0],player_pos[1]+scarf_dis[int(pdir)][1],spos[0]+scarf_dis[int(pdir)][0],spos[1]+scarf_dis[int(pdir)][1],col1)
 
  def gen_terrain(self,length):
    """generates the points that define the terrain.

    Args:
        len (int): minimum length of the generated terrain. will therefore probably go over this limit

    """
    global terrain,terrain_size_mult
    slope_start=terrain[len(terrain)-1]
    end_of_slopes=slope_start[0]
    while slope_start[0]<end_of_slopes+length: #check if the limit has been passed.
      slope_add=[pyxel.rndi(10*terrain_size_mult,50*terrain_size_mult),pyxel.rndi(terrain_size_mult,10*terrain_size_mult)] #defines how much further away [X,Y] is the next point.
      slope_start=[slope_start[0]+slope_add[0],slope_start[1]+slope_add[1]] #puts slope start to the new point  
      terrain.append(slope_start)
    #print("Terrain has now",len(terrain),"points") #useful for debug


  def draw_terrain(self):
      """
      draws the terrain using the points stored in terrain. Those points have been generated gen_terrain()

      """
      #slope_start and slope_end_Y stock values on the Y axis while slope_end_X is on the X axis.

      global terrain
      for i in range(len(terrain)-1):
        pointA=terrain[i]
        pointB=terrain[i+1]
        for x in range(pointB[0]-pointA[0]):
          down_distance=self.terrain_y(x,pointA,pointB)#adapts the cosine function between 0 and pi to match the two points (yeah crappy explanation)
          y=pointA[1]+down_distance

          #main snow layers
          pyxel.rect(int((x+pointA[0])/10),int(y/10),1,5,7)
          pyxel.rect(int((x+pointA[0])/10),int(y/10)+5,1,300,6)

          #dithering between the two snow layers
          if not int((x+pointA[0])/10)%2==0:
            pyxel.pset(int((x+pointA[0])/10),int(y/10)+5,7)
          else:
            pyxel.pset(int((x+pointA[0])/10),int(y/10)+6,7)  

  def neige_draw(self):
    """does everything related to snowflakes.
    """    
    global snow_flake_list,cam,snow_col
    snow_flake_list.append([pyxel.rndi(30,286)+cam[0],pyxel.rndi(-30,98)+cam[1],pyxel.rndi(100,150),pyxel.rndi(1,3)])
    to_be_deleted=[]
    for i in range(len(snow_flake_list)): #each snowflake in the list
        self.neige_mouvement(i)
        if snow_flake_list[i][2]<=0 :
          to_be_deleted.append(i)
        pyxel.circb(snow_flake_list[i][0],snow_flake_list[i][1],[0,0,0,1][snow_flake_list[i][3]],snow_col[snow_flake_list[i][3]])
    for n in to_be_deleted:
      snow_flake_list.pop(n)

  def neige_mouvement(self,i):
    """updates the position and lifespan of the snowflake at the position i of the snow_flake_list

    Args:
        i (int): position of snow_flake_list to update
    """    
    global snow_flake_list
    snow_flake_list[i][1]+=snow_flake_list[i][3]/2 #movement Y
    snow_flake_list[i][0]-=snow_flake_list[i][3]/2 #movement X
    snow_flake_list[i][2]-=1 #lower lifespan

class obstacle:  
  def __init__(self,x,y,type,variant=random.randint(0,3)):
    """create a new obstacle at the position[X,Y] and will have an appearence depending on type

    Args:
        x (int): x position
        y (int): y position
        type (str): defines the apperance and properties of an obstacle. see type list below
    """

    #type list:
    #'rock' smol rock. Texture is randomized
    #'tree' lil tree.
    #'tree_snowy' lil tree but snowy. snow falls when hit by the player.
    self.variant=variant  #texture variation of a same object
    self.pos=[x,y]
    self.original_pos=list(self.pos)
    self.type=type
    self.is_shivering=True #used for shiver animation on hit
    self.shiver_time=10
    #defines the hitbox of each type of obstacle with:[hitbox_x,hitbox_y,hitbox_end_x,hitbox_end_y]
    #hitbox is relative to obstacle position
    #definit des infos sur la texture dependant du type de l element selon: [X,Y,size_x,size_y]
    if type=='rock':
      self.hitbox=[x+0,y+0,x+8,y+8]
      self.texture_info=[[8,0,8,8],[16,0,8,8],[8,8,8,8],[16,8,8,8]][self.variant]
      self.texture_overlay=[0,0,0,0]
    if type=='tree_snowy':
      self.hitbox=[x+6,y+0,x+10,y+16]
      self.texture_info=[0,16,16,16]
      self.texture_overlay=[16,16,16,16]
    if type=='tree':
      self.hitbox=[x+6,y+0,x+10,y+16]
      self.texture_info=[0,16,16,16]
      self.texture_overlay=[0,0,0,0]


  def shiver(self):
    self.pos=[self.original_pos[0]+pyxel.rndi(-1,1),self.original_pos[1]]

  def end_shiver(self):
    self.is_shivering=False
    self.pos=self.original_pos  

class coin:
  def __init__(self,x,y):
    self.pos=[x,y]


Game()