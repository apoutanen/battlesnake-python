import bottle
import os
import random


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff00',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'deadsnake'
    }



@bottle.post('/move')
def move():
    data = bottle.request.json
    
    game_id = data['game_id']
    width = data['width']
    height = data['height']

    snake = {}
    allSnakes = data.get("snakes")
    for tempsnake in allSnakes:
        if tempsnake.get("id") == data["you"]:
            snake = tempsnake
            
            
    
    bodyArray = snake["coords"]
    head = bodyArray[0]
    neck = bodyArray[1]

    upCoords = [head[0], head[1]-1]
    downCoords = [head[0], head[1]+1]
    leftCoords = [head[0]-1, head[1]]
    rightCoords = [head[0]+1, head[1]]
    
    directions = {'up' : [0, upCoords], 'down' : [0, downCoords], 'left' : [0, leftCoords], 'right' : [0, rightCoords]}
    
    
    for key in directions:
       #if move will kill snek
        if directions[key][1] == neck or (0 > directions[key][1][0]) or (directions[key][1][0] > width-1) or (0 > directions[key][1][1]) or (directions[key][1][1] > height-1):
            del directions[key]
        
   
    nextMove = ''
    x = -1
    for i in directions:
        if x < directions[i][0]:
            x = directions[i][0]
            nextMove = i
        
   
    
    return {
        'move': nextMove,
        'taunt': nextMove
    }


@bottle.post('/end')
def end():
    data = bottle.request.json
    
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']
    # TODO: Do things with data

    return {
        'taunt': ' u r hissstory'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
