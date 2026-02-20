import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")

current_player = "X"
buttons = []

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Ganador", f"El jugador {current_player} ganó!")
            root.quit()
        current_player = "O" if current_player == "X" else "X"

frame = tk.Frame(root)
frame.pack()

for row in range(3):
    row_buttons = []
    for col in range(3):
        btn = tk.Button(frame, text="", width=8, height=4,
                        command=lambda r=row, c=col: button_click(r, c))
        btn.grid(row=row, column=col)
        row_buttons.append(btn)
    buttons.append(row_buttons)

root.mainloop()