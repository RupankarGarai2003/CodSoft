from tkinter import *

def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get().strip()

    if new_task:  # Make sure the new task is not empty
        listbox.insert(0, new_task)  # Insert at the beginning

        with open('tasks.txt', 'r+') as tasks_list_file:
            lines = tasks_list_file.readlines()
            tasks_list_file.seek(0)
            tasks_list_file.truncate()
            
            tasks_list_file.write(f'{new_task}\n')  # Add the new task at the beginning
            tasks_list_file.writelines(lines)
        
        entry.delete(0, END)  # Clear the entry field after adding a task

def delete_item(listbox: Listbox):
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        deleted_task = listbox.get(index)

        listbox.delete(index)

        with open('tasks.txt', 'r+') as tasks_list_file:
            lines = tasks_list_file.readlines()
            tasks_list_file.seek(0)
            tasks_list_file.truncate()

            for line in lines:
                if line.strip() != deleted_task:
                    tasks_list_file.write(line)

root = Tk()
root.title('Rupankar Garai To-Do-List')
root.geometry('400x500')
root.resizable(0, 0)
root.config(bg="blue")

# Centering the window on the screen
root.update_idletasks()
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f"+{position_right}+{position_down}")

Label(root, text='Rupankar Garai To-Do-List', bg='PaleVioletRed', font=("Comic Sans MS", 15), wraplength=300).place(relx=0.5, y=0, anchor="n")

tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=14, width=30)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(relx=1, y=50, height=262, anchor="ne")
tasks.config(yscrollcommand=scroller.set)
tasks.place(x=35, y=50)

with open('tasks.txt', 'a+') as tasks_list:
    tasks_list.seek(0)
    for task in tasks_list:
        tasks.insert(END, task.strip())

new_item_entry = Entry(root, width=44)
new_item_entry.place(x=35, y=330)

add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),
                 command=lambda: add_item(new_item_entry, tasks))
add_btn.place(x=45, y=360)

delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12),
                 command=lambda: delete_item(tasks))
delete_btn.place(x=150, y=360)

root.mainloop()
