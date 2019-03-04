import pandas as pd
import numpy as np

class source_num:
    def __init__(self):
        self.res = 'nan'
    def komaManga(self):
        self.res = 0
    def book(self):
        self.res = 1
    def cardGame(self):
        self.res = 2
    def digitalManga(self):
        self.res = 3
    def game(self):
        self.res = 4
    def lightNovel(self):
        self.res = 5
    def manga(self):
        self.res = 6
    def music(self):
        self.res = 7
    def novel(self):
        self.res = 8
    def original(self):
        self.res = 9
    def other(self):
        self.res = 10
    def pictureBook(self):
        self.res = 11
    def radio(self):
        self.res = 12
    def visualNovel(self):
        self.res = 13
    def webManga(self):
        self.res = 14
    def otro(self):
        self.res = 15
    def getRes(self):
        return self.res

def source_parser(source):
    sw = source_num()
    switcher={
        '4-Koma manga': sw.komaManga,
        'Book': sw.book,
        'Card game': sw.cardGame,
        'Digital manga': sw.digitalManga,
        'Game': sw.game,
        'Light novel': sw.lightNovel,
        'Manga': sw.manga,
        'Music': sw.music,
        'Novel': sw.novel,
        'Original': sw.original,
        'Other': sw.other,
        'Picture book': sw.pictureBook,
        'Radio': sw.radio,
        'Visual novel': sw.visualNovel,
        'Web manga': sw.webManga
    }
    func=switcher.get(source, sw.otro)

    return func(), sw.getRes()

a = 'Visual novel'

swi = source_num()

print source_parser(a)[1]
