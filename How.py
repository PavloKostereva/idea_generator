import tkinter as tk
from random import choice
from tkinter import messagebox

# Функція додавання ідеї
def AddIdea():
    value = EnterText.get()
    if value.strip():  # Перевіряємо, що поле не порожнє і без пробілів
        with open('HOW.txt', 'a+', encoding="utf-8") as file:
            file.write(value + '\n')
        EnterText.delete(0, 'end')  # Очищаємо поле введення
    else:
        tk.messagebox.showinfo("Помилка", "Поле для вводу пусте")  # Виправлена назва messagebox

# Обробник натискання клавіші Enter
def EnterClick(e):
    AddIdea()

# Функція для вибору випадкової ідеї
def RandomChoice():
    try:
        with open('HOW.txt', 'r', encoding="utf-8") as file:  # Виправлено відкриття файлу
            lines = file.readlines()
        if lines:  # Перевірка, чи файл не порожній
            tk.messagebox.showinfo("Ідея", choice(lines))
        else:
            tk.messagebox.showinfo("Ідея", "Список ідей порожній!")  # Повідомлення, якщо файл порожній
    except FileNotFoundError:
        tk.messagebox.showinfo("Помилка", "Файл HOW.txt не знайдено")  # Помилка, якщо файл відсутній

# Налаштування головного вікна
window = tk.Tk()
window.resizable(width=False, height=False)
window.title("Генератор ідей")
window.geometry("720x360")
window["bg"] = "black"

# Текстова мітка
idea = tk.Label(window, text="Добавити ідею", font=("Arial Bold", 15), fg="lime", bg="black")
idea.place(x=290, y=25)

# Поле для введення тексту
EnterText = tk.Entry(fg="black", width=47)
EnterText.place(x=220, y=65)

# Кнопка для додавання ідеї
btn_add = tk.Button(window, text="Добавити", command=AddIdea, width=40, height=2, fg="black", bg="white")  # Передаємо функцію без виклику
btn_add.place(x=220, y=110)

# Прив'язка кнопки Enter до додавання
window.bind('<Return>', EnterClick)

# Текстова мітка для генерації
GiveIdea = tk.Label(window, text="Згенерувати ідею", font=("Arial Bold", 15), fg="lime", bg="black")
GiveIdea.place(x=260, y=170)

# Кнопка для показу випадкової ідеї
btn_show = tk.Button(window, text="Показати ідею", command=RandomChoice, width=40, height=2, fg="black", bg="white")
btn_show.place(x=220, y=210)

# Запуск програми
window.mainloop()
