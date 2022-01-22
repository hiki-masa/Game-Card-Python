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
        self.trump.del_drow_list()
        self.trump.Shuffle()
        # プレイヤーの設定
        self.player1 = PLAYER(0, "相手")
        self.player2 = PLAYER(1, "自分")
        # ラベルの設置
        self.player1.info.place(x = 0, y = Trump.card_height * 2, width = Trump.card_width * 7 / 2, height = 50)
        self.player2.info.place(x = 0, y = Trump.card_height * 2 + 50, width = Trump.card_width * 7 / 2, height = 50)
        # ボタンの作成
        self.drow_button = tk.Button(text = "drow", command = lambda:self.game_player_turn(self.player2))
        self.button_bool_var = tk.BooleanVar(value = False) # False : player1-turn, True : player2-turn
        self.drow_button.place(x = Trump.card_width * 7 / 2, y = Trump.card_height * 2, width = Trump.card_width * 7 / 4, height = 100)
        self.not_drow_button = tk.Button(text = "don't drow")
        self.not_drow_button.place(x = Trump.card_width * 7 * 3 / 4, y = Trump.card_height * 2, width = Trump.card_width * 7 / 4, height = 100)
        # ゲームスタート
        self.game()

    def game(self):
        self.game_player_turn(self.player1)
        self.game_player_turn(self.player2)
        while (self.trump.can_drow()):
            self.game_player_turn(self.player1)
            self.drow_button.wait_variable(self.button_bool_var)

    def game_player_turn(self, player):
        player.drow(self.trump)
        player.info["text"] = player.name + "の合計：" + str(player.sum_card_number())
        player.drow_list[-1].display_surface_image(Trump.card_width * (len(player.drow_list) - 1), Trump.card_height * player.id, self.app.canvas)
        self.update_variable()

    def update_variable(self):
        # player-turn 交換による変数の更新
        if self.button_bool_var.get() == False:
            self.button_bool_var.set(True)
            self.drow_button["state"] = tk.NORMAL
        else:
            self.button_bool_var.set(False)
            self.drow_button["state"] = tk.DISABLED