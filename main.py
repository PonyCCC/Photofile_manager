# main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from file_manager import filter_files_by_extension, move_files

class App:
    def  __init__(self, root):
        self.root = root
        self.root.title("ARW/JRPG 批量管理器")

        self.src_path = tk.StringVar()
        self.dst_path = tk.StringVar()

        tk.Label(root, text="源文件夹:").pack()
        tk.Entry(root, textvariable=self.src_path, width=50).pack()
        tk.Button(root, text="选择源文件夹", command=self.select_src).pack()

        tk.Label(root, text="目标文件夹:").pack()
        tk.Entry(root, textvariable=self.dst_path, width=50).pack()
        tk.Button(root, text="选择目标文件夹", command=self.select_dst).pack()

        tk.Button(root, text="移动文件", command=self.move_files).pack(pady=10)

    def select_src(self):
        path = filedialog.askdirectory()
        if path:
            self.src_path.set(path)
    
    def select_dst(self):
        path = filedialog.askdirectory()
        if path:
            self.dst_path.set(path)
    
    def move_files(self):
        src = self.src_path.get()
        dst = self.dst_path.get()
        if not os.path.isdir(src) or not os.path.isdir(dst):
            messagebox.showerror("error","wrong path")
            return
        files = filter_files_by_extension(src, [".arw", "jpeg","jpg"])
        if not files:
            messagebox.showinfo("no files","no removeable file found")
            return
        move_files(files, src, dst)
        messagebox.showinfo("completed", f"succeed move {len(files)} files")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


