import random
def lambda_handler(event, context):
    print("In lambda handler")
    game_title = '<h1>My Silly Tic Tac Toe Game</h1><h2>You must play as X</h2>'
    
    cells = event['cells']
    if(game_won(cells, 'X')): 
        # checking if X won the game
        win_html = "<h1> X wins the game</h1>"
        html_resp = game_title + win_html
        return(html_resp)
    cells = place_char(cells, 'O')
    if(game_won(cells, 'O')):
        #checking if O won the game
        win_html = "<h1> O wins the game</h1>"
        html_resp = game_title + win_html
        return(html_resp)
    html_resp_table = '<table style="width:50%"><tr>'
    for i, cell in enumerate(cells):
        if(cell == 'E'):
            new_cells = cells[0:i] + "X" + cells[i+1:]
            html_resp_table += '<td><a href=/prod/TicTacToeGame?cells={}><button>{}</button></a></td>'.format(new_cells,'_')
        else:
            html_resp_table += '<td><button>{}</button></td>'.format(cell)
        
        if((i + 1) % 3 == 0):
            html_resp_table += '</tr><tr>'
            
    html_resp_table += '</table>'
    
    
    #html_resp_table = '<table style="width:50%"><tr><td><button type="button" onclick="google.com"</button></td><td>X</td><td>X</td></tr><tr><td>X</td><td>X</td><td>X</td></tr><tr><td>X</td><td>X</td> <td>X</td></tr></table>'
    html_resp = game_title + html_resp_table
    html_resp = add_restart_tags(html_resp)
    #button_google = '<a href=/prod/TicTacToeGame?cells=2><button>{}</button></a>'.format('X')
    #html_resp += button_google
    return(html_resp)

def place_char(cells, char):
    available_spots = []
    
    for i, cell in enumerate(cells):
        if(cell == 'E'):
            available_spots.append(i)
            
    indx = random.choice(available_spots)
    print(indx)
    #Need to add a try catch for later
    return(cells[0:indx] + char + cells[indx+1:])
  
def game_won(cells, char):
    # Brute forced check, limited number of possibilities
    trip_char = char + char + char # Representation for 'XXX' or 'OOO'
    if(cells[0:3] == trip_char or cells[3:6] == trip_char or cells[6:] == trip_char):
        return(True)
    elif(cells[0] == char and cells[4] == char and cells[8] == char):
        return(True)
    elif(cells[6] == char and cells[4] == char and cells[2] == char):
        return(True)
        
    for i in range(0, 3):
        if(cells[i] == char and cells[i] == cells[i+3] and cells[i] == cells[i+6]):
            return(True)
    
    return(False)
    
def add_restart_tags(html_resp):
    #Redirect to the original empty page
    restart_cells_state = "EEEEEEEEE"
    restart_button = '<a href=/prod/TicTacToeGame?cells={}><button>{}</button></a>'.format(restart_cells_state, "RESTART")
    html_resp += restart_button
    return(html_resp)
