# Pythonによるカードゲーム実装

トランプカードのイラスト：https://www.irasutoya.com/2017/05/card.html

## スタートメニュー
この画面で，遊ぶゲームを選択する

![image](https://user-images.githubusercontent.com/78514639/158544412-c2db8779-61a9-4f59-bf77-158d34b92ffd.png)

## BlackJackの遊び方
ブラックジャック（英語: Blackjack）は、トランプを使用するゲームの一種。
カジノで行われるカードゲームではポーカーやバカラと並ぶ人気ゲームである。
カードの合計点数が21点を超えないように、プレイヤーがディーラーより高い点数を得ることを目指す。
(wikipedia参照)

- スタート画面

相手が引いたカードは上段，自分が引いたカードは下段に表示される．相手が1枚目に引いたカードは確認できない．
自分の引いたカードの合計数を見て，カードを引く(draw) か 引かないか(don't draw) を選択する．

![image](https://user-images.githubusercontent.com/78514639/158545086-66eaffbc-6cb1-47dd-a7e8-ce07ee91f340.png)

- 途中画面

21を超えないようにカードを引いていく．

![image](https://user-images.githubusercontent.com/78514639/158545869-f68bdedf-3e86-4423-9b10-17c0de7d9e40.png)

- リザルト画面

don't drawボタンを押すと，リザルト画面に飛ぶ．引いたカードの合計値が21に近い方が勝者となる．ただし，21を超えた場合は強制的に負けになる．

![image](https://user-images.githubusercontent.com/78514639/158546230-512cdd7f-f203-439a-a2e4-4158a796751f.png)