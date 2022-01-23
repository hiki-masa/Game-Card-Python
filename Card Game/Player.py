import tkinter as tk
from Trump import CARD

class PLAYER():
    # コンストラクタ
    def __init__(self, _id, _name):
        self.id = _id
        self.draw_list = []
        self.name = _name
        self.info = tk.Label(text = "", bg = "green")

    # ドロー
    def draw(self, trump):
        draw_card = trump.draw()
        if type(draw_card) == CARD:
            self.draw_list.append(draw_card)
        else:
            print("Error : enter something different class from planned")

    # 与えられたCardクラス配列の合計値計算
    def sum_card_number(self):
        sum = 0
        for i in range(len(self.draw_list)):
            sum = sum + self.draw_list[i].number_list.number
        return sum


class COMPUTER(PLAYER):
    # コンストラクタ
    def __init__(self, _id, _name):
        super().__init__(_id, _name)
        self.judg_draw = True

    # カードを引くかどうかの判定
    def judg_draw_card(self):
        if self.judg_draw == False:
            return False
        else:
            if self.sum_card_number() >= 21:
                self.judg_draw = False
                return False
            else:
                return True

class HUMAN(PLAYER):
    # コンストラクタ
    def __init__(self, _id, _name):
        super().__init__(_id, _name)
        self.judg_draw = True

    def update_judg_draw_card(self, button_bool_var):
        self.judg_draw = False
        button_bool_var.set(not button_bool_var.get())