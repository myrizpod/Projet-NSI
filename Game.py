

"""
Notes about the project ( bugs and other...):
-there's an issue with obstacle generation when the player is too fast


"""
#info and imports
print("Launched Ü")
print("Press Q to quit (and save info)")
print("Press P to pause the game")
print("Press space to restart")

import pyxel
import time
import math
import random



#Main class
class GameEngine:


  def __init__(self,screen_size,show_player=True,pieces=0):

    #Variable setup
    self.show_player=show_player
    self.scarf=Custom(name="yellow_scarf")
    self.ski=Custom(name="red_ski")
    self.player=Custom(name="donald")
    self.screen_size=screen_size #constant, size of the screen [Height,Width]
    self.terrain=list([[-1500,0]]) #list of points that define the terrain, each point as [X,Y]
    self.obstacle_list=[] #list of the obstacles present in the game. Should be obstacle class.
    self.coin_list=[] #list of the coins present in the game. Should be coin class.
    self.grounded=False #defines wether or not the player is grounded
    self.cam=[-100,-50] # position of the camera
    self.scarf_height=0 #scarf end Y relative to player Y
    self.dead=False #if player is dead (for death screen)
    self.first_iteration=False #used for first iteration
    self.player_pos=[0,0,0,0,2] #player position info with [X,Y,indext of next closest point on terrain,downward momentum,forward momentum]
    self.terrain_size_mult=70 #defines how zoomed in is the terrain
    self.snow_flake_list=[] # individual snow flakes
    self.pdir=0 #direction of the player in range [0;8[ with 0/8=forward,2=up,4=backward and 6=down
    self.obstacle_distance=0 #distance from the last obstacle
    self.obstacle_distance_min=200 #minimum distance between two obstacles
    self.score=0 #score of the player
    self.pieces=pieces #number of coins of the player
    self.snow_col=[None,12,6,7] #colors for different snowflake layers
    self.coin_distance=0 #current distance between screen border and last coin patch
    self.coin_distance_min=300 #minimum distance between two coin patches
    self.is_paused=False
    self.cam_offset=[self.screen_size[0]/2-20,50] #offset of the camera with the player
    self.coin_mult=1
    self.coin_mult_timer=0
    self.invincible_timer=0
    self.double_jump=False
    self.dash=False
    self.skis="dash"
    
    #generation at the beiginning, to avoid holes
    print("Starting Gen")
    self.gen_terrain(self.screen_size[0]*15)
    print("Added points")
  def game_update(self):
    """
    the function that runs most of the game, but doesnt do graphics
    """
    # Disco mode
    if pyxel.btn(pyxel.KEY_B):
      self.scarf=Custom(name=random.choice(["yellow_scarf","red_scarf","green_scarf"]))

    #check if player is trying to pause/unpause
    if pyxel.btnp(pyxel.KEY_P):
      if self.is_paused:
        self.is_paused=False
      else:
        self.is_paused=True
    #quit if currently paused
    if self.is_paused:
      return True
    #remove the mouse
    pyxel.mouse(False)
    #camera movement for the beiginning animation
    self.cam_offset[0]=max(30,self.cam_offset[0]-self.cam_offset[0]/50)
    
    #update score, quicker = more score/iteration
    self.score+=self.player_pos[4]
    if not self.dead:
      self.player_pos[4]=max(self.player_pos[4],self.score/500)
    #remove unused terrain points (behind the player)-
    if self.terrain[1][0]+self.cam_offset[0]*10+100<self.player_pos[0]*10:
      self.terrain.pop(0)
      #update player nearest terrain point
      self.player_pos[2]-=1

    #generate new terrain points when needed
    if self.terrain[-1][0]-self.screen_size[0]*10<=(self.player_pos[0]+50)*10:
      self.gen_terrain(1)


    
    #Obstacle generation
    #check if it can spawn a new obstacle (chances augment with the distance with the last obstacle)
    self.obstacle_distance+=self.player_pos[4]
    if self.obstacle_distance>self.obstacle_distance_min and random.random()<0.02*self.player_pos[4]:
      self.obstacle_distance=0
      self.coin_distance=100
      #calculate obstacle position
      pointA,pointB=self.terrain[self.find_next_point(self.player_pos[0]+self.screen_size[0])-1],self.terrain[self.find_next_point(self.player_pos[0]+self.screen_size[0])]
      y=int(pointB[1]/10-self.terrain_y(pointB[0]-((self.player_pos[0]+self.screen_size[0])*10),pointA,pointB)/10)
      #choose a random obstacle type using the propper obstacle class
      r=random.random()
      if r>1/2:
        self.obstacle_list.append(obstacle(self.player_pos[0]+246,y-8,'rock'))
      elif r<1/4:
        self.obstacle_list.append(obstacle(self.player_pos[0]+242,y-16,'tree'))
      else:  
        self.obstacle_list.append(obstacle(self.player_pos[0]+242,y-16,'tree_snowy'))

      
      
    #coin patch generaton
    #check if it can spawn a new coin patch (chances augment with the distance with the last coin patch)
    self.coin_distance+=self.player_pos[4]
    if self.coin_distance>self.coin_distance_min and random.random()<0.02*self.player_pos[4]:
      self.coin_distance=0
      self.obstacle_distance=50
      #spawns multiple coins at once to make a patch
      for i in range(0,random.randint(3,10)*8,8):
        #calculate obstacle position
        pointA,pointB=self.terrain[self.find_next_point(self.player_pos[0]+self.screen_size[0]+i)-1],self.terrain[self.find_next_point(self.player_pos[0]+self.screen_size[0]+i)]
        y=int(pointB[1]/10-self.terrain_y(pointB[0]-((self.player_pos[0]+self.screen_size[0]+i)*10),pointA,pointB)/10)
        #Randomly spawns 2 types of coins who have different values when picked up  
        if random.random()<0.5:
          if random.random()<1:
            self.coin_list.append(coin(self.player_pos[0]+246+i,y-8,0,effect="invincible"))
          elif random.random()<0.2: 
            self.coin_list.append(coin(self.player_pos[0]+246+i,y-8,0,effect="double"))
          else: 
            self.coin_list.append(coin(self.player_pos[0]+246+i,y-8,5))
        else:
          self.coin_list.append(coin(self.player_pos[0]+246+i,y-8,1))
          
    #go to def for info
    self.player_movement()

    self.update_player_points()
    #updates camera position based on player pos
    self.cam=[self.player_pos[0]-self.cam_offset[0],self.player_pos[1]-self.cam_offset[1]]

    #respawn/restart
    if pyxel.btnp(pyxel.KEY_SPACE) and self.dead:
        self.__init__(self.screen_size)
        pyxel.pal()
        self.dead=False
    
    #jump
    if pyxel.btnp(pyxel.KEY_SPACE) and not self.dead:
      if not self.grounded:
        if self.double_jump:
          self.player_pos[3]=-1.5
          self.double_jump=False
        if self.dash:
          self.player_pos[0]+=35
          self.dash=False

      else:
        if self.skis=="double_jump":
          self.double_jump=True
        if self.skis=="dash":
          self.dash=True
        self.player_pos[3]=-2
    
        self.player_pos[3]=-2
    
    if pyxel.btn(pyxel.KEY_SPACE) and not self.dead and not self.grounded:
      self.pdir=(self.pdir+0.15)%8 

       
    self.detect_collisions_obstacles()
    self.detect_collision_coins()  

    if self.dead:
      return True
  
  def die(self):
    """
    mostly changing screen color
    """
    self.dead=True
    pyxel.pal(5,2)
    pyxel.pal(7,15)
    pyxel.pal(6,14)
    pyxel.pal(12,13)

  def getstats(self):
    return self.score,self.pieces
    
  def detect_collisions_obstacles(self):
    """
    Detects collisions between the player's hitbox and the obstacles' hitbox and kills the player
    if the player's hitbox touches it.
    """
    if not self.dead:
      for o in range(len(self.obstacle_list)):
        obs=self.obstacle_list[o]
        for i in range(0,9):
          if obs.hitbox[0]<self.player_pos[0]+i<obs.hitbox[2] and obs.hitbox[1]<self.player_pos[1]+i<obs.hitbox[3] and self.invincible_timer <= 0:
            self.obstacle_list[o].__init__(obs.pos[0],obs.pos[1],obs.type)  
            self.obstacle_list[o].shiver_time=10
            pyxel.play(0, 0)
            self.player_pos[4]=0
            self.die()
            break

  def detect_collision_coins(self):
    """
    Detects collisions between the player's hitbox and the coins' hitbox and collects it
    if the player's hitbox touches it.
    """
    self.coin_mult_timer=max(0,self.coin_mult_timer-1)
    if self.coin_mult_timer==0:
      self.coin_mult=1
    self.invincible_timer=max(0,self.invincible_timer-1)
    if not self.dead:
      for c in range(len(self.coin_list)):
        coi=self.coin_list[c]
        if not coi.picked_up:
          for i in range(0,9):
            if coi.pos[0]<self.player_pos[0]+i<coi.pos[0]+4 and coi.pos[1]<self.player_pos[1]+i<coi.pos[1]+4:
              if coi.effect=="double":
                self.coin_mult_timer=150
                self.coin_mult=2
              self.pieces+=coi.value*self.coin_mult
              if coi.effect=="invincible":
                self.invincible_timer=150
              coi.pickup()
              break      

            

  def update_player_points(self):
    """
    Updates the player's nearest point based on its position
    """
    if self.terrain[self.player_pos[2]][0]<=self.player_pos[0]*10:
      self.player_pos[2]+=1

  def find_next_point(self,x):
    """
    find the next closest terrain point for a given location
    
      x(int): location to check for, in pixels, should not be greater than the current max terrain point 
    """
    for i in range(len(self.terrain)):
      if self.terrain[i][0]>=x*10:
        return i
    return i

  def terrain_y(self,x,pointA,pointB):
    return (pointB[1]-pointA[1])*((math.cos(((x/(pointB[0]-pointA[0]))*math.pi)-math.pi)+1)/2)  


  def player_movement(self):
    """a bunch of things to update player properties relative to the movement
    """
    #moves the player his speed
    self.player_pos[0]+=self.player_pos[4]
    #calculates whether the player is grounded or not
    pointA,pointB=self.terrain[self.player_pos[2]-1],self.terrain[self.player_pos[2]]
    if int(pointB[1]/10-self.terrain_y(pointB[0]-(self.player_pos[0]*10),pointA,pointB)/10)-8>self.player_pos[1]:
      self.grounded=False
      #if not grounded, vertical speed goes up
      self.player_pos[3]+=0.1
    else:
      if not self.grounded:
        #check if the player can properly land
        if self.pdir<1.5 or self.pdir>7.5:
          self.pdir=0
        #otherwise die
        elif not self.dead:
          self.die()
      #land properly
      self.grounded=True
      self.player_pos[3]=min(0,self.player_pos[3])

    #check if player should fall or not + tries to stick it to the ground
    if int(pointB[1]/10-self.terrain_y(pointB[0]-(self.player_pos[0]*10),pointA,pointB)/10)-12<self.player_pos[1] and self.player_pos[3]>=0:
      #reset downard speed when grounded
      self.player_pos[3]=0
      if not self.grounded:
        if self.pdir<1.5 or self.pdir>7.5:
          self.pdir=0
        elif not self.dead:
          self.die()
      self.grounded=True
      #tries to stick the player to the ground if close enough (so that light slopes feel smoother)
      self.player_pos[1]=(pointB[1]/10-self.terrain_y(pointB[0]-(self.player_pos[0]*10),pointA,pointB)/10)-8
    self.player_pos[1]+=self.player_pos[3]

 
  def game_draw(self):
    """
    Draws all visible elements on the scree including text (score,coins,death)
    """
    #clear the screen with blue sky
    pyxel.cls(5)
    pyxel.camera(self.cam[0],self.cam[1]) #update camera to the position stored in the variable self.cam[X,Y]
    #refer to function docstring for more info
    self.draw_terrain()
    self.obstacles_draw()
    self.coins_draw()
    if self.show_player:
      self.draw_scarf(self.scarf.texture[2])
      self.draw_player()
    self.snow_draw()
    #coin counter
    pyxel.text(self.cam[0]+1,self.cam[1],"Coins: "+str(self.pieces),1)
    pyxel.text(self.cam[0],self.cam[1],"Coins: "+str(self.pieces),10)
    #coin mult coutner
    if self.coin_mult>1:
      pyxel.text(self.cam[0]+1,self.cam[1]+8,"x"+str(self.coin_mult)+" - "+str(int(self.coin_mult_timer/30))+"s",1)
      pyxel.text(self.cam[0],self.cam[1]+8,"x"+str(self.coin_mult)+" - "+str(int(self.coin_mult_timer/30))+"s",10)
    if self.invincible_timer>1:
      pyxel.text(self.cam[0]+1,self.cam[1]+16,"invincible - "+str(int(self.invincible_timer/30))+"s",1)
      pyxel.text(self.cam[0],self.cam[1]+16,"invincible - "+str(int(self.invincible_timer/30))+"s",10)
    #pause menu
    if self.is_paused:
      pyxel.blt(self.cam[0]+self.screen_size[0]/2-33,self.cam[1]+20,1,0,0,80,16,0)
      pyxel.text(self.cam[0]+self.screen_size[0]/2-40,self.cam[1]+40,"Press P to return",1)
    #score counter
    pyxel.text(self.cam[0]+self.screen_size[0]-19-len(str(int(self.score)))*4,self.cam[1],'score:'+str(int(self.score/10)),1)
    pyxel.text(self.cam[0]+self.screen_size[0]-20-len(str(int(self.score)))*4,self.cam[1],'score:'+str(int(self.score/10)),9)
    #debug, show the grounded variable
    if self.grounded and pyxel.btn(pyxel.KEY_B):
      pyxel.text(self.cam[0],self.cam[1],'grounded',8)
    #death screen
    if self.dead:
      self.player_pos[4]=max(0,self.player_pos[4]-0.1)
      pyxel.blt(self.cam[0]+self.screen_size[0]/2-33,self.cam[1]+20,1,0,16,48,16,0)
      pyxel.text(self.cam[0]+self.screen_size[0]/2-55,self.cam[1]+40,"Press Space to restart",8)

        

 
  def obstacles_draw(self):
    """draws each obstacle at its position and
    """    
    for obs in self.obstacle_list:
      #managing the shiver animation when we hit an obstacle
      obs.shiver_time=max(obs.shiver_time-1,0)
      if obs.shiver_time==0:
        obs.is_shivering=False
      if obs.is_shivering:
        obs.shiver()
      #draws each obstacle with two different layers (to allow more variation)
      pyxel.blt(obs.pos[0], obs.pos[1], 0, obs.texture_info[0], obs.texture_info[1], obs.texture_info[2], obs.texture_info[3], 0)
      pyxel.blt(obs.pos[0], obs.pos[1], 0, obs.texture_overlay[0], obs.texture_overlay[1], obs.texture_overlay[2], obs.texture_overlay[3], 0)
      #debug, hitboxes of the obstacles
      if pyxel.btn(pyxel.KEY_B):  
        pyxel.rectb(obs.hitbox[0],obs.hitbox[1],obs.hitbox[2]-obs.hitbox[0],obs.hitbox[3]-obs.hitbox[1],8)


  def coins_draw(self):
      """draws the coins, color depends on their value
        also used for the pickup animation and therefore deletion from coins_list
      """    
      
      to_be_deleted=[]
      for c in range(len(self.coin_list)):
        coin=self.coin_list[c]
        if coin.picked_up:
          coin.momentum-=1
        if coin.momentum<=-5:
          to_be_deleted.append(c)
        coin.pos[1]-=coin.momentum
        #draw 
        if coin.value==1:
          pyxel.blt(coin.pos[0], coin.pos[1], 0, 24+int(time.monotonic()*3)%4*4, 8, 4, 4, 0)
        if coin.value==5:
          pyxel.blt(coin.pos[0], coin.pos[1], 0, 24+int(time.monotonic()*3)%4*4, 12, 4, 4, 0)
        if coin.effect=="double":
          pyxel.blt(coin.pos[0], coin.pos[1], 0, 40+int(time.monotonic()*3)%4*4, 8, 4, 4, 0)
        if coin.effect=="invincible":
          pyxel.blt(coin.pos[0], coin.pos[1], 0, 40+int(time.monotonic()*3)%4*4, 12, 4, 4, 0)

        if pyxel.btn(pyxel.KEY_B):  
          pyxel.rectb(coin.pos[0], coin.pos[1],4,4,2)
      for n in to_be_deleted:
        self.coin_list.pop(n)

  def draw_player(self):
    """draws player at its position and defines its hitbox
    """    
    rotframes=[[0, 32],[0, 40],[ 0, 48],[ 0, 56],[8, 32],[8, 40],[8, 48],[8, 56]] # sprites for player rotation range([0,7])
    disframes=[[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
    xdis,ydis=disframes[int(self.pdir)]
    #Skis
    pyxel.blt(self.player_pos[0], self.player_pos[1], 0,self.ski.texture[0]+rotframes[int(self.pdir)][0]+16,self.ski.texture[1]+rotframes[int(self.pdir)][1], 8, 8, 0)
    #Player
    pyxel.blt(self.player_pos[0]+xdis, self.player_pos[1]+ydis, 0,self.player.texture[0]+rotframes[int(self.pdir)][0],self.player.texture[1]+rotframes[int(self.pdir)][1], 8, 8, 0)
    #Scarf
    pyxel.blt(self.player_pos[0], self.player_pos[1], 0,self.scarf.texture[0]+rotframes[int(self.pdir)][0]+32,self.scarf.texture[1]+rotframes[int(self.pdir)][1], 8, 8, 0)
    if pyxel.btn(pyxel.KEY_B):  
        pyxel.rectb(self.player_pos[0],self.player_pos[1],8,8,11)
 
  def draw_scarf(self,col1):
      """draws the player's scarf
     
      !!To do:
        make the scarf use 2 colors

      Args:
          col1 (int [0,15]): scarf color
      """
      scarf_dis=[[2,2],[0,3],[2,5],[7,3],[5,5],[7,4],[5,2],[4,0]] #scarf displacement depending on player rotation
      self.scarf_height=min(self.scarf_height+pyxel.rndi(0,1),self.player_pos[4])
      self.scarf_height=max(self.scarf_height-pyxel.rndi(0,1),-self.player_pos[4])
      spos=[self.player_pos[0]-3*self.player_pos[4],self.player_pos[1]+self.scarf_height]
      pyxel.line(self.player_pos[0]+scarf_dis[int(self.pdir)][0],self.player_pos[1]+scarf_dis[int(self.pdir)][1],spos[0]+scarf_dis[int(self.pdir)][0],spos[1]+scarf_dis[int(self.pdir)][1],col1)
 
  def gen_terrain(self,length):
    """generates the points that define the self.terrain.

    Args:
        len (int): minimum length of the generated self.terrain. will therefore probably go over this limit

    """
    slope_start=self.terrain[len(self.terrain)-1]
    end_of_slopes=slope_start[0]
    while slope_start[0]<end_of_slopes+length: #check if the limit has been passed.
      slope_add=[pyxel.rndi(10*self.terrain_size_mult,50*self.terrain_size_mult),pyxel.rndi(self.terrain_size_mult,10*self.terrain_size_mult)] #defines how much further away [X,Y] is the next point.
      slope_start=[slope_start[0]+slope_add[0],slope_start[1]+slope_add[1]] #puts slope start to the new point  
      self.terrain.append(slope_start)
    #print("self.terrain has now",len(self.terrain),"points") #useful for debug


  def draw_terrain(self):
      """
      draws the self.terrain using the points stored in self.terrain. Those points have been generated gen_terrain()

      """
      #slope_start and slope_end_Y stock values on the Y axis while slope_end_X is on the X axis.
      for i in range(len(self.terrain)-1):
        pointA=self.terrain[i]
        pointB=self.terrain[i+1]
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

  def snow_draw(self):
    """does everything related to snowflakes.
    """    
    self.snow_flake_list.append([pyxel.rndi(30,286)+self.cam[0],pyxel.rndi(-30,98)+self.cam[1],pyxel.rndi(100,150),pyxel.rndi(1,3)])
    to_be_deleted=[]
    for i in range(len(self.snow_flake_list)): #each snowflake in the list
        self.snow_movement(i)
        if self.snow_flake_list[i][2]<=0 :
          to_be_deleted.append(i)
        pyxel.circb(self.snow_flake_list[i][0],self.snow_flake_list[i][1],[0,0,0,1][self.snow_flake_list[i][3]],self.snow_col[self.snow_flake_list[i][3]])
    for n in to_be_deleted:
      self.snow_flake_list.pop(n)

  def snow_movement(self,i):
    """updates the position and lifespan of the snowflake at the position i of the self.snow_flake_list

    Args:
        i (int): position of self.snow_flake_list to update
    """
    if self.is_paused:
      self.snow_flake_list[i][1]+=self.snow_flake_list[i][3]/10 #movement Y
      self.snow_flake_list[i][0]-=self.snow_flake_list[i][3]/10 #movement X
    else:  
      self.snow_flake_list[i][1]+=self.snow_flake_list[i][3]/2 #movement Y
      self.snow_flake_list[i][0]-=self.snow_flake_list[i][3]/2 #movement X
    self.snow_flake_list[i][2]-=1 #lower lifespan

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
    """
    Does a little shake when a player dies
    """
    self.pos=[self.original_pos[0]+pyxel.rndi(-1,1),self.original_pos[1]]

  def end_shiver(self):
    """
    Stops the shake
    """
    self.is_shivering=False
    self.pos=self.original_pos  

class coin:
  def __init__(self,x,y,value,effect="coin"):
    self.effect=effect
    self.pos=[x,y]
    self.value=value
    self.momentum=0
    self.picked_up=False
  def pickup(self):
    """
    Defines a momentum(height) for the coins and picking up the coins
    """
    self.momentum=5
    self.picked_up=True

class Custom:
  """
  The class for all custom modifiers like player, skis and scarf
  """
  def __init__(self,name="duck",ondeath=None,constant=None):
    self.name=name
    self.ondeath=ondeath
    self.const=constant

    if self.name=="duck":
      self.texture=[0,0]
    if self.name=="golden_duck":
      self.texture=[0,32]
    if self.name=="ninja_turtle":
      self.texture=[0,64]
    if self.name=="donald":
      self.texture=[0,96]
    
    if self.name=="green_ski":
      self.texture=[0,0]
    if self.name=="yellow_ski":
      self.texture=[0,64]
    if self.name=="red_ski":
      self.texture=[0,32]
    if self.name=="black_ski":
      self.texture=[0,96]

    if self.name=="green_scarf":
      self.texture=[0,32,11]
    if self.name=="yellow_scarf":
      self.texture=[0,64,10]
    if self.name=="red_scarf":
      self.texture=[0,0,8]
    if self.name=="god_scarf":
      self.texture=[0,96,1]

class Trail:
  def __init__(self):
    self.trail_col=[1,2,8,9,10]
     
  def update(self):
    global player
    for i in range(len(player.pos_old)):
      player.pos_old[i].pop(0)
      player.pos_old[i].append([player.pos[0]+(r.random()-0.5)*3,player.pos[1]+(r.random()-0.5)*3])
    if player.movement_ability_time>90:
      for x in range(len(player.pos_old)):
        for each_color in range(len(self.trail_col)):
          p.line(player.pos_old[x][each_color][0], player.pos_old[x][each_color][1], player.pos_old[x][each_color+1][0],player.pos_old[x][each_color+1][1],self.trail_col[each_color])

