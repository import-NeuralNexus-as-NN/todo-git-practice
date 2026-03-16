import tkinter as tk

window = tk.Tk()
window.title("Мой ToDo-лист")

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


btn_complete = tk.Button(window, text="Выполнено", width=15, bg="#b4f2a1", command=complete_task)
btn_complete.pack(pady=5)

delete_btn = tk.Button(window, text="Удалить задачу", command=delete_task)
delete_btn.pack()

btn = tk.Button(window, text="Добавить задачу", command=add_task)
btn.pack()

listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

window.mainloop()
