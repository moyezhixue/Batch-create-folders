import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def create_folders():
    folder_names = folders_entry.get(1.0, tk.END).strip().split('\n')
    base_dir = directory_entry.get()

    if not base_dir:
        messagebox.showerror("错误", "请选择一个基础目录。")
        return

    if not folder_names:
        messagebox.showerror("错误", "请输入至少一个文件夹名称。")
        return

    # 替换文件夹名称中的模板
    created_folders = []
    for i, folder_name in enumerate(folder_names):
        if folder_name:  # 跳过空字符串
            folder_name = folder_name.replace("{{number}}", str(i + 1))
            try:
                os.makedirs(os.path.join(base_dir, folder_name), exist_ok=True)
                created_folders.append(folder_name)
            except OSError as e:
                messagebox.showerror("错误", f"无法创建文件夹'{folder_name}'。原因：{e}")

    # 如果有文件夹创建成功，显示摘要
    if created_folders:
        messagebox.showinfo("摘要", "成功创建了 {} 个文件夹：\n{}".format(len(created_folders), '\n'.join(created_folders)))

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

def save_input():
    folder_names = folders_entry.get(1.0, tk.END).strip()
    if folder_names:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="folders.txt")
        if file_path:
            with open(file_path, 'w') as file:
                file.write(folder_names)

def load_input():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            folders_entry.delete(1.0, tk.END)
            folders_entry.insert(1.0, file.read())

# 创建主窗口
root = tk.Tk()
root.title("批量创建文件夹")
root.resizable(width=False, height=False)  # 防止窗口大小调整

# 创建文本输入框，用于输入文件夹名称
folders_label = tk.Label(root, text="请输入想要创建的文件夹名称，每行一个（使用{{number}}作为模板）：")
folders_label.pack()
folders_entry = tk.Text(root, height=10, width=50)
folders_entry.pack()

# 创建按钮，用于选择目录
directory_label = tk.Label(root, text="选择基础目录：")
directory_label.pack()
directory_entry = tk.Entry(root, width=50)
directory_entry.pack()
select_dir_button = tk.Button(root, text="选择目录", command=select_directory)
select_dir_button.pack()

# 创建按钮，用于创建文件夹
create_button = tk.Button(root, text="创建文件夹", command=create_folders)
create_button.pack()

# 创建按钮，用于保存和加载输入
save_button = tk.Button(root, text="保存输入", command=save_input)
save_button.pack()
load_button = tk.Button(root, text="加载输入", command=load_input)
load_button.pack()

# 运行主循环
root.mainloop()
