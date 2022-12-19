# firstNum = int(input("Введи первое число"))
# scndNum = int(input("Введи второе число"))
#
# summa = 0
# for i in range(firstNum, scndNum+1):
#         summa = firstNum + (scndNum)
# print(summa)


from tkinter import *
from tkinter import ttk


window = Tk()
window.title("Summa chisel")
window.geometry('400x250')
lbl1 = Label(window, text="Первое число", font=("Arial Bold", 15))
lbl1.grid(column=0, row=0)
txt1 = Entry(window, width=10)
txt1.grid(column=1, row=0)
lbl2 = Label(window, text="Второе число", font=("Arial Bold", 15))
lbl2.grid(column=0, row=1)
txt2 = Entry(window, width=10)
txt2.grid(column=1, row=1)

def summa():
        first_num = int(txt1.get())
        second_num = int(txt2.get())
        total1 = 0
        for i in range(first_num, second_num + 1):
                total1 = first_num + (second_num)
        print(total1)

btn = Button(window, text="Сумма всех чисел", command=summa)
btn.grid(column=1, row=2)
window.mainloop()
