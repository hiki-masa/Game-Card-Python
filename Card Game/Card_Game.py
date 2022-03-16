import Blackjack
import Window
import tkinter as tk

def main():
    win = tk.Tk()

    app = Window.WINDOW(win, 500, 500)
    label1 = tk.Label(text = "Card Game", font = ('メイリオ', 20), bg = 'green').pack(anchor = tk.N)
    label2 = tk.Label(text = "", font = ('メイリオ', 20), bg = 'green').pack(anchor = tk.N)
    tk.Button(text = "Blackjack", command = lambda:Blackjack.BLACKJACK(master = win), font = ('Century', 16)).pack(anchor = tk.N)
    tk.Button(text = "???", font = ('Century', 16), state = "disable").pack(anchor = tk.N)

    #while(True):
    #    blackjack = Blackjack.BLACKJACK(master = win)
    #    # ゲームスタート
    #    blackjack.game()
    #    blackjack.result()
    #    del blackjack
    
    app.mainloop()


if __name__ == "__main__":
    main()