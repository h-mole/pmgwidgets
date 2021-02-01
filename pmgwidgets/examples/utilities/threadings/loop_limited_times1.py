"""
关于有限次数循环的一个实例。
适用于后台线程刷新滚动条的场合。
此时无需考虑线程退出等问题，这些繁琐的问题将由线程管理类自动处理。
"""
import sys
import time
from qtpy.QtWidgets import QTextEdit, QApplication
from pmgwidgets import PMGLoopThreadRunner


def run(i, j):
    time.sleep(0.1)
    return i + j


def on_step_finished(step, result):
    global text1
    text1.append('传入每步不同的可迭代参数\nstep:%d,result:%s\n' % (step, repr(result)))


def on_finished():
    global text1
    text1.append('所有任务完成！')


app = QApplication(sys.argv)
text1 = QTextEdit()
text1.show()
oneshot = PMGLoopThreadRunner(run, iter_args=[(i, i + 1) for i in range(36)])
# 传入一个列表可迭代对象（当然也可以是其他迭代器。）作为参数。列表的长度就是循环的次数，列表的每一个元素代表每一步传入的参数。
oneshot.signal_step_finished.connect(on_step_finished)  # 每一步执行后的结果由signal_step_finished传回。多参数则会放进tuple里面。
oneshot.signal_finished.connect(on_finished)

sys.exit(app.exec_())
