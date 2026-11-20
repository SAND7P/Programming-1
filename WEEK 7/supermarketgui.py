import tkinter as tk
window = tk.Tk()
window.title("Supermarket GUI")
window.geometry("500x500")

tk.Label(window, text="Item Name").pack()
item_name=tk.Entry(window)
item_name.pack()

tk.Label(window, text="Price").pack()
item_price=tk.Entry(window)
item_price.pack()

items_pr={}
def add():
   name=item_name.get()
   price=item_price.get()
   items_pr[name]=price
   result.config(text="Items added successfully")
def calculate_total():
   total=0
   for i in items_pr.values():
      total=total+ int(i)
      result.config(text="Total= "+ str(total))

def display_items():
   cont_text="  "
   for i,j in items_pr.items():
      cont_text+=i+" "+str(j)+"\n"
   result.config(text=cont_text)
tk.Button(window, text="Add", command=add).pack()
tk.Button(window, text="Calculate", command=calculate_total).pack()
tk.Button(window, text="Display", command=display_items).pack()
result=tk.Label(window, text="Output Display")
result.pack()



window.mainloop()

