import os
import shutil
import tkinter as tk
from tkinter import filedialog

def AutoFileClassification():
    user_file_extension = file_extension_entry.get()
    separator = separator_entry.get()
    split_index = int(split_index_entry.get())

    working_directory = filedialog.askdirectory()

    files = [f for f in os.listdir(working_directory) if os.path.isfile(os.path.join(working_directory, f))]

    for file in files:
        filename, file_extension = os.path.splitext(file)

        if file_extension.lower() == user_file_extension.lower():
            if separator:  # 如果用户输入了分割符号
                if separator in filename:
                    parts = filename.split(separator)
                    if len(parts) >= split_index:
                        target_folder_name = separator.join(parts[:split_index])
                    else:
                        target_folder_name = filename
                else:
                    continue  # 跳过没有分割符号的文件
            else:  # 如果用户没有输入分割符号
                parts = [filename[i:i+split_index] for i in range(0, len(filename), split_index)]
                target_folder_name = parts[0]  # 修改这里，只取第一个部分作为目标文件夹名称

            if target_folder_name:  # 确保有目标文件夹名称
                target_directory = os.path.join(working_directory, target_folder_name)
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)
                shutil.move(os.path.join(working_directory, file), os.path.join(target_directory, file))

# 创建GUI界面
root = tk.Tk()
root.title("文件分类移动工具")
root.geometry("550x350")

# 设置背景颜色
root.configure(bg="#f2eada")

# 获取屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 计算窗口位置
x = int((screen_width - root.winfo_reqwidth()) / 2)
y = int((screen_height - root.winfo_reqheight()) / 2)

# 设置窗口位置
root.geometry(f"+{x-100}+{y-100}")

# 后缀名输入
file_extension_label = tk.Label(root, text="请输入文件后缀（如.txt）:", font=
('楷体', 12), bg="#f2eada")
file_extension_label.pack(pady=0)  # 修改这里，减小标题和输入框之间的距离
file_extension_entry = tk.Entry(root, bd=0, relief=tk.SOLID, highlightbackground="black", highlightthickness=2, font=
('楷体', 12))
file_extension_entry.pack(pady=5)

# 分割符号输入
separator_label = tk.Label(root, text="请输入分割符号（如_）\n如果什么都不输入，则按照下方分割数来从头开始对文件名进行分割:", font=
('楷体', 12), bg="#f2eada")
separator_label.pack(pady=0)  # 修改这里，减小标题和输入框之间的距离
separator_entry = tk.Entry(root, bd=0, relief=tk.SOLID, highlightbackground="black", highlightthickness=2, font=
('楷体', 12))
separator_entry.pack(pady=5)

# 分割索引输入
split_index_label = tk.Label(root, text="请输入分割位置（如2，表示将文件的前两个文字当作分类标识）:", font=
('楷体', 12), bg="#f2eada")
split_index_label.pack(pady=0)  # 修改这里，减小标题和输入框之间的距离
split_index_entry = tk.Entry(root, bd=0, relief=tk.SOLID, highlightbackground="black", highlightthickness=2, font=
('楷体', 12))
split_index_entry.pack(pady=5)

# 移动文件按钮
move_files_button = tk.Button(root, text="选择目录并进行文件分类", command=AutoFileClassification, bg="#426ab3", fg="white", bd=0, relief=tk.RAISED, borderwidth=2, padx=10, pady=5, highlightthickness=0, font=
('楷体', 12))
move_files_button.pack(pady=10)

# 运行GUI
root.mainloop()