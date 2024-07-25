# APPLE TREE GAME

![Apple Tree Screenshot.](https://github.com/cramayar/apple-tree/blob/main/assets/images/apple_tree_screen.png?raw=true)

## About the game
Minimalistic implementation of a popular word guessing game formerly known as
*hangman* but the premise of the game does not withstand the test of time, and
seems not only unnecesary but also insensitive for most educators and children.

## How to play

In the console run:
```
python3 apple_tree.py
```

The word that will be guessed is represented by the underscores _ _ _ ... and
the word length is also displayed.
The player needs to input a letter from the english alphabet and then press
**Enter**.
If the letter is in the word to be guessed, the player will be directly allowed
to continue guessing new letters and no apples are deducted.
If the inserted letter is not in the word, then an apple will disappear from
the tree.

The game ends either when the player guessed all the letters, or when the tree
runs out of apples.

I wrote this game mostly to provide educational tools for my kids and I thought
it might be useful to you.

## Word list
The words used are taken from a first grade level vocabulary:
* admire
* allowed
* amaze
* angry
* beg
* big
* block
* bud
* buildings
* burrow
* carefully
* cattle
* check
* cheer
* concentrate
* corner
* create
* crosswalk
* decorate
* deep
* dig
* discover
* dolphin
* drive
* eagle
* eat
* egg
* elephant
* exactly
* experience
* fairly
* fast
* field
* frog
* gather
* gills
* group
* guard
* happy
* help
* imagine
* join
* leader
* learn
* leaves
* left
* library
* listen
* meet
* memory
* mutters
* nature
* necessary
* new
* notice
* patch
* pattern
* plant
* possible
* quiet
* railroad
* ranch
* reason
* record
* remember
* right
* right
* sad
* sadly
* sand
* school
* settle
* skip
* sleep
* small
* soil
* stars
* stem
* store
* street
* stripe
* supply
* suppose
* surprise
* tadpole
* think
* type
* various
* view
* vote
* wonder
* zoom

> [!TIP]
> I tried to run this game in a Raspberry Pi 3+ and found out that the emojis were missing.
> It ran well after I installed the noto color emoji font:
> ```
> sudo apt install fonts-noto-color-emoji
> ```

## Credits
* The ASCII logo was created with the [Text to ascii Art](https://www.asciiart.eu/text-to-ascii-art) generator.
* The Apple Tree ASCII original pure ASCII Art can be found at the [ASCII Art Archive] (https://www.asciiart.eu/plants/other)
The author is unknown.

