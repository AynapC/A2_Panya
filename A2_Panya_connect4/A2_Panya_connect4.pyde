grid_collum = 7
grid_rows = 6

size_ = 80
off_x = 50
off_y = 50

current_player = 1
game_over = False
winner = 0
draw_game = False

black_score = 0
white_score = 0

board = []

def setup():
    size(650, 650)
    init_board()
    #print(board)

def draw():
    background(240)
    draw_board(0, 0)
    if game_over:
        draw_winner()
        
    else:
        draw_turn()
    draw_score()

### create 2d array for game check ###

def init_board():
    global board, current_player, game_over, winner, draw_game
    board = create_2D_array(grid_collum, grid_rows)
    current_player = 1
    game_over = False
    winner = 0
    draw_game = False
    
def create_2D_array(cols, rows):
    if cols == 0:
        return []
    return [create_1D_array(rows)] + create_2D_array(cols - 1, rows)

def create_1D_array(length):
    if length == 0:
        return []
    return [0] + create_1D_array(length - 1)

### end p ###

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
    
### end l ###

    ### draw coin ###
    
    if board[cols][rows] == 1:
        fill(0)
        ellipse(x + size_/2, y + size_/2, 60, 60)
        
    elif board[cols][rows] == 2:
        fill(255)
        ellipse(x + size_/2, y + size_/2, 60, 60)
        
### drop coin ###

def mousePressed():
    global game_over, winner, draw_game, black_score, white_score
    if game_over:
        init_board()
        #draw_game = False
        return

    if mouseX >= off_x and mouseX < off_x + grid_collum * size_:
        cols = int((mouseX - off_x)/ size_)
        rows = drop_coin(cols)
        
        if rows != -1:
            if check_win(cols, rows):
                game_over = True
                winner = current_player
                if current_player == 1:
                    black_score += 1
                else:
                    white_score += 1
            
            elif check_full():
                game_over = True
                draw_game = True
                
            else:
                switch_player()

def drop_coin(cols):                                              
    rows = grid_rows - 1
    while rows >= 0:
        if board[cols][rows] == 0:
            board[cols][rows] = current_player
            return rows
        rows -= 1
    return -1

### switch player ###

def switch_player():
    global current_player
    if current_player == 1:
        current_player = 2
        
    else:
        current_player = 1
        
### draw turn ###

def draw_turn():
    textSize(20)
    if current_player == 1:
        fill(0)
        text("Turn: Black Player", 50, 570)
    
    else:
        fill(100)
        text("Turn: White Player", 50, 570)
        
### ein e $$$$%#$

### chendk win ###

def check_win(cols, rows):
    cols = 0
    while cols < grid_collum:
        rows = 0
        while rows < grid_rows:
            player = board[cols][rows]
            if player != 0:
                # naew norn
                if cols <= 3:
                    if board[cols + 1][rows] == player:
                        if board[cols + 2][rows] == player:
                            if board[cols + 3][rows] == player:
                                return True

                # naew tang
                if rows <= 2:
                    if board[cols][rows + 1] == player:
                        if board[cols][rows + 2] == player:
                            if board[cols][rows + 3] == player:
                                return True

                # bae sai
                if cols <= 3 and rows <= 2:
                    if board[cols + 1][rows + 1] == player:
                        if board[cols + 2][rows + 2] == player:
                            if board[cols + 3][rows + 3] == player:
                                return True

                # bae khwa
                if cols <= 3 and rows >= 3:
                    if board[cols + 1][rows - 1] == player:
                        if board[cols + 2][rows - 2] == player:
                            if board[cols + 3][rows - 3] == player:
                                return True

            rows += 1
        cols += 1
    return False

### end h ###

### draw win n ere ### 45t t544
def draw_winner():
    textSize(20)
    if draw_game:
        fill(0)
        text("Draw!", 50, 570)
    elif winner == 1:
        fill(0)
        text("Black Win!", 50, 570)
        
    elif winner == 2:
        fill(100)
        text("White Win!", 50, 570)
### git commit -m "add headache to my brain"
### 72756b206a61726e20736f706f6e

### check full baord for reset board ###
def check_full():
    cols = 0
    while cols < grid_collum:
        rows = 0
        
        while rows < grid_rows:
            if board[cols][rows] == 0:
                return False
            rows += 1
        cols += 1
    return True

### draew scorje ###
def draw_score():
    textSize(20)
    fill(0)
    text("Black: "+ str(black_score), 50, 610)
    
    fill(100)
    text("White: "+ str(white_score), 200, 610)
    
##$# end lawn ###

### Save ###
def save_game():
    save_board = ""
    cols = 0
    while cols < grid_collum:
        rows = 0
        
        while rows < grid_rows:
            save_board = save_board + str(board[cols][rows])
            rows += 1
        cols += 1
    save_data = save_board + "|" + str(current_player) + "|" + str(black_score) + "|" + str(white_score)
    saveStrings("c4_save.txt", [save_data])
    print("Game Saved")

def keyPressed():
    if key == 's' or key == 'S':
        save_game()
        
### end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end ###    
