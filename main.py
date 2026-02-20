import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("320x450")
root.config(bg="#1e1e1e")

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

def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for button in row:
            button.config(text="", fg="white")

def button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        buttons[row][col].config(fg="#00ffcc" if current_player == "X" else "#ff4d4d")

        if check_winner():
            messagebox.showinfo("Ganador", f"El jugador {current_player} ganó!")
            reset_game()
            return

        current_player = "O" if current_player == "X" else "X"

title = tk.Label(root, text="TIC TAC TOE",
                 font=("Arial", 24, "bold"),
                 bg="#1e1e1e",
                 fg="white")
title.pack(pady=20)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

for row in range(3):
    row_buttons = []
    for col in range(3):
        btn = tk.Button(frame,
                        text="",
                        width=6,
                        height=3,
                        font=("Arial", 20, "bold"),
                        bg="#2d2d2d",
                        fg="white",
                        activebackground="#3e3e3e",
                        command=lambda r=row, c=col: button_click(r, c))
        btn.grid(row=row, column=col, padx=5, pady=5)
        row_buttons.append(btn)
    buttons.append(row_buttons)

reset_button = tk.Button(root,
                         text="Reiniciar Juego",
                         font=("Arial", 14, "bold"),
                         bg="#444",
                         fg="white",
                         command=reset_game)

reset_button.pack(pady=20)

root.mainloop()