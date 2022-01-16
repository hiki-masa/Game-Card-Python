import tkinter as tk
from time import sleep
from Window import WINDOW
import Trump
from Player import PLAYER

class BLACKJACK():
    # コンストラクタ
    def __init__(self, master):
        # ウィンドウの設定
        self.app = WINDOW(master = master, _width = Trump.card_width * 7, _height = Trump.card_height * 2 + 100)
        self.app.master.title("Blackjack")
        self.app.option_add("*font", ["MS ゴシック", 20])
        # トランプの作成，使用しないカードの破棄 & シャッフル
        self.trump = Trump.TRUMP()
        for i in range (len(Trump.NUMBER_LIST) * (len(Trump.SYMBOL_LIST) - 1)):
            self.trump.drow()
        self.trump.del_trush_list()
        self.trump.Shuffle()
        # プレイヤーの設定
        self.player1 = PLAYER(0, "相手")
        self.player2 = PLAYER(1, "自分")
        # ラベルの設置
        self.player1.info.place(x = 0, y = Trump.card_height * 2, width = Trump.card_width * 7 / 2, height = 50)
        self.player2.info.place(x = 0, y = Trump.card_height * 2 + 50, width = Trump.card_width * 7 / 2, height = 50)
        # ボタンの作成
        #drow_button = tk.Button(text = "drow", command = lambda:self.game_player_turn(self.player2))
        #drow_button.place(x = Trump.card_width * 7 / 2, y = Trump.card_height * 2, width = Trump.card_width * 7 / 2, height = 100)
        self.game()

    def game(self):
        self.game_player_turn(self.player1)
        self.game_player_turn(self.player2)
        
        while (self.trump.can_drow()):
            self.game_player_turn(self.player1)
            sleep(0.5)
            self.game_player_turn(self.player2)
            sleep(0.5)

    def game_player_turn(self, player):
        player.drow(self.trump)
        player.info["text"] = player.name + "の合計：" + str(player.sum_card_number())
        player.drow_list[-1].display_surface_image(Trump.card_width * (len(player.drow_list) - 1), Trump.card_height * player.id, self.app.canvas)