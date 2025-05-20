# ARW 文件管理器（带 GUI 界面）

一个使用 Python 构建的图形化工具，用于批量管理相机拍摄产生的 `.ARW` 原始格式文件。支持从文件夹中**分离 `.ARW` 文件并移动到指定目录**，保留 `.JPEG` 文件。内置**图形界面 + 实时进度条**，操作简单直观。

---

## ✨ 功能特性

- ✅ 批量扫描源文件夹中的 `.ARW` 文件
- ✅ 将 `.ARW` 文件移动到目标文件夹
- ✅ 保留 `.JPEG` 文件在原地
- ✅ 图形界面操作（使用 `tkinter` 实现）
- ✅ 实时进度条反馈（基于 `ttk.Progressbar`）
- ✅ 多线程操作，界面不卡顿

---
Macos 打包 
pyinstaller --windowed --name ARW_Manager --icon=assets/icon.icns main.py

Window打包：
pyinstaller --onefile --windowed --icon=icon.ico main.py

