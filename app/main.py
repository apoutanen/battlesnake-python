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
    board_width = data['width']
    board_height = data['height']


    allSnakes = data.get("snakes")
    for tempsnake in allSnakes:
        if tempsnake.get("id") == "5c0528b6-9afb-4d7e-b0cf-c46fa0593cda":
            snake = tempsnake
            
            
    
    
    directions = ['up': 0 , 'down' : 0, 'left' : 0 , 'right' : 0 ]
    
    bodyArray = snake["coords"]
    head = bodyArray[0]
    neck = bodyArray[1]
    
    


    return {
        'move': "up",
        'taunt': 'u r hissssstory'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json
    
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']
    # TODO: Do things with data

    return {
        'taunt': ''
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
