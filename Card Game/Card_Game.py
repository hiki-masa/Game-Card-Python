import Trump
import Window
import tkinter as tk
from time import sleep

def main():
    WindowWidth  = 500
    WindowHeight = 500
    win = tk.Tk()
    app = Window.WINDOW(master = win, _width = WindowWidth, _height = WindowHeight)
    trump = Trump.TRUMP()

    for i in range (len(trump.card_list)):
        drow_card = trump.drow()
        drow_card.display_surface_image(0, 0, app.canvas)
        drow_card.display_back_image(135, 0, app.canvas)
        sleep(0.1)
    
    app.mainloop()


if __name__ == "__main__":
    main()