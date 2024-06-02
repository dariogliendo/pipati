import os
from pynput import keyboard

keyboard_map = {
  's': {
    player: 1,
    action: 'rock'
  },
  'd': {
    player: 1,
    action: 'paper'
  },
  'f': {
    player: 1,
    action: 'scissors'
  },
  'j': {
    player: 2,
    action: 'rock'
  },
  'k': {
    player: 2,
    action: 'paper'
  },
  'l': {
    player: 2,
    action: 'scissors'
  }
}

def on_press(key):
  print('Key: ')
  print(key)

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
  game()

def game():
  with keyboard.Listener(
    on_press=on_press,
  ) as listener:
    listener.join()

main()