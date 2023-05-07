import tkinter as tk
from tkinter import ttk
import csv
import threading
import \
    secrets  # make sure there's a secrets.py file, and within that file, sure theres the following: CSV_FILE_PATH = "path/to/your/csv/file.csv"


# also make sure import secrets is in main.py of this project

class UserData:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserDataCollector:
    def __init__(self):
        self.user_data = []
        self.file_lock = threading.Lock()

    def collect_data(self, name, email):
        user_data = UserData(name, email)
        self.user_data.append(user_data)
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.status_label.config(text="Thank you for submitting your data!", fg="green")

    def save_data(self):
        with open(secrets.CSV_FILE_PATH, mode='w', newline='') as data_file:
            data_writer = csv.writer(data_file)
            data_writer.writerow(['Name', 'Username' 'Email'])
            for data in self.user_data:
                data_writer.writerow([data.name, data.email])
        self.status_label.config(text="Your data has saved successfully!", fg="green")

    def delete_data(self):
        self.user_data = []
        self.status_label.config(text="Your data has been deleted successfully!", fg="green")

    def get_user_data(self):
        return self.user_data

    def privacy_notice(self):
        notice = "To help create a better user experience, Futurecoder securely collects user data, including your name and email address.\n\nBy submitting your data, you are consenting to its collection and storage.\n\nHowever, you may opt-out of data collection at any time by entering 'opt-out' for both name and email."
        self.notice_label.config(text=notice, font=("Segoe UI", 10), fg="#4CAF50", wraplength=350)


if __name__ == '__main__':
    data_collector = UserDataCollector()

    root = tk.Tk()
    root.title("User Data Collector")
    root.geometry("400x350")
    root.configure(bg="#FFFFFF")

    # creating GUI elements
    label_style = ttk.Style()
    label_style.configure('TLabel', background="#FFFFFF", foreground="#000000", font=("Segoe UI Light, 10"))

    entry_style = ttk.Style()
    entry_style.configure('TEntry', background="F2F2F2", foreground="#000000", font=("Segoe UI Light, 10"))

    button_style = ttk.Style()
    button_style.configure('TButton', background="#4CAF50", foreground="#FFFFFF", font=("Segoe UI Light, 10"),
                           padding=8)

    name_label = ttk.Label(root, text="Please enter your Name:")
    name_label.pack(pady=10)
    name_label.place(x=50, y=50)
    name_label.configure(style='TLabel')

    name_entry = ttk.Label(root)
    name_entry.pack(pady=5)
    name_entry.place(x=50, y=80)
    name_entry.configure(style='TEntry')
    data_collector.name_entry = name_entry

    username_label = ttk.Label(root, text="Please enter your Username:")
    username_label.pack(pady=10)
    username_label.place(x=50, y=120)
    username_label.configure(style='TLabel')

    username_entry = ttk.Entry(root)
    username_entry.pack(pady=5)
    username_entry.place(x=50, y=150)
    username_entry.configure(style='TEntry')
    data_collector.username_entry = username_entry

    email_label = ttk.Label(root, text="Please enter your Email:")
    email_label.pack(pady=10)
    email_label.place(x=50, y=180)
    email_label.configure(style='TLabel')

    email_entry = ttk.Entry(root)
    email_entry.pack(pady=5)
    email_entry.place(x=50, y=210)
    email_entry.configure(style='TEntry')
    data_collector.email_entry = email_entry

    # creating button elements

    button_frame = ttk.Frame(root, style="My.TFrame", padding=10)
    button_frame.pack(fill="x", padx=10, pady=10)

    style = ttk.Style()
    style.configure("My.TSaveButton", background="#2196F3", foreground="white", font=("Helvetica", 10), padding=(10, 5))

    submit_button = tk.Button(button_frame, text="Submit", style="My.TButton",
                              command=lambda: data_collector.collect_data(name_entry.get(), email_entry.get()))
    submit_button.pack(side="left", padx=10)

    style.configure("My.TSaveButton", background="#2196F3", foreground="white", font=("Helvetica", 10), padding=(10, 5))

    save_button = tk.Button(button_frame, text="Click here to save your data", style="My.TSaveButton",
                            command=data_collector.save_data)
    save_button.pack(side="left", padx=10)

    delete_button = tk.Button(button_frame, text="Click here to opt-out and delete your data from our servers",
                              bg="#F44336", fg="white", font=("Helvetica", 10), padx=10, pady=5, bd=0,
                              command=data_collector.delete_data)
    delete_button.pack(side="left", padx=10)

    status_label = tk.Label(root, text="", fg="F44336", font=("Helvetica", 10))
    status_label.pack(pady=(10, 0))
    data_collector.status_label = status_label

    notice_label = tk.Label(root, text="", font=("Helvetica", 10), wraplength=350, justify="left")
    notice_label.pack(pady=10)
    data_collector.notice_label = notice_label

    # display privacy notice
    data_collector.privacy_notice()

    root.mainloop()
