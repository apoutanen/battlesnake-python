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
        'color': '#48C9B0',
        'head': head_url,
        'head_type' : 'smile',
        'tail_type' : 'round-bum'
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
        'color': '#48C9B0',
        'taunt': ';) :))))))))))',
        'head_url': head_url,
        'name': 'beeeeeeeeeesssssssssneeeeeeekk',
        'head_type' : 'smile',
        'tail_type' : 'round-bum'
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
            #del directions[key]
            directions[key][0] = -2
    
    
    for snek in allSnakes:
        for coords in snek["coords"]:
            for key in directions:
                if directions[key][1] == coords:
                    directions[key][0] = -2
    
    
    
    nextMove = ''
    x = -1
    for key, value in directions.iteritems():
        if x < value[0]:
            x = value[0]
            nextMove = key
        
   
    taunts = ['According', 'to', 'all', 'known', 'laws', 'of', 'aviation,', 'there', 'is', 'no', 'way', 'a', 'bee', 'should', 'be', 'able', 'to', 'fly.', 'Its', 'wings', 'are', 'too', 'small', 'to', 'get', 'its', 'fat', 'little', 'body', 'off', 'the', 'ground.', 'The', 'bee,', 'of', 'course,', 'flies', 'anyway', 'because', 'bees', "don't", 'care', 'what', 'humans', 'think', 'is', 'impossible']

    
    
    return {
        'move': nextMove,
        #'taunt': taunts[data["turn"]%(len(taunts))]
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
