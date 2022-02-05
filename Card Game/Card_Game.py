import Blackjack
import tkinter as tk

def main():
    win = tk.Tk()
    blackjack = Blackjack.BLACKJACK(master = win)
    # ゲームスタート
    blackjack.game()
    print("Game finish")
    blackjack.result()
    
    blackjack.app.mainloop()


if __name__ == "__main__":
    main()