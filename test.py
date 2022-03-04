import xxx.yyy.zzz

# fichier de test
valeur = 1


class Toto:
    def __init__(self, x):
        self.ma_valeur = x
        self.ma_valeur = self.ma_valeur * 2
        self.test = "quoted line"

    def __repr__(self):
        return repr(self.ma_valeur)


t = Toto(5)
print(t)
