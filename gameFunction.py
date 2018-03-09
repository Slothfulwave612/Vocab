# Vocab's game gameFunction
# it will contain the main code of every menu present in the game.

import time                              # importing time module
import os                               # importing os module
import sys                             # importing sys module
import random                         # importing random module
import logging                       # importing logging module
import operator                     # importing operator module
import pickle                      # importing pickle module
import gameException as ge        # importing gameException file and using it as ge
import gameDictFile as gd        # importing gameDictFile file and using it as gd

logging.basicConfig(filename='vocabLog.log', level=logging.INFO, format='%(asctime)s : %(message)s')
# using basicConfig function to keep a track what is happening in the program


class FunctionCode(object):
    # these function include all the code for all the options in the game.

    def __init__(self, name, total_score, success, fail):
        # using init for initialising all the data members of the class
        self.name = name                # self.name data member a string for storing name
        self.total_score = total_score  # self.total_score data member an integer for storing total scores
        self.success = success          # self.success data member an integer for storing success scores
        self.fail = fail                # self.fail data member an integer for storing failed scores

    # total score will be calculated as :-
    # total_score = success - fail
    # class FunctionCode will contain all the main function.
    # where 1 success attempt is equal to 5 points and 1 failed attempt is equal to -3 points
    # success score will be granted when the word guessed it right
    # failed score will be there when the word is guessed wrong

    def reuse_calculateScore(self, right, wrong):
        return((right * 5) - (wrong * 3))

    def reuse_enterException(self):
        # reuse function for reusing the enter exception
        while True:
            try:
                # try-exception block
                x = input("Press the Enter key to continue ")
                # this will ask user to press the enter key to play the game
                if(x != ''):
                    raise ge.EnterException
                    # if some other key is pressed other than enter key
                    # than EnterException will be rasied by the program
                break   # breaking when enter key is pressed

            except ge.EnterException:
                # when EnterException is rasied
                time.sleep(0.5)             # stopping the time for 0.5 seconds

            except ValueError:
                print()
                time.sleep(0.5)    # stopping the time for 0.5 seconds
                print('Invalid Input...')   # printing invalid input if the error type - Value Error

    def display_score(self, nme, right, wrong, tot_score):
        # will display the score
        # when the game ends, when a guess is right or wrong
        print()
        time.sleep(0.5)       # stopping the time for 0.5 seconds

        print(f'{nme} you score is as follows :-')
        time.sleep(0.5)      # stopping the time for 0.5 seconds

        print()
        time.sleep(0.5)      # stopping the time for 0.5 seconds

        print(f'Total Score :- {tot_score}')
        time.sleep(0.5)      # stopping the time for 0.5 seconds
        print(f'Number of Successful guesses :- {right}')
        time.sleep(0.5)      # stopping the time for 0.5 seconds
        print(f'Number of Failed guesses :- {wrong}')

        # using logging.info
        logging.info(f'Name :- {nme}, Total Score :- {tot_score}, Successful Guesses :- {right}, Failed Guesses :- {wrong}')

    def LetsPlay(self):
        # this function is for the option 1
        # the code here will execute all the functions required for the play option

        sys.stdout.write('\r')
        sys.stdout.write('Starting Your Game')         # printing message using stdout

        for i in range(6):
            sys.stdout.write("\r")
            sys.stdout.write('Starting Your Game' + '.' * i)    # using stdout to print the message in an interactive way
            sys.stdout.flush()                                  # using the flush function
            time.sleep(0.5)                # stopping the time for 0.5 seconds

        sys.stdout.write('\r')
        sys.stdout.write('                                       \n')

        print()

        while True:
            # try-exception block
            try:
                time.sleep(0.5)      # stopping the time for 0.5 seconds

                nme = input('Enter Your Name :- ')
                # this name data member will store the name of the user playing the game

                break               # breaking the clause if the vaild input is entered

            except ValueError:
                print()
                time.sleep(0.5)    # stopping the time for 0.5 seconds

                print('Invalid Input...')   # printing invalid input if the error type - Value Error

        logging.info(f'Name has been inputted.. Name :- {nme}')
        # logging-info for name has been inputted

        select_word = []      # randomly we will put our word's meaning in the list select_word

        select_word = random.sample(list(gd.vocab_dict), k=len(gd.vocab_dict))
        # here we will randomly put every meaning in of select_word list

        logging.info('Word\'s Meaning were randomly selected and were organised into the list select_word')
        # logging-info for word's meaing were randomly selected

        tot_turns = 3       # total turns to play the game is 3

        right = 0           # right for the total no of right guesses
        wrong = 0           # wrong for the total no of wrong guesses

        print()
        time.sleep(0.5)    # stopping the time for 0.5 seconds

        print(f'{nme} you have {tot_turns} turns to play the game')

        while(tot_turns > 0):
            for i in select_word:
                if(len(gd.vocab_dict[i]) <= 4):
                    # if the length of the word is less than or equal to four
                    select_char = random.sample(gd.vocab_dict[i], k=1)  # randomly generating any one charater from the word
                    # and putting it in a list
                    turns = 2        # turns to guess the word is 2 if the length of word is less than or equal to 4

                elif(len(gd.vocab_dict[i]) <= 6):
                    # if the length of the word is less than or equal to six
                    select_char = random.sample(gd.vocab_dict[i], k=2)  # randomly generating any two charater from the word
                    # and putting it in a list
                    turns = 3        # turns to guess the word is 3 if the length of word is less than or equal to 6

                elif(len(gd.vocab_dict[i]) <= 8):
                    # if the length of the word is less than or equal to eight
                    select_char = random.sample(gd.vocab_dict[i], k=3)  # randomly generating any three charater from the word
                    # and putting it in a list
                    turns = 4        # turns to guess the word is 4 if the length of word is less than or equal to 8

                else:
                    # else, i.e. for every cases when the length of the word is greater than 8
                    # then the following code will work
                    select_char = random.sample(gd.vocab_dict[i], k=4)  # randomly generating any four charater from the word
                    # and putting it in a list
                    turns = 5        # turns to guess the word is 5 if the length of word is greater than 8

                select_char = ''.join(select_char)     # converting the list to string

                word, guesses = gd.vocab_dict[i], select_char
                # assigning word from our dictionary to variable word and randomly generated character to variable guesses

                logging.info(f'Word :- {word}, Guesses :- {select_char}, Turns :- {turns}')
                # logging-info about word, guesses, turns

                print()
                time.sleep(0.5)        # stopping the time for 0.5 seconds

                print(f'{nme} you will get {turns} turns to guess the word')

                x = 0
                c = 0
                # for increasing the functunality of the program
                # c for seeing if the words are guessed right for three consecutive times then the tot_turns will be incremented by 1
                # x to see if user comes second time up then don't display the firstly displayed message

                while(turns > 0):
                    print()
                    time.sleep(0.5)         # stopping the time for 0.5 seconds

                    # now we will print the message for the user
                    # to help him understand how to play the game
                    # number of turns, the meaning of the word will be displayed here
                    # so that the user can guess the word

                    if(x == 0):
                        print(f'{nme} have to guess the word which have the following meaning :-')
                        print()
                        time.sleep(2)         # stopping the time for 0.5 seconds

                        print(i)              # here we will display the meaning of the word

                        print()
                        time.sleep(0.5)       # stopping the time for 0.5 seconds

                        while True:
                            try:
                                # try-exception block
                                x = input("Press the Enter key to start guessing ")
                                # this will ask user to press the enter key to play the game
                                if(x != ''):
                                    raise ge.EnterException
                                    # if some other key is pressed other than enter key
                                    # than EnterException will be rasied by the program
                                break   # breaking when the enter key is pressed

                            except ge.EnterException:
                                # when EnterException is rasied
                                time.sleep(0.5)             # stopping the time for 0.5 seconds

                            except ValueError:
                                print()
                                time.sleep(0.5)    # stopping the time for 0.5 seconds
                                print('Invalid Input...')   # printing invalid input if the error type - Value Error

                    else:
                        print(i)              # here we will display the meaning of the word
                        time.sleep(0.5)       # stopping the time for 0.5 seconds

                    a = 0            # initialising a counter variable a to 0
                    # it will help us to know whether the word is guessed or not

                    print()
                    time.sleep(0.5)     # stopping the time for 0.5 seconds

                    logging.info('Game is started')        # using logging.info

                    for j in word:
                        if j in guesses:
                            print(j, end=' ')
                            # if guesses and word both contains the same character then it will be printed on the screen
                        else:
                            print('_', end=' ')
                            # else an underscore will be printed
                            a += 1

                    logging.info('Starting the guessing')

                    print()
                    time.sleep(0.5)             # stopping the time for 0.5 seconds

                    if(a == 0):
                        # if the value of a is 0 then the word is rightly guessed
                        # and in that case right will increase by 1 point
                        c += 1         # incrementing c by one
                        print()
                        time.sleep(0.5)                 # stopping the time for 0.5 seconds
                        print(f'{nme} have guessed the word correctly')

                        logging.info(f'{nme} have guessed the word correctly')

                        print()
                        time.sleep(0.5)                 # stopping the time for 0.5 seconds

                        print(f'{word} :- {i}')
                        # displaying the word with it's meaning

                        right += 1          # right counter will be increased by one

                        logging.info('Guess is right, success is increased by 1')
                        logging.info('c the consecutive variable is increased by 1')

                        if(c == 3):
                            c = 0
                            print()
                            time.sleep(0.5)        # stopping the time for 0.5 seconds

                            print(f'{nme} you have rightly guessed 3 consecutive words.')
                            time.sleep(0.5)        # stopping the time for 0.5 seconds
                            print(f'So, one turn will be added to your Total Turns')

                            logging.info('3 consecutive guesses are right, one turn is incremented')

                            print()
                            time.sleep(0.5)        # stopping the time for 0.5 seconds

                            tot_turns += 1

                        print()
                        time.sleep(0.5)     # stopping the time for 0.5 seconds

                        tot_score = self.reuse_calculateScore(right, wrong)  # calling the reuse_calculateScore

                        logging.info('Calculating score')       # using logging.info

                        logging.info('Displaying score')        # using logging.info

                        self.display_score(nme, right, wrong, tot_score)    # calling the display_score function
                        # to display the score
                        time.sleep(0.5)     # stopping the time for 0.5 seconds
                        print(f'Total Turns left :- {tot_turns}')

                        print()
                        time.sleep(0.5)             # stopping the time for 0.5 seconds

                        self.reuse_enterException()            # calling the reuse function

                        time.sleep(0.5)    # stopping the time for 0.5 seconds

                        break

                    while True:
                        try:
                            # try-except clause
                            print()

                            guess = input("Guess a character :- ").strip()

                            logging.info(f'Guess is taken as {guess}')

                            # here the user can input the character which he/she want to guess
                            if(len(guess) < 1):
                                # if no character is entered
                                raise ge.ValueLessOne
                            elif(len(guess) > 1):
                                # if more than one character is entered
                                raise ge.ValueMoreOne
                            break   # breaking when only one character is entered

                        except ValueError:
                            print()
                            time.sleep(0.5)    # stopping the time for 0.5 seconds
                            print('Invalid Input...')   # printing invalid input if the error type - Value Error
                            logging.info('Value Error')  # using logging.info

                        except ge.ValueLessOne:
                            print()
                            time.sleep(0.5)    # stopping the time for 0.5 seconds
                            print('You have to enter only one character')
                            logging.info('One than one character is entered')      # using logging.info

                        except ge.ValueMoreOne:
                            print()
                            time.sleep(0.5)    # stopping the time for 0.5 seconds
                            print('You have to enter only one character')
                            logging.info('NO character has been entered')          # using logging.info

                    guesses += guess
                    # appending all the guess in guesses

                    x = 1

                    if guess not in word:
                        turns -= 1

                        if(turns > 1):
                            print()
                            time.sleep(0.5)    # stopping the time for 0.5 seconds

                            print(f'{nme} your guess {guess} is wrong!!!')  # displaying the message that the guess is wrong

                            logging.info(f'{nme} your guess {guess} is wrong!!!')    # using logging.info

                            time.sleep(0.5)    # stopping the time for 0.5 seconds

                            print(f'Total guesses left :- {turns}')

                            logging.info(f'Total guesses left :- {turns}')     # using logging.info

                            time.sleep(0.5)    # stopping the time for 0.5 seconds
                            print('Try Again!')

                            logging.info('Try Again!')      # using logging.info

                            time.sleep(0.5)    # stopping the time for 0.5 seconds

                        elif(turns == 1):
                            print()
                            time.sleep(0.5)    # stopping the time for 0.5 seconds

                            print(f'{nme} your guess {guess} is wrong!!!')  # displaying the message that the guess is wrong

                            logging.info(f'{nme} your guess {guess} is wrong!!!')     # using logging.info

                            time.sleep(0.5)    # stopping the time for 0.5 seconds

                            print(f'Total guesses left :- {turns}')

                            logging.info(f'Total guesses left :- {turns}')           # using logging.info

                            time.sleep(0.5)    # stopping the time for 0.5 seconds
                            print('It\'s your last guess. Guess it properly')

                            logging.info('It\'s your last guess. Guess it properly')  # using logging.info

                            time.sleep(0.5)    # stopping the time for 0.5 seconds

                        elif(turns == 0):
                            tot_turns -= 1
                            c = 0
                            wrong += 1
                            # if all your turns ended for guessing the word then
                            # 1 will be decremented from you total turns
                            # and c also becomes zero
                            print()
                            time.sleep(0.5)    # stopping the time for 0.5 seconds
                            print(f'{nme} you have guessed the word wrong')

                            print()
                            time.sleep(0.5)    # stopping the time for 0.5 seconds

                            print(f'The answer is {word}')

                            logging.info(f'{nme} you have guessed the word wrong')       # using logging.info

                            print()
                            time.sleep(0.5)    # stopping the time for 0.5 seconds

                            print('So, 1 turn is deducted from you total turn')

                            logging.info('So, 1 turn is deducted from you total turn')   # using logging.info

                            time.sleep(0.5)    # stopping the time for 0.5 seconds

                            tot_score = self.reuse_calculateScore(right, wrong)

                            logging.info('Calculating total score')

                            logging.info('Displaying the score')

                            print()

                            self.display_score(nme, right, wrong, tot_score)    # calling display_score()

                            # to display the score
                            time.sleep(0.5)    # stopping the time for 0.5 seconds
                            print(f'Total Turns Left :- {tot_turns}')

                            # using logging.info
                            logging.info(f'Total Turns Left :- {tot_turns}')

                            print()
                            time.sleep(0.5)    # stopping the time for 0.5 seconds

                            self.reuse_enterException()            # calling the reuse function

                if(tot_turns == 0):
                    print()
                    time.sleep(0.5)     # stopping the time for 0.5 seconds

                    print(f'{nme} you have lost all you turns')

                    logging.info(f'{nme} you have lost all you turns')        # using logging.info

                    tot_score = self.reuse_calculateScore(right, wrong)

                    logging.info('Calculating total score')                  # using logging.info
                    logging.info('Displaying the score')                     # using logging.info

                    print()
                    time.sleep(0.5)    # stopping the time for 0.5 seconds

                    self.display_score(nme, right, wrong, tot_score)    # calling display_score()
                    # to display the score
                    time.sleep(0.5)    # stopping the time for 0.5 seconds

                    self.listofArray(nme, tot_score, right, wrong)
                    # calling listofArray function

                    logging.info('Saving the information in the file gameInfo.txt')       # using logging.info

                    print()
                    time.sleep(0.5)    # stopping the time for 0.5 seconds

                    g = 19
                    # initialising variable g to value 19

                    sys.stdout.write('Saving Your Score')
                    sys.stdout.flush()
                    time.sleep(1)
                    sys.stdout.write('\r')
                    sys.stdout.write('                       \n')
                    # using sys.stdout function displaying interactive message

                    for i in range(20):
                        sys.stdout.write('\r')
                        sys.stdout.write('[' + '=' * i + ' ' * (g - i) + ']')
                        sys.stdout.flush()
                        time.sleep(0.05)

                    sys.stdout.write('\r')
                    sys.stdout.write('                                \n')

                    print(f'{nme} your score has been saved')
                    # printing the message that the user's score has been saved

                    logging.info(f'{nme} your score has been saved')      # using logging.info

                    print()
                    time.sleep(0.5)

                    print('* The Game Ends Here *')

                    logging.info('The Game Ends Here')          # using logging.info

                    print()
                    time.sleep(0.5)       # stopping the time for 0.5 seconds

                    self.reuse_enterException()     # calling reuse_enterException function

                    break         # breaking the loop when the game ends

    def scoreTable(self):
        # screTable function for creating a table to display the score of the users
        # it will display position, name, successful attempts, unsuccessful attempts and total score of the users
        # it will display the stats of every individual who have played the game.

        self.sortScore()             # calling sortScore function

        logging.info('Displaying the score in a tabular format')        # using logging.info

        try:
            # try-except exception
            with open('gameInfo.txt', 'rb') as my_file:
                # opening the file as read binary
                file_loader = pickle.load(my_file)          # loading the file

                max_name = max(len(i.name) for i in file_loader)    # max length of name

                max_totscore = max(len(str(i.total_score)) for i in file_loader)   # max length of total score

                max_success = max(len(str(i.success)) for i in file_loader)        # max length of sucess

                max_fail = max(len(str(i.fail)) for i in file_loader)              # max length of fail

                top_name = ['Position', 'Name', 'Total Score', 'Successful Attempts', 'Failed Attempts']

                # maxl is the list of maximum length of every element
                maxl = [max(len(file_loader), len(top_name[0])), max(max_name, len(top_name[1])), max(max_totscore, len(top_name[2])),
                        max(max_success, len(top_name[3])), max(max_fail, len(top_name[4]))]

                num_dashes = 0      # initialising num_dashes to 0

                # printing all the headings into the table
                for i in range(len(maxl)):
                    num_dashes += len('| ' + top_name[i] + ' ' * (maxl[i] - len(top_name[i])) + ' |')
                    print('| ' + top_name[i] + ' ' * (maxl[i] - len(top_name[i])) + ' |', end='')
                print(end='\n')

                print('=' * num_dashes)

                z, pos = [], 1
                # z is a list which will contain every information

                # appending every information in z
                # which is to be printed in the table
                for i in file_loader:
                    z.append(str(pos))
                    z.append(i.name)
                    z.append(str(i.total_score))
                    z.append(str(i.success))
                    z.append(str(i.fail))
                    pos += 1

                i, j, v, k = 0, 0, len(z) - 1, 5

                # printing the required information into the table
                while(i <= v):
                    print('| ' + z[i] + ' ' * (maxl[j] - len(z[i])) + ' |', end='')
                    i += 1
                    j += 1

                    if(i == k):
                        time.sleep(0.5)       # stopping the time for 0.5 seconds
                        print(end='\n')

                        k += 5

                    if(j == 5):
                        j = 0

        except FileNotFoundError:
            # if file not found error is caught
            print('No user has palyed the game yet')

            logging.info('No user has palyed the game yet')      # using logging.info


class Insert_list(FunctionCode):
    # this class is the sub class of FunctionCode
    # it will there to include all the info into a list
    # which will be a list of objects

    def __init__(self, name, total_score, success, fail, user_info):
        super(FunctionCode, self).__init__()     # using super function
        self.user_info = user_info      # self.user_info data member a list of objects

    def listofArray(self, nme, tot_score, right, wrong):
        try:
            # try-exception clause
            with open('gameInfo.txt', 'rb') as my_file:
                x = pickle.load(my_file)    # loading the content of the file
                self.user_info = x
        except FileNotFoundError:
            # pass when File not found error is caught
            pass
        with open('newfile.txt', 'wb') as new_file:
            self.user_info.append(FunctionCode(nme, tot_score, right, wrong))
            # appending the info as object into the list user_info
            # which is actually is a list of objects
            pickle.dump(self.user_info, new_file)
            # dumping the info to the file

        try:
            # try-exception clause
            os.remove('gameInfo.txt')   # removing the file
        except FileNotFoundError:
            # passing when the program encounters File not found error
            pass

        os.rename('newfile.txt', 'gameInfo.txt')
        # gameInfo.txt is the file where we are going to dump evey information of the user

    def sortScore(self):
        # sortScore will sort the scores in desending order

        logging.info('Sorting Score in decending form')

        try:
            # try-except clause
            with open('gameInfo.txt', 'rb') as my_file:
                x = pickle.load(my_file)
                # loading the content of the file
        except FileNotFoundError:
            # pass when fine not found error is caught
            pass

        with open('newfile.txt', 'wb') as new_file:
            x.sort(key=operator.attrgetter('total_score'), reverse=True)
            # sorting our list of array as per the total score
            self.game_info = x
            pickle.dump(self.game_info, new_file)
            # dumping the list of objects into our file

        try:
            # try-except clause
            os.remove('gameInfo.txt')
            # removing the file
        except FileNotFoundError:
            # passing it when file not found error is caught
            pass

        os.rename('newfile.txt', 'gameInfo.txt')
        # renaming the file
