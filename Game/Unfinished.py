import pygame



pygame.init()
clock = pygame.time.Clock()

standing =  [pygame.image.load("Standing/1.png"),pygame.image.load("Standing/1.png"),
pygame.image.load("Standing/2.png"),pygame.image.load("Standing/3.png"),
pygame.image.load("Standing/4.png"),pygame.image.load("Standing/5.png")]
standing_left = []
running_right = [pygame.image.load("Running/1R.png"),pygame.image.load("Running/2R.png"),pygame.image.load("Running/3R.png"),
pygame.image.load("Running/4R.png"),pygame.image.load("Running/5R.png"),pygame.image.load("Running/6R.png"),
pygame.image.load("Running/7R.png"),pygame.image.load("Running/8R.png")]
jumping_right = [pygame.image.load("Jumping/1J.png"),pygame.image.load("Jumping/2J.png"),pygame.image.load("Jumping/3J.png"),
pygame.image.load("Jumping/4J.png"),pygame.image.load("Jumping/5J.png")]
jumping_left = []
attack1_right = [pygame.image.load("Attack1/1A.png"),pygame.image.load("Attack1/2A.png"),
pygame.image.load("Attack1/3A.png"),pygame.image.load("Attack1/4A.png"),pygame.image.load("Attack1/5A.png"),
pygame.image.load("Attack1/6A.png"),pygame.image.load("Attack1/7A.png"),pygame.image.load("Attack1/8A.png"),]
attack1_left = []
death = [pygame.image.load("Death/1D.png"),pygame.image.load("Death/2D.png"),pygame.image.load("Death/3D.png"),
pygame.image.load("Death/4D.png"),pygame.image.load("Death/5D.png"),pygame.image.load("Death/6D.png"),
pygame.image.load("Death/7D.png")]
home_left = [pygame.image.load("HomeRunning/HR1.png"),pygame.image.load("HomeRunning/HR2.png"),
pygame.image.load("HomeRunning/HR3.png"),pygame.image.load("HomeRunning/HR4.png"),pygame.image.load("HomeRunning/HR5.png")]
home_right = []
home_up = [pygame.image.load("HomeBehind/HB1.png"),pygame.image.load("HomeBehind/HB2.png"),
pygame.image.load("HomeBehind/HB3.png"),pygame.image.load("HomeBehind/HB4.png"),pygame.image.load("HomeBehind/HB5.png")]
home_down =[pygame.image.load("HomeForward/HF1.png"),pygame.image.load("HomeForward/HF2.png"),
pygame.image.load("HomeForward/HF3.png"),pygame.image.load("HomeForward/HF4.png"),pygame.image.load("HomeForward/HF5.png")]
home_standing_right =[]
home_standing_left = [pygame.image.load("HomeRunning/HR1.png")]
home_standing_up =[pygame.image.load("HomeBehind/HB1.png")]
home_standing_down = [pygame.image.load("HomeForward/HF1.png")]
mob_standing = [pygame.image.load("MobStanding/tile000.png"),pygame.image.load("MobStanding/tile001.png"),
pygame.image.load("MobStanding/tile002.png"),pygame.image.load("MobStanding/tile003.png"),
pygame.image.load("MobStanding/tile004.png")]
mob_right = [pygame.image.load("MobWalking/tile011.png"),pygame.image.load("MobWalking/tile012.png"),
pygame.image.load("MobWalking/tile013.png"),pygame.image.load("MobWalking/tile014.png"),
pygame.image.load("MobWalking/tile015.png"),pygame.image.load("MobWalking/tile016.png"),
pygame.image.load("MobWalking/tile017.png"),pygame.image.load("MobWalking/tile018.png")]
mob_attack1_right = [pygame.image.load("MobAttack1/tile033.png"),pygame.image.load("MobAttack1/tile034.png"),
pygame.image.load("MobAttack1/tile035.png"),pygame.image.load("MobAttack1/tile036.png"),pygame.image.load("MobAttack1/tile037.png"),
pygame.image.load("MobAttack1/tile038.png"),pygame.image.load("MobAttack1/tile040.png"),pygame.image.load("MobAttack1/tile041.png")]
mob_attack1_left =[]
mob_left = []
running_left = []  
player_images = [standing,running_right,jumping_right,attack1_right,death,home_up,home_left,home_down,home_standing_left,
home_standing_up,home_standing_down]
counter = 0
for image in player_images:
    for sprite in image:
        image[counter] = pygame.transform.scale(sprite, (130,110))
        counter += 1
    counter = 0
counter =0
mob_images = [mob_standing,mob_right,mob_attack1_right]
for image in mob_images:
    for sprite in image:
        image[counter] = pygame.transform.scale(sprite, (150,150))
        counter +=1
    counter =0
for image in running_right:
    image = pygame.transform.flip(image, True, False)
    running_left.append(image)
for image in mob_right:
    image = pygame.transform.flip(image, True, False)
    mob_left.append(image)
for image in standing:
    image = pygame.transform.flip(image, True, False)
    standing_left.append(image)
for image in jumping_right:
    image = pygame.transform.flip(image, True, False)
    jumping_left.append(image) 
for image in attack1_right:
    image = pygame.transform.flip(image, True, False)
    attack1_left.append(image) 
for image in mob_attack1_right:
    image = pygame.transform.flip(image, True, False)
    mob_attack1_left.append(image) 
for image in home_left:
    image = pygame.transform.flip(image, True, False)
    home_right.append(image) 
home_standing_right =[home_right[0]]
    
bg = pygame.image.load("Backgrounds/b24ea4a8f600a24da0552c1ae8cfb355-700.jpg")
bg = pygame.transform.scale(bg, (1400, 800))
pygame.display.set_caption('Game')

win=pygame.display.set_mode((1400,800))
win_width = 1400
win_height = 800
clock = pygame.time.Clock()
run = True
WHITE = (255, 255, 255) #1
BLACK = (0, 0, 0) #2
RED = (255, 0, 0) #3
GREEN = (0, 255, 0) #4
BLUE = (0, 0, 255) #5
YELLOW = (255, 255, 0) #6
LIGHTBLUE = (0, 155, 155) #7
BROWN = (139,76,57) #8
ORANGE = (255,128,0) #9
DARKGREEN = (0,100,0)
BGCOLOR = LIGHTBLUE
colors = {1:WHITE, 2:BLACK, 3:RED, 4:GREEN, 6:YELLOW, 7:LIGHTBLUE, 8:BROWN, 9:ORANGE, 10:DARKGREEN}
rec_images = {5:pygame.image.load("Backgrounds/Water.jpg")}

class player:
    def __init__(self):
        self.x = 800
        self.y = 500
        self.tempy = 0
        self.vel = 10
        self.width = 130
        self.height = 98
        self.jump = False
        self.jumplimit = -20
        self.up = 20
        self.up0 = False
        self.jumpcount = -6
        self.cooldown_jump = 30
        self.jumptemp = True
        self.down = 20
        self.leftcut = 30
        self.distance = 3
        self.right = False
        self.left = False
        self.standing = True
        self.attack = False
        player.spritex = 800
        player.spritey = 500
        player.interact = False
        player.stoptext= False
        self.hitbox = pygame.Rect(self.spritex + self.leftcut, self.spritey , 40, self.height)
        player.colliderect = 0
        player.sprite = pygame.Rect(self.x, self.y, self.width, self.height)
        self.point = pygame.Rect(self.spritex + 50, self.spritey+ 50, 0, 0)
        self.health = 10
        self.move = True
        self.swordout = False
        self.sword_counter = 1000
        self.stop = False
        self.walkcount = 0
        self.swordcount = 0
        self.swordin = False
        self.jump_bool = False
        player.standcount = 30
        player.jump_anim = 20
        self.attackcount = 0
        self.swing = False
        self.hitbox_right = pygame.Rect(self.spritex + self.width/2, self.spritey, self.width/2, self.height)
        self.hitbox_left = pygame.Rect(self.spritex, self.spritey, self.width/2, self.height)
        player.kills = 0
        self.death = False
        self.deathcount = 0
        self.s = False
    def draw(self):
        player.sprite = pygame.Rect(player.x, player.y, player.width, player.height)
        player.sprite = camera.apply(player.sprite)
        player.spritex = player.sprite[0]
        player.spritey = player.sprite[1]
        self.hitbox_right = pygame.Rect(self.x + 90, self.y, 30, self.height)
        self.hitbox_left = pygame.Rect(self.x + 10, self.y, 30, self.height) 
        self.hitbox_right = camera.apply(self.hitbox_right)
        self.hitbox_left = camera.apply(self.hitbox_left)
        self.hitbox = camera.apply(self.hitbox)
        self.point = camera.apply(self.point)
        self.hitbox = pygame.Rect(self.spritex + 30, self.spritey + 5, 50, self.height - 10)
        self.point = pygame.Rect(self.spritex + 50, self.spritey+ 50, 0, 0)

        font = pygame.font.SysFont('comicsans', 50)
        controls = font.render(f'X:{player.x}   Y:{player.y}', 1, GREEN)
        win.blit(controls, (50,50))
        font = pygame.font.SysFont('comicsans', 50)
        controls = font.render(f'Press R to Reset at any time', 1, GREEN)
        win.blit(controls, (50,80))
        
        
        if rec.level != 0:
          
            player.running()
            if not(self.death):
                healthbar_red = pygame.Rect(self.x + 5, self.y - 10, 100, 10)
                healthbar_green = pygame.Rect(self.x + 5, self.y - 10, 100 - (10*(10-self.health)), 10)
                healthbar_red = camera.apply(healthbar_red)
                healthbar_green = camera.apply(healthbar_green)
                pygame.draw.rect(win, RED, healthbar_red)
                pygame.draw.rect(win, GREEN, healthbar_green)
        elif rec.level == 0:
            
            player.home_running()
        if self.health ==0:
            self.death = True
            self.swing = False
            self.standing = False
            self.left = False
            self.right = False
            self.jump = False
            self.stop = True
            
    def hit(self):
        if self.attackcount//3 == 8:
            self.attackcount = 0
            player.attack = False
        if self.attackcount//3 == 4 or self.attackcount//3 == 5:
            player.swing = True
        else: 
            player.swing = False
    def running(self):
        if self.left and not(self.standing) and not(self.attack) and not(self.jump) and collisiony(player.vel, False):
            if self.walkcount >= 24:
                self.walkcount = 0
                
            
            win.blit(running_left[self.walkcount//3], player.sprite)
            self.walkcount +=1  
            
        elif self.right and not(self.standing) and not(self.attack) and not(self.jump) and collisiony(player.vel, False):
            if self.walkcount >= 24:
                self.walkcount = 0
                
        
            win.blit(running_right[self.walkcount//3], player.sprite)
            self.walkcount +=1  
        elif self.standing and self.right and not(self.attack):
            if self.standcount >= 30:
                self.standcount = 0
                
            
            win.blit(standing[self.standcount//5], player.sprite)
            self.standcount +=1 
        elif self.standing and self.left and not(self.attack) and not(self.jump):
            if self.standcount >= 30:
                self.standcount = 0
                
            
            win.blit(standing_left[self.standcount//5], player.sprite)
            self.standcount +=1 
        elif self.attack and self.right:
            if self.attackcount >= 24:
                self.attackcount = 0
                
                
        
            win.blit(attack1_right[self.attackcount//3], player.sprite)
            self.attackcount +=1  
            player.hit()
        elif self.attack and self.left:
            if self.attackcount >= 24:
                self.attackcount = 0
            
        
            win.blit(attack1_left[self.attackcount//3], player.sprite)
            self.attackcount +=1 
            player.hit()
        elif self.jump and self.right:
            if self.jump_anim >= 20:
                self.jump_anim =0
                
            win.blit(jumping_right[self.jump_anim//4], player.sprite)
            self.jump_anim += 1
        elif self.jump and self.left:
            if self.jump_anim >= 20:
                self.jump_anim =0
                
            win.blit(jumping_left[self.jump_anim//4], player.sprite)
            self.jump_anim += 1
        elif not(collisiony(player.vel,False)) and not player.jump and self.left:
            win.blit(jumping_left[3], player.sprite)
        elif not(collisiony(player.vel,False)) and not player.jump and self.right:
            win.blit(jumping_right[3], player.sprite)
        elif player.death:
            if self.deathcount >= 100:
                self.deathcount = 0
            if self.deathcount == 99:
                player.death = False
                game.death = True
                game.move = False
                
            if self.deathcount < 35:
                win.blit(death[self.deathcount//5], player.sprite)
            if self.deathcount <= 100 and not(self.deathcount < 35):
                win.blit(death[6], player.sprite)
            
            self.deathcount += 1
        else:
            if self.standcount >= 30:
                self.standcount = 0
                
            
            win.blit(standing[self.standcount//5], player.sprite)
            self.standcount +=1 
            self.standing = True
            self.right = True
    def home_running(self):
        if self.left and not(self.standing):
            if self.walkcount >= 24:
                self.walkcount = 0
                
            
            win.blit(home_left[self.walkcount//6], player.sprite)
            self.walkcount +=1  
            
        elif self.right and not(self.standing):
            if self.walkcount >= 24:
                self.walkcount = 0
                
        
            win.blit(home_right[self.walkcount//6], player.sprite)
            self.walkcount +=1  
        elif self.up0 and not(self.standing):
            if self.walkcount >= 24:
                self.walkcount = 0
                
        
            win.blit(home_up[self.walkcount//6], player.sprite)
            self.walkcount +=1 
        elif self.s and not(self.standing):
            if self.walkcount >= 24:
                self.walkcount = 0
                
        
            win.blit(home_down[self.walkcount//6], player.sprite)
            self.walkcount +=1 
        elif self.standing and self.right:

            win.blit(home_standing_right[0], player.sprite)
  
        elif self.standing and self.left:

            win.blit(home_standing_left[0], player.sprite)
            
        elif self.standing and self.up0:
            
            win.blit(home_standing_up[0], player.sprite)
            
        elif self.standing and self.s:
            
            win.blit(home_standing_down[0], player.sprite)
        else:
            self.standing = True
            self.up0 = True
            
        
            
        
            
        
        
            
class rectangle:
    def __init__(self):
        self.ground = []
        self.sprites0 = []
        self.sprites1 =[]
        self.sprites2 =[]
        self.sprites3 =[]
        self.sprites4 =[]
        self.sprites5 =[]
        self.sprites6 =[]
        self.sprites7 =[]
        self.sprites8 =[]
        self.sprites9 =[]
        self.sprites10 =[]
        self.color0 = {}
        self.color1 ={}
        self.color2 = {}
        self.color3 ={}
        self.color4 = {}
        self.color5 ={}
        self.color6 = {}
        self.color7 ={}
        self.color8 = {}
        self.color9 ={}
        self.color10 = {}
        self.number = 0
        self.level = 1
        self.spritesall = []
    def add(self, x, y, width, height, level):
        self.level = level
        rect = (x, y, width, height, self.number)
        if self.level == 0:
            self.sprites0.append(rect)
        if self.level == 1:
            self.sprites1.append(rect)
        if self.level == 2:
            self.sprites2.append(rect)
        if self.level == 3:
            self.sprites3.append(rect)
        if self.level == 4:
            self.sprites4.append(rect)
        if self.level == 5:
            self.sprites5.append(rect)
        if self.level == 6:
            self.sprites6.append(rect)
        if self.level == 7:
            self.sprites7.append(rect)
        if self.level == 8:
            self.sprites8.append(rect)
        if self.level == 9:
            self.sprites9.append(rect)
        if self.level == 10:
            self.sprites10.append(rect)
        self.spritesall = [self.sprites0,self.sprites1,self.sprites2,self.sprites3,self.sprites4,self.sprites5,
        self.sprites6,self.sprites7,self.sprites8,self.sprites9,self.sprites10]
    def read(self, file, level):
        with open((f'Ground/{file}.txt'), 'rt') as f:
            self.level = level
            self.number = 0
            for line in f:
                if file == '0':
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        rec.add(int(line[0]), int(line[1]), int(line[2]), int(line[3]), self.level)
                        self.color0[self.number] = int(line[4])
                        self.number += 1
                if file =='1':
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        rec.add(int(line[0]), int(line[1]), int(line[2]), int(line[3]), self.level)
                        self.color1[self.number] = int(line[4])
                        self.number += 1
                elif file == '2':
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        rec.add(int(line[0]), int(line[1]), int(line[2]), int(line[3]), self.level)
                        self.color2[self.number] = int(line[4])
                        self.number += 1
    def draw(self, level):
        self.level = level
        self.ground.clear()
        if self.level == 0:
            for sprite in self.sprites0:
                new_color = self.color0[sprite[4]]
                rec.rectangle_draw(sprite, new_color)
        if self.level == 1:
            for sprite in self.sprites1:
                new_color = self.color1[sprite[4]]
                rec.rectangle_draw(sprite, new_color)  
        if self.level == 2:
            for sprite in self.sprites2:
                new_color = self.color2[sprite[4]]
                rec.rectangle_draw(sprite, new_color)
        if self.level == 3:
            for sprite in self.sprites3:
                new_color = self.color3[sprite[4]]
                rec.rectangle_draw(sprite, new_color)
        if self.level == 4:
            for sprite in self.sprites4:
                new_color = self.color4[sprite[4]]
                rec.rectangle_draw(sprite, new_color)
        if self.level == 5:
            for sprite in self.sprites5:
                new_color = self.color5[sprite[4]]
                rec.rectangle_draw(sprite, new_color)
        if self.level == 6:
            for sprite in self.sprites6:
                new_color = self.color6[sprite[4]]
                rec.rectangle_draw(sprite, new_color)
        if self.level == 7:
            for sprite in self.sprites7:
                new_color = self.color7[sprite[4]]
                rec.rectangle_draw(sprite, new_color)
        if self.level == 8:
            for sprite in self.sprites8:
                new_color = self.color8[sprite[4]]
                
                rec.rectangle_draw(sprite, new_color)
        if self.level == 9:
            for sprite in self.sprites9:
                new_color = self.color9[sprite[4]]
                rec.rectangle_draw(sprite, new_color)
        if self.level == 10:
            for sprite in self.sprites10:
                new_color = self.color10[sprite[4]]
                rec.rectangle_draw(sprite, new_color)
            
    def rectangle_draw(self, sprite, new_color):
        try: 
            color = colors[new_color]
            sprite = pygame.Rect(sprite[0], sprite[1], sprite[2], sprite[3])
            sprite = camera.apply(sprite)
            pygame.draw.rect(win, color, (sprite))
            self.ground.append(sprite)
        except:
            color = rec_images[new_color]
            sprite = pygame.Rect(sprite[0], sprite[1], sprite[2], sprite[3])
            sprite = camera.apply(sprite)
            color = pygame.transform.scale(color, (sprite[2], sprite[3]))
            win.blit(color, sprite)
            self.ground.append(sprite)


class Camera:
    def __init__(self, width=9000, height=2000):
        self.camera = pygame.Rect(0,0, width, height)
        self.height = height
        self.width = width
        self.x = 0
        self.y = 0
    def apply(self, rec):
        return rec.move(self.camera[0], self.camera[1])
    def update(self, x1, y1):
        x = -player.x + win_width*.5
        y = -player.y + win_height*.5
        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - win_width), x)  # right
        y = max(-(self.height - win_height), y )  # bottom
        self.camera = pygame.Rect(x,y, self.width, self.height)
        x = self.x
        y = self.y
    def change(self,width, height):
        self.height = height
        self.width = width
        
       

        
class Text:
    def __init__(self):
        self.move = False
        self.default = 1000
        self.intro = True
        self.controls = False
        self.talk = False
        self.death = False
        self.mouse1, self.mouse2, self.mouse3 = pygame.mouse.get_pressed()
        self.event = pygame.event.get()
        self.deathcounter = 200
        self.run = True
        
    def check(self):
        if self.intro:
            game.intro_txt()
        elif self.controls:
            game.control()
        elif self.talk:
            game.talks(inter.string)
        elif self.death:
            game.end()
    def intro_txt(self):
        if self.intro:
            win.fill(BGCOLOR)
            
            font = pygame.font.SysFont('comicsans', 200)
            font.set_bold(True)
            text = font.render('Unfinished', 1, WHITE)
            win.blit(text, (win_width*.5 - (text.get_width()/2), 180))
            
            font = pygame.font.SysFont('comicsans', 25)
            start_game = font.render('Start Game', 1, GREEN)
            pygame.draw.rect(win, RED, (win_width*.5-start_game.get_width()/2, 700, start_game.get_width(), start_game.get_height()))
            win.blit(start_game, (win_width*.5-start_game.get_width()/2, 700))
            
            font = pygame.font.SysFont('comicsans', 25)
            controls = font.render('Controls', 1, GREEN)
            pygame.draw.rect(win, RED, (win_width*.5-controls.get_width()/2, 600, controls.get_width(), controls.get_height()))
            win.blit(controls, (win_width*.5-controls.get_width()/2, 600))
                             
            
            self.mouse1, self.mouse2, self.mouse3 = pygame.mouse.get_pressed()
            if self.mouse1:
                x, y = pygame.mouse.get_pos()
                start_game = pygame.Rect(win_width*.5-start_game.get_width()/2, 700, start_game.get_width(), 30)
                controls = pygame.Rect(win_width*.5-controls.get_width()/2, 600, controls.get_width(), 30)
                if start_game.collidepoint(x,y):
                    player.stop = False
                    self.move = True
                    self.intro = False
                elif controls.collidepoint(x,y):
                    win.fill(BGCOLOR)
                    self.move = False
                    self.intro = False
                    self.controls = True
    def control(self):
        font = pygame.font.SysFont('comicsans', 50)
        controls = font.render('Controls In Levels', 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 10))
        
        font = pygame.font.SysFont('comicsans', 25)
        controls = font.render('A = Move Left', 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 100))
        
        controls = font.render('D = Move Right', 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 150))
        
        controls = font.render('SPACE = Jump', 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 200))
        
        
        controls = font.render('LSHIFT = Attack', 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 250))
        
        controls = font.render('F = Interact', 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 300))
        
        font = pygame.font.SysFont('comicsans', 50)
        controls = font.render('Controls in Home Island', 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 350))
        
        font = pygame.font.SysFont('comicsans', 25)
        controls = font.render("W = Move Up", 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 450))
        
        controls = font.render('S = Move Down', 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 500))
        
        controls = font.render("A = Move Left", 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 550))
        
        controls = font.render('D = Move Right', 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 600))
        
        controls = font.render('F = Interact', 1, GREEN)
        win.blit(controls, ((win_width*.5 - controls.get_width()/2), 650))
        
        font = pygame.font.SysFont('comicsans', 50)
        controls = font.render('Back', 1,GREEN)
        Out = pygame.Rect(win_width*.5-controls.get_width()/2, 750, controls.get_width(),controls.get_height())
        pygame.draw.rect(win, RED, (win_width*.5-controls.get_width()/2, 750, controls.get_width(),controls.get_height()))
        win.blit(controls, (win_width*.5-(controls.get_width()/2), 750))
        self.mouse1, self.mouse2, self.mouse3 = pygame.mouse.get_pressed()
        if self.mouse1:
            x, y = pygame.mouse.get_pos()
            if Out.collidepoint(x,y):
                self.move = False
                self.controls = False
                self.intro = True
    def talks(self, string):
        all_string = string.split('-')
        counter = 1
        pygame.draw.rect(win, BROWN, (0, 0, 1800, 200))
        for string in all_string:
            font = pygame.font.SysFont('comicsans', 50)
            string = font.render(string, 1, GREEN)
            win.blit(string, ((win_width*.5 - string.get_width()/2), 50*counter))
            counter += 1
        font = pygame.font.SysFont('comicsans', 25)
        tab = font.render('Press Tab to Continue', 1, GREEN)
        win.blit(tab, (1100, 150))
        if player.stoptext:
            game.move = True
            game.talk = False
    def end(self):
        if self.deathcounter != 0:
            endscreen = pygame.Rect(0, 0, win_width, win_height)
            pygame.draw.rect(win, BLACK, (endscreen))
            font = pygame.font.SysFont('comicsans', 100 )
            end = font.render('YOU HAVE DIED', 1, RED)
            win.blit(end, (win_width*.5-end.get_width()/2, 400))
            self.deathcounter -= 1
        if self.deathcounter == 0:
            self.deathcounter = 200
            game.run = False
        
class Exits:
    def __init__(self):
        self.number = 0
        self.level = 0
        self.color0 = {}
        self.color1 = {}
        self.color2 = {}
        self.color3 = {}
        self.color4 = {}
        self.color5 = {}
        self.color6 = {}
        self.color7 = {}
        self.color8 = {}
        self.color9 = {}
        self.color10 = {}
        self.sprites0= []
        self.sprites1= []
        self.sprites2= []
        self.sprites3= []
        self.sprites4= []
        self.sprites5= []
        self.sprites6= []
        self.sprites7= []
        self.sprites8= []
        self.sprites9= []
        self.sprites10= []
        self.tele = []
        self.destination = 1
        self.dest0 = {}
        self.dest1 = {}
        self.dest2 = {}
        self.dest3 = {}
        self.dest4 = {}
        self.dest5 = {}
        self.dest6 = {}
        self.dest7 = {}
        self.dest8 = {}
        self.dest9 = {}
        self.dest10 = {}
        self.tp0 = {}
        self.tp1 = {}
        self.tp2 = {}
        self.tp3 = {}
        self.tp4 = {}
        self.tp5 = {}
        self.tp6 = {}
        self.tp7 = {}
        self.tp8 = {}
        self.tp9 = {}
        self.tp10 = {}
        self.wat_x = -1
        self.wwat_y = -1
        self.wat_level = -1
        self.counter = 0
        self.walkcount = {}
        self.spritesall = []
    def read(self, file, level):
        with open((f'Exits/{file}.txt'), 'rt') as f:
            self.number = 0
            self.level = level
            for line in f:
                if file == '0E':
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        exits.add(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
                        self.color0[self.number] = int(line[4])
                        self.dest0[self.number] = int(line[5])
                        self.tp0[self.number] = int(line[6]) , int(line[7])
                        self.number += 1
                elif file =='1E':
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        exits.add(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
                        self.color1[self.number] = int(line[4])
                        self.dest1[self.number] = int(line[5])
                        self.tp1[self.number] = int(line[6]) , int(line[7])
                        self.number += 1
                elif file == '2E':
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        exits.add(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
                        self.color2[self.number] = int(line[4])
                        self.dest2[self.number] = int(line[5])
                        self.tp2[self.number] = int(line[6]), int(line[7])
                        self.number += 1
                
    def check(self, level):
        self.level = level
        self.tele.clear()
        if self.level == 0:
            for sprite in self.sprites0:
                new_color = self.color0[sprite[4]]
                exits.rectangle_draw(sprite, new_color)
        if self.level == 1:
            for sprite in self.sprites1:
                new_color = self.color1[sprite[4]]
                exits.rectangle_draw(sprite, new_color)  
        if self.level == 2:
            for sprite in self.sprites2:
                new_color = self.color2[sprite[4]]
                exits.rectangle_draw(sprite, new_color)
        if self.level == 3:
            for sprite in self.sprites3:
                new_color = self.color3[sprite[4]]
                exits.rectangle_draw(sprite, new_color)
        if self.level == 4:
            for sprite in self.sprites4:
                new_color = self.color4[sprite[4]]
                exits.rectangle_draw(sprite, new_color)
        if self.level == 5:
            for sprite in self.sprites5:
                new_color = self.color5[sprite[4]]
                exits.rectangle_draw(sprite, new_color)
        if self.level == 6:
            for sprite in self.sprites6:
                new_color = self.color6[sprite[4]]
                exits.rectangle_draw(sprite, new_color)
        if self.level == 7:
            for sprite in self.sprites7:
                new_color = self.color7[sprite[4]]
                exits.rectangle_draw(sprite, new_color)
        if self.level == 8:
            for sprite in self.sprites8:
                new_color = self.color8[sprite[4]]
                exits.rectangle_draw(sprite, new_color)
        if self.level == 9:
            for sprite in self.sprites9:
                new_color = self.color9[sprite[4]]
                exits.rectangle_draw(sprite, new_color)
        if self.level == 10:
            for sprite in self.sprites10:
                new_color = self.color10[sprite[4]]
                exits.rectangle_draw(sprite, new_color) 
    def add(self, x, y, width, height):
        self.level = rec.level
        rect = (x, y, width, height, self.number)
        if self.level == 0:
            self.sprites0.append(rect)
        if self.level == 1:
            self.sprites1.append(rect)
        if self.level == 2:
            self.sprites2.append(rect)
        if self.level == 3:
            self.sprites3.append(rect)
        if self.level == 4:
            self.sprites4.append(rect)
        if self.level == 5:
            self.sprites5.append(rect)
        if self.level == 6:
            self.sprites6.append(rect)
        if self.level == 7:
            self.sprites7.append(rect)
        if self.level == 8:
            self.sprites8.append(rect)
        if self.level == 9:
            self.sprites9.append(rect)
        if self.level == 10:
            self.sprites10.append(rect)
        self.spritesall = [self.sprites0,self.sprites1,self.sprites2,self.sprites3,self.sprites4,self.sprites5,
        self.sprites6,self.sprites7,self.sprites8,self.sprites9,self.sprites10]
    def rectangle_draw(self, sprite, new_color):
        number = sprite[4]
        try:
            color = colors[new_color]
            sprite = pygame.Rect(sprite[0], sprite[1], sprite[2], sprite[3])
            sprite = camera.apply(sprite)
            pygame.draw.rect(win, color, sprite)
            self.tele.append(sprite)
        except: 
            color = rec_images[new_color]
            sprite = pygame.Rect(sprite[0], sprite[1], sprite[2], sprite[3])
            sprite = camera.apply(sprite)
            win.blit(color, sprite)
            self.tele.append(sprite)
        exits.collision(sprite, self.level, number)
    def collision(self, sprite, level, number):
            
            if sprite.colliderect(player.hitbox) and self.counter == 0:
                if level ==0:
                    levels.level0 = False
                    self.wat_level = self.dest0[number]
                    self.wat_x,self.wat_y = self.tp0[number]
                if level == 1:
                    levels.level1 = False
                    self.wat_level = self.dest1[number]
                    self.wat_x,self.wat_y = self.tp1[number]
                if level == 2:
                    levels.level2 = False
                    self.wat_level = self.dest2[number]  
                    self.wat_x,self.wat_y = self.tp2[number]
                    
                if self.wat_level == 2:
                    self.level = 2
                    rec.level = 2
                    mobs.level = 2
                    key.level = 2
                    levels.level2 = True
                    player.x = self.wat_x
                    player.y = self.wat_y
                if self.wat_level == 1:
                    self.level = 1
                    rec.level = 1
                    mobs.level = 1
                    key.level = 1
                    levels.level1 = True
                    player.x = self.wat_x
                    player.y = self.wat_y
                if self.wat_level == 0:
                    self.level = 0
                    rec.level = 0
                    mobs.level = 0
                    key.level = 1
                    levels.level0 = True
                    player.x = self.wat_x
                    player.y = self.wat_y
                self.counter = 10
            elif self.counter != 0:
                self.counter -= 1

class Mobs:
    def __init__(self):
        self.number = 0
        self.level = 0
        self.color0 = {}
        self.color1 = {}
        self.color2 = {}
        self.color3 = {}
        self.color4 = {}
        self.color5 = {}
        self.color6 = {}
        self.color7 = {}
        self.color8 = {}
        self.color9 = {}
        self.color10 = {}
        self.sprites0= []
        self.sprites1= []
        self.sprites2= []
        self.sprites3= []
        self.sprites4= []
        self.sprites5= []
        self.sprites6= []
        self.sprites7= []
        self.sprites8= []
        self.sprites9= []
        self.sprites10= []
        self.enemy = []
        self.health = {}
        self.counter = 0
        self.starting_health = 3
        self.standing = {}
        self.right = {}
        self.left = {}
        self.spritex = {}
        self.spritey = {}
        self.height = {}
        self.width = {}
        self.time = 0
        self.vel = 5
        self.limit = {}
        self.walkcount = {}
        self.attackcount = {}
        self.standing = True
        self.left = False
        self.right = False
        self.attack = {}
        self.attack_counter = {}
        self.cooldown = 0
        self.spritesall = []
    def read(self, file, level):
        with open((f'Mobs/{file}.txt'), 'rt') as f:
            self.level = level
            for line in f:
                # text = 1
                # finds out wich number is first in notepad (level), appends it to a dictionary with the corresponding rectangle
                # in the draw function, it takes the corresponding number to the rectangle and draws it. 10 dictionaries 
                #within the big one, for the 10 levels
                if file =='0M':
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        mobs.add(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
                        
                        self.health[self.number] = self.starting_health
                        self.spritex[self.number] = int(line[0])
                        self.spritey[self.number] = int(line[1])
                        self.width[self.number] = int(line[2])
                        self.height[self.number] = int(line[3])
                        self.number += 1
                if file =='1M':
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        mobs.add(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
                        
                        self.health[self.number] = self.starting_health
                        self.spritex[self.number] = int(line[0])
                        self.spritey[self.number] = int(line[1])
                        self.width[self.number] = int(line[2])
                        self.height[self.number] = int(line[3])
                        self.attackcount[self.number] = 0
                        self.walkcount[self.number] = 0
                        self.attack_counter[self.number] = 50
                        mobs.attack[self.number] = False
                        self.number += 1
                elif file == '2M':
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        mobs.add(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
                        
                        self.health[self.number] = self.starting_health
                        self.spritex[self.number] = int(line[0])
                        self.spritey[self.number] = int(line[1])
                        self.width[self.number] = int(line[2])
                        self.height[self.number] = int(line[3])
                        self.walkcount[self.number] = 0
                        self.attackcount[self.number] = 0
                        self.attack_counter[self.number] = 50
                        mobs.attack[self.number] = False
                        self.number += 1
    def check(self, level):
        self.level = level
        self.enemy.clear()
        new_color = 'pass'
        if self.level == 0:
            for sprite in self.sprites0:
                
                mobs.rectangle_draw(sprite, new_color)
        if self.level == 1:
            for sprite in self.sprites1:
                
                mobs.rectangle_draw(sprite, new_color)
        if self.level == 2:
            for sprite in self.sprites2:
                
                mobs.rectangle_draw(sprite, new_color)
        if self.level == 3:
            for sprite in self.sprites3:
                
                mobs.rectangle_draw(sprite, new_color)
        if self.level == 4:
            for sprite in self.sprites4:
                
                mobs.rectangle_draw(sprite, new_color)
        if self.level == 5:
            for sprite in self.sprites5:
                
                mobs.rectangle_draw(sprite, new_color)
        if self.level == 6:
            for sprite in self.sprites6:
                
                mobs.rectangle_draw(sprite, new_color)
        if self.level == 7:
            for sprite in self.sprites7:
                
                mobs.rectangle_draw(sprite, new_color)
        if self.level == 8:
            for sprite in self.sprites8:
                
                mobs.rectangle_draw(sprite, new_color)
        if self.level == 9:
            for sprite in self.sprites9:
                
                mobs.rectangle_draw(sprite, new_color)
        if self.level == 10:
            for sprite in self.sprites10:
                
                mobs.rectangle_draw(sprite, new_color) 
    def add(self, x, y, width, height):
        self.level = rec.level
        rect = [x, y, width, height, self.number]
        if self.level == 0:
            self.sprites0.append(rect)
        if self.level == 1:
            self.sprites1.append(rect)
        if self.level == 2:
            self.sprites2.append(rect)
        if self.level == 3:
            self.sprites3.append(rect)
        if self.level == 4:
            self.sprites4.append(rect)
        if self.level == 5:
            self.sprites5.append(rect)
        if self.level == 6:
            self.sprites6.append(rect)
        if self.level == 7:
            self.sprites7.append(rect)
        if self.level == 8:
            self.sprites8.append(rect)
        if self.level == 9:
            self.sprites9.append(rect)
        if self.level == 10:
            self.sprites10.append(rect)
        self.spritesall = [self.sprites0,self.sprites1,self.sprites2,self.sprites3,self.sprites4,self.sprites5,
        self.sprites6,self.sprites7,self.sprites8,self.sprites9,self.sprites10]
    def rectangle_draw(self, sprite, new_color):
        number = sprite[4]
        color= 'x'
        if self.health[number] > 0:

            originalx = sprite[0]
            
            
            sprite = pygame.Rect(self.spritex[number], self.spritey[number], 150, 150)
            sprite = camera.apply(sprite)
            sprite_radius = pygame.Rect(self.spritex[number] - 600, self.spritey[number] - 600, 1200, 1200)
            sprite_radius = camera.apply(sprite_radius)
            
            
            
            if sprite_radius.collidepoint(player.spritex,player.spritey) and not(mobs.collision_wall(number, sprite)):
                if player.x < self.spritex[number] and not(mobs.attack[number]):
                    neg = -1
                    self.spritex[number] += self.vel*neg
                    self.left = True
                    self.right = False
                    self.standing = False

                if player.x > self.spritex[number] and not(mobs.attack[number]):
                    neg = 1
                    self.spritex[number] += self.vel*neg
                    self.right = True
                    self.left = False
                    self.standing = False
                    

            else:
                self.standing = True
            if mobs.collision_wall(number,sprite):
                self.spritey[number] -= 10
                if sprite_radius.collidepoint(player.spritex,player.spritey) and player.x < self.spritex[number]:
                    self.left = True
                    self.right = False
                    self.standing = False

            if not(mobs.collision_y(number,sprite)):
                self.spritey[number] += 10
                if sprite_radius.collidepoint(player.spritex,player.spritey) and player.x > self.spritex[number]:
                    self.left = False
                    self.right = True
                    self.standing = False
            if sprite.colliderect(player.hitbox) and self.attack_counter[number] == 0:
                mobs.attack[number] = True
                self.attack_counter[number] = 50
            if not(self.attack_counter[number] == 0):
                self.attack_counter[number] -= 1
            


              

                    
                    
            
            sprite = pygame.Rect(self.spritex[number], self.spritey[number], 150, 150)
            healthbar_red = pygame.Rect(sprite[0], sprite[1] - 20, 150, 10)
            healthbar_green = pygame.Rect(sprite[0], sprite[1] - 20, 150 - ((50)*(3-self.health[number])), 10)
            healthbar_red = camera.apply(healthbar_red)
            healthbar_green = camera.apply(healthbar_green)
            sprite = camera.apply(sprite)
            pygame.draw.rect(win, RED, healthbar_red)
            pygame.draw.rect(win, GREEN, healthbar_green)
            self.enemy.append(sprite)
                        
                        
                
            
            mobs.animation(number, sprite)
            
            
        mobs.collision(sprite, self.level, number)
    def collision(self, sprite, level, number):
        sprite = pygame.Rect(sprite[0], sprite[1], sprite[2], sprite[3])
        if True:
            if sprite.colliderect(player.hitbox_right) and self.counter == 0 and player.swing and player.right:
                self.health[number] -= 1
                self.counter = 25
            if sprite.colliderect(player.hitbox_left) and self.counter == 0 and player.swing and player.left:
                self.health[number] -= 1
                self.counter = 25
            
            if self.health[number] == 0:
                player.kills += 1
        
            
        
        if self.counter != 0:
            self.counter -= 1
                    
                
 
    def collision_wall(self, number, sprite):
        check = False
        sprite = pygame.Rect(sprite[0], sprite[1], 150, 150)
        for item in rec.ground:
            item = rec.ground.index(item)
            if rec.ground[item][0] < sprite[0] + 130 and rec.ground[item][0] + rec.ground[item][2] > sprite[0]+20:
                if sprite[1] < rec.ground[item][1] + rec.ground[item][3] and sprite[1] + 100 > rec.ground[item][1]:
                    check = True
                    break
        return check
    def collision_y(self, number, sprite):
        check = False
        for item in rec.ground:
            item = rec.ground.index(item)
            if rec.ground[item][0] < sprite[0] + 130 and rec.ground[item][0] + rec.ground[item][2] > sprite[0]+20:
                if sprite[1] < rec.ground[item][1] + rec.ground[item][3] and sprite[1] + 100 +10 > rec.ground[item][1]:

                    check = True
                    break     
                    
        return check
    def animation(self,number,sprite):
        if self.left and not(mobs.attack[number]) and not(self.standing):
            if self.walkcount[number] >= 24:
                self.walkcount[number] = 0
                
        
            win.blit(mob_left[self.walkcount[number] //3], sprite)
            self.walkcount[number]  +=1  
            
        if self.right and not(mobs.attack[number]) and not(self.standing):
            if self.walkcount[number] >= 24:
                self.walkcount[number] = 0
                
        
            win.blit(mob_right[self.walkcount[number] //3], sprite)
            self.walkcount[number]  +=1  
        if self.standing and not(mobs.attack[number]):
            if self.walkcount[number] >= 30:
                self.walkcount[number] = 0
                
        
            win.blit(mob_standing[self.walkcount[number] //6], sprite)
            self.walkcount[number]  +=1 
        if mobs.attack[number] and self.right:
            if self.attackcount[number] >= 40:
                self.attackcount[number] = 0
            if self.attackcount[number] == 39:
                mobs.attack[number] = False
            
            win.blit(mob_attack1_right[self.attackcount[number]//5], sprite)
            mobs.hit_player(number,sprite)
            self.attackcount[number] += 1
        if mobs.attack[number] and self.left:
            if self.attackcount[number] >= 40:
                self.attackcount[number] = 0
            if self.attackcount[number] == 39:
                mobs.attack[number] = False
            
            win.blit(mob_attack1_left[self.attackcount[number]//5], sprite)
            mobs.hit_player(number,sprite)
            self.attackcount[number] += 1
        
        
        
    def hit_player(self,number,sprite):
            if self.attackcount[number]//5 == 2 or self.attackcount[number]//5 == 3 or self.attackcount[number]//5 == 4:
                
                if sprite.colliderect(player.hitbox) and self.cooldown == 0:
                    player.health -=1
                    self.cooldown = -15
                if self.cooldown != 0:
                    self.cooldown += 1
        

class Keys:
    def __init__(self):
        self.number = 0
        self.level = 1
        self.sprites0 = []
        self.sprites1 = []
        self.sprites2 = []
        self.sprites3 = []
        self.sprites4 = []
        self.sprites5 = []
        self.sprites6 = []
        self.sprites7 = []
        self.sprites8 = []
        self.sprites9 = []
        self.sprites10 = []
        self.place = []
        self.color = {}
        self.keys = 0
        self.spritesall =[]
    def read(self, file, level):
        with open((f'Keys/{file}.txt'), 'rt') as f:
            for line in f:
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        key.add(int(line[0]), int(line[1]), int(line[2]), int(line[3],), level)
                        self.color[self.number] = int(line[4])
                        self.number += 1
    def add(self, x, y, width, height, level):
        self.level = level
        rect = [x, y, width, height, self.number]
        if self.level == 0:
            self.sprites0.append(rect)
        if self.level == 1:
            self.sprites1.append(rect)
        if self.level == 2:
            self.sprites2.append(rect)
        if self.level == 3:
            self.sprites3.append(rect)
        if self.level == 4:
            self.sprites4.append(rect)
        if self.level == 5:
            self.sprites5.append(rect)
        if self.level == 6:
            self.sprites6.append(rect)
        if self.level == 7:
            self.sprites7.append(rect)
        if self.level == 8:
            self.sprites8.append(rect)
        if self.level == 9:
            self.sprites9.append(rect)
        if self.level == 10:
            self.sprites10.append(rect)
        self.spritesall = [self.sprites0,self.sprites1,self.sprites2,self.sprites3,self.sprites4,self.sprites5,
        self.sprites6,self.sprites7,self.sprites8,self.sprites9,self.sprites10]
    def check(self, level):
        self.level = level
        self.place.clear()
        if self.level == 0:
            for sprite in self.sprites0:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 1:
            for sprite in self.sprites1:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 2:
            for sprite in self.sprites2:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 3:
            for sprite in self.sprites3:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 4:
            for sprite in self.sprites4:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 5:
            for sprite in self.sprites5:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 6:
            for sprite in self.sprites6:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 7:
            for sprite in self.sprites7:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 8:
            for sprite in self.sprites8:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 9:
            for sprite in self.sprites9:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 10:
            for sprite in self.sprites10:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color) 
    def rectangle_draw(self,sprite, new_color):
        number = sprite[4]
        try:
            color = colors[new_color]
        except: 
            color = rec_images[new_color]
        originalx = sprite[0]
            
            
        sprite = pygame.Rect(sprite[0], sprite[1], sprite[2], sprite[3])
        sprite = camera.apply(sprite)

        self.place.append(sprite)
            
        if sprite.colliderect(player.hitbox):
            if self.level == 1:
                self.sprites1.clear()
            
            if self.level == 2:
                self.sprites2.clear()
            player.health = 10
            self.keys += 1
                        
                        
                
        try: 
            win.blit(color, sprite)
        except:
            pygame.draw.rect(win, color, sprite)
class Interact:
    def __init__(self):
        self.number = 0
        self.level = 1
        self.sprites0 = []
        self.sprites1 = []
        self.sprites2 = []
        self.sprites3 = []
        self.sprites4 = []
        self.sprites5 = []
        self.sprites6 = []
        self.sprites7 = []
        self.sprites8 = []
        self.sprites9 = []
        self.sprites10 = []
        self.color = {}
        self.text = {}
        self.counter = 0
        self.string = 'wrong'
        self.require = {}
        self.require0 = {}
        self.col = {}
        self.spritesall = []
    def read(self,file, level):
    
        with open((f'Inter/{file}.txt'), 'rt') as f:
            for line in f:
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        inter.add(int(line[0]), int(line[1]), int(line[2]), int(line[3],), level)
                        self.color[self.number] = int(line[4])
    
                        self.text[self.number] = str(line[5])
                        self.col[self.number] = False

                        self.require[self.number] = str(line[6])
                        self.number += 1
    def add(self, x, y, width, height, level):
        self.level = level
        rect = [x, y, width, height, self.number]
        if self.level == 0:
            self.sprites0.append(rect)
        if self.level == 1:
            self.sprites1.append(rect)
        if self.level == 2:
            self.sprites2.append(rect)
        if self.level == 3:
            self.sprites3.append(rect)
        if self.level == 4:
            self.sprites4.append(rect)
        if self.level == 5:
            self.sprites5.append(rect)
        if self.level == 6:
            self.sprites6.append(rect)
        if self.level == 7:
            self.sprites7.append(rect)
        if self.level == 8:
            self.sprites8.append(rect)
        if self.level == 9:
            self.sprites9.append(rect)
        if self.level == 10:
            self.sprites10.append(rect)
        self.spritesall = [self.sprites0,self.sprites1,self.sprites2,self.sprites3,self.sprites4,self.sprites5,
        self.sprites6,self.sprites7,self.sprites8,self.sprites9,self.sprites10]
    def check(self, level):
        self.level = level
        if self.level == 0:
            for sprite in self.sprites0:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
        if self.level == 1:
            for sprite in self.sprites1:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
        if self.level == 2:
            for sprite in self.sprites2:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
        if self.level == 3:
            for sprite in self.sprites3:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
        if self.level == 4:
            for sprite in self.sprites4:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
        if self.level == 5:
            for sprite in self.sprites5:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
        if self.level == 6:
            for sprite in self.sprites6:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
        if self.level == 7:
            for sprite in self.sprites7:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
        if self.level == 8:
            for sprite in self.sprites8:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
        if self.level == 9:
            for sprite in self.sprites9:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
        if self.level == 10:
            for sprite in self.sprites10:
                new_color = self.color[sprite[4]]
                inter.rectangle_draw(sprite, new_color)
    def rectangle_draw(self, sprite, new_color):
        number = sprite[4]
        try:
            color = colors[new_color]
        except: 
            color = rec_images[new_color]
        originalx = sprite[0]
            
            
        sprite = pygame.Rect(sprite[0], sprite[1], sprite[2], sprite[3])
        sprite = camera.apply(sprite)
        pygame.draw.rect(win, WHITE, sprite)
        temp = self.require[number] in ['True']
        if sprite.colliderect(player.hitbox):
            if player.interact:
                game.talk = True
                game.move = False
                inter.string = self.text[number]
            if not(temp) and self.col[number]:
                game.talk = True
                game.move = False
                inter.string = self.text[number]
                self.col[number] = False
        else:
            self.col[number] = True
            
            
            
                
   
class Images:
    def __init__(self):
        self.number = 0
        self.level = 1
        self.sprites0 = []
        self.sprites1 = []
        self.sprites2 = []
        self.sprites3 = []
        self.sprites4 = []
        self.sprites5 = []
        self.sprites6 = []
        self.sprites7 = []
        self.sprites8 = []
        self.sprites9 = []
        self.sprites10 = []
        self.place = []
        self.color = {}
        self.keys = 0
        self.spritesall =[]
    def read(self, file, level):
        with open((f'Images/{file}.txt'), 'rt') as f:
            for line in f:
                    line = line.split(',')
                    if line[0] == '#':
                        pass
                    elif line[0] == '\n':
                        pass
                    else:
                        key.add(int(line[0]), int(line[1]), int(line[2]), int(line[3],), level)
                        self.color[self.number] = int(line[4])
                        self.number += 1
    def add(self, x, y, width, height, level):
        self.level = level
        rect = [x, y, width, height, self.number]
        if self.level == 0:
            self.sprites0.append(rect)
        if self.level == 1:
            self.sprites1.append(rect)
        if self.level == 2:
            self.sprites2.append(rect)
        if self.level == 3:
            self.sprites3.append(rect)
        if self.level == 4:
            self.sprites4.append(rect)
        if self.level == 5:
            self.sprites5.append(rect)
        if self.level == 6:
            self.sprites6.append(rect)
        if self.level == 7:
            self.sprites7.append(rect)
        if self.level == 8:
            self.sprites8.append(rect)
        if self.level == 9:
            self.sprites9.append(rect)
        if self.level == 10:
            self.sprites10.append(rect)
        self.spritesall = [self.sprites0,self.sprites1,self.sprites2,self.sprites3,self.sprites4,self.sprites5,
        self.sprites6,self.sprites7,self.sprites8,self.sprites9,self.sprites10]
    def check(self, level):
        self.level = level
        self.place.clear()
        if self.level == 0:
            for sprite in self.sprites0:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 1:
            for sprite in self.sprites1:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 2:
            for sprite in self.sprites2:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 3:
            for sprite in self.sprites3:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 4:
            for sprite in self.sprites4:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 5:
            for sprite in self.sprites5:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 6:
            for sprite in self.sprites6:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 7:
            for sprite in self.sprites7:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 8:
            for sprite in self.sprites8:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 9:
            for sprite in self.sprites9:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color)
        if self.level == 10:
            for sprite in self.sprites10:
                new_color = self.color[sprite[4]]
                key.rectangle_draw(sprite, new_color) 
    def rectangle_draw(self,sprite, new_color):
        number = sprite[4]
        try:
            color = colors[new_color]
        except: 
            color = rec_images[new_color]
        originalx = sprite[0]
            
            
        sprite = pygame.Rect(sprite[0], sprite[1], sprite[2], sprite[3])
        sprite = camera.apply(sprite)

        self.place.append(sprite)
            
                        
                        
                
        try: 
            win.blit(color, sprite)
        except:
            color = pygame.transform.scale(color, (sprite[2], sprite[3]))
            pygame.draw.rect(win, color, sprite)
        
class Levels:
    def __init__(self):
        self.level0 = False
        self.level1 = True
        self.level2 =False
        self.level3 = False
        self.level4 = False
        self.level5 = False
        self.level6 = False
        self.level7 = False
        self.level8 = False
        self.level9 = False
        self.level10 = False
        self.levelrun = True
    def check(self):
        if self.level0:
            levels.levels0()
        elif self.level1:
            levels.levels1()
        elif self.level2:
            levels.levels2()
    def levels1(self):
        camera.change(9000,2000)
        win.blit(bg, (0,0))
        inter.check(1)
        rec.draw(1)
        jump_draw()
        exits.check(1)
        mobs.check(1)
        key.check(1)
        camera.update(player.x, player.y)
        player.draw() 
        
    def levels2(self):
        camera.change(9000,2000)
        win.blit(bg, (0,0))
        inter.check(2)
        rec.draw(2)
        jump_draw()
        exits.check(2)
        mobs.check(2)
        key.check(2)
        camera.update(player.x, player.y)
        player.draw()
       
    def levels0(self):
        bg = pygame.image.load("Backgrounds/green-grass-background_1373-334.jpg")
        bg = pygame.transform.scale(bg, (1400, 800))
        camera.change(1700,1800)
        win.fill(DARKGREEN, (0,0,win_width,win_height))
        inter.check(0)
        rec.draw(0)
        exits.check(0)
        mobs.check(0)
        key.check(0)
        camera.update(player.x, player.y)
        player.draw()
       
def collisionx(t, test=False):
    check = False
    for item in rec.ground:
        item = rec.ground.index(item)
# left # right
        if rec.ground[item][0] < player.spritex + 100 + player.distance*t and rec.ground[item][0] + rec.ground[item][2] > player.spritex + player.leftcut+ player.distance*t:
# above #below # player above below
            if player.spritey + 20 < rec.ground[item][1] + rec.ground[item][3] and player.spritey + player.height > rec.ground[item][1]:
                check = True
                break
    return check
def collisiony(t, test=True):
    check = False
    for item in rec.ground:
        item = rec.ground.index(item)
        if rec.ground[item][0] < player.spritex + 100  and rec.ground[item][0] + rec.ground[item][2] > player.spritex + 30:
            if player.spritey + 20 < rec.ground[item][1] + rec.ground[item][3] and player.spritey + player.height + player.up> rec.ground[item][1]:
  
                check = True
                if player.spritey + player.height + 2 < rec.ground[item][1] and test:
                    player.y += 2
 
                break

    return check
def collision_jump():
    check = True
    for item in rec.ground:
        item = rec.ground.index(item)
        if player.spritey  >= rec.ground[item][1] + rec.ground[item][3] and rec.ground[item][0] < player.spritex + player.width + 20 and rec.ground[item][0] + rec.ground[item][2] > player.spritex-10:
            if player.spritey - player.up < rec.ground[item][1] + rec.ground[item][3]:
                check = False
                break
    return check
def collision0():
    check = False
    for item in rec.ground:
            if item.colliderect(player.hitbox):
                check = True
    return check
def jump_draw():
    if player.jump and collision_jump():
        if player.jumpcount >= player.jumplimit:
            neg = -1

            player.y += player.up *neg
            player.jumpcount -= 1
            player.up -= 1
        elif player.jumpcount < player.jumplimit:
            player.jumpcount = -6
            player.jump = False
            player.cooldown_jump = 30
            player.jump_bool = False
        
    if player.jump and not(collision_jump()):
        player.jump = False
        player.jumpcount = -6
        player.cooldown_jump = 30
        player.jump_bool = False
    
    
        
    
    if not(collisiony(player.down)) and not(player.jump):
        player.y += player.up
        if player.up != 20:
            player.up +=1
        

        
def redraw():
    if not(game.intro) and game.move and not(game.talk):
        levels.check()
    else:
        game.check()
    pygame.display.update()
    
    
camera = Camera()
rec = rectangle()
player = player()
game = Text()
levels = Levels()
exits = Exits()
mobs = Mobs()
key = Keys()
inter = Interact()
image = Images()
while levels.levelrun:
    game.intro = True
    game.run = True
    rec.spritesall.clear()
    exits.spritesall.clear()
    mobs.spritesall.clear()
    key.spritesall.clear()
    inter.spritesall.clear()
    
    rec.sprites0.clear()
    rec.sprites1.clear()
    rec.sprites2.clear()
    rec.sprites3.clear()
    rec.sprites4.clear()
    rec.sprites5.clear()
    rec.sprites6.clear()
    rec.sprites7.clear()
    rec.sprites8.clear()
    rec.sprites9.clear()
    rec.sprites10.clear()
    
    exits.sprites0.clear()
    exits.sprites1.clear()
    exits.sprites2.clear()
    exits.sprites3.clear()
    exits.sprites4.clear()
    exits.sprites5.clear()
    exits.sprites6.clear()
    exits.sprites7.clear()
    exits.sprites8.clear()
    exits.sprites9.clear()
    exits.sprites10.clear()
    
    mobs.sprites0.clear()
    mobs.sprites1.clear()
    mobs.sprites2.clear()
    mobs.sprites3.clear()
    mobs.sprites4.clear()
    mobs.sprites5.clear()
    mobs.sprites6.clear()
    mobs.sprites7.clear()
    mobs.sprites8.clear()
    mobs.sprites9.clear()
    mobs.sprites10.clear()
    
    key.sprites0.clear()
    key.sprites1.clear()
    key.sprites2.clear()
    key.sprites3.clear()
    key.sprites4.clear()
    key.sprites5.clear()
    key.sprites6.clear()
    key.sprites7.clear()
    key.sprites8.clear()
    key.sprites9.clear()
    key.sprites10.clear()
    
    inter.sprites0.clear()
    inter.sprites1.clear()
    inter.sprites2.clear()
    inter.sprites3.clear()
    inter.sprites4.clear()
    inter.sprites5.clear()
    inter.sprites6.clear()
    inter.sprites7.clear()
    inter.sprites8.clear()
    inter.sprites9.clear()
    inter.sprites10.clear()
    rec.read('0', 0)
    exits.read('0E', 0)
    #mobs.read('0M', 0)
    rec.read('1', 1)
    exits.read('1E', 1)
    mobs.read('1M', 1)
    rec.read('2', 2)
    exits.read('2E', 2)
    mobs.read('2M', 2)
    
    key.read('Keys', 1)
    key.read('Keys2', 2)
    #inter.read('Inter0', 0)
    inter.read('Inter1', 1)
    inter.read('Inter2', 2)
    player.health = 10
    key.keys = 0
    levels.level0 = True
    levels.level1 = False
    levels.level2 =False
    levels.level3 = False
    levels.level4 = False
    levels.level5 = False
    levels.level6 = False
    levels.level7 = False
    levels.level8 = False
    levels.level9 = False
    levels.level10 = False
    player.x = 850
    player.y = 1250
    player.jump_bool = False
    player.cooldown_jump = 0
    player.right = False
    player.left = False
    player.standing = False
    player.jump = False

    



    while game.run:
        clock.tick(35)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False
                levels.levelrun= False
        if game.move and rec.level != 0 and player.move and not(player.stop):           
            if keys[pygame.K_d]:
                player.vel = 15
                if player.attack:
                    player.vel = 10


                if not(collisionx(player.vel)):
                    player.x += player.vel
                    player.right = True
                    player.left= False
                    player.standing = False
                else: 
                    pass
            if keys[pygame.K_a]:
                player.vel = -15
                if player.attack:
                    player.vel = -10

                if not(collisionx(player.vel)):
                    player.x += player.vel
                    player.standing = False
                    player.left = True
                    player.right = False
                else: 

                    pass
            if keys[pygame.K_f]:
                player.interact = True
            else:
                player.interact = False
            if not(keys[pygame.K_a]) and not(keys[pygame.K_d]):
                player.standing = True




            if player.cooldown_jump != 0:
                player.cooldown_jump -= 1

            else:
                if keys[pygame.K_SPACE] and not(player.jump_bool):

                    player.up = 20
                    player.jump = True
                    player.standing = False
                    player.jump_bool = True
            if keys[pygame.K_LSHIFT]:
                player.attack = True






        elif rec.level == 0 and game.move:
            
            player.stop = False
            if keys[pygame.K_d]:
                player.vel = 8

                if not(collisionx(player.vel)):
                    player.x += player.vel
                    player.right = True
                    player.left= False
                    player.standing = False
                    player.s = False
                    player.up0 = False
                else: 
                    pass
            elif keys[pygame.K_a]:
                player.vel = -8

                if not(collisionx(player.vel)):
                    player.x += player.vel
                    player.standing = False
                    player.left = True
                    player.right = False
                    player.s = False
                    player.up0 = False
                else: 
                    pass

            elif keys[pygame.K_w]:
                player.vel = -8

                if not(collision0()):
                    player.y += player.vel
                    player.standing = False
                    player.left = False
                    player.right = False
                    player.s = False
                    player.up0 = True
                else: 
                    pass
            elif keys[pygame.K_s]:
                player.vel = 8

                if not(collisiony(player.vel)):
                    player.y += player.vel
                    player.standing = False
                    player.left = False
                    player.right = False
                    player.up0 = False
                    player.s = True
                else: 
                    pass

            if keys[pygame.K_f]:
                player.interact = True
            else:
                player.interact = False
            if not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and not(keys[pygame.K_s]) and not(keys[pygame.K_w]):
                player.standing = True





        if not(game.move):
            if keys[pygame.K_TAB]:
                player.stoptext = True
            else:
                player.stoptext = False
        if keys[pygame.K_r]:
            game.run = False
            

        redraw()


pygame.quit()