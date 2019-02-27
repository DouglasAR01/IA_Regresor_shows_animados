import pandas as pd
import numpy as np

class vec:
    def __init__(self):
        self.lista = np.zeros(17)
    def romance(self):
        self.lista[0] = 1
    def shoujo(self):
        self.lista[1] = 1
    def ecchi(self):
        self.lista[2] = 1
    def shounen(self):
        self.lista[3] = 1
    def fantasy(self):
        self.lista[4] = 1
    def comedy(self):
        self.lista[5] = 1
    def music(self):
        self.lista[6] = 1
    def sports(self):
        self.lista[7] = 1
    def hentai(self):
        self.lista[8] = 1
    def historical(self):
        self.lista[9] = 1
    def mistery(self):
        self.lista[10] = 1
    def thriller(self):
        self.lista[11] = 1
    def supernatural(self):
        self.lista[12] = 1
    def gore(self):
        self.lista[13] = 1
    def sciFi(self):
        self.lista[14] = 1
    def action(self):
        self.lista[15] = 1
    def otro(self):
        self.lista[16] = 1
    def getLista(self):
        return self.lista

def indirect(i, o):
    sw = o;
    switcher={
        'Romance': sw.romance,
        'Shoujo': sw.shoujo,
        'Ecchi': sw.ecchi,
        'Shounen': sw.shounen,
        'Fantasy': sw.fantasy,
        'Comedy': sw.comedy,
        'Music': sw.music,
        'Sports': sw.sports,
        'Hentai': sw.hentai,
        'Historical': sw.historical,
        'Mistery': sw.mistery,
        'Thriller': sw.thriller,
        'Supernatural': sw.supernatural,
        'Gore': sw.gore,
        'Sci-Fi': sw.sciFi,
        'Action': sw.action
    }
    func=switcher.get(i,sw.otro)

    return func(), sw.getLista()

a = 'Action, Drama, Fantasy, Horror, Romance, Sci-Fi, Vampire'
b = a.split(', ')
obj = vec()
for i in b:
    lista = indirect(i, obj)
a = lista
print a
