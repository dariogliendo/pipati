import os
from pynput import keyboard
import game_logic as gl
from time import sleep

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def main():
  clear()
  print('Player 1 - Enter your name:')
  name1 = input()
  clear()
  print('Player 2 - Enter your name:')
  name2 = input()
  clear()
  game(name1, name2)
  
    

def game(name1, name2):
  print('Bienvenidx a Piedra, Papel, Tijera')
  print(f'{name1}' + ' vs ' + f'{name2}')
  print(f'{name1} puede elegir:\n Piedra, presionando s\n Papel, presionando d\n Tijera, presionando f')
  print(f'{name2} puede elegir:\n Piedra, presionando j\n Papel, presionando k\n Tijera, presionando l')
  print('Ambos jugadores deben presionar su tecla al mismo tiempo')
  print('3...')
  sleep(1)
  print('2...')
  sleep(1)
  print('1...')
  sleep(1)
  print('Ya!')
  print('\n\n\n')
  print(f'{name1}                      {name2}')
  
  game = {
  'player1': {
    'name': name1,
    'action': None,
  },
  'player2': {
    'name': name2,
    'action': None
  }
}

  def on_press(key):
    gl.capture_presses(key, game)
  
  with keyboard.Listener(
    on_press=on_press,
  ) as listener:
    try:
      listener.join()
    except Exception as e:
      print(e)

main()