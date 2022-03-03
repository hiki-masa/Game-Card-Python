import tkinter as tk
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
        self.button_bool_var = tk.BooleanVar(False)

    # Game all-over
    def game(self):
        # player1
        self.game_player_turn(self.player1)
        self.player1.draw_list[-1].display_back_image(0, 0, self.app.canvas)
        # player2
        self.game_player_turn(self.player2)
        # 2枚目以降
        while (self.player1.judg_draw or self.player2.judg_draw):
            # player1
            if self.player1.judg_draw_card(self.trump):
                self.game_player_turn(self.player1)
            # player2
            if self.player2.judg_draw:
                self.draw_button.wait_variable(self.button_bool_var)

    # Game processing in one-turn 
    def game_player_turn(self, player):
        player.draw(self.trump)
        if id(player) == id(self.player2):
            player.info["text"] = f"{player.name}の合計：{player.sum_card_number()}"
        player.draw_list[-1].display_surface_image(Trump.CARD.width * (len(player.draw_list) - 1), Trump.CARD.height * player.id, self.app.canvas)
        self.button_bool_var.set(not self.button_bool_var.get())

    # リザルト画面の表示
    def result(self):
        # 不要なボタンの削除
        self.draw_button.destroy()
        self.not_draw_button.destroy()
        # ボタンの作成
        push_flag = tk.BooleanVar(False)
        next_game_button = tk.Button(text = "Next Game", command = lambda:update_BooleanVar(push_flag))
        next_game_button.place(x = Trump.CARD.width * 7 / 2, y = Trump.CARD.height * 2, width = Trump.CARD.width * 7 / 4, height = 100)
        exit_game_button = tk.Button(text = "Exit", state = "disable")
        exit_game_button.place(x = Trump.CARD.width * 7 * 3 / 4, y = Trump.CARD.height * 2, width = Trump.CARD.width * 7 / 4, height = 100)
        # 勝敗の判定
        result = tk.StringVar()
        result_label = tk.Label(textvariable = result, font = ('ゴシック', 40), bg = 'green')
        result_label.pack(expand = True)
        if self.player1.sum_card_number() <= BLACKJACK.upper_limit and self.player2.sum_card_number() <= BLACKJACK.upper_limit:
            if self.player1.sum_card_number() == self.player2.sum_card_number():
                result.set("DRAW")
            elif self.player1.sum_card_number() > self.player2.sum_card_number():
                result.set(self.player1.name + " WIN")
            else:
                result.set(self.player2.name + " WIN")
        elif self.player1.sum_card_number() > BLACKJACK.upper_limit and self.player2.sum_card_number() > BLACKJACK.upper_limit:
            result.set("DRAW")
        elif self.player1.sum_card_number() > BLACKJACK.upper_limit:
            result.set(self.player2.name + " WIN")
        elif self.player2.sum_card_number() > BLACKJACK.upper_limit:
            result.set(self.player1.name + " WIN")
        # Player1 の結果の表示
        self.player1.info["text"] = f"{self.player1.name}の合計：{self.player1.sum_card_number()}"
        self.player1.draw_list[0].display_surface_image(0, 0, self.app.canvas)
        
        # ボタンが押されるまで処理の停止
        next_game_button.wait_variable(push_flag)
        result_label.destroy()
        next_game_button.destroy()
        exit_game_button.destroy()

# tk.BooleanVar の更新
def update_BooleanVar(_boolean):
    if type(_boolean) == tk.BooleanVar:
        _boolean.set(not _boolean.get())
    else:
        exit()