class Rational:
    def __init__(self,n=0,d=0):
        self.__numerateur = n
        self.__denominateur = d

    def __add__(self, r2):
        return Rational(self.__numerateur * r2.__denominateur + r2.__numerateur * self.__denominateur, self.__denominateur * r2.__denominateur)

    def __sub__(self, r2):
        return Rational(self.__numerateur * r2.__denominateur - r2.__numerateur * self.__denominateur, self.__denominateur * r2.__denominateur)

    def __mul__(self, r2):
        return Rational(self.__numerateur * r2.__numerateur, self.__denominateur * r2.__denominateur)

    def __truediv__(self, r2):
        return Rational(self.__numerateur * r2.__denominateur, self.__denominateur * r2.__numerateur)

    def __eq__(self, r2):
        if self.__numerateur == r2.__numerateur and self.__denominateur == r2.__denominateur :
            return True
        else:
            return False

r1 = Rational(3,4)
r2 = Rational(2,9)
r3 = r1 + r2
r4 = r3 - r1
r5 = r4 * r3
r6 = r5 / r1
r7 = r6 == r4
print(r7)
