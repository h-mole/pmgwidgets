from pmgwidgets import PMGPanel
import sys
from qtpy.QtWidgets import QApplication

app = QApplication(sys.argv)
views = [
    [
        ('eval_ctrl', 'code_eval', 'Evaluate this code', 123 + 456, 'normal'),
        ('eval_ctrl', 'code_eval2', 'Evaluate this code', (1, 2, 3), 'safe')
    ],
    ('keymap_ctrl', 'key_map2', 'Key For Find', 'Ctrl+F'),
    {'type': 'keymap_ctrl', 'name': 'key_map3', 'title': 'Key For Replace', 'init': 'Ctrl+H'}  # 也支持用字典格式输入各个参数。
]
sp2 = PMGPanel(views=views, layout_dir='v')
sp2.set_items(views)
sp2.show()

sys.exit(app.exec_())
