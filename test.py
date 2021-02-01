# -*- coding:utf-8 -*-
# @Time: 2021/1/30 11:44
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: test.py
from qtpy.QtWidgets import QApplication

from pmgwidgets import PMGPanel

if __name__ == '__main__':
    app = QApplication([])
    e = PMGPanel()
    e.show()
    e.set_items([('line_ctrl', 'aaa', 'aaa', 'aaa')])
    app.exec_()
