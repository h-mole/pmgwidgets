# -*- coding:utf-8 -*-
# @Time: 2021/2/11 21:09
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: run.py.py
from qtpy.QtGui import QGuiApplication
from qtpy.QtQml import QQmlApplicationEngine
from qtpy.QtCore import QObject, Signal, Slot


class Calculator(QObject):
    def __init__(self):
        QObject.__init__(self)

    # Signal sending sum
    # Necessarily give the name of the argument through arguments=['sum']
    # Otherwise it will not be possible to get it up in QML
    sumResult = Signal(int, arguments=['sum'])

    subResult = Signal(int, arguments=['sub'])

    # Slot for summing two numbers
    @Slot(int, int)
    def sum(self, arg1, arg2):
        # Sum two arguments and emit a signal
        self.sumResult.emit(arg1 + arg2)


    # Slot for subtraction of two numbers
    @Slot(int, int)
    def sub(self, arg1, arg2):
        # Subtract arguments and emit a signal
        self.subResult.emit(arg1 - arg2)


if __name__ == "__main__":
    import sys

    # Create an instance of the application
    app = QGuiApplication(sys.argv)
    # Create QML engine
    engine = QQmlApplicationEngine()
    # Create a calculator object
    calculator = Calculator()
    # And register it in the context of QML
    engine.rootContext().setContextProperty("calculator", calculator)
    # Load the qml file into the engine
    engine.load("main.qml")

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())