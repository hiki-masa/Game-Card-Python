import Trump
import Window
import tkinter as tk
from time import sleep

def main():
    win = tk.Tk()
    app = Window.WINDOW(master = win)
    a = Trump.TRUMP()

    for i in range (len(a.card_list)):
        drow_card = a.drow()
        drow_card.display_surface_image(0, 0, app.get_canvas())
        drow_card.display_back_image(135, 0, app.get_canvas())
        sleep(0.1)
    
    app.mainloop()


if __name__ == "__main__":
    main()