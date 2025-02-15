import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_digits = digits_var.get()
    include_specials = specials_var.get()
    
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_specials:
        characters += string.punctuation
    
    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")

digits_var = tk.BooleanVar()
specials_var = tk.BooleanVar()

digits_check = tk.Checkbutton(frame, text="Include Numbers", variable=digits_var)
digits_check.grid(row=1, column=0, columnspan=2)

specials_check = tk.Checkbutton(frame, text="Include Special Characters", variable=specials_var)
specials_check.grid(row=2, column=0, columnspan=2)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

password_entry = tk.Entry(root, width=30, font=("Arial", 14))
password_entry.pack(pady=10)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=5)

root.mainloop()
