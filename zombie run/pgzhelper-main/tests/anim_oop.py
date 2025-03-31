from pgzhelper import *

class Test(Actor):
    def __init__(self):
        pass

    def move(self):
        if keyboard.left:
            print('left')
