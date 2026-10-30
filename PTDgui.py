import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def devgui():
    conn = sqlite3.connect("priditor.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)
 
    conn.commit()

    def Show_data():
        for item in tree.get_children():
            tree.delete(item)
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)

    def add_data():
        name = entry_name.get()
        age = entry_age.get()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",(name, age))
        conn.commit()
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        Show_data()

    def delete_data():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("warning","please select the info that you wanna delete")
            return
        if selected:
            lop = messagebox.askyesno("Warning","Do you wanna delete data ?")
            if lop == True:
                item = tree.item(selected)
                value = item["values"]
                user_id = value[0]
                cursor.execute(
                    "DELETE FROM users WHERE id = ?",(user_id,)
                )
                conn.commit()
                Show_data()
            else:
                return
            
    root = tk.Tk()
    root.title("Priditor Data Management(PDM)")
    root.geometry("540x390")

    frame_input = tk.Frame(root)

    frame_input.pack(
        pady=20
    )

    label_name = tk.Label(
        
        frame_input,
        text="username :"
    )
    label_name.grid(
        row=0,
        column=0,
        padx=5,
        pady=5
    )

    entry_name = tk.Entry(
        frame_input,
        width=30
    )
    entry_name.grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )

    label_age = tk.Label(
        frame_input,
        text="password :"
    )
    label_age.grid(
        row=1,
        column=0,
        padx=5,
        pady=5
    )

    entry_age = tk.Entry(
        frame_input,
        width=30
    )
    entry_age.grid(
        row=1,
        column=1,
        padx=5,
        pady=5
    )

    frame_button = tk.Frame(root)
    # สร้าง Frame สำหรับเก็บปุ่ม
    frame_button.pack(
        pady=5
    )

    button_add = tk.Button(
        frame_button,
        text="add info",
        width=15,
        command=add_data
    )
    button_add.grid(
        row=0,
        column=0,
        padx=5
    )

    button_delete = tk.Button(
        frame_button,
        text="delete info",
        width=15,
        command=delete_data
    )
    button_delete.grid(
        row=0,
        column=1,
        padx=5
    )


    # ส่วนตารางแสดงข้อมูล
    tree = ttk.Treeview(
        root,
        columns=("ID", "username", "password"),
        show="headings"
    )
    tree.pack(
        fill=tk.BOTH,
        expand=True,
        pady=20
    )
    tree.heading(
        "ID",
        text="ID"
    )
    tree.heading(
        "username",
        text="username"
    )
    tree.heading(
        "password",
        text="password"
    )
    tree.column(
        "ID",
        width=150,
        anchor=tk.CENTER
    )
    tree.column(
        "username",
        width=180,
        anchor=tk.CENTER
    )
    tree.column(
        "password",
        width=150,
        anchor=tk.CENTER
    )


    Show_data()  
    root.mainloop()