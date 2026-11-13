import tkinter as tk

root = tk.Tk()
root.title("Клікер")

data = {"name": "", "score": 0, "active": False}

label = tk.Label(root, text="Введіть ім'я та натисніть Enter", font=("Arial", 20))
label.pack(pady=15)

entry = tk.Entry(root, font=("Arial", 20), justify="center")
entry.pack(pady=5)
entry.focus()


def key_press(event):
  if event.keysym == "Return":
    if not data["active"]:
      data["name"] = entry.get()
      data["active"] = True
      data["score"] = 0
      entry.delete(0, tk.END)
      label.config(text=f"{data['name']} | Бали: 0")
    else:
      data["score"] += 1
      label.config(text=f"{data['name']} | Бали: {data['score']}")
  else:
    if data["active"]:
      data["active"] = False
      label.config(text=f"Гравець: {data['name']}\nРахунок: {data['score']}")


root.mainloop()