collum = 7
row = 6

size_ = 80
off_x = 50
off_x = 50
current_player = 1
game_over = False
winner = 0

board = []

def setup():
    size(650,650)
    init_board()
    
def draw():
    background(240)

def init_board():
    global board, current_player, game_over, winner
    board = create_2D_array(collum, row)
    current_player = 1
    game_over = False
    winner = 0
    
def create_2D_array(cols, rows):
    if cols <= 0:
        return []
    return [create_1D_array(rows)] + create_2D_array(cols - 1, rows)

def create_1D_array(length):
    if length <= 0:
        return []
    
    return [0] + create_1D_array(length - 1)


    
