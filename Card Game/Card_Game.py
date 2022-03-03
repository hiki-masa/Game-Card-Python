import Blackjack
import tkinter as tk

def main():
    win = tk.Tk()
    while(True):
        blackjack = Blackjack.BLACKJACK(master = win)
        # ゲームスタート
        blackjack.game()
        blackjack.result()
        del blackjack
    
    #blackjack.app.mainloop()


if __name__ == "__main__":
    main()