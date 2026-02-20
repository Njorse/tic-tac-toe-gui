import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")

label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 20))
label.pack(pady=20)

root.mainloop()