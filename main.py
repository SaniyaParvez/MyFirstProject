import tkinter as tk
from tkinter import messagebox

# Function to update expression in the text entry
def press(key):
    entry.insert(tk.END, key)

# Function to evaluate the final expression
def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid Expression")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to handle backspace
def backspace():
    entry.delete(len(entry.get()) - 1)

# Create main window
root = tk.Tk()
root.title("🧮 Python Calculator")
root.geometry("320x420")
root.resizable(False, False)
root.configure(bg="#222")

# Entry field
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right", bg="#eee")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('C', 5, 2), ('=', 5, 3)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, bg="#28a745", fg="white",
                        font=("Arial", 16, "bold"), command=evaluate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, bg="#dc3545", fg="white",
                        font=("Arial", 16, "bold"), command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, bg="#444", fg="white",
                        font=("Arial", 16, "bold"), command=lambda key=text: press(key))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Bind keyboard keys
root.bind('<Return>', lambda event: evaluate())
root.bind('<BackSpace>', lambda event: backspace())

# Run the main loop
root.mainloop()
