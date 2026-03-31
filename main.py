import tkinter as tk

window = tk.Tk()
window.title("Мой ToDo-лист")

# Добавим переменную для темы
dark_mode = False

entry = tk.Entry(window, width=40)
entry.pack(pady=10)


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])


def complete_task():
    selected = listbox.curselection()
    for index in selected:
        task_text = listbox.get(index)
        # Если ещё не отмечено как выполнено
        if not task_text.startswith("✔ "):
            listbox.delete(index)
            listbox.insert(index, f"✔ {task_text}")
            listbox.itemconfig(index, fg="gray")


def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        window.config(bg="#2e2e2e")
        listbox.config(bg="#3c3c3c", fg="white")
        entry.config(bg="#3c3c3c", fg="white")
    else:
        window.config(bg="white")
        listbox.config(bg="white", fg="black")
        entry.config(bg="white", fg="black")

# Кнопка переключения темы
btn_theme = tk.Button(window, text="Сменить тему", width=15, command=toggle_theme)
btn_theme.pack(pady=5)

btn_complete = tk.Button(window, text="Выполнено", width=15, bg="#b4f2a1", command=complete_task)
btn_complete.pack(pady=5)

delete_btn = tk.Button(window, text="Удалить задачу", command=delete_task)
delete_btn.pack()

btn = tk.Button(window, text="Добавить задачу", command=add_task)
btn.pack()

listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

window.mainloop()
