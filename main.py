# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

#play(player, quincy, 1000)
#play(player, abbey, 1000)
#play(player, kris, 1000)
#play(player, mrugesh, 1000)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically

#MY CODE PASSES THE TEST BUT NOT EVERY TIME FOR ABBEY, SOMETIMES ITS A LITTE LESS THAN 60 BUT IT'S ALWAYS ABOVE 50 AND ITS WAY ABOVE 60 FOR EVERYONE ELSE EVERYTIME
main(module='test_module', exit=False)