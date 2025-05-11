
# 🗓️ Date Difference Calculator (Arabic GUI with Theme Toggle)

A simple, user-friendly GUI application built with Python's `tkinter` that calculates the difference between two dates. This tool supports Arabic labels and messages and includes both light and dark themes.

## 🌟 Features

- 📅 **Date Picker** inputs using `tkcalendar`
- 🧮 Calculates the difference in:
  - Years
  - Months
  - Days
  - Total days
- 🌗 **Light/Dark Theme Toggle**
- 🌐 Fully localized interface in **Arabic**
- ⚠️ Error handling for invalid date inputs and logic

## 🖼️ Preview

![App Screenshot](assets/screenshot.png)

## 🛠️ Requirements

- Python 3.7+
- [tkcalendar](https://pypi.org/project/tkcalendar/)
- [dateutil](https://pypi.org/project/python-dateutil/)

### Install dependencies

```bash
pip install tkcalendar python-dateutil
```

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/date-difference-arabic.git
cd date-difference-arabic
```

2. Run the script:

```bash
python date_difference_calculator.py
```

## 📂 File Structure

```
date-difference-arabic/
├── date_difference_calculator.py
├── README.md
├── assets/
│   └── screenshot.png
```

## 🧑‍💻 Usage

1. أدخل التاريخ الأول والثاني باستخدام الحقول المتاحة.
2. اضغط على زر **"احسب الفرق"**.
3. سترى الفرق بالسنة، والشهر، واليوم، بالإضافة إلى إجمالي الأيام.
4. يمكنك التبديل بين الوضع النهاري والليلي باستخدام الزر في الأسفل.

## 🌙 Themes

- **Light Theme** (Default)
- **Dark Theme** with adjusted color palette for night use

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
