import tkinter as tk
from Trump import CARD

class PLAYER():
    # コンストラクタ
    def __init__(self, _id, _name):
        self.id = _id
        self.drow_list = []
        self.name = _name
        self.info = tk.Label(text = "", bg = "green")

    # ドロー
    def drow(self, trump):
        drow_card = trump.drow()
        if type(drow_card) == CARD:
            self.drow_list.append(drow_card)
        else:
            print("Error : enter something different class from planned")

    # 与えられたCardクラス配列の合計値計算
    def sum_card_number(self):
        sum = 0
        for i in range(len(self.drow_list)):
            sum = sum + self.drow_list[i].number_list.number
        return sum