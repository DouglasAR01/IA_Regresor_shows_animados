import pandas as pd
import numpy as np

class atype_num:
    def __init__(self):
        self.res = 'nan'
    def movie(self):
        self.res = 0
    def music(self):
        self.res = 1
    def ona(self):
        self.res = 2
    def ova(self):
        self.res = 3
    def special(self):
        self.res = 4
    def tv(self):
        self.res = 5
    def otro(self):
        self.res = 6
    def getRes(self):
        return self.res

def atype_parser(atype):
    sw = atype_num()
    switcher={
        'Movie': sw.movie,
        'Music': sw.music,
        'ONA': sw.ona,
        'OVA': sw.ova,
        'Special': sw.special,
        'TV': sw.tv
    }
    func=switcher.get(atype, sw.otro)

    return func(), sw.getRes()

a = 'Music'

swi = atype_num()

print atype_parser(a)[1]
