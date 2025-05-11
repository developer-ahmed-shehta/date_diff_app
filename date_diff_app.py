import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tkcalendar import DateEntry

# === Themes ===
LIGHT_THEME = {
    "BG": "#f8f9fa",
    "PRIMARY": "#3498db",
    "ACCENT": "#2ecc71",
    "TEXT": "#2c3e50",
    "FOOTER": "#7f8c8d",
    "ENTRY_BG": "#ffffff",
    "BUTTON_HOVER": "#2980b9"
}

DARK_THEME = {
    "BG": "#2c3e50",
    "PRIMARY": "#1abc9c",
    "ACCENT": "#f1c40f",
    "TEXT": "#ecf0f1",
    "FOOTER": "#bdc3c7",
    "ENTRY_BG": "#34495e",
    "BUTTON_HOVER": "#16a085"
}

current_theme = LIGHT_THEME


def apply_theme():
    theme = current_theme
    root.configure(bg=theme["BG"])
    header.configure(bg=theme["PRIMARY"])
    header_label.configure(bg=theme["PRIMARY"], fg="white")
    main.configure(bg=theme["BG"])
    label1.configure(bg=theme["BG"], fg=theme["TEXT"])
    label2.configure(bg=theme["BG"], fg=theme["TEXT"])
    result_label.configure(bg=theme["BG"], fg=theme["PRIMARY"])
    total_label.configure(bg=theme["BG"], fg=theme["ACCENT"])
    footer_label.configure(bg=theme["BG"], fg=theme["FOOTER"])
    theme_toggle.configure(bg=theme["PRIMARY"], fg="white")
    calc_button.configure(bg=theme["PRIMARY"], fg="white")


def toggle_theme():
    global current_theme
    current_theme = DARK_THEME if current_theme == LIGHT_THEME else LIGHT_THEME
    apply_theme()


def calculate_difference():
    try:
        date1 = datetime.strptime(entry1.get(), "%Y-%m-%d")
        date2 = datetime.strptime(entry2.get(), "%Y-%m-%d")

        if date2 <= date1:
            messagebox.showerror("خطأ", "يجب أن يكون التاريخ الثاني بعد التاريخ الأول!")
            result_label.config(text="")
            total_label.config(text="")
            return

        diff = relativedelta(date2, date1)
        result = f"الفرق: {diff.years} سنة، {diff.months} شهر، {diff.days} يوم"
        result_label.config(text=result)

        total_days = (date2 - date1).days
        total_label.config(text=f"إجمالي الأيام: {total_days} يوم")

    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال التواريخ بالتنسيق الصحيح: YYYY-MM-DD")
        result_label.config(text="")
        total_label.config(text="")


# === GUI Setup ===
root = tk.Tk()
root.title("حساب الفرق بين تاريخين - مميز")
root.geometry("500x520")
root.resizable(False, False)

header = tk.Frame(root, height=60)
header.pack(fill=tk.X)
header_label = tk.Label(header, text="حاسبة الفرق بين تاريخين", font=("Arial", 18, "bold"))
header_label.pack(pady=15)

main = tk.Frame(root, padx=40, pady=30)
main.pack(fill="both", expand=True)

label1 = tk.Label(main, text="أدخل التاريخ الأول:")
label1.pack(anchor="w")
entry1 = DateEntry(main, width=30, date_pattern='yyyy-mm-dd')
entry1.pack(pady=(0, 15))

label2 = tk.Label(main, text="أدخل التاريخ الثاني:")
label2.pack(anchor="w")
entry2 = DateEntry(main, width=30, date_pattern='yyyy-mm-dd')
entry2.pack(pady=(0, 20))


# Hover effect
def on_enter(e): calc_button.config(bg=current_theme["BUTTON_HOVER"])
def on_leave(e): calc_button.config(bg=current_theme["PRIMARY"])


calc_button = tk.Button(main, text="احسب الفرق", font=("Arial", 12, "bold"),
                        padx=20, pady=10, command=calculate_difference)
calc_button.pack()
calc_button.bind("<Enter>", on_enter)
calc_button.bind("<Leave>", on_leave)

result_label = tk.Label(main, text="", font=("Arial", 13, "bold"))
result_label.pack(pady=(20, 5))

total_label = tk.Label(main, text="", font=("Arial", 12))
total_label.pack()

footer_label = tk.Label(root,
                        text="صيغة التاريخ: YYYY-MM-DD (مثال: 2023-12-31)",
                        font=("Arial", 10))
footer_label.pack(side=tk.BOTTOM, pady=10)

# Theme toggle
theme_toggle = tk.Button(root, text="تبديل الوضع الليلي / النهاري",
                         font=("Arial", 10), command=toggle_theme)
theme_toggle.pack(pady=(0, 10))

apply_theme()
root.mainloop()
