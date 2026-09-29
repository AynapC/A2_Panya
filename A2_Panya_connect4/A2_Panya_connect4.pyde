grid_collum = 7
grid_rows = 6

size_ = 80
off_x = 50
off_y = 50

current_player = 1
game_over = False
winner = 0

board = []

def setup():
    size(650, 650)
    init_board()
    #print(board)
    
def draw():
    background(240)
    draw_board(0, 0)

### create 2d array for game check ###

def init_board():
    global board, current_player, game_over, winner
    board = create_2D_array(grid_collum, grid_rows)
    current_player = 1
    game_over = False
    winner = 0
    
def create_2D_array(cols, rows):
    if cols == 0:
        return []
    return [create_1D_array(rows)] + create_2D_array(cols - 1, rows)

def create_1D_array(length):
    if length == 0:
        return []
    return [0] + create_1D_array(length - 1)

### end section maybeee ###

### draw borad ###

def draw_board(cols, rows):
    if cols == grid_collum:
        return
    
    if rows == grid_rows:
        draw_board(cols + 1, 0)
        return
    
    draw_cell(cols, rows)
    draw_board(cols, rows + 1)
    
def draw_cell(cols, rows):
    x = off_x + (cols * size_)
    y = off_y + (rows * size_)
    
    stroke(0)
    strokeWeight(2)
    noFill()
    
    rect(x, y, size_, size_)
    
### end ###
'''
    ### draw coin ###
    
    if board[cols][rows] == 1:
        fill(0)
        ellipse(x + size_/2, y + size_/2, 60, 60)
        
    elif board[cols][rows] == 2:
        fill(255)
        ellipse(x + size_/2, y + size_/2, 60, 60)
        
### drop coin ###

def mousePressed():
    if mouseX >= off_x and mouseX < off_x + grid_collum * size_:
        cols = int((mouseX - off_x)/ size_)
        drop_coin(cols)
    
def drop_coin(cols):
    rows = grid_rows - 1
    while rows >= 0:
        if board[cols][rows] == 0:
            board[cols][rows] = current_player
            return
        rows -= 1
