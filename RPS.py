# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
play_order={}
from random import randint
def player(prev_play, opponent_history=[]):
  if prev_play != '':
    opponent_history.append(prev_play)
  rand = randint(0,2)
  pred = ["P", "R", "S"]
  guess = pred[rand]
  if len(opponent_history) > 5:
    
    lastFive = "".join(opponent_history[-5:])
    if lastFive in play_order:
      play_order[lastFive] += 1
    else:
      play_order[lastFive] = 1

    lastFour = "".join(opponent_history[-4:])
    potential_plays = [
        lastFour + "R",
        lastFour + "P",
        lastFour + "S",
    ]
    
    for i in potential_plays:
      if i not in play_order.keys():
        play_order[i] = 0
    
    sub_order = {
        k: play_order[k]
        for k in potential_plays if k in play_order
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    guess = ideal_response[prediction]
  return guess
