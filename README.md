# Vocab---Python_v3.6

The project Vocab contains four files :-

    1. gameDictFile.py :- it contains all the words and their meaning inside a dictionary.

    2. gameException.py :- it contains all the user defined exception, these exceptions are used in the main code time to time 
                       when needed.
                       
    3. gameFunction.py :- it contains the class which contains various functions, which is there for the program executions from                         playing the game to displaying the score in a tablular format.

    4. gameMenu.py :- it contains our main menu all and the linking to the functions are done in this file. gameFunction.py file is                   linked as it contains our main code.

** NOTE :- In order to see the execution of the program, you have to run gameMenu.py file as it is our main file where all the            functions are linked.


# HOW THE GAME WORKS?

The game will randomly select all the words from the dictionary which is there in gameDictFile.py file (using random module) and the program also randomly selects some of the characters(alphabets) in the word randomly to be displayed and all other words are displayed as dashes and the user has to guess the characters(alphabets) in place of those dashes if the word is guessed correctly then points will be added to your score otherwise the points will be deducted from your score. The program will offer total three chances to play the game and guessing choice will be offered on the basis of the length of the words, if the length of the word is larger then the guessing choice will be large too and for small length a small number will be there as the guessing choice.
