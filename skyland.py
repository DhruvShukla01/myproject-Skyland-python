# cse30
# pa5
# skyland.py - a one-level platform video game
# author: Dhruv Shukla
# date: 9 June, 2023

from tkinter import *
import tkinter.font as font
from random import random, randint # optional
import math
from math import sin, cos, pi, radians # optional
import time
#from pygame import mixer # do not use it in the submitted version

WIDTH, HEIGHT = 600, 400 # global variables (constants) go here
CLOCK_RATE = 15
START_X, START_Y = 20, 350
END_X, END_Y = 400, 350

class Skyland:
    
    def __init__(self, canvas):
        
        self.canvas = canvas
        self.paused = False 
        self.canvas.bind_all('<KeyPress-space>', self.pause)
        # self.canvas.bind_all('<KeyPress-Alt_L>', self.restart)
        self.canvas.bind_all('<KeyPress-r>', self.restart)
        self.game_con = False
        self.game_over_text = None
        self.restart_button = None
        self.start_time = time.time()
        self.land = Land(canvas)
        self.trophy = Trophy(canvas)
        self.obstacles = self.land.create_obstacles()
        self.ai = AI(canvas,110,110)
        self.ai_2 = AI(canvas,400,200)
        self.avatar = Avatar(canvas, self.obstacles)
        self.score = 0
        self.text = canvas.create_text(150, 370, text=f'Score:{self.score}  Time ? ',
                                       font=font.Font(family='Helveca', size='15', weight='bold'))

        #self.play_music() # do not include it in the submitted version
        while self.score < 3:
            self.update()
            break

    def restart(self, event=None):# Reset the avatar's position
        self.trophy.replace()  # Reset the trophy's position

        self.start_time = time.time()  # Reset the start time
        self.score = 0  # Reset the score

        self.paused = False  # Unpause the game

        self.canvas.delete(self.text)  # Delete the current score and time display
        self.text = self.canvas.create_text(150, 370, text='Score: ?  Time: ?',
                                            font=font.Font(family='Helveca', size=15, weight='bold'))  # Create a new score and time display



        
    def pause(self, event=None):
        if self.paused:
            self.paused = False
            self.update()  # Resume the game
        else:
            self.paused = True

    def update_score(self):

        self.score+=1
    def update_time(self):
        elapsed_time = round(time.time() - self.start_time)
        self.canvas.itemconfig(self.text, text='Score: ' + str(self.score) + '  Time: ' + str(elapsed_time))
        self.canvas.after(1000, self.update_time)  # Update time display every 1 second (1000 milliseconds)

    def update(self):
        if not self.paused:
            print(self.trophy)
            print(type(self.trophy))
            self.avatar.update(self.land, self.trophy)
            self.ai.update(5,100)
            self.ai_2.update(5,200)
            self.update_time()
            if self.avatar.collision_spider(self.ai) or self.avatar.collision_spider(self.ai_2):
                self.paused = True

                # self.game_con =True
            if self.game_con == True:
                self.canvas.delete(self.text)
                self.pause
                self.text.delete()
                self.text = canvas.create_text(150, 370, text=f' You Died',
                                       font=font.Font(family='Helveca', size='15', weight='bold'))

                self.restart()
            if self.avatar.collision_trophy(self.trophy):
                self.update_score()
            if Trophy.len_troph == self.score:
                self.text = canvas.create_text(150, 370, text=f' You Win',
                                       font=font.Font(family='Helveca', size='15', weight='bold'))
                self.pause()
                self.restart()
            self.canvas.after(CLOCK_RATE, self.update)
class Land():
    
    def __init__(self, canvas):

        self.canvas = canvas

        # sky
        self.canvas.create_rectangle( 0, 0, WIDTH, START_Y-100,
                                 fill='lightblue')
        # valley
        self.canvas.create_rectangle( 0, START_Y-120, WIDTH, START_Y,
                                 fill='tan4')
        
        self.make_hill( 50, 230, 250, 230, height=100, delta=3)
        self.make_hill(150, 300, 350, 300, height=100, delta=3)
        self.make_hill(250, 250, 450, 250, height=100, delta=3)
        self.make_hill(350, 300, 550, 300, height=100, delta=3)

        cloud1 = self.make_cloud(100, 120)
        cloud2 = self.make_cloud(200, 140)
        cloud3 = self.make_cloud(300, 80)
        self.clouds = [cloud1, cloud2, cloud3]

    def make_hill(self, x1, y1, x2, y2, height=100, delta=3):

        square_size = 5


        num_cols = 50
        num_rows = height

        # Create the first square
        for row in reversed(range(num_rows)):
            squares_to_remove = row
            
            # Calculate the starting and ending column indices
            start_col = squares_to_remove
            end_col = num_cols - squares_to_remove
            
            
            # Iterate over columns within the adjusted start_col and end_col range
            for col in range(start_col, end_col):
                # Calculate the coordinates of the current square
                sq_x1 = x1 + col * square_size
                sq_y1 = y1 - row * square_size
                sq_x2 = sq_x1 + square_size 
                sq_y2 = sq_y1 + square_size
                # Create the square
                if row>= 18:
                    self.canvas.create_rectangle(sq_x1, sq_y1, sq_x2, sq_y2, fill="gray95", outline='gray95')
                else:
                   self.canvas.create_rectangle(sq_x1, sq_y1, sq_x2, sq_y2, fill="gray50", outline='gray69') 

    def make_cloud(self, x, y):
        radius = 15
        cloud_parts = []
        y_new = y + 10
        for i in range(3):
            cloud_part = self.canvas.create_oval(x - radius + i * radius * 0.8 + 15, y - radius- 18,
                                                x + radius + i * radius * 0.8 + 15+3, y + radius-18,
                                                fill='white', outline='black')
            cloud_parts.append(cloud_part)
       
        for i in range(5):
            cloud_part = self.canvas.create_oval(x - radius + i * radius * 0.8, y - radius,
                                                x + radius + i * radius * 0.8+3, y + radius,
                                                fill='white', outline='black')
            cloud_parts.append(cloud_part)
        for i in range(3):
            cloud_part = self.canvas.create_oval(x - radius + i * radius * 0.8 + 15, y - radius + 18,
                                                x + radius + i * radius * 0.8 + 15+3, y + radius + 18 , fill='white', outline='black')


            cloud_parts.append(cloud_part)
        return cloud_parts
    
    def create_obstacles(self):
        obstacles = []
        x_temp = START_X
        y_temp = START_Y
        # Add the ground as an obstacle
        ground = self.canvas.create_line(0, y_temp, WIDTH, y_temp, fill='black', width=10)
        obstacles.append(ground)
        print(self.canvas.coords(ground))
        print(obstacles[0])

        # Add horizontal obstacles
        obstacle_width = 100
        obstacle_height = 30
        obstacle_gap = 200
        num_obstacles = 2

        obstacle_x = (x_temp+ 0 * obstacle_gap) + 250
        obstacle_y = (y_temp - obstacle_height) // 2
        obstacle = self.canvas.create_rectangle(obstacle_x, obstacle_y+100, obstacle_x + obstacle_width, obstacle_y + obstacle_height+100, fill='Brown',outline='black')
        obstacles.append(obstacle)
        obstacle_width = 40
        obstacle_height = 60
        obstacle_gap = 100
        obstacle_x = (x_temp ) + 210
        obstacle_y = (y_temp - obstacle_height) - 30 
        obstacle = self.canvas.create_rectangle(obstacle_x, obstacle_y, obstacle_x + obstacle_width, y_temp, fill='Brown',outline='black')
        obstacles.append(obstacle)
        obstacle_x = (x_temp + 0 * obstacle_gap) + 250
        obstacle_width = 100
        obstacle_height = 20
        obstacle_gap = 200
        num_obstacles = 2
        obstacle = self.canvas.create_rectangle(obstacle_x, obstacle_y+70, obstacle_x + obstacle_width, obstacle_y + obstacle_height+70, fill='Brown', outline='black')
        obstacles.append(obstacle)
        obstacle_width = 5
        obstacle_height = 100
        obstacle = self.canvas.create_rectangle(obstacle_x, obstacle_y-90, obstacle_x + obstacle_width, y_temp-90, fill='Brown',outline='black')
        obstacles.append(obstacle)
        obstacle_x = 0
        obstacle_y = 280
        obstacle_width = 600
        obstacle_height = 10
        obstacle_gap = 200
        obstacle = self.canvas.create_rectangle(obstacle_x, obstacle_y+70, obstacle_x + obstacle_width, obstacle_y + obstacle_height+70, fill='Brown', outline='black')
        obstacles.append(obstacle)


        return obstacles



    def get_obstacles(self):
        return [self.ground, self.start, self.stop] + self.platforms
    
    def update(self):
        pass
    
class Trophy:
    len_troph = 0
    def __init__(self, canvas):
        self.trophies = []
        
        self.canvas = canvas
        purple_egg = self.canvas.create_oval(400, 330, 450, 350, fill='orchid')
        self.trophies.append(purple_egg)
        pink_egg = self.canvas.create_oval(200, 200, 250, 230, fill='pink')
        self.trophies.append(pink_egg)
        red_egg = self.canvas.create_oval(300,230,350,260, fill='red')
        self.trophies.append(red_egg)
        Trophy.len_troph = len(self.trophies)
        
    def get_trophy(self):
        return self.trophies

    def replace(self):
        for trophy in self.trophies:
            self.canvas.delete(trophy)
        purple_egg = self.canvas.create_oval(400, 330, 450, 350, fill='orchid')
        self.trophies.append(purple_egg)
        pink_egg = self.canvas.create_oval(200, 200, 250, 230, fill='pink')
        self.trophies.append(pink_egg)
        red_egg = self.canvas.create_oval(300, 230, 350, 260, fill='red')
        self.trophies.append(red_egg)

    def del_trophy(self):
        self.trophies.pop(0)
    def is_empty(self):
        return len(self.trophies) == 0
class AI:

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.web = self.make_web(x, y)
        self.spider = self.make_spider(x, y)
        self.thread = self.canvas.create_line(x + 10, 0, x + 10, y + 5,
                                              fill='ivory2', width=3)
        self.x, self.y = 0, 0.5
        self.canvas_width = canvas.winfo_width()
        self.canvas_height = canvas.winfo_height()
        self.con = False

    def make_spider(self, x, y):
        color1 = 'black'
        head = self.canvas.create_oval(5, 5, 15, 13, fill=color1)
        torso = self.canvas.create_oval(0, 10, 20, 40, fill=color1)
        legs = [self.canvas.create_line(-5 - i * 5, 10 * i + 5, 5, 10 * i + 15,
                                        fill=color1, width=4) for i in range(2)] + \
               [self.canvas.create_line(15, 10 * i + 15, 25 + i * 5, 10 * i + 5,
                                        fill=color1, width=4) for i in range(2)] + \
               [self.canvas.create_line(-10 + i * 5, 10 * i + 35, 5, 10 * i + 25,
                                        fill=color1, width=4) for i in range(2)] + \
               [self.canvas.create_line(15, 10 * i + 25, 30 - i * 5, 10 * i + 35,
                                        fill=color1, width=4) for i in range(2)]

        spider = [head, torso] + legs
        for part in spider:
            self.canvas.move(part, x, y)
        return spider


    def make_web(self, x, y, radius=50, num_lines=24):
            color = "red"  # Gray color
            self.canvas.create_oval(x - radius+10, y - radius+10, x + radius+10, y + radius+10, outline=color, width=2)

            angle_increment = 360 / num_lines

            for i in range(num_lines):
                angle = math.radians(i * angle_increment)
                x1 = x + int(radius * math.cos(angle))
                y1 = y + int(radius * math.sin(angle))

                self.canvas.create_line(x+10, y+10, x1+10, y1+10, fill=color, width=2)
    def move (self, X, Y):
        tallspider = self.canvas.coords(self.spider [0])[1]
        if tallspider <= X:
            self.con = False
        elif tallspider >= Y:
            self.con = True

        if not self .con:
            self.y = 5
        else:
            self.y = -5

        for part in self.spider:
            self.canvas .move (part, self.x, self.y)


    def update(self, X,Y):
        # Update spider's position
        spider_head = self.spider[0]
        spider_torso = self.spider[1]
        spider_legs = self.spider[2:]

        spider_head_coords = self.canvas.coords(spider_head)
        spider_torso_coords = self.canvas.coords(spider_torso)

        spider_head_x, spider_head_y = spider_head_coords[0], spider_head_coords[1]
        spider_torso_x, spider_torso_y = spider_torso_coords[0], spider_torso_coords[1]

        if spider_head_x <= 0 or spider_head_x >= self.canvas_width:
            self.x *= -1  # Reverse horizontal direction if spider reaches canvas edge

        if spider_head_y <= 0 or spider_head_y >= self.canvas_height:
            self.y *= -1  # Reverse vertical direction if spider reaches canvas edge

        # Update spider's movement
        # self.x += random.uniform(-0.5, 0.5)  # Add random horizontal movement
        # self.y += random.uniform(-0.5, 0.5)  # Add random vertical movement

        self.move(X,Y)  # Move the spider by updating the coordinates



class Avatar:
    
    def __init__(self, canvas, obstacles):

        color1 = 'lime'
        color2 = 'sandybrown'
        self.bit_vec = ['False','False','False','False']
        self.canvas = canvas
        self.head = self.canvas.create_oval(0, 0-10, 10, 0, fill=color2)
        self.torso = self.canvas.create_rectangle(0, 0, 10, 10,
                                                  fill=color1)
        self.canvas.move(self.head, START_X, START_Y-20)
        self.canvas.move(self.torso, START_X, START_Y-20)
        self.canvas.bind_all('<KeyPress-Left>', self.move)
        self.canvas.bind_all('<KeyPress-Right>', self.move)
        self.canvas.bind_all('<KeyPress-Up>', self.move)
        self.canvas.bind_all('<KeyPress-Down>', self.move)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop)
        self.obstacles_n = obstacles


        self.x = 0
        self.y = 0
    
    # Inside the update method of the Avatar class
    def check_boundary(self):
        avatar_coords = self.canvas.coords(self.head)
        x1, y1, x2, y2 = avatar_coords
        avatar_width = x2 - x1
        avatar_height = y2 - y1

        if x1 < 0:
            self.x = abs(self.x)  # Move away from the left wall
        if x2 > WIDTH:
            self.x = -abs(self.x)  # Move away from the right wall
        if y1 < 0:
            self.y = abs(self.y)  # Move away from the top wall
        if y2 > HEIGHT:
            self.y = -abs(self.y)  # Move away from the bottom wall

        # Adjust avatar position to stay within boundaries
        if x1 < 0:
            self.x = 0  # Stop horizontal movement
            self.canvas.move(self.head, -x1, 0)
            self.canvas.move(self.torso, -x1, 0)
        if x2 > WIDTH:
            self.x = 0  # Stop horizontal movement
            self.canvas.move(self.head, WIDTH - x2, 0)
            self.canvas.move(self.torso, WIDTH - x2, 0)
        if y1 < 0:
            self.y = 0  # Stop vertical movement
            self.canvas.move(self.head, 0, -y1)
            self.canvas.move(self.torso, 0, -y1)
        if y2 > HEIGHT:
            self.y = 0  # Stop vertical movement
            self.canvas.move(self.head, 0, HEIGHT - y2)
            self.canvas.move(self.torso, 0, HEIGHT - y2)

    def update(self, land, trophy):
        self.y += 0.025

        # Check for collisions with obstacles
        for obj in self.obstacles_n:
            self.hit_object(obj)

        # Move the avatar
        self.canvas.move(self.head, self.x, self.y)
        self.canvas.move(self.torso, self.x, self.y)

        # Check for collision with trophy
        # if self.check_collision_trophy(trophy):
        #     self.score += 1
        #     self.update_score()

        # Check for collision with ground
        avatar_coords_torso = self.canvas.coords(self.torso)
        if avatar_coords_torso[3] >= START_Y:
            self.y = 0
        self.check_boundary()


    def replace(self):
        color1 = 'lime'
        color2 = 'sandybrown'
        self.bit_vec = ['False','False','False','False']
        self.canvas = canvas
        self.head = self.canvas.create_oval(0, 0-10, 10, 0, fill=color2)
        self.torso = self.canvas.create_rectangle(0, 0, 10, 10,
                                                  fill=color1)
        self.canvas.move(self.head, START_X, START_Y-20)
        self.canvas.move(self.torso, START_X, START_Y-20)
        self.canvas.bind_all('<KeyPress-Left>', self.move)
        self.canvas.bind_all('<KeyPress-Right>', self.move)
        self.canvas.bind_all('<KeyPress-Up>', self.move)
        self.canvas.bind_all('<KeyPress-Down>', self.move)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop)


        self.x = 0
        self.y = 0

    def move(self, event=None):
       
        if event.keysym == 'Left':
                self.x = -2
        if event.keysym == 'Right':
                self.x = 2
        if event.keysym == 'Up': # jumping
                self.y = -3
        if event.keysym == 'Down':
                self.y = 3
    def stop(self, event=None):
        if event.keysym == 'Left':
            self.x = 0
        elif event.keysym == 'Right':
            self.x = 0

   
    def hit_object(self, obj): # recommended
        
        torso_coords = self.canvas .coords (self.torso)
        torso_x1, torso_y1, torso_x2, torso_y2 = torso_coords
        obstacles = self.obstacles_n
        for obstacle in obstacles:
            object_x1, object_y1, object_x2, object_y2 = self .canvas. coords(obstacle)
            if torso_x2 >= object_x1 and torso_x1 <= object_x2 and torso_y2 >= object_y1 and torso_y1 <= object_y2:
                if torso_x1 < object_x1:
                    self.canvas.move(self.torso, -(torso_x2 - object_x1), 0) 
                    self.canvas.move(self. head, -(torso_x2 - object_x1), 0)
                elif torso_x2 > object_x2:
                    self.canvas.move(self.torso, object_x2 - torso_x1, 0)
                    self.canvas.move(self.head, object_x2 - torso_x1, 0)
                if torso_y1 < object_y1:
                    self.canvas.move(self.torso, 0, -(torso_y2 - object_y1)) 
                    self.canvas.move(self.head, 0, -(torso_y2 - object_y1))
                elif torso_y2 > object_y2:
                    self.canvas.move(self.torso, 0, object_y2 - torso_y1) 
                    self.canvas.move(self.head, 0, object_y2 - torso_y1)

        # condition 1: Right Collision:
        # if avatar_coords_torso[2]<= obj_coords[0] and ((obj_coords[3]<=avatar_coords_head[1]<=obj_coords[1]) or (obj_coords[3]<=avatar_coords_torso[3]<= obj_coords[1])):
        #     self.bit_vec[2] = 'True'
        # return self.bit_vec
    def collision_trophy(self, trophy):
        avatar_coords = self.canvas.coords(self.head)
        trophy_list = trophy.get_trophy()  # Retrieve the list of trophies
        for trophy_item in trophy_list:
            trophy_coords = self.canvas.coords(trophy_item)
            if len(trophy_coords) >= 4 and len(avatar_coords)>=4:
                x1_avatar, y1_avatar, x2_avatar, y2_avatar = avatar_coords
                x1_trophy, y1_trophy, x2_trophy, y2_trophy = trophy_coords
                if x2_avatar >= x1_trophy and x1_avatar <= x2_trophy and y2_avatar >= y1_trophy and y1_avatar <= y2_trophy:
                    self.canvas.delete(trophy_item)
                    return True
        return False
    def collision_spider(self, spider):
        avatar_coords = self.canvas.coords(self.torso)
        avatar_coords_head = self.canvas.coords(self.head) 
        spider_coords = self.canvas.coords(spider.spider[0])
        spider_bottom = self.canvas.coords(spider.spider[3]) 

        x1_avatar, y1_avatar, x2_avatar, y2_avatar = avatar_coords
        x1_head, y1_head,x2_head,y2_head = avatar_coords_head
        x1_spider, y1_spider, x2_spider, y2_spider = spider_coords
        x1_spider_bottom, y1_spider_bottom, x2_spider_bottom, y2_spider_bottom = spider_bottom

        if x2_avatar >= x1_spider and x1_avatar <= x2_spider and y2_avatar >= y1_spider and y1_avatar <= y2_spider or\
           x2_head >= x1_spider and x1_head <= x2_spider and y2_head >= y1_spider and y1_head <= y2_spider :
            return True
        if x2_avatar >= x1_spider and x1_avatar <= x2_spider and y2_avatar >= y1_spider and y1_avatar <= y2_spider or\
           x2_head >= x1_spider_bottom and x1_head <= x2_spider_bottom and y2_head >= y1_spider_bottom and y1_head <= y2_spider_bottom : 
            return True
        return False


    




    def find_trophy(self, trophy): # recommended
        pass


if __name__ == '__main__':
    
    tk = Tk()
    tk.title('Skyland')
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    canvas.pack()
    game = Skyland(canvas)
    mainloop()
