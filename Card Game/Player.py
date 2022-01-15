class PLAYER():
    # コンストラクタ
    def __init__(self):
        self.drow_card = []

    # ドロー
    def drow(self, trump):
        self.drow_card.append(trump.drow())

    # 与えられたCardクラス配列の合計値計算
    def sum_card_number(self):
        sum = 0
        for i in range(len(self.drow_card)):
            sum = sum + self.drow_card[i].number_list.number
        return sum