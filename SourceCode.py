import os
import shutil
import tkinter as tk
from tkinter import filedialog

def move_files():
    user_file_extension = file_extension_entry.get()
    separator = separator_entry.get()
    split_index = int(split_index_entry.get())

    working_directory = filedialog.askdirectory()

    files = [f for f in os.listdir(working_directory) if os.path.isfile(os.path.join(working_directory, f))]

    for file in files:
        filename, file_extension = os.path.splitext(file)

        if file_extension.lower() == user_file_extension.lower():
            if separator:  # セパレータが入力されている場合
                if separator in filename:
                    parts = filename.split(separator)
                    if len(parts) >= split_index:
                        target_folder_name = separator.join(parts[:split_index])
                    else:
                        target_folder_name = filename
                else:
                    continue  # セパレータがないファイルはスキップする
            else:  # セパレータが入力されていない場合
                parts = [filename[i:i+split_index] for i in range(0, len(filename), split_index)]
                target_folder_name = parts[0]  # ここを変更して、最初の部分だけをターゲットフォルダ名とする

            if target_folder_name:  # ターゲットフォルダ名が存在することを確認する
                target_directory = os.path.join(working_directory, target_folder_name)
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)
                shutil.move(os.path.join(working_directory, file), os.path.join(target_directory, file))

# GUIを作成する
root = tk.Tk()
root.title("ファイル分類移動ツール")
root.geometry("600x400")

# 背景色を設定する
root.configure(bg="#f2eada")

# 画面サイズを取得する
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# ウィンドウの位置を計算する
x = int((screen_width - root.winfo_reqwidth()) / 2)
y = int((screen_height - root.winfo_reqheight()) / 2)

# ウィンドウの位置を設定する
root.geometry(f"+{x-100}+{y-100}")

# ファイルの拡張子入力
file_extension_label = tk.Label(root, text="ファイルの種類を入力してください（例 .txt ）:", font=
('楷体', 12), bg="#f2eada")
file_extension_label.pack(pady=0)  # タイトルと入力ボックスの間隔を縮小する
file_extension_entry = tk.Entry(root, bd=0, relief=tk.SOLID, highlightbackground="black", highlightthickness=2, font=
('楷体', 12))
file_extension_entry.pack(pady=5)

# セパレータ入力
separator_label = tk.Label(root, text="分割マークを入力してください（例 _ ）：\n何も入力しない場合は、次の分割番号に従ってファイル名が最初から分割される", font=
('楷体', 12), bg="#f2eada")
separator_label.pack(pady=0)  # タイトルと入力ボックスの間隔を縮小する
separator_entry = tk.Entry(root, bd=0, relief=tk.SOLID, highlightbackground="black", highlightthickness=2, font=
('楷体', 12))
separator_entry.pack(pady=5)

# 分割インデックス入力
split_index_label = tk.Label(root, text="分割番号を入力してください（例 2 ，どこから分割を示す）:", font=
('楷体', 12), bg="#f2eada")
split_index_label.pack(pady=0)  # タイトルと入力ボックスの間隔を縮小する
split_index_entry = tk.Entry(root, bd=0, relief=tk.SOLID, highlightbackground="black", highlightthickness=2, font=
('楷体', 12))
split_index_entry.pack(pady=5)

# ファイル移動ボタン
move_files_button = tk.Button(root, text="目標フォルダを選択してください", command=move_files, bg="#426ab3", fg="white", bd=0, relief=tk.RAISED, borderwidth=2, padx=10, pady=5, highlightthickness=0, font=
('楷体', 12))
move_files_button.pack(pady=10)

# GUIを実行する
root.mainloop()
