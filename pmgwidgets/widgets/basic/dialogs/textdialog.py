# -*- coding:utf-8 -*-
# @Time: 2021/2/10 10:12
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: textdialog.py
from qtpy.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextBrowser


class TextShowDialog(QDialog):
    def __init__(self, parent=None):
        super(TextShowDialog, self).__init__(parent=parent)
        self.setLayout(QVBoxLayout())
        self.text_widget = QTextBrowser()
        self.layout().addWidget(self.text_widget)

    def set_markdown(self, markdown: str):
        self.text_widget.setMarkdown(markdown)
