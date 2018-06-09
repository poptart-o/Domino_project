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


class Caja(object):

    def __init__(self):

        self.caja = []

    def crear(self):
        for valor1 in range(0, 7):
            for valor2 in range(valor1, 7):
                self.caja.append(Ficha(valor1, valor2))

    def mostrar(self):
        if len(self.caja) == 0:
            print 'No hay fichas en la caja'
        for ficha in self.caja:
            print [ficha.value1, ficha.value2]

    def barajar(self):
        for i in range(1, len(self.caja) - 1, -1):
            r = random.randint(0, i)
            self.caja[i], self.caja[r] = self.caja[r], self.caja[i]

    def tomar_ficha(self):
        return self.caja.pop()
