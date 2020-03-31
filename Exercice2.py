class Complex:
    def __init__(self,r=0,i=0):
        self.__reel = r
        self.__im = i

    def __add__(self, c2):
        return Complex(self.__reel + c2.__reel, self.__im + c2.__im)

    def __sub__(self, c2):
        return Complex(self.__reel - c2.__reel, self.__im - c2.__im)

    def __mul__(self, c2):
        return Complex(self.__reel * c2.__reel, self.__im * c2.__im)

    def __truediv__(self, c2):
        return Complex(self.__reel / c2.__reel, self.__im / c2.__im)

    def __abs__(self):
        if self.__reel < 0 :
            self.__reel = - self.__reel
        if self.__im < 0 :
            self.__im = - self.__im

    def __eq__(self, c2):
        if self.__reel == c2.__reel and self.__im == c2.__im :
            return True
        else:
            return False

    def __ne__(self, c2):
        if self.__reel == c2.__reel and self.__im == c2.__im :
            return False
        else:
            return True

complex1 = Complex(1,1)
complex2 = Complex(2,2)
complex3 = complex1 + complex2
complex4 = complex1 - complex2
complex5 = complex1 / complex2
complex6 = abs(complex1)
c4 = complex1 == complex2
c5 = complex1 != complex2
print(c4)
print(c5)
