# Vocab's game gameException code.
# it will contain all the user-defined exception.
# these exceptions will be used in our main file.
# by including this file in gameMenu file.


class ValueMoreOne(Exception):
    # exception for value length more than one
    pass


class ValueLessOne(Exception):
    # exception for value length less than one
    pass


class EnterException(Exception):
    # exception when enter key is not pressed
    pass
