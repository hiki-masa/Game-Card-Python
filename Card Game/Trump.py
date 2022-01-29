from enum import Enum
import os
import random
import tkinter as tk
from PIL import Image, ImageTk

# シンボルクラス
class SYMBOL_LIST(Enum):
    Spade = (0, "♠", "spade")
    Heart = (1, "♡", "heart")
    Dia   = (2, "♢", "diamond")
    Club  = (3, "♣", "club")

    # コンストラクタ
    def __init__(self, _id, _symbol, _symbol_name):
        self.id = _id
        self.symbol = _symbol
        self.symbol_name = _symbol_name

    # 全メンバー取得
    @classmethod
    def symbol_list(cls):
        return [*cls.__members__.values()]

    # 指定した id のメンバーを取得 
    @classmethod
    def return_symbol(cls, _id):
        for s in cls.symbol_list():
            if s.id == _id:
                return s


# ナンバークラス
class NUMBER_LIST(Enum):
    Ace   = ( 1, "01", 11)
    Two   = ( 2, "02", 12)
    Three = ( 3, "03", 0)
    Four  = ( 4, "04", 1)
    Five  = ( 5, "05", 2)
    Six   = ( 6, "06", 3)
    Seven = ( 7, "07", 4)
    Eight = ( 8, "08", 5)
    Nine  = ( 9, "09", 6)
    Ten   = (10, "10", 7)
    Jack  = (11, "11", 8)
    Queen = (12, "12", 9)
    King  = (13, "13", 10)

    # コンストラクタ
    def __init__(self, _number, _number_tag, _strong):
        self.number = _number
        self.number_tag = _number_tag
        self.strong = _strong

    # 全メンバー取得
    @classmethod
    def number_list(cls):
        return [*cls.__members__.values()]

    # 指定した number のメンバーを取得 
    @classmethod
    def return_number(cls, _number):
        for n in cls.number_list():
            if n.number == _number:
                return n


# カードクラス
class CARD():
    width = 135
    height = 200
    # コンストラクタ
    def __init__(self, _symbol_list, _number_list):
        # シンボル
        self.symbol_list = _symbol_list
        # ナンバー
        self.number_list = _number_list
        # カード画像（表画像の読み込み）
        self.surface_image = self.read_file_image("trump/card_" + self.symbol_list.symbol_name + "_" + self.number_list.number_tag + ".png")
        # カード画像（裏画像の読み込み）
        self.back_image = self.read_file_image("trump/card_back.png")
        
    # デコンストラクタ
    def __del__(self):
        print("memory-release : " + self.symbol_list.symbol_name + "-" + self.number_list.number_tag)

    # 指定されたファイル画像の読み込み
    def read_file_image(self, _file_name):
        if os.path.exists(_file_name):
            return ImageTk.PhotoImage(Image.open(_file_name).resize((CARD.width, CARD.height)))
        else:
            print("There isn't the file : " + _file_name)
            exit()

    # 表示
    def display(self):
        print(self.symbol_list.symbol, " - ", self.number_list.number_tag)

    # 画像表示
    def display_surface_image(self, _display_x, _display_y, _window):
        _window.create_image(_display_x + self.surface_image.width() / 2, _display_y + self.surface_image.height() / 2, image=self.surface_image)
        _window.update()
    def display_back_image(self, _display_x, _display_y, _window):
        _window.create_image(_display_x + self.back_image.width() / 2, _display_y + self.back_image.height() / 2, image=self.back_image)
        _window.update()


# トランプクラス
class TRUMP():
    # コンストラクタ
    def __init__(self):
        self.draw_list = []
        self.card_list = []
        for s in range(len(SYMBOL_LIST)):
            for n in range(len(NUMBER_LIST)):
                self.card_list.append(
                    CARD(_symbol_list = SYMBOL_LIST.return_symbol(_id = s),
                         _number_list = NUMBER_LIST.return_number(_number = n + 1)
                         )
                )

    # 現在のカードリストの表示
    def show_card_list(self):
        for i in range(len(self.card_list)):
            self.card_list[i].display()

    # シャッフル
    def Shuffle(self):
        random.shuffle(self.card_list)

    # ドロー可能判定
    def can_draw(self):
        if len(self.card_list) == 0:
            return False
        else:
            return True
    # ドロー
    def draw(self):
        if not self.can_draw():
            print("can't draw card")
        else:
            # 引いたカードは draw_list に保存
            self.draw_list.append(self.card_list.pop())
            return self.draw_list[-1]

    # 捨てたカードリストを解放
    def del_draw_list(self):
        self.draw_list.clear()