class Duree:
    def __init__(self,h=0,m=0,s=0):
        self.__heure = h
        self.__minute = m
        self.__seconde = s

    def __str__(self):
        return ( str(self.__heure) + "h"+ str(self.__minute) + "m" + str(self.__seconde) + "s" )

    def __add__(self, d2):
        sc= self.__seconde + d2.__seconde
        counter = 0
        while sc > 59 :
            sc = sc - 60
            counter = counter + 1
        mc= self.__minute + d2.__minute + counter
        counter = 0
        while mc > 59 :
            sc = sc - 60
            counter = counter + 1
        hc= self.__heure + d2.__heure + counter
        return Duree(hc,mc,sc)

d1 = Duree(1,2,3)
print(d1)
d2 = Duree(2,3,59)
d3 = d1 + d2
print(d3)
