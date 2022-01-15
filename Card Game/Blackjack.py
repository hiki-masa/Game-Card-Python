import tkinter as tk
from time import sleep
import Window
import Trump
import Player

class BLACKJACK():
    # コンストラクタ
    def __init__(self, master):
        self.app = Window.WINDOW(master = master, _width = Trump.card_width * 7, _height = Trump.card_height * 2 + 100)
        self.app.master.title("Blackjack")
        self.app.option_add("*font", ["MS ゴシック", 20])
        self.trump = Trump.TRUMP()
        # 使用しないカードの破棄 & シャッフル
        for i in range (len(Trump.NUMBER_LIST) * (len(Trump.SYMBOL_LIST) - 1)):
            self.trump.drow()
        self.trump.del_trush_list()
        self.trump.Shuffle()
        # プレイヤーの設定
        self.player1 = Player.PLAYER()
        self.player2 = Player.PLAYER()
        self.game()

    def game(self):
        self.player1.drow(self.trump)
        self.player1.drow_card[-1].display_back_image(0, 0, self.app.canvas)
        self.player1_info = tk.Label(text = "相手の合計：" + str(self.player1.sum_card_number()), bg = "green")
        self.player1_info.place(x = 2, y = Trump.card_height * 2, width = 500, height = 50)
        
        self.player2.drow(self.trump)
        self.player2.drow_card[-1].display_surface_image(0, Trump.card_height, self.app.canvas)
        self.player2_info = tk.Label(text = "\n自分の合計：" + str(self.player2.sum_card_number()), bg = "green")
        self.player2_info.place(x = 2, y = Trump.card_height * 2 + 50, width = 500, height = 50)
        
        while (self.trump.can_drow()):
            if self.trump.can_drow():
                self.player1.drow(self.trump)
                self.player1_info["text"] = "相手の合計：" + str(self.player1.sum_card_number())
                self.player1.drow_card[-1].display_surface_image(Trump.card_width * (len(self.player1.drow_card) - 1), 0, self.app.canvas)
            sleep(2)
            if self.trump.can_drow():
                self.player2.drow(self.trump)
                self.player2_info["text"] = "\n自分の合計：" + str(self.player2.sum_card_number())
                self.player2.drow_card[-1].display_surface_image(Trump.card_width * (len(self.player2.drow_card) - 1), Trump.card_height, self.app.canvas)
            sleep(2)
