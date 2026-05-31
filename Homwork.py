import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        if principal < 0 or rate < 0 or time < 0:
            messagebox.showerror("Invalid Input", "Values must be non-negative.")
            return

        interest = (principal * rate * time) / 100
        total_amount = principal + interest

        label_result.config(
            text=f"Interest: {interest:.2f}\nTotal Amount: {total_amount:.2f}"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Principal Amount:", font=("Arial", 12)).pack(pady=5)
entry_principal = tk.Entry(root, font=("Arial", 12))
entry_principal.pack()

tk.Label(root, text="Rate of Interest (%):", font=("Arial", 12)).pack(pady=5)
entry_rate = tk.Entry(root, font=("Arial", 12))
entry_rate.pack()

tk.Label(root, text="Time Period (years):", font=("Arial", 12)).pack(pady=5)
entry_time = tk.Entry(root, font=("Arial", 12))
entry_time.pack()

tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate_interest).pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack(pady=5)

root.mainloop()
