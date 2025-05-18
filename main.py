# main.py

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import threading
from file_manager import filter_files_by_extension, move_files_one_by_one

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("ARW 文件移动器")

        self.src_path = tk.StringVar()
        self.dst_path = tk.StringVar()

        # 路径输入 & 按钮
        tk.Label(root, text="源文件夹:").pack()
        tk.Entry(root, textvariable=self.src_path, width=50).pack()
        tk.Button(root, text="选择源文件夹", command=self.select_src).pack()

        tk.Label(root, text="目标文件夹:").pack()
        tk.Entry(root, textvariable=self.dst_path, width=50).pack()
        tk.Button(root, text="选择目标文件夹", command=self.select_dst).pack()

        # 执行按钮
        tk.Button(root, text="移动 ARW 文件", command=self.start_moving_thread).pack(pady=10)

        # 进度条和状态
        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        self.status_label = tk.Label(root, text="等待操作...")
        self.status_label.pack()

    def select_src(self):
        path = filedialog.askdirectory()
        if path:
            self.src_path.set(path)

    def select_dst(self):
        path = filedialog.askdirectory()
        if path:
            self.dst_path.set(path)

    def start_moving_thread(self):
        thread = threading.Thread(target=self.move_arw_files)
        thread.start()

    def move_arw_files(self):
        src = self.src_path.get()
        dst = self.dst_path.get()

        if not os.path.isdir(src) or not os.path.isdir(dst):
            messagebox.showerror("错误", "路径无效")
            return

        files = filter_files_by_extension(src, [".arw"])
        total = len(files)
        if total == 0:
            messagebox.showinfo("无文件", "没有找到 ARW 文件")
            return

        self.progress["maximum"] = total
        self.progress["value"] = 0

        def progress_callback(i, total):
            self.progress["value"] = i
            percent = int(i / total * 100)
            self.status_label.config(text=f"已移动 {i}/{total} 个文件（{percent}%）")
            self.root.update_idletasks()

        move_files_one_by_one(files, src, dst, progress_callback)

        self.status_label.config(text="移动完成！")
        messagebox.showinfo("完成", f"成功移动了 {total} 个 ARW 文件")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()