import sys
from time import sleep

def typingEffect(text, speed, hangTime):
    for char in text:
        sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(hangTime)

def asciiArt(whatArt):

    if (whatArt == 'Intro'):
        print('''
        \033[0m-----------------------------------------------------------------------
        |*********************************************************************|
        |                                  ,,,,                               |
        |                      ////       ,_ _ \                              |
        |                      \ ( /     ('* \*(                              |
        |                       ` '       '  -`,                              |
        |                        '\        `_C/       \\\|                     |
        |                         .\      __,(___   \ ) /                     |
        |                          .\__.-'       `.  ` |                      |
        |                           .____          \  '|                      |
        |                                |     /`   \ '|                      |
        |                                |    /    `  \'|                      |
        |                                |   /      `  |                      |
        |                                |  /        `-'                      |
        |                      _________))||(                                 |
        |                     (  __\         \                                |
        |                      ` \  `----.  __\                               |
        |                       ` \       `(_. \                              |
        |                         `\          ` \                             |
        |                          ,)           >)                            |
        |                         /(          ( /                             |
        |                        ""o          ,/                              |
        |                                    ,/                               |
        |                                   (                                 |
        |                                    )\                               |
        |                                    o""                              |
        |*********************************************************************|
        -----------------------------------------------------------------------     
        ''')
        typingEffect("Welcome to treasure island!\n", .04, 0)
    elif(whatArt == 'Death'):
        print('''
        -----------------------------------------------------------------------
                                    ,--.
                                   {    }
                                   K,   }
                                  /  ~Y`
                             ,   /   /
                            {_'-K.__/
                              `/-.__L._
                              /  ' /`\_}
                             /  ' /
                     ____   /  ' /
              ,-'~~~~    ~~/  ' /_
            ,'             ``~~~  ',
           (                        Y
          {                         I
         {      -                    `,
         |       ',                   )
         |        |   ,..__      __. Y
         |    .,_./  Y ' / ^Y   J   )|
         \           |' /   |   |   ||
          \          L_/    . _ (_,.'(
           \,   ,      ^^""' / |      )
             \_  \          /,L]     /
               '-_~-,       ` `   ./`
                  `'{_            )
                      ^^\..___,.--`
        -----------------------------------------------------------------------
                     ''')
        typingEffect('It would seem that you have died ', .04, 0)
        typingEffect('. . . \n', 1, 1)
        