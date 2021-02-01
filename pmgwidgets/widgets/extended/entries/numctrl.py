from qtpy.QtWidgets import QLineEdit, QLabel, QHBoxLayout
from .baseentryctrl import PMGBaseEntryCtrl


class PMGNumberCtrl(PMGBaseEntryCtrl):
    """
    用于输入数值。
    """

    def __init__(self, layout_dir: str, title: str, initial_value: int, unit: str = '', rang: tuple = None):
        super().__init__(layout_dir=layout_dir)
        self.on_check_callback = None
        if rang is None:
            rang = (float('-inf'), float('inf'))
        if isinstance(initial_value, int) and isinstance(rang[0], int) and isinstance(rang[1], int):
            self.num_type = int
        else:
            self.num_type = float

        self.prefix = QLabel(text=title)
        entryLayout = QHBoxLayout()
        entryLayout.setContentsMargins(0, 0, 0, 0)

        self.ctrl = QLineEdit()
        self.ctrl.textChanged.connect(self.ontext)

        self.postfix = QLabel(text=unit)

        self.central_layout.addWidget(self.prefix)
        self.central_layout.addLayout(entryLayout)
        entryLayout.addWidget(self.ctrl)
        entryLayout.addWidget(self.postfix)

        self.min, self.max = rang
        self.accury = initial_value
        self.set_value(initial_value)

    def ontext(self, event):
        if self.get_value() is None:
            self.set_ctrl_warning(True)
        else:
            self.set_ctrl_warning(False)
            self.para_changed()
        self.ctrl.update()
        if callable(self.on_check_callback):
            self.on_check_callback()
        self.signal_param_changed.emit(self.name)

    def set_value(self, n):
        self.ctrl.clear()
        self.ctrl.setText(str(n))

    def get_value(self):
        text = self.ctrl.text()
        try:
            num = self.num_type(text)
        except ValueError:
            import traceback
            traceback.print_exc()
            return None
        if num < self.min or num > self.max:
            return None
        return num
