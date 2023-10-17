import tkinter as tk

root = tk.Tk()

# 创建一个文本框
text = tk.Text(root, height=10, width=40)
text.pack()

# 创建垂直滚动条，并将其与文本框关联
scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.config(yscrollcommand=scrollbar.set)

root.mainloop()