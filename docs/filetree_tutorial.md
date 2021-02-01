## FileTree widget/文件树控件

```python
# -*- coding:utf-8 -*-
# @Time: 2021/2/1 21:35
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: filetree.py
import os
from qtpy.QtWidgets import QApplication
from pmgwidgets import PMGFilesTreeview

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    tree = PMGFilesTreeview(os.path.expanduser('~'), None)
    tree.show()
    sys.exit(app.exec_())
```

## Initial Arguments/初始参数:

- initial_dir:str,The path for initialization/初始时的路径。
- parent: The parent widget,default None/父控件，默认为None。

## Widget Signals/控件的信号

- new_file_signal = Signal(str)
Signal for a file is created. It returns a parameter which is the absolute path of the file.
新建文件信号，返回一个参数，是新建文件的绝对路径
- new_folder_signal = Signal(str) 
Signal for a folder is created. It returns a parameter which is the absolute path of the folder.
新建文件夹信号，返回一个参数，是新建文件夹的绝对路径
- delete_file_signal = Signal(str)            
Signal for a file or a folder is deleted. It returns a parameter which is the absolute path of the file/fplder.
删除文件或者文件夹信号，返回一个参数，是文件/文件夹的绝对路径。
- rename_file_signal = Signal(str, str)
Signal for file/folder renaming. It returns two parameters: abs path before renaming, abs path after renaming.
文件重命名的信号，返回两个参数，分别是重命名之前的绝对路径和重命名之后的绝对路径。 

NOTE/注意:

- The Signals above are triggered only if corresponding operations are succeeded

  这些信号只有在操作成功时才会触发。如果操作不成功（比如重命名时存在相同文件、删除文件时权限不够），那么就不会触发。