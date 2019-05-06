class MyBad(Exception):
    pass

def stuff():
    raise MyBad #ele taca essa excessao

try:
    stuff()
except MyBad:
    print('got it')


##########################################################################################

class Sorry(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

def anything(message):
    raise Sorry(message)

try:
    anything("Your bad")
except Sorry as error:
    print('got it (message: {})'.format(error.message))    