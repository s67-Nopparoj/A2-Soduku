from tkinter import *

game = Tk()
game.title("Sudoku Game")
game.geometry("600x800")

win_width = 600
win_height = 600
cells = []

canvas = Canvas(game, width=win_width, height=win_height)

def draw_grid(canvas, win_width, win_height):
    for i in range(4):
        canvas.create_line(i * (win_width / 3), 0, i * (win_width / 3), win_height, fill="black", width=5)
        canvas.create_line(0, i * (win_height / 3), win_width, i * (win_height / 3), fill="black", width=5)

    for i in range(9):
        canvas.create_rectangle(i * (win_width / 9), 0, i * (win_width / 9), win_height, fill="black", width=1)
        canvas.create_rectangle(0, i * (win_height / 9), win_width, i * (win_height / 9), fill="black", width=1)

draw_grid(canvas, win_width, win_height)

canvas.pack()
game.mainloop()