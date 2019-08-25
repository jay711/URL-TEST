import tkinter as tk
from tkinter import *
from tkinter import filedialog


def windows():
    window = tk.Tk()
    window.title('URL测试器')
    window.geometry("500x300")

    def open_file():
        global filename
        filename = filedialog.askopenfilename(title='打开excel文件', filetypes=[('xlsx', '*.xlsx')])
        entry_filename.insert('insert', filename)

    def save_file():
        global filename_1
        filename_1 = filedialog.asksaveasfilename()
        save_filename1.insert('insert', filename_1)

    def closeThisWindow():
        window.destroy()



    button_import = tk.Button(window, text="导入文件", command=open_file)
    button_save = tk.Button(window, text="输出文件", command=save_file)
    button_close = tk.Button(window, text='开始测试', width=8, command=closeThisWindow)

    entry_filename = tk.Entry(window, width=40, font=("宋体", 12, 'bold'))
    save_filename1 = tk.Entry(window, width=40, font=("宋体", 12, 'bold'))

    entry_filename.pack()
    save_filename1.pack()
    button_import.pack()
    button_save.pack()
    button_close.pack()

    button_import.place(x=30, y=30)
    entry_filename.place(x=100, y=30)
    button_save.place(x=30, y=80)
    save_filename1.place(x=100, y=80)
    button_close.place(x=210, y=150)



    window.mainloop()

    return (filename, filename_1)

'''
a,b = windows()
print(a,b)
'''


