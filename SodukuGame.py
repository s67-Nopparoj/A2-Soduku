from tkinter import *
import random

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
            
def check_number(cells, row, col, num):
    for i in range(9):
        if cells[row * 9 + i].get() == str(num):
            return False
    
    for i in range(9):
        if cells[i * 9 + col].get() == str(num):
            return False
    
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if cells[(start_row + i) * 9 + (start_col + j)].get() == str(num):
                return False
            
    return True

def fill_random_number(num_cells):
    count = 0
    while count < num_cells:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if cells[row * 9 + col].get() == "":
            num = random.randint(1, 9)
            if check_number(cells, row, col, num):
                cells[row * 9 + col].insert(0, str(num))
                cells[row * 9 + col].config(state='disabled')
                count += 1

def check_solution():
    for row in range(9):
        for col in range(9):
            num = cells[row * 9 + col].get()
            if num == "":
                return False
            if not check_number(cells, row, col, int(num)):
                return False
    return True

solution = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]

def show_solution():
    for row in range(9):
        for col in range(9):
            if cells[row * 9 + col].get() == "":
                cells[row * 9 + col].insert(0, str(solution[row][col]))
                cells[row * 9 + col].config(state='disabled')
                
def reset_game():
    for cell in cells:
        cell.config(state='normal')
        cell.delete(0, 'end')
    fill_random_number(50)

check_button = Button(game, text="Check Solution", command=lambda: print("Correct!" if check_solution() else "Incorrect!"))
check_button.pack(side='bottom', pady=10)

show_solution_button = Button(game, text="Show Solution", command=show_solution)
show_solution_button.pack(side='bottom', pady=10)

reset_button = Button(game, text="Reset", command=reset_game)
reset_button.pack(side='bottom', pady=10)

draw_grid(canvas, win_width, win_height)
create_entrybox()
fill_random_number(50)

canvas.pack()
game.mainloop()
