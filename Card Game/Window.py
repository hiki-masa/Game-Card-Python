import tkinter as tk

class WINDOW(tk.Frame):
    # コンストラクタ
    def __init__(self, master, _width, _height):
        super().__init__(master)
        # ウィンドウサイズを固定
        master.resizable(width = False, height = False)
        # ウィンドウの設定
        master.minsize(_width, _height)
        master.title("Window")
        # キャンバスの設定
        self.canvas = tk.Canvas(master, width = _width, height = _height, bg = "green", bd = -2)
        self.canvas.place(x = 0, y = 0)