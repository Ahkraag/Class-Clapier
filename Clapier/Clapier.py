class Lapins:
    # Cette classe représente les lapins
    '''Cette classe représente les lapins'''

    def __init__(self, a=0):
        '''Constructeur de la classe Lapins, reçoit un paramêtre de type entier naturel'''
        self.setAge(a)

    def vieillir(self):  # fais vieillir le couple de lapins
        self.age += 1
        return self.age

    def getAge(self):
        '''Permet l'accès en mode lecture de l'age des lapins'''
        print(self.age)
        return self.age

    def setAge(self, n):
        '''Permet de modifier l'age des lapins avec un nombre entier supérieur a zero'''
        if type(n) == int and n >= 0:
            self.age = n

    def reproduire(self):  # permet de determiner si un couple de lapin peut se reproduire
        return self.age >= 2

    def reproduction(self):  # permet de faire reproduire un couple de lapins
        if self.reproduire():
            lapinou = Lapins()
            return lapinou

    def affiche(self):
        print(self.age)

    def __str__(self):
        return str(self.age) + " Mois"


######################################################################

class Clapier:
    # Cette classe représente le clapier qui contient les lapins
    '''Cette classe représente le clapier qui contient les lapins'''

    def __init__(self, a=[]):
        '''Constructeur de la classe Clapier, reçoit en paramêtre un tableau'''
        self.setCouple(a)

    def getCouple(self):
        '''Renvoi en mode lecture le nombre de tous les lapins'''
        return len(self.leslapins)

    def setCouple(self, n):
        '''Permet la modification du clapier avec vos lapins, reçoit en paramêtre un tableau'''
        if type(n) == list:
            self.leslapins = n
            self.couples = len(self.leslapins)

    def mois(self):  # fais passer un mois
        for couple in self.leslapins:
            couple.vieillir()
        for couple in self.leslapins:
            a = couple.reproduction()
            if a is not None:
                self.leslapins.append(a)
                self.couples += 1

    def __str__(self):
        fin = "Ce clapier contient " + str(self.getCouple()) + " couples de lapins\n"
        fin += "["
        for k in self.leslapins:
            fin += str(k.age) + " mois,"
        fin += "]"
        return fin


##################--TEST--####################################################

mois = 5
c = Clapier()
a = [Lapins(478779), Lapins(5444), Lapins(676874)]
a = [Lapins(5)]
c.setCouple(a)
b = Lapins()
print(c.couples)
for nb_mois in range(mois):
    c.mois()
    print(c.couples)

# help(Lapins)
print(c)