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
