import random

'''
This is a code for the game. 
The new features of the game are as follows:
    1) Everything has been written in the form of classes
    2) The user now can chose the value of n. It can be 4 or 5.
'''

'''The following is a class of constants that will 
be useful for the User Interface (UI)'''

class Constants:
    def __init__(self,n):
        self.S = 400
        self.length = n
        self.pad = 10
        
        self.back_color = "#92877d"
        self.empty_cell_color = "#9e948a"
        self.back_color_dict = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                                 16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                                 128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                                 1024: "#edc53f", 2048: "#edc22e",
    
                                 4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179",
                                 32768: "#f59563", 65536: "#f67c5f", }
        
        self.font_color_dict = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                           32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
                           256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
                           2048: "#f9f6f2",
    
                           4096: "#776e65", 8192: "#f9f6f2", 16384: "#776e65",
                           32768: "#776e65", 65536: "#f9f6f2", }
        
        self.FONT = ("Verdana", 40, "bold")
        self.KEY_UP = "'w'"
        self.KEY_DOWN = "'s'"
        self.KEY_LEFT = "'a'"
        self.KEY_RIGHT = "'d'"
        
        
''' 
The following is a class of Functions which is important for the game 
'''     
class Logics:
    def __init__(self,n):
        self.n = n
        #self.mat = []
        
    def start_game(self):
        mat = []
        for i in range(self.n):
            mat.append([0]*self.n)
        return mat
    
    
    def add_two(self,matrix):
        r = random.randint(0,self.n-1)
        c = random.randint(0,self.n-1)
        while (matrix[r][c]!=0):
            r = random.randint(0,self.n-1)
            c = random.randint(0,self.n-1)
        matrix[r][c]=2
        
    
    def check_status(self,matrix):
        # if 2048 is present --> Win
        for i in range(self.n):
            for j in range(self.n):
                if matrix[i][j]==2048:
                    return 'You Won!'
        
        # if zero is present anywhere --> game is still going on
        for i in range(self.n):
            for j in range(self.n):
                if matrix[i][j]==0:
                    return 'Game not over'
        
        # if there are equal numbers present adjacently in the places 
        # except the right and bottom column
        for i in range(self.n-1):
            for j in range(self.n-1):
                if (matrix[i][j]==matrix[i+1][j]) or (matrix[i][j]==matrix[i][j+1]):
                    return 'Game not over'
       
        # bottom row
        for j in range(self.n-1):
            if (matrix[self.n-1][j]==matrix[self.n-1][j+1]):
                return 'Game not over'
        
        # right column 
        for i in range(self.n-1):
            if (matrix[i][self.n-1]==matrix[i+1][self.n-1]):
                return 'Game not over'
        
        # if none of the above are true then the user has lost the game
        return 'You lose!'
    
    # Merge function 
    def Merge(self,matrix):
        change = False
        for i in range(self.n):
            for j in range(self.n-1):
                if matrix[i][j]==matrix[i][j+1] and matrix[i][j]!=0:
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i][j+1]=0
                    change = True
        return matrix,change
    
    
    
    # Compress function
    def Compress(self,matrix):
        # creating a new matrix of zeros
        new_mat = []
        change = False
        for i in range(self.n):
            new_mat.append([0]*self.n)
        for i in range(self.n):
            pos = 0
            for j in range(self.n):
                if matrix[i][j]!=0:
                    new_mat[i][pos] = matrix[i][j]
                    if j!=pos:
                        change = True
                    pos+=1
        # The variable - change will tell us whether the board has changed or not
        # after the compression/merging has been executed
        # if there is a change, then we can add a 2 at a random location in the board
        return new_mat,change
        
    
    # Reverse function
    def Reverse(self,matrix):
        new_mat = []
        for i in range(self.n):
            new_mat.append([])
            for j in range(self.n):
                new_mat[i].append(matrix[i][(self.n-1)-j])
        return new_mat
                
    
    # Transpose function
    def Transpose(self,matrix):
        new_mat = []
        for i in range(self.n):
            new_mat.append([])
            for j in range(self.n):
                #print(f"The new matrix is: {new_mat}. The value of i and j are: {i}, {j}")
                new_mat[i].append(matrix[j][i])
        return new_mat
    
    # The following functions are for several moves the user can make
    def move_left(self,matrix):
        new_mat,change1 = self.Compress(matrix)
        new_mat,change2 = self.Merge(new_mat)
        change = change1 or change2
        new_mat,temp = self.Compress(new_mat)
        return new_mat,change
    
    def move_right(self,matrix):
        new_mat = self.Reverse(matrix)
        new_mat,change1 = self.Compress(new_mat)
        new_mat,change2 = self.Merge(new_mat)
        change = change1 or change2
        new_mat,temp = self.Compress(new_mat)
        new_mat = self.Reverse(new_mat)
        return new_mat,change
    
    def move_up(self,matrix):
        new_mat = self.Transpose(matrix)
        new_mat,change1 = self.Compress(new_mat)
        new_mat,change2 = self.Merge(new_mat)
        change = change1 or change2
        new_mat,temp = self.Compress(new_mat)
        new_mat = self.Transpose(new_mat)
        return new_mat,change
    
    
    def move_down(self,matrix):
        new_mat = self.Transpose(matrix)
        new_mat = self.Reverse(new_mat)
        new_mat,change1 = self.Compress(new_mat)
        new_mat,change2 = self.Merge(new_mat)
        change = change1 or change2
        new_mat,temp = self.Compress(new_mat)
        new_mat = self.Reverse(new_mat)
        new_mat = self.Transpose(new_mat)
        return new_mat,change
  
from tkinter import Frame, Label, CENTER

# The following class is a child of three classes :
# 1) Frame, 2) Logics, 3) Constants


class Game_2048(Frame,Logics,Constants):
    # constructor function containing all the functions necessary
    # for the game
    def __init__(self,n):
        # create an empty grid from Frame object
        # in other words we are inheriting the properties of Frame class
        
        Frame.__init__(self)
        self.grid()
        
        Constants.__init__(self,n)
        Logics.__init__(self,n)
        
        # Title of the game
        self.master.title('GAME 2048')
        
        # When any key is pressed call the key_down function
        self.master.bind("<Key>",self.key_down)
        
        # commands that connect the keys --> w,a,s,d to move_up,move_dwon
        # move_left, and move_right respectively
        self.commands = {self.KEY_UP:self.move_up, self.KEY_DOWN:self.move_down,
                         self.KEY_LEFT:self.move_left,self.KEY_RIGHT:self.move_right}
        
        # initializing the cells of the grid as empty list
        self.grid_cells = []
        
        # function to construct an inner frame inside the outer frame
        # which will have grids with labels and appropriate background colors
        self.init_grid()
        
        # function to start the game and add two 2's at random locations
        self.init_matrix()
        
        # function to update the cell's color, whenever changes are made. 
        # These changes will be made in the UI
        self.update_cells()
        
        # to run the program 
        self.mainloop()
        
    
    def init_grid(self):
        # creating an inner frame
        background = Frame(self,bg = self.back_color,width = self.S, height = self.S)
        background.grid()
        
        for i in range(self.length):
            grid_row = []
            for j in range(self.length):
                cell = Frame(background, bg = self.empty_cell_color,
                             width = (self.S//self.length), height = (self.S//self.length))
                # the cell is frame class
                # it has a function to adjust the padding
                cell.grid(row=i,column=j,padx = self.pad,pady = self.pad)
                
                # calling the label class to set the default settings for the label
                text = Label(master=cell,text="",bg=self.empty_cell_color,
                             justify=CENTER,font=self.FONT, width = 5, height = 2)
                
                text.grid()
                
                # appending this text to the grid_row list
                grid_row.append(text)
        
            # appending the each grid row into the grid_cell.
            # grid rows will populate the grid_cell and make it filled up with either text values
            # or empty backgrounds
            self.grid_cells.append(grid_row)
        
    def init_matrix(self):
        self.matrix = self.start_game()
        self.add_two(self.matrix)
        self.add_two(self.matrix)
    
    def update_cells(self):
        for i in range(self.length):
            for j in range(self.length):
                new_num = self.matrix[i][j]
                if new_num==0:
                    self.grid_cells[i][j].configure(text='',bg=self.empty_cell_color)
                else:
                    self.grid_cells[i][j].configure(text=str(new_num),
                                                    bg = self.back_color_dict[new_num],
                                                    fg = self.font_color_dict[new_num])
        
        # to wait till all the colors and texts are filled
        self.update_idletasks()
    
    def key_down(self,pressed_key):
        key = repr(pressed_key.char)
        
        # only if the key is w,a,s,d do the following
        # if not do nothing
        if key in self.commands:
            
            # to find out the output for the move_up/move_down/move_left/move_right functions
            self.matrix, change = self.commands[key](self.matrix)
            
            if change is True:
                # add 2 and update the cells
                self.add_two(self.matrix)
                self.update_cells()
                
                # re-intialize change to False
                change = False
                
                # check if the user has won or lost
                if self.check_status(self.matrix)=='You Won!':
                    self.grid_cells[1][1].configure(text='YOU', bg = self.empty_cell_color)
                    self.grid_cells[1][2].configure(text='WIN!', bg = self.empty_cell_color)
                
                if self.check_status(self.matrix)=='You lose!':
                    self.grid_cells[1][1].configure(text='YOU', bg = self.empty_cell_color)
                    self.grid_cells[1][2].configure(text='LOSE!', bg = self.empty_cell_color)

     
#---------------------------------------------------------------------------------------------------#    
# Run the game

n = int(input())
if n==4 or n==5:
    
    g = Game_2048(n)
else:
    print('Please choose any number from the numbers: 4 and 5')
    n = int(input())
    g = Game_2048(n)
         