import tkinter as tk
import calendar

okno = tk.Tk()
okno.title("Kalendář")

text = calendar.month(2026, 7)

label = tk.Label(okno, text=text, font=("Courier New", 12), justify="left")
label.pack(padx=10, pady=10)

okno.mainloop()
