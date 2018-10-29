def lambda_handler(event, context):
    print("In lambda handler")
    game_title = '<h1>My Silly Tic Tac Toe Game</h1><h2>You must play as X</h2>'
    
    cells = event['cells']
    if(game_won(cells)):
        win_html = "<h1> X wins the game</h1>"
        html_resp = game_title + win_html
        return(html_resp)
        
    html_resp_table = '<table style="width:50%"><tr>'
    for i, cell in enumerate(cells):
        if(cell == 'E'):
            new_cells = cells[0:i] + "X" + cells[i+1:]
            html_resp_table += '<td><a href=/prod/TicTacToeGame?cells={}><button>{}</button></a></td>'.format(new_cells,'_')
        elif(cell == 'X'):
            html_resp_table += '<td><button>X</button></td>'
        
        if((i + 1) % 3 == 0):
            html_resp_table += '</tr><tr>'
            
    html_resp_table += '</table>'
    
    
    #html_resp_table = '<table style="width:50%"><tr><td><button type="button" onclick="google.com"</button></td><td>X</td><td>X</td></tr><tr><td>X</td><td>X</td><td>X</td></tr><tr><td>X</td><td>X</td> <td>X</td></tr></table>'
    html_resp = game_title + html_resp_table
    
    #button_google = '<a href=/prod/TicTacToeGame?cells=2><button>{}</button></a>'.format('X')
    #html_resp += button_google
    return(html_resp)
    
def game_won(cells):
    if(cells[0:3] == 'XXX' or cells[3:6] == 'XXX' or cells[6:] == 'XXX'):
        return(True)
    elif(cells[0] == 'X' and cells[4] == 'X' and cells[8] == 'X'):
        return(True)
    elif(cells[6] == 'X' and cells[4] == 'X' and cells[2] == 'X'):
        return(True)
        
    for i in range(0, 3):
        if(cells[i] == 'X' and cells[i] == cells[i+3] and cells[i] == cells[i+6]):
            return(True)
    
    return(False)
    
    
