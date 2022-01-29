import tkinter as tk
from time import sleep
from Window import WINDOW
import Trump
from Player import COMPUTER, HUMAN

class BLACKJACK():
    upper_limit = 21
    # コンストラクタ
    def __init__(self, master):
        # ウィンドウの設定
        self.app = WINDOW(master = master, _width = Trump.CARD.width * 7, _height = Trump.CARD.height * 2 + 100)
        self.app.master.title("Blackjack")
        self.app.option_add("*font", ["MS ゴシック", 20])
        # トランプの作成，使用しないカードの破棄 & シャッフル
        self.trump = Trump.TRUMP()
        for i in range (len(Trump.NUMBER_LIST) * (len(Trump.SYMBOL_LIST) - 1)):
            self.trump.draw()
        self.trump.del_draw_list()
        self.trump.Shuffle()
        # プレイヤーの設定
        self.player1 = COMPUTER("相手")
        self.player2 = HUMAN("自分")
        # ラベルの設置
        self.player1.info.place(x = 0, y = Trump.CARD.height * 2, width = Trump.CARD.width * 7 / 2, height = 50)
        self.player2.info.place(x = 0, y = Trump.CARD.height * 2 + 50, width = Trump.CARD.width * 7 / 2, height = 50)
        # ボタンの作成
        self.draw_button = tk.Button(text = "draw", command = lambda:self.game_player_turn(self.player2))
        self.draw_button.place(x = Trump.CARD.width * 7 / 2, y = Trump.CARD.height * 2, width = Trump.CARD.width * 7 / 4, height = 100)
        self.not_draw_button = tk.Button(text = "don't draw", command = lambda:self.player2.update_judg_draw_card(self.button_bool_var))
        self.not_draw_button.place(x = Trump.CARD.width * 7 * 3 / 4, y = Trump.CARD.height * 2, width = Trump.CARD.width * 7 / 4, height = 100)
        self.button_bool_var = tk.BooleanVar(value = False)
        # ゲームスタート
        self.game()
        print("Game finish")
        self.result()

    def game(self):
        self.game_player_turn(self.player1)
        self.game_player_turn(self.player2)
        while (self.player1.judg_draw or self.player2.judg_draw):
            # player1
            if self.player1.judg_draw_card():
                self.game_player_turn(self.player1)
            # player2
            if self.player2.judg_draw:
                self.draw_button.wait_variable(self.button_bool_var)

    def game_player_turn(self, player):
        player.draw(self.trump)
        player.info["text"] = player.name + "の合計：" + str(player.sum_card_number())
        player.draw_list[-1].display_surface_image(Trump.CARD.width * (len(player.draw_list) - 1), Trump.CARD.height * player.id, self.app.canvas)
        self.button_bool_var.set(not self.button_bool_var.get())

    def result(self):
        #self.player1.info.destroy()
        #self.player2.info.destroy()
        self.draw_button.destroy()
        self.not_draw_button.destroy()
        if self.player1.sum_card_number() < BLACKJACK.upper_limit and self.player2.sum_card_number() < BLACKJACK.upper_limit:
            if self.player1.sum_card_number() == self.player2.sum_card_number():
                print("DRAW")
            elif self.player1.sum_card_number() > self.player2.sum_card_number():
                print(self.player1.name + " WIN")
            else:
                print(self.player2.name + "WIN")
        elif self.player1.sum_card_number() > BLACKJACK.upper_limit and self.player2.sum_card_number() > BLACKJACK.upper_limit:
            print("DRAW")
        elif self.player1.sum_card_number() > BLACKJACK.upper_limit:
            print(self.player2.name + "WIN")
        elif self.player2.sum_card_number() > BLACKJACK.upper_limit:
            print(self.player1.name + "WIN")
            