import random


class Ficha(object):

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def mostrar_ficha(self):
        print '''
         {}
        ---
         {}'''.format(self.value1, self.value2)
