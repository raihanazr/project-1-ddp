import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Invalid", "Harap masukkan tugas terlebih dahulu.")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Pilih Tugas", "Harap pilih tugas yang ingin dihapus.")

def complete_task():
    selected_task = listbox.curselection()
    if selected_task:
        task = listbox.get(selected_task)
        completed_listbox.insert(tk.END, task)
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Pilih Tugas", "Harap pilih tugas yang ingin dicentang sebagai selesai.")

# Membuat jendela utama
root = tk.Tk()
root.title("To-Do List App")

# Widget dan layout
entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Tambah Tugas", command=add_task)
remove_button = tk.Button(root, text="Hapus Tugas", command=remove_task)
complete_button = tk.Button(root, text="Tugas Selesai", command=complete_task)

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
completed_listbox = tk.Listbox(root, selectmode=tk.SINGLE)

# Menempatkan widget dalam grid
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
add_button.grid(row=1, column=0, pady=5)
remove_button.grid(row=1, column=1, pady=5)
complete_button.grid(row=1, column=2, pady=5)
listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
completed_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Menjalankan aplikasi
root.mainloop()