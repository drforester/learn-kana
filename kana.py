from tkinter import Tk, Button
from tkinter.font import Font
from copy import deepcopy
import random

tsz = 20 # the default text size

class Board:
  
    def __init__(self,other=None):
        
        self.hchars = [['ぱ','ば','だ','ざ','が','ん','わ','ら','や','ま','は','な','た','さ','か','あ'],
                       ['ぴ','び','ぢ','じ','ぎ',' ',' ','り',' ','み','ひ','に','ち','し','き','い'],
                       ['ぷ','ぶ','づ','ず','ぐ',' ',' ','る','ゆ','む','ふ','ぬ','っ','す','く','う'],
                       ['ぺ','べ','で','ぜ','げ',' ',' ','れ',' ','め','へ','ね','て','せ','け','え'],
                       ['ぽ','ぼ','ど','ぞ','ご',' ','を','ろ','よ','も','ほ','の','と','そ','こ','お']]

        self.kchars = [['パ','バ','ダ','ザ','ガ','ン','ワ','ラ','ヤ','マ','ハ','ナ','タ','サ','カ','ア'],
                       ['ピ','ビ','ヂ','ジ','ギ',' ',' ','リ',' ','ミ','ヒ','ニ','チ','シ','キ','イ'],
                       ['プ','ブ','ヅ','ズ','グ',' ',' ','ル','ユ','ム','フ','ヌ','ツ','ス','ク','ウ'],
                       ['ペ','ベ','デ','ゼ','ゲ',' ',' ','レ',' ','メ','ヘ','ネ','テ','セ','ケ','エ'],
                       ['ポ','ボ','ド','ゾ','ゴ',' ','ヲ','ロ','ヨ','モ','ホ','ノ','ト','ソ','コ','オ']]

        self.rchars = [['pa','ba','da','za','ga','n','wa','ra','ya','ma','ha','na','ta','sa','ka','a'],
                       ['pi','bi','ji(di)','ji','gi','','','ri','','mi','hi','ni','chi','shi','ki','i'],
                       ['pu','bu','zu(du)','zu','gu','','','ru','yu','mu','fu','nu','tsu','su','ku','u'],
                       ['pe','be','de','ze','ge','','','re','','me','he','ne','te','se','ke','e'],
                       ['po','bo','do','zo','go','','o(wo)','ro','yo','mo','ho','no','to','so','ko','o']]

        self.nrows = 5
        self.ncols = 16
        self.hfields = {}
        for y in range(self.nrows):
            for x in range(self.ncols):
                self.hfields[y,x] = self.hchars[y][x]
        self.kfields = {}
        for y in range(self.nrows):
            for x in range(self.ncols):
                self.kfields[y,x] = self.kchars[y][x]
        self.rfields = {}
        for y in range(self.nrows):
            for x in range(self.ncols):
                self.rfields[y,x] = self.rchars[y][x]
        
        # copy constructor
        if other:
            self.__dict__ = deepcopy(other.__dict__)

class Hiragana:

    def __init__(self):
        self.app = Tk()
        self.app.title('Learn Kana')
        self.app.resizable(width=False, height=False)
        self.board = Board()
        self.kana = 'i'
        self.width = 5
        self.font = Font(family="Hack", size=tsz)
        self.foreground = 'white'

        # switch buttons
        handler = lambda: self.switch_kana()
        self.button1 = Button(self.app, text='かな - ろーまじ', bg='crimson', fg='white',
                              font=self.font, command=handler)
        self.button1.grid(row=0, column=0, columnspan=int((self.board.ncols/2)), sticky="WE")
        handler = lambda: self.switch_roma()
        self.button2 = Button(self.app, text='ろーまじ - かな', bg='crimson', fg='white',
                              font=self.font, command=handler)
        self.button2.grid(row=0, column=int((self.board.ncols/2)), columnspan=self.board.ncols, sticky="WE")

        # array of character buttons
        self.buttons = {}
        for y in range(self.board.nrows):
            for x in range(self.board.ncols):
                handler = lambda y=y,x=x: self.reveal(y,x)
                button = Button(self.app, bg='lightsalmon', command=handler, font=self.font, width=self.width, height=2)
                button.grid(row=y+1, column=x)
                self.buttons[y,x] = button
      
    def switch_kana(self):
        if self.kana == 'h':
            self.kana = 'k'
            self.button1['text'] = 'かたかな - ろーまじ'
        else:
            self.kana = 'h'
            self.button1['text'] = 'ひらがな - ろーまじ'
        self.button2['text'] = 'ろーまじ'
        self.update()
        
    def switch_roma(self):
        if self.kana == 'th':
            self.kana = 'tk'
            self.button2['text'] = 'ろーまじ - かたかな'
        else:
            self.kana = 'th'
            self.button2['text'] = 'ろーまじ - ひらがな'
        self.button1['text'] = 'かな'
        self.update()
    
    def reveal(self,y,x):
        self.board = Board()
        if self.kana == 'h' or self.kana == 'k':
            self.buttons[y,x]['text'] = self.board.rchars[y][x]
            self.buttons[y,x]['width'] = int(round(self.width))
            self.buttons[y,x]['bg'] = 'darksalmon'
            self.app.after(1000, self.update)
        elif self.kana == 'th':
            self.buttons[y,x]['text'] = self.board.hchars[y][x]
            self.buttons[y,x]['width'] = int(round(self.width))
            self.buttons[y,x]['bg'] = 'darksalmon'
            self.app.after(1000, self.update)
        elif self.kana == 'tk':
            self.buttons[y,x]['text'] = self.board.kchars[y][x]
            self.buttons[y,x]['width'] = int(round(self.width))
            self.buttons[y,x]['bg'] = 'darksalmon'
            self.app.after(1000, self.update)
        else:
            self.buttons[y,x]['text'] = random.choice(['|･ω･)','|_・)','(¯︶¯)','(⁀ᗢ⁀)','(^ ω ^)'])
            self.buttons[y,x]['width'] = int(round(self.width))
            self.buttons[y,x]['bg'] = 'darksalmon'
            self.app.after(1000, self.update)            
     
    def update(self):
        for (y,x) in self.board.hfields:
            if self.kana == 'k':
                text = self.board.kfields[y,x]
            elif self.kana == 'h':
                text = self.board.hfields[y,x]
            elif self.kana == 'th' or self.kana == 'tk':
                text = self.board.rfields[y,x]
            else:
                text = ''
            self.buttons[y,x]['text'] = text
            self.buttons[y,x]['width'] = self.width
            self.buttons[y,x]['bg'] = 'lightsalmon'
            if self.buttons[y,x]['text'] in [' ']:
                self.buttons[y,x]['state'] = 'disabled' 
    
    def mainloop(self):
        self.app.mainloop()


if __name__ == '__main__':
    Hiragana().mainloop()
