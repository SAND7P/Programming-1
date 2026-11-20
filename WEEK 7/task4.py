from tkinter import *
window = Tk()
window.title("Simple Calculator")

def calculate():
    total = float(entry1.get()) + float(entry2.get())
    result_label.config(text=f"Total = {total}")
Label(window, text="First Number").pack()
entry1 = Entry(window)
entry1.pack()

Label(window, text="Second Number").pack()
entry2 = Entry(window)
entry2.pack()

Button(window, text="Calculate", command=calculate).pack()

result_label = Label(window, text="Total =")
result_label.pack()

window.mainloop()
