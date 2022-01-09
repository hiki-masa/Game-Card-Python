import tkinter as tk
from time import sleep
import Window
import Trump

class BLACKJACK(Window.WINDOW, Trump.TRUMP):
    # コンストラクタ
    def __init__(self, master):
        self.app = Window.WINDOW(master = master, _width = Trump.card_width * 7, _height = Trump.card_height * 2 + 100)
        self.app.master.title("Blackjack")
        self.app.option_add("*font", ["MS ゴシック", 20])
        self.trump = Trump.TRUMP()
        # 使用しないカードの破棄
        for i in range (len(Trump.NUMBER_LIST) * (len(Trump.SYMBOL_LIST) - 1)):
            self.trump.drow()
        self.trump.Shuffle()
        self.game()

    def game(self):
        opponent, myself = [], []
        opponent.append(self.trump.drow())
        opponent[0].display_back_image(0, 0, self.app.canvas)
        self.opp_info = tk.Label(text = "相手の合計：" + str(sum_card_number(opponent)), bg = "green")
        self.opp_info.place(x = 0, y = Trump.card_height * 2, width = 500, height = 50)
        myself.append(self.trump.drow())
        myself[0].display_surface_image(0, Trump.card_height, self.app.canvas)
        self.mys_info = tk.Label(text = "\n自分の合計：" + str(sum_card_number(myself)), bg = "green")
        self.mys_info.place(x = 0, y = Trump.card_height * 2 + 50, width = 500, height = 50)
        
        i = 0
        while (self.trump.can_drow()):
            i = i + 1
            if self.trump.can_drow():
                opponent.append(self.trump.drow())
                self.opp_info["text"] = "相手の合計：" + str(sum_card_number(opponent))
                opponent[i].display_surface_image(Trump.card_width * i, 0, self.app.canvas)
            sleep(2)
            if self.trump.can_drow():
                myself.append(self.trump.drow())
                self.mys_info["text"] = "\n自分の合計：" + str(sum_card_number(myself))
                myself[i].display_surface_image(Trump.card_width * i, Trump.card_height, self.app.canvas)
            sleep(2)
    

# 与えられたCardクラス配列の合計値計算
def sum_card_number(player_drow_card):
    sum = 0
    for i in range(len(player_drow_card)):
        sum = sum + player_drow_card[i].number_list.number
    return sum
