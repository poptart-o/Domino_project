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


class Jugador(object):

    def __init__(self, name):
        self.name = name
        self.mano = []

    def tomar(self, caja):
        self.mano.append(caja.tomar_ficha())
        return self

    def mostrar_mano(self):
        for e in self.mano:
            e.mostrar_ficha()


class Mesa(Jugador):

    def __init__(self, name):
        super(Mesa, self).__init__(name)
        self.juego = {}

    def make_game(self, caja):
        self.juego[self.name] = []
        self.tomar(caja).tomar(caja).tomar(caja).tomar(caja).tomar(caja).tomar(caja).tomar(caja)

        for e in self.mano:
            self.juego[self.name].append([e.value1, e.value2])

    def mostrar_juego(self):
        return self.juego[self.name]


class Gameplay(object):

    game = []

    def __init__(self, player, game):
        self.name = player
        self.mano = game

    @staticmethod
    def revisar_si_jugador_esta_bloqueado(player, game):
        for ficha in player:
            for value in ficha:
                if value == Gameplay.game[-1][-1] or value == Gameplay.game[0][0]:
                    return False
        return True

    @staticmethod
    def revisar_si_juego_esta_bloqueado(p1, p2, p3, p4):
        if Gameplay.revisar_si_jugador_esta_bloqueado(p1, Gameplay.game) == True:

            if Gameplay.revisar_si_jugador_esta_bloqueado(p2, Gameplay.game) == True:

                if Gameplay.revisar_si_jugador_esta_bloqueado(p3, Gameplay.game) == True:

                    if Gameplay.revisar_si_jugador_esta_bloqueado(p4, Gameplay.game) == True:

                        return True
        return False

    @classmethod
    def poner_ficha(cls, player, player_game_mod, player_game, fichas_jugables=None):
        if fichas_jugables is None:
            fichas_jugables = []

        else:
            fichas_jugables = fichas_jugables

        if len(player_game) == 0:
            print "{} no tiene fichas".format(player.name)
            return True

        if [6, 6] in player_game_mod and len(cls.game) == 0:
            cls.game.append([6, 6])
            print "{} pone [6,6] en la mesa".format(player.name)
            player_game_mod.pop(player_game_mod.index([6, 6]))
            return

        if len(player_game) == 1:
            if len(fichas_jugables) == 0:
                if player_game[0][0] != cls.game[-1][-1] and player_game[0][1] != cls.game[-1][-1] and player_game[0][0] != cls.game[0][0] and player_game[0][1] != cls.game[0][0]:
                    print "{} ha sido bloqueado".format(player.name)
                    return False

                else:
                    if player_game[0][0] == cls.game[-1][-1]:
                        cls.game.append(player_game[0])
                        print "{} pone {} en la mesa".format(player.name, player_game[0])

                        player_game_mod.pop(player_game_mod.index(player_game[0]))
                        if len(player_game) == 0:
                            print "{} ha ganado el juego".format(player.name)
                        return True

                    elif player_game[0][1] == cls.game[-1][-1]:
                        cls.game.append(player_game[0][::-1])
                        print "{} pone {} en la mesa".format(player.name, player_game[0])

                        player_game_mod.pop(player_game_mod.index(player_game[0]))
                        if len(player_game) == 0:
                            print "{} ha ganado el juego".format(player.name)
                        return True

                    elif player_game[0][0] == cls.game[0][0]:
                        cls.game[0:0] = [player_game[0][::-1]]
                        print "{} pone {} en la mesa".format(player.name, player_game[0])

                        player_game_mod.pop(player_game_mod.index(player_game[0]))
                        if len(player_game) == 0:
                            print "{} ha ganado el juego".format(player.name)
                        return True

                    else:
                        if player_game[0][1] == cls.game[0][0]:
                            cls.game[0:0] = [player_game[0]]
                            print "{} pone {} en la mesa".format(player.name, player_game[0])

                            player_game_mod.pop(player_game_mod.index(player_game[0]))
                            if len(player_game) == 0:
                                print "{} ha ganado el juego".format(player.name)
                            return True

            if len(fichas_jugables) > 0:
                if player_game[0][0] == cls.game[-1][-1] or player_game[0][1] == cls.game[-1][-1] or player_game[0][0] == cls.game[0][0] or player_game[0][1] == cls.game[0][0]:
                    fichas_jugables.append(player_game[0])

                ficha_random = random.randint(0, len(fichas_jugables) - 1)

                if fichas_jugables[ficha_random][0] == cls.game[-1][-1]:
                    cls.game.append(fichas_jugables[ficha_random])
                    print "{} pone {} en la mesa".format(player.name, fichas_jugables[ficha_random])
                    player_game_mod.pop(player_game_mod.index(fichas_jugables[ficha_random]))

                elif fichas_jugables[ficha_random][1] == cls.game[-1][-1]:
                    cls.game.append(fichas_jugables[ficha_random][::-1])
                    print "{} pone {} en la mesa".format(player.name, fichas_jugables[ficha_random])
                    player_game_mod.pop(player_game_mod.index(fichas_jugables[ficha_random]))

                elif fichas_jugables[ficha_random][0] == cls.game[0][0]:
                    cls.game[0:0] = [fichas_jugables[ficha_random][::-1]]
                    print "{} pone {} en la mesa".format(player.name, fichas_jugables[ficha_random])
                    player_game_mod.pop(player_game_mod.index(fichas_jugables[ficha_random]))

                else:
                    if fichas_jugables[ficha_random][1] == cls.game[0][0]:
                        cls.game[0:0] = [fichas_jugables[ficha_random]]
                        print "{} pone {} en la mesa".format(player.name, fichas_jugables[ficha_random])
                        player_game_mod.pop(player_game_mod.index(fichas_jugables[ficha_random]))
        else:
            if player_game[0][0] == cls.game[-1][-1] or player_game[0][1] == cls.game[-1][-1] or player_game[0][0] == cls.game[0][0] or player_game[0][1] == cls.game[0][0]:
                fichas_jugables.append(player_game[0])
                return cls.poner_ficha(player, player_game_mod, player_game[1:], fichas_jugables)
            else:
                return cls.poner_ficha(player, player_game_mod, player_game[1:], fichas_jugables)

