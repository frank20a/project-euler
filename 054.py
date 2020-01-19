class Hand:
    def __init__(self, r, s=0, t=0, f=0):
        self.rank = r
        self.second = s
        self.third = t
        self.fourth = f
    def compare(self, Card: a):
        if self.rank 

class Highcard (Hand):
    def __init__(self, s, t, f):
        super(1, s, t, f)

class Card:
    def __init__(self, x):
        self.n = x[0]
        if self.n == 'A':
            self.n = 14
        elif self.n == 'T':
            self.n = 10
        elif self.n == 'J':
            self.n = 11
        elif self.n == 'Q':
            self.n = 12
        elif self.n == 'K':
            self.n = 13
        else:
            self.n = int(self.n)

        self.s = x[1]

    def __str__(self):
        return str(self.n) + self.s


def rateHand(x):
    pass


f = open('input/p054_poker.txt', 'r')
a = f.readlines()
for i in a:
    p1 = [Card(j) for j in i[:14].split(' ')]
    p2 = [Card(j) for j in i[15:len(i) - 1].split(' ')]
