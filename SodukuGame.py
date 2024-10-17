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

def single_digit_number(char):
    return char.isdigit() and len(char) == 1 or char == ""

def create_entrybox():
    for i in range(9):
        for j in range(9):
            single_digit = game.register(single_digit_number)
            entry = Entry(game, width=2, font=('Arial', 24), justify='center', validate='key', validatecommand=(single_digit, '%P'))
            entry.place(x=i * (win_width / 9) + 10, y=j * (win_height / 9) + 10)
            cells.append(entry)

draw_grid(canvas, win_width, win_height)
create_entrybox()

canvas.pack()
game.mainloop()
