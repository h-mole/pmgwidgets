import sys
from typing import List

from qtpy.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit
from pmgwidgets import PMFlowWidget, PMGFlowContent


class ContentDialog(QDialog):
    def __init__(self, parent=None, initial_value: float = 0):
        super().__init__(parent)
        self.setLayout(QVBoxLayout())
        self.line_edit = QLineEdit()
        self.layout().addWidget(self.line_edit)
        self.line_edit.setText(str(initial_value))


class CustomFlowContent(PMGFlowContent):
    def __init__(self):
        super(CustomFlowContent, self).__init__()
        self.input_args_labels = ['input1']
        self.output_ports_labels = ['output1']
        self.class_name = 'Integrate'
        self.text = '积分'
        self.icon_path = ''
        self._initial_value = 0
        self.x = self._initial_value

    def process(self, *args) -> List[object]:
        self.x += args[0]
        return [self.x]

    def on_settings_requested(self, parent):
        dlg = ContentDialog(parent)

        dlg.exec_()
        self._initial_value = float(dlg.line_edit.text())
        print(self._initial_value)

    def refresh(self):
        self.x = self._initial_value

    def format_param(self) -> str:
        return '初值:' + str(self._initial_value)


if __name__ == '__main__':
    from pmgwidgets import PMGFlowContent
    import cgitb

    cgitb.enable()
    app = QApplication(sys.argv)

    graphics = PMFlowWidget()
    graphics.load(path='flowchart_stat.pmcache')
    graphics.show()
    sys.exit(app.exec_())
