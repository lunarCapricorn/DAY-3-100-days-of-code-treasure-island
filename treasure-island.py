import asciiArt # typingEffect(text, typing effect speed, wait time)
import os
os.system('clear')
typeSpeed = .04

def playAgain():
  asciiArt.typingEffect('. . . \n', .4, 2)
  asciiArt.typingEffect('Would you like to play again?[yes/no] ', typeSpeed, 0)
  choice = input()
  if (choice.lower() != 'yes'):
    asciiArt.typingEffect('Thank you for playing! :) ', typeSpeed, 3)
    exit()
  else:
    os.system('clear')
    main()

def choices(choice):
  choiceLower = choice.lower()
  switches = { # list of correct choices
    'left' : 'Great, you survived!\n',
    'wait' : 'Great, you survived! Now\n',
    'yellow' : 'You win! ',
  }

  for index, value in switches.items(): # checks if input is correct by matching the index, if yes then prints value
    if (choiceLower == index):
      asciiArt.typingEffect(value, typeSpeed, 0)
      return
  
  asciiArt.asciiArt('Death')
  playAgain()

def outputAndInput(output, typeSpeed, waitSpeed): # to not repeat prints and inputs // types in the prompt, asks for input, gives input to choices
  asciiArt.typingEffect(output, typeSpeed, waitSpeed)
  choice = input()
  choices(choice.lower())

# ----- calls ----- 
def main():
  asciiArt.asciiArt('Intro')

  outputAndInput('Your task is to locate the treasure.\nleft or right? ', typeSpeed, 0)
  outputAndInput('Now, do you swim or wait? ', typeSpeed, 0)

  asciiArt.typingEffect('. . . \n', .4, 2)
  outputAndInput('You see three doors, one is \033[1;31;40mRed\033[0m, other is \033[1;34;40mBlue\033[0m, and the last one is \033[1;33;40mYellow\033[0m, which door will you choose? ', typeSpeed, 0)
  playAgain()
main()