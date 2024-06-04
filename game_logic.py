keyboard_map = {
  's': {
    "player": 1,
    "action": 'rock'
  },
  'd': {
    "player": 1,
    "action": 'paper'
  },
  'f': {
    "player": 1,
    "action": 'scissors'
  },
  'j': {
    "player": 2,
    "action": 'rock'
  },
  'k': {
    "player": 2,
    "action": 'paper'
  },
  'l': {
    "player": 2,
    "action": 'scissors'
  }
}

def resolve_game(game):
  if game['player1']['action'] == game['player2']['action']:
    print('Empate. Vamos de nuevo!')
    game['player1'].action = None
    game['player2'].action = None
  elif game['player1']['action'] == 'rock' and game['player2']['action'] == 'scissors':
    print(f'{game["player1"]["name"]} gana')
  elif game['player1']['action'] == 'paper' and game['player2']['action'] == 'rock':
    print(f'{game["player1"]["name"]} gana')
  elif game['player1']['action'] == 'scissors' and game['player2']['action'] == 'paper':
    print(f'{game["player1"]["name"]} gana')
  else:
    print(f'{game["player2"]["name"]} gana')

def capture_presses(key, game):
  try:
    key_char = key.char
    if key_char in keyboard_map:
      if (keyboard_map[key_char]['player'] == 1):
        game['player1']['action'] = keyboard_map[key_char]['action']
        print('x')
      if (keyboard_map[key_char]['player'] == 2):
        game['player2']['action'] = keyboard_map[key_char]['action']
        print('x')
      if (game['player1']['action'] is not None and game['player2']['action'] is not None):
        resolve_game(game)

    else:
      return
  except Exception as e:
    return