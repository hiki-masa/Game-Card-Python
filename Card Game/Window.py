import tkinter as tk

DisplayWidth  = 500
DisplayHeight = 500

class WINDOW(tk.Frame):
    # コンストラクタ
    def __init__(self, master):
        super().__init__(master)
        # ウィンドウサイズを固定
        master.resizable(width = False, height = False)
        # ウィンドウの設定
        master.minsize(DisplayWidth, DisplayHeight)
        master.title("Window")
        # キャンバスの設定
        self.canvas = tk.Canvas(master, width = DisplayWidth, height = DisplayHeight, bg = "green")
        self.canvas.pack()

    # キャンバスIDの取得
    def get_canvas(self):
        return self.canvas