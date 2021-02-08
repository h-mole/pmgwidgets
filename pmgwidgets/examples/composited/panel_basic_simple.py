# -*- coding:utf-8 -*-
# @Time: 2021/2/1 18:44
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: panel_basic.py

from qtpy.QtWidgets import QApplication
from pmgwidgets import PMGPanel

views = [('line_ctrl', 'name', 'What\'s your name?', 'hzy'),
         ('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150)),
         ('number_ctrl', 'height', 'How High could This Plane fly?', 12000, 'm', (10, 20000)),
         ('check_ctrl', 'do_you_like_planes', 'do you like fighters', True),
         ('combo_ctrl', 'plane_type', 'Fighters(Ordered by production time)', 'f22', ['f22', 'j20', 'su57'],
          ['Lockheed-Martin f22', '成都 j20', 'Сухо́й su57']),
         ('color_ctrl', 'color', 'Which color do u like?', (0, 200, 0)),
         ]
if __name__ == '__main__':
    app = QApplication([])
    panel = PMGPanel(views=views)

    panel.show()
    panel.set_as_controller('do_you_like_planes', ['plane_type'], True, 'enable')
    panel.set_as_controller('plane_type', ['color'], 'f22', 'disable')  # 当plane_type中值为f22的时候，设置颜色选择框为禁用。
    # 其他情况下不是禁用。
    print('Panel Value', panel.get_value())
    app.exec_()
