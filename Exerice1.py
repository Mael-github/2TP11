class Cercle:
    def __init__(self,r):
        self.__rayon = r

    def __add__(self, c2):
        return Cercle(self.__rayon+c2.__rayon)

    def __lt__(self, c2):
        return self.__rayon < c2.__rayon

    def __gt__(self, c2):
        return self.__rayon > c2.__rayon

if __name__ == "__main__":
    c1 = Cercle(2)
    c2 = Cercle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c5)
