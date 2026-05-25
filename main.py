import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="habit_tracker"
)

cursor = db.cursor()

# ---------------- Functions ---------------- #

def load_habits():
    text_box.delete("1.0", tk.END)

    cursor.execute("SELECT * FROM habits")
    data = cursor.fetchall()

    if not data:
        text_box.insert(tk.END, "No habits found.\n")
        return

    for habit in data:
        status = "Done" if habit[2] == 1 else "Not Done"
        text_box.insert(
            tk.END,
            f"ID: {habit[0]} | {habit[1]} | {status} | Streak: {habit[3]}\n"
        )


def add_habit():
    name = entry_name.get()

    if name == "":
        messagebox.showwarning("Warning", "Enter a habit name")
        return

    query = "INSERT INTO habits (name,status,streak) VALUES (%s,%s,%s)"
    cursor.execute(query, (name, 0, 0))
    db.commit()

    entry_name.delete(0, tk.END)
    load_habits()


def delete_habit():
    hid = entry_id.get()

    if hid == "":
        messagebox.showwarning("Warning", "Enter habit ID")
        return

    cursor.execute("DELETE FROM habits WHERE id=%s", (hid,))
    db.commit()

    entry_id.delete(0, tk.END)
    load_habits()


def mark_done():
    hid = entry_id.get()

    if hid == "":
        messagebox.showwarning("Warning", "Enter habit ID")
        return

    cursor.execute("SELECT streak FROM habits WHERE id=%s", (hid,))
    result = cursor.fetchone()

    if result:
        streak = result[0] + 1

        cursor.execute(
            "UPDATE habits SET status=1, streak=%s WHERE id=%s",
            (streak, hid)
        )
        db.commit()

    entry_id.delete(0, tk.END)
    load_habits()


def reset_day():
    cursor.execute("UPDATE habits SET status=0,streak=0")
    db.commit()
    load_habits()


# ---------------- GUI ---------------- #

window = tk.Tk()
window.title("Habit Tracker")
window.geometry("700x500")

title = tk.Label(window, text="Habit Tracker System", font=("Arial", 18, "bold"))
title.pack(pady=10)

frame = tk.Frame(window)
frame.pack(pady=10)

entry_name = tk.Entry(frame, width=25)
entry_name.grid(row=0, column=0, padx=5)

btn_add = tk.Button(frame, text="Add Habit", command=add_habit)
btn_add.grid(row=0, column=1, padx=5)

entry_id = tk.Entry(frame, width=10)
entry_id.grid(row=0, column=2, padx=5)

btn_delete = tk.Button(frame, text="Delete Habit", command=delete_habit)
btn_delete.grid(row=0, column=3, padx=5)

btn_done = tk.Button(frame, text="Mark Done", command=mark_done)
btn_done.grid(row=0, column=4, padx=5)

btn_reset = tk.Button(frame, text="Reset Day", command=reset_day)
btn_reset.grid(row=0, column=5, padx=5)

# Text box instead of Treeview
text_box = tk.Text(window, width=80, height=20)
text_box.pack(pady=20)

load_habits()

window.mainloop()
