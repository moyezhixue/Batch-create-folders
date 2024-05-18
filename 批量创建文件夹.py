# 引入 tkinter 库，用于创建 GUI 界面
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from tkinter import ttk

# 定义文件夹创建工具的类
class CreateFoldersApp:
    def __init__(self, master):
        # 初始化类的实例
        self.master = master
        self.master.title("文件夹创建工具")  # 设置窗口标题

        # 设置按钮的样式
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#FFC0CB", foreground="#FFC0CB")

        # 创建一个包含标签和按钮的框架
        self.grid = ttk.LabelFrame(master, text="文件夹创建", padding=(20, 20))
        self.grid.grid(padx=20, pady=20, sticky="ew")

        # 定义两个字符串变量，用于存储用户输入的父目录和文件夹数量
        self.parent_directory = tk.StringVar()
        self.folder_count = tk.StringVar()

        # 创建“选择父目录”按钮，并将其放置在界面上
        self.choose_parent_directory_button = ttk.Button(self.grid, text="选择父目录", command=self.choose_parent_directory)
        self.choose_parent_directory_button.grid(row=0, column=0, pady=10, sticky="w")
        ttk.Label(self.grid, text="父目录:").grid(row=0, column=1, pady=10, sticky="e")  # 显示标签，提示用户

        # 创建输入框用于输入文件夹数量
        self.folder_count_entry = ttk.Entry(self.grid, textvariable=self.folder_count, width=30)
        self.folder_count_entry.grid(row=1, column=1, pady=10, sticky="e")
        ttk.Label(self.grid, text="文件夹数量:").grid(row=1, column=0, pady=10, sticky="w")

        # 创建“创建文件夹”按钮
        self.create_button = ttk.Button(self.grid, text="创建文件夹", command=self.create_folders)
        self.create_button.grid(row=2, column=1, pady=10, sticky="e")

        # 创建用于显示结果的标签
        self.result_text = ttk.Label(self.grid, text="")
        self.result_text.grid(row=3, column=1, pady=10, sticky="e")

    # “选择父目录”按钮点击时执行的方法
    def choose_parent_directory(self):
        # 弹出文件夹选择对话框，并获取用户选择的目录
        selected_directory = filedialog.askdirectory()
        if selected_directory:
            self.result_text.config(text="")
            self.parent_directory.set(selected_directory)

    # “创建文件夹”按钮点击时执行的方法
    def create_folders(self):
        parent_directory = self.parent_directory.get()
        try:
            folder_count = int(self.folder_count.get())

            # 循环创建文件夹
            for i in range(folder_count):
                # 弹出对话框，获取用户输入的文件夹名称
                folder_name = simpledialog.askstring("输入文件夹名称", f"请输入第 {i + 1} 个文件夹名称:")
                if folder_name:
                    folder_path = f"{parent_directory}/{folder_name}"
                    success = self.create_folder(folder_path)

                    if success:
                        self.result_text.config(text=f"文件夹创建成功：{folder_path}")
                        # 创建一个新的按钮，并将其放置在界面上
                        button = ttk.Button(self.grid, text=f"按钮{i + 1}", command=lambda i=i: self.on_button_click(i),
                                            style="Custom.TButton")
                        button.grid(row=4 + i, column=1, pady=5, sticky="w")

                    else:
                        self.result_text.config(text=f"文件夹创建失败：{folder_path}")

        except ValueError:
            self.result_text.config(text="请输入有效的文件夹数量")

    # 创建文件夹的方法
    def create_folder(self, folder_path):
        import os
        try:
            os.makedirs(folder_path)
            return True
        except OSError:
            return False

    # 按钮点击时执行的方法
    def on_button_click(self, button_index):
        # 弹出消息框，显示按钮被点击的信息
        messagebox.showinfo("按钮点击", f"按钮 {button_index + 1} 被点击了！")

# 主程序入口
if __name__ == "__main__":
    root = tk.Tk()
    app = CreateFoldersApp(root)
    root.resizable(False, False)  # 设置窗口大小不可调整
    root.mainloop()
