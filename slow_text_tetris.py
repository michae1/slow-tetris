#!/usr/bin/env python2
import random, copy, sys

WIDTH = 20
HEIGHT = 20
SYMBOL = "*"
ALLOWED_ACTIONS = ('a','d','s','w')

# possible pieces
pieces = [
    [
        [0,0,0,0],
        [1,1,1,1],
        [0,0,0,0],
        [0,0,0,0]
    ],[   
        [0,1,0],
        [0,1,0],
        [1,1,0]
    ],[
        [0,1,0],
        [0,1,0],
        [0,1,1]
    ],[
        [1,1,0],
        [0,1,1],
        [0,0,0]
    ],[
        [1,1],
        [1,1]
    ]
]

def generate_next_piece():
    # Generate random piece from list on random x
    current_piece_object = {}
    current_piece_object['piece'] = random.choice(pieces)
    current_piece_object['x'] = random.randrange(0, WIDTH - len(current_piece_object['piece'][0]))
    current_piece_object['y'] = 0
    return current_piece_object

def rotate_piece(current_piece_object, direction = 0):
    # rotate piece matrix
    if direction:
        current_piece_object['piece'] = zip(*current_piece_object['piece'][::-1])
    else:
        current_piece_object['piece'] = zip(*current_piece_object['piece'])[::-1]    



def mix_field_and_current_piece(current_piece_object, temp_field):
    # mix piece into current field (to visualize)
    piece_width = len(current_piece_object['piece'][0])
    piece_height = len(current_piece_object['piece'])
    px = current_piece_object['x']
    py = current_piece_object['y']
    for y in range(py, py + piece_height):
        for x in range(px, px + piece_width):
            if current_piece_object['piece'][y-py][x-px] and x < WIDTH:
                temp_field[y][x] = current_piece_object['piece'][y-py][x-px]
    return temp_field        
 
def draw_field(current_piece_object, play_field, game_over=False):
    # just print generated matrix with borders and active piece
    if game_over:
        # game over screen
        line = SYMBOL + " " * WIDTH + SYMBOL
        for y in range(0, HEIGHT):
            if y == 9:
                print SYMBOL + " "*5 + "Game Over" + " "*6 + SYMBOL
            else:    
                print line    

        print SYMBOL*(WIDTH+2)
        return False

    visual_field = mix_field_and_current_piece(current_piece_object, copy.deepcopy(play_field))
    for y in visual_field:
        line = SYMBOL # left border
        for x in y:
            line += SYMBOL if x else " "
        line += SYMBOL #right border    
        print line    
    print SYMBOL*(WIDTH+2)        

def ask_user_action():
    action = raw_input("Next action: ")
    while action not in ALLOWED_ACTIONS:
        action = raw_input("Valid actions: %s. Next action: "%",".join(ALLOWED_ACTIONS))
    return action

def freeze_piece(current_piece_object, play_field):
    # piece cannot move, leave it here
    play_field = mix_field_and_current_piece(current_piece_object, play_field)

def move_left(current_piece_object, play_field):
    if current_piece_object['x'] > 0 and not is_occupied(current_piece_object['piece'], current_piece_object['y'], current_piece_object['x'], play_field, -1):       
        current_piece_object['x'] -= 1

def move_right(current_piece_object, play_field):
    piece_width = len(current_piece_object['piece'][0])
    if current_piece_object['x'] < WIDTH-piece_width and not is_occupied(current_piece_object['piece'], current_piece_object['y'], current_piece_object['x'], play_field, 1):       
        current_piece_object['x'] += 1        

def get_bottom_visible_heigth(piece):
    height = len(piece)
    for y in reversed(piece):
        if 1 in y:
            return height
        else:
            height -=1    
        
def is_occupied(piece, py, px, play_field, dx=0):
    # Check if place occupied before move
    result = False
    piece_height = len(piece)
    piece_width = len(piece[0])

    for y in range(py, py + piece_height):
        if py + piece_height > HEIGHT:
            continue
        #check if next step will affect field
        for x in range(px, px + piece_width):
            if px + piece_width > WIDTH:
                continue
            if piece[y-py][x-px] and play_field[y+1][x+dx]:
                print play_field[y+1][x+dx]
                return True
    return result

def main():
    # main func

    # empty play field
    play_field = [[0 for x in range(WIDTH)] for x in range(HEIGHT)] 

    # get new random piece
    current_piece_object = generate_next_piece()
    draw_field(current_piece_object, play_field)

    while 1:
        action = ask_user_action()
        if action == 'a':
            move_left(current_piece_object, play_field)
        if action == 'd':
            move_right(current_piece_object, play_field)
        if action == 'w':
            rotate_piece(current_piece_object)
        if action == 's':
            rotate_piece(current_piece_object,1)
    
        # move down    
        current_piece_object['y'] += 1

        if (current_piece_object['y'] == HEIGHT - get_bottom_visible_heigth(current_piece_object['piece']) 
            or is_occupied(current_piece_object['piece'], current_piece_object['y'], current_piece_object['x'], play_field)):
            freeze_piece(current_piece_object, play_field);
            if current_piece_object['y'] == 1:
                draw_field(current_piece_object, play_field, game_over=True);
                sys.exit()

            current_piece_object = generate_next_piece();
        draw_field(current_piece_object, play_field)


if __name__ == "__main__":
    main()   
