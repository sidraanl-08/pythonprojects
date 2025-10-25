import tkinter as tk
from tkinter import messagebox
import random

# --- Game logic ---
target = random.randint(1, 100)

def check_guess():
    guess = guess_entry.get()
    if not guess.isdigit():
        messagebox.showwarning("Invalid input", "Please enter a number!")
        return

    guess = int(guess)
    if guess == target:
        messagebox.showinfo("Success!", f"You guessed it! The number was {target}")
    elif guess < target:
        result_label.config(text="Your number is too small. Try bigger!")
    else:
        result_label.config(text="Your number is too big. Try smaller!")

def restart_game():
    global target
    target = random.randint(1, 100)
    result_label.config(text="")
    guess_entry.delete(0, tk.END)

# --- GUI ---
root = tk.Tk()
root.title("Guess The Number")
root.geometry("400x250")

tk.Label(root, text="Guess a number between 1 and 100").pack(pady=10)

guess_entry = tk.Entry(root)
guess_entry.pack(pady=5)

check_btn = tk.Button(root, text="Check", command=check_guess)
check_btn.pack(pady=5)   # <-- fixed here

restart_btn = tk.Button(root, text="Restart", command=restart_game)
restart_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
