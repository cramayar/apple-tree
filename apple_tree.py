#!/usr/bin/python3

import random
import os
import time
import signal
import sys

assets_ascii_logo = """
                       _        _______
     /\               | |      |__   __|
    /  \   _ __  _ __ | | ___     | |_ __ ___  ___
   / /\ \ | '_ \| '_ \| |/ _ \    | | '__/ _ \/ _ :
  / ____ \| |_) | |_) | |  __/    | | | |  __/  __/
 /_/    \_\ .__/| .__/|_|\___|    |_|_|  \___|\___|
          | |   | |
          |_|   |_|
"""

assets_ascii_tree = ['''
                   🌿 🌿
                🌿    🌿  🌿
           🌿  🌿    🌿     🌿  🌿
          🌿     🌿    🌿  🌿    🌿
      🌿 🌿   🌿    🌿    🌿    🌿   🌿
      🌿     🌿  🌿    🌿 🌿 .#  🌿   🌿
      🌿   🌿     🌿 #.  .# 🌿   🌿
       🌿     "#.  #: #" 🌿 🌿    🌿
      🌿   🌿 🌿 "#. ##"       🌿
        🌿       "###
                  "##
                   ##.
                   .##:
                   :###
                   ;###
                 ,####.
     /\/\/\/\/\/.######.\/\/\/\/\
     \n     🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
''','''
                  🌿 🌿
                🌿    🌿  🌿
           🌿  🌿    🌿     🌿  🌿
          🌿   🌿    🌿 🌿    🌿
      🌿 🌿   🌿    🌿    🌿    🌿  🌿
      🌿     🌿  🌿   🌿 🌿 .#  🌿   🌿
      🌿   🌿    🌿 #.  .# 🌿   🌿
       🌿     "#.  #: #" 🌿 🌿🍎   🌿
      🌿   🌿 🌿 "#. ##"       🌿
        🌿       "###
                  "##
                   ##.
                   .##:
                   :###
                   ;###
                 ,####.
     /\/\/\/\/\/.######.\/\/\/\/\
     \n     🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
''','''
                  🍎🌿 🌿
                🌿    🌿  🌿
           🌿  🌿    🌿     🌿  🌿
          🌿   🌿    🌿 🌿    🌿
      🌿 🌿   🌿    🌿    🌿    🌿  🌿
      🌿     🌿  🌿   🌿 🌿 .#  🌿   🌿
      🌿   🌿    🌿 #.  .# 🌿   🌿
       🌿     "#.  #: #" 🌿 🌿🍎   🌿
      🌿   🌿 🌿 "#. ##"       🌿
        🌿       "###
                  "##
                   ##.
                   .##:
                   :###
                   ;###
                 ,####.
     /\/\/\/\/\/.######.\/\/\/\/\
     \n     🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
''','''
                  🍎🌿 🌿
                🌿    🌿  🌿
           🌿  🌿    🌿     🌿  🌿
          🌿     🌿    🌿   🌿    🌿
      🌿 🌿   🌿    🌿    🌿    🌿  🌿
      🌿     🌿  🌿     🌿 🌿 .#  🌿   🌿
      🌿   🌿🍎    🌿 #.  .# 🌿   🌿
       🌿     "#.  #: #" 🌿 🌿🍎   🌿
      🌿   🌿 🌿 "#. ##"       🌿
        🌿       "###
                  "##
                   ##.
                   .##:
                   :###
                   ;###
                 ,####.
     /\/\/\/\/\/.######.\/\/\/\/\
     \n     🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
''','''
                  🍎🌿 🌿
                🌿    🌿  🌿
           🌿  🌿    🌿     🌿  🌿
          🌿     🌿    🌿   🌿    🌿
      🌿 🌿   🌿    🌿    🌿    🌿   🌿
      🌿     🌿  🌿  🍎 🌿 🌿 .#  🌿   🌿
      🌿   🌿🍎    🌿 #.  .# 🌿   🌿
       🌿     "#.  #: #" 🌿 🌿🍎   🌿
      🌿   🌿 🌿 "#. ##"       🌿
        🌿       "###
                  "##
                   ##.
                   .##:
                   :###
                   ;###
                 ,####.
     /\/\/\/\/\/.######.\/\/\/\/\
     \n     🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
''','''
                  🍎🌿 🌿
                🌿    🌿  🌿
           🌿  🌿    🌿     🌿  🌿
          🌿     🌿    🌿   🌿    🌿
      🌿 🌿   🌿    🌿    🌿    🌿 🍎 🌿
      🌿     🌿  🌿  🍎 🌿 🌿 .#  🌿   🌿
      🌿   🌿🍎    🌿 #.  .# 🌿   🌿
       🌿     "#.  #: #" 🌿 🌿🍎   🌿
      🌿   🌿 🌿 "#. ##"       🌿
        🌿       "###
                  "##
                   ##.
                   .##:
                   :###
                   ;###
                 ,####.
     /\/\/\/\/\/.######.\/\/\/\/\
     \n     🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
''','''
                  🍎🌿 🌿
                🌿    🌿  🌿
           🌿  🌿    🌿     🌿  🌿
          🌿     🌿    🌿🍎 🌿    🌿
      🌿 🌿   🌿    🌿    🌿    🌿 🍎 🌿
      🌿     🌿  🌿  🍎 🌿 🌿 .#  🌿   🌿
      🌿   🌿🍎    🌿 #.  .# 🌿   🌿
       🌿     "#.  #: #" 🌿 🌿🍎   🌿
      🌿   🌿 🌿 "#. ##"       🌿
        🌿       "###
                  "##
                   ##.
                   .##:
                   :###
                   ;###
                 ,####.
     /\/\/\/\/\/.######.\/\/\/\/\
     \n     🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
''','''
                  🍎🌿 🌿
                🌿    🌿  🌿
           🌿  🌿    🌿     🌿  🌿
          🌿 🍎  🌿    🌿🍎 🌿    🌿
      🌿 🌿   🌿    🌿    🌿    🌿 🍎 🌿
      🌿     🌿  🌿  🍎 🌿 🌿 .#  🌿   🌿
      🌿   🌿🍎    🌿 #.  .# 🌿   🌿
       🌿     "#.  #: #" 🌿 🌿🍎   🌿
      🌿   🌿 🌿 "#. ##"       🌿
        🌿       "###
                  "##
                   ##.
                   .##:
                   :###
                   ;###
                 ,####.
     /\/\/\/\/\/.######.\/\/\/\/\
     \n     🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
''']

word_list = [
    # Source 1
    "block", "buildings", "check", "corner", "crosswalk", "group",
    "guard", "help", "join", "left", "library", "listen", "meet",
    "mutters", "plant", "quiet", "right", "sand", "school", "settle",
    "store", "street", "type", "various",
    # Source 2
    "big", "bud", "burrow", "dig", "dolphin", "eagle", "eat",
    "egg", "elephant", "fast", "frog", "gills", "leaves", "nature",
    "new", "notice", "pattern", "reason", "sleep", "small", "soil",
    "stem", "tadpole",
    # Source 3
    "angry", "beg", "carefully", "concentrate", "create", "decorate",
    "deep", "exactly", "fairly", "gather", "happy", "imagine", "learn",
    "possible", "remember", "sad", "sadly", "skip", "suppose", "surprise",
    "think", "zoom",
    # Source 4
    "admire", "allowed", "amaze", "cattle", "cheer", "discover",
    "drive", "experience", "field", "leader", "memory", "necessary",
    "patch", "railroad", "ranch", "record", "right", "stars",
    "stripe", "supply", "view", "vote", "wonder"
]

# Handle the early exit signal.
def signal_handler(sig, frame):
    print("\n     Good-bye!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
# not needed: signal.pause()

chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)

#  print(f"[DEBUG] solution is '{chosen_word}'")

displayed_word = []

# Generate the word place holder: _ _ _ _ ...
for _ in chosen_word:
    displayed_word += "_"

has_game_ended = False
letter_count = 0
tried_wrong_letters = []
lives = 7

while not has_game_ended:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        # For Darwin and linux
        os.system('clear')

    print(assets_ascii_logo)
    print(assets_ascii_tree[lives])
    print("     Press CTRL + C to exit the game.\n")

    print(f"      {' '.join(displayed_word)}          {chosen_word_length} letters")

    user_guess_letter = input("\n     Guess a letter:  ").lower()
    found_letter = False
    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if letter == user_guess_letter:
            displayed_word[position] = letter
            letter_count += 1
            found_letter = True

    if not found_letter:
        if user_guess_letter not in tried_wrong_letters:
            tried_wrong_letters.append(user_guess_letter)
            print(f"You guessed {user_guess_letter}, that's not in the word\nYou lose an apple.")
            time.sleep(3)
            lives -= 1

            # If lives go down to 0 then the game should stop and it should print "You lose."
            if lives == 0:
                has_game_ended = True
        else:
            print(f"You already tried the letter {user_guess_letter}, that's not in the word\n")
            time.sleep(3)

    # Join all the elements in the list and turn it into a string.
    print(f"      {' '.join(displayed_word)}")

    # Check if user has got all letters.
    if not '_' in displayed_word:
        has_game_ended = True

if lives != 0:
    print("\n     You won! 🏆   🎉 Congrats 🎉")
else:
    print(f" The word was {chosen_word}")
    print("\n     Game over 😔  Try next time.")

print("     The game finished!")
