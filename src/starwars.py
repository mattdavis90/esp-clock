from micropython import const
from utime import sleep_ms

from buzzer import buzzer


C4  = const(261)
D4  = const(294)
E4  = const(329)
F4  = const(349)
G4  = const(391)
G4S = const(415)
A4  = const(440)
A4S = const(455)
B4  = const(466)
C5  = const(523)
C5S = const(554)
D5  = const(587)
D5S = const(622)
E5  = const(659)
F5  = const(698)
F5S = const(740)
G5  = const(784)
G5S = const(830)
A5  = const(880)


class StarWars():
    """Plays StarWars!!!"""
    def __init__(self, buzzer):
        self._buzzer = buzzer

    def _buzz(self, f, t):
        """Wraps buzzer's buzz with a slight pause
        """
        self._buzzer.buzz(f, t)
        sleep_ms(50)

    def play(self):
        """Play the song
        """
        #Play first section
        self._firstSection()

        #Play second section
        self._secondSection()

        #Variant 1
        self._buzz(F4,  250)
        self._buzz(G4S, 500)
        self._buzz(F4,  350)
        self._buzz(A4,  125)
        self._buzz(C5,  500)
        self._buzz(A4,  375)
        self._buzz(C5,  125)
        self._buzz(E5,  650)

        sleep_ms(500)

        #Repeat second section
        self._secondSection()

        #Variant 2
        self._buzz(F4,  250)
        self._buzz(G4S, 500)
        self._buzz(F4,  375)
        self._buzz(C5,  125)
        self._buzz(A4,  500)
        self._buzz(F4,  375)
        self._buzz(C5,  125)
        self._buzz(A4,  650)

        sleep_ms(650)

    def _firstSection(self):
        self._buzz(A4, 500)
        self._buzz(A4, 500)
        self._buzz(A4, 500)
        self._buzz(F4, 350)
        self._buzz(C5, 150)
        self._buzz(A4, 500)
        self._buzz(F4, 350)
        self._buzz(C5, 150)
        self._buzz(A4, 650)

        sleep_ms(500)

        self._buzz(E5,  500)
        self._buzz(E5,  500)
        self._buzz(E5,  500)
        self._buzz(F5,  350)
        self._buzz(C5,  150)
        self._buzz(G4S, 500)
        self._buzz(F4,  350)
        self._buzz(C5,  150)
        self._buzz(A4,  650)

        sleep_ms(500)

    def _secondSection(self):
        self._buzz(A5,  500)
        self._buzz(A4,  300)
        self._buzz(A4,  150)
        self._buzz(A5,  500)
        self._buzz(G5S, 325)
        self._buzz(G5,  175)
        self._buzz(F5S, 125)
        self._buzz(F5,  125)
        self._buzz(F5S, 250)

        sleep_ms(325)

        self._buzz(A4S, 250)
        self._buzz(D5S, 500)
        self._buzz(D5,  325)
        self._buzz(C5S, 175)
        self._buzz(C5,  125)
        self._buzz(B4,  125)
        self._buzz(C5,  250)

        sleep_ms(350)


starwars = StarWars(buzzer)
