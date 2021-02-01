# -*- coding:utf-8 -*-
# @Time: 2021/2/1 18:44
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: panel_basic.py

from qtpy.QtWidgets import QApplication
from pmgwidgets import PMGPanel

views = [
    {"type": 'line_ctrl', 'name': 'name', 'title': 'What\'s your name?', 'init': 'hzy'},
    {'type': 'number_ctrl', 'name': 'age', 'title': 'How old are you?', 'init': 88,
     'unit': 'years old', 'range': (0, 150)},
    {'type': 'number_ctrl', 'name': 'height', 'title': 'How High could This Plane fly?', 'init': 12000,
     'unit': 'm', 'range': (10, 20000)},
    {'type': 'check_ctrl', 'name': 'sport', 'title': 'do you like sport', 'init': True},
    {'type': 'combo_ctrl', 'name': 'plane_type', 'title': 'Fighters(Ordered by production time)', 'init': 'f22',
     'choices': ['f22', 'j20', 'su57'], 'texts': ['Lockheed-Martin f22', '成都 j20', 'Сухо́й su57']},
    {'type': 'color_ctrl', 'name': 'color', 'title': 'Which color do u like?', 'init': (0, 200, 0)}
]
if __name__ == '__main__':
    app = QApplication([])
    panel = PMGPanel(views=views)

    panel.show()
    print('Panel Value', panel.get_value())
    app.exec_()
