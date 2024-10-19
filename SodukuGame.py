from tkinter import *
import random

game = Tk()
game.title("Sudoku Game")
game.geometry("550x700")

start_frame = Frame(game)
difficulty_frame = Frame(game)
game_frame = Frame(game)

for frame in (start_frame, difficulty_frame, game_frame):
    frame.grid(row=0, column=0, sticky='nsew')

difficulty_level = None
win_width = 550
win_height = 550
cells = []

canvas = Canvas(game_frame, width=win_width, height=win_height)
canvas.grid(row=0, column=0, columnspan=9)

def draw_grid(canvas):
    for i in range(4):
        canvas.create_line(i * (win_width / 3), 0, i * (win_width / 3), win_height, fill="black", width=5)
        canvas.create_line(0, i * (win_height / 3), win_height, i * (win_height / 3), fill="black", width=5)
    
    for i in range(1, 9):
        canvas.create_line(i * (win_width / 9), 0, i * (win_width / 9), win_height, fill="gray", width=1)
        canvas.create_line(0, i * (win_height / 9), win_width, i * (win_height / 9), fill="gray", width=1)

def single_digit_number(char):
    return char.isdigit() and len(char) == 1 or char == ""

def create_entrybox():
    for i in range(9):
        for j in range(9):
            single_digit = game.register(single_digit_number)
            entry = Entry(game_frame, width=2, font=('Arial', 24), justify='center', validate='key', validatecommand=(single_digit, '%P'))
            entry.place(x=i * (win_width / 9) + 10, y=j * (win_height / 9) + 10)
            cells.append(entry)

def check_number(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def random_number(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if check_number(board, row, col, num):
                        board[row][col] = num
                        if random_number(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_finish_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    random_number(board)
    return board

def fill_random_number(num_cells):
    count = 0
    fill_position = set()
    while count < num_cells:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if (row, col) not in fill_position and cells[row * 9 + col].get() == "":
            cells[row * 9 + col].insert(0, str(solution[row][col]))
            cells[row * 9 + col].config(state='disabled')
            fill_position.add((row, col))
            count += 1

def check_solution():
    for row in range(9):
        for col in range(9):
            num = cells[row * 9 + col].get()
            if num == "":
                return False
            if int(num) != solution[row][col]:
                return False
    return True

def update_result():
    if check_solution():
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Incorrect!", fg="red")

def show_solution():
    for row in range(9):
        for col in range(9):
            if cells[row * 9 + col].get() == "":
                cells[row * 9 + col].insert(0, str(solution[row][col]))
                cells[row * 9 + col].config(state='disabled')

def reset_game():
    global solution
    solution = generate_finish_board()
    for cell in cells:
        cell.config(state='normal')
        cell.delete(0, 'end')
    fill_random_number(difficulty_level)
    result_label.config(text="")

def show_frame(frame):
    frame.tkraise()

def select_difficulty(level):
    global difficulty_level
    difficulty_level = level
    reset_game()
    show_frame(game_frame)

button_frame = Frame(game_frame)
button_frame.grid(row=10, column=0, columnspan=9, pady=20)

check_button = Button(button_frame, text="Check Answer", command=update_result, padx=20, pady=10, font=('Arial', 14))
check_button.grid(row=0, column=0, padx=15)

show_solution_button = Button(button_frame, text="Show Answer", command=show_solution, padx=20, pady=10, font=('Arial', 14))
show_solution_button.grid(row=0, column=1, padx=20)

reset_button = Button(button_frame, text="Reset", command=reset_game, padx=20, pady=10, font=('Arial', 14))
reset_button.grid(row=0, column=2, padx=15)

result_label = Label(game_frame, text="", font=('Arial', 16))
result_label.grid(row=11, column=0, columnspan=9, pady=20)

Label(start_frame, text="Sudoku Game !!", font=('Arial', 40)).pack(pady=100)
start_button = Button(start_frame, text="Start Game", font=('Arial', 25), command=lambda: show_frame(difficulty_frame))
start_button.pack(pady=10)

quit_button = Button(start_frame, text="Quit", font=('Arial', 25), command=game.quit)
quit_button.pack(pady=10)

Label(difficulty_frame, text="Select Difficulty", font=('Arial', 40)).pack(pady=100)
Button(difficulty_frame, text="Easy", font=('Arial', 25), command=lambda: select_difficulty(50)).pack(pady=10)
Button(difficulty_frame, text="Medium", font=('Arial', 25), command=lambda: select_difficulty(40)).pack(pady=10)
Button(difficulty_frame, text="Hard", font=('Arial', 25), command=lambda: select_difficulty(30)).pack(pady=10)

show_frame(start_frame)
draw_grid(canvas)
create_entrybox()
game.mainloop()
