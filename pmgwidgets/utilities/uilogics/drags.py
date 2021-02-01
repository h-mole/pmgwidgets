import sys
from qtpy.QtWidgets import QApplication, QTextBrowser


class Demo(QTextBrowser):  # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.setAcceptDrops(True)  # 2

    def dragEnterEvent(self, QDragEnterEvent):  # 3
        print('Drag Enter')
        if QDragEnterEvent.mimeData().hasText():
            QDragEnterEvent.acceptProposedAction()
            print()

    def dragMoveEvent(self, QDragMoveEvent):  # 4
        # print('Drag Move')
        pass

    def dragLeaveEvent(self, QDragLeaveEvent):  # 5
        # print('Drag Leave')
        pass

    def dropEvent(self, QDropEvent):  # 6
        print('Drag Drop')
        print('text', QDropEvent.mimeData().text())
        # MacOS
        txt_path = QDropEvent.mimeData().text().replace('file:///', '/')

        # Linux
        # txt_path = QDropEvent.mimeData().text().replace('file:///', '/').strip()

        # Windows
        # txt_path = QDropEvent.mimeData().text().replace('file:///', '')
        print(txt_path)
        # with open(txt_path, 'r') as f:
        #     self.setText(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
