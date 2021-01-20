from art import logo,vs
from game_data import data
from replit import clear
import random as r

print(logo)
score = 0
isCorrect = True

def play_again(again):
  global isCorrect
  if again == 'n':
    isCorrect = False
    clear()
  elif again == 'y':
    clear()

while isCorrect:
  p1 = data[r.randint(0,len(data)-1)]
  p2 = data[r.randint(0,len(data)-1)]
  if p1 != p2:
    print(f"Compare A: {p1['name']} a {p1['description']} from {p1['country']}")
    print(vs)
    print(f"Against B: {p2['name']} a {p2['description']} from {p2['country']}")
    choose = input("Who has more followers ? 'A' or 'B' ").lower()
    if choose == 'a':
      clear()
      if p1['follower_count'] > p2['follower_count']:
        score += 1
        print(f"You are right! Score {score}")
      else:
        print(f"Sorry, that's wrong, Final score {score}")
        score = 0
        is_play_again = input("Play again? 'n' for no ")
        play_again(is_play_again)

    elif choose == 'b':
      clear()
      if p1['follower_count'] < p2['follower_count']:
        score += 1
        print(f"You are right! Score {score}")
      else:
        print(f"Sorry, that's wrong, Final score {score}")
        score = 0
        is_play_again = input("Play again? 'n' for no ")
        play_again(is_play_again)