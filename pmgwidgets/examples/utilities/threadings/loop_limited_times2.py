"""
关于有限次数循环的一个实例。
适用于后台线程刷新滚动条的场合。
此时无需考虑线程退出等问题，这些繁琐的问题将由类自动处理。
"""
import sys
import time
from qtpy.QtWidgets import QTextEdit, QApplication
from pmgwidgets import PMGLoopThreadRunner


def run(i, j):
    time.sleep(0.1)
    return i + j


def on_step_finished(step, result):
    global text1, loop_steps
    text1.append('传入同一参数(2,2),' + '进度:%.2f' % (step / loop_steps * 100) + '%' + ',结果:%s\n' % repr(result))


def on_finished():
    global text1
    text1.append('所有任务完成！')


loop_steps = 48  # 循环一共执行48次
app = QApplication(sys.argv)
text1 = QTextEdit()
text1.show()
oneshot = PMGLoopThreadRunner(run, loop_times=loop_steps, step_args=(2, 2))
oneshot.signal_step_finished.connect(on_step_finished)
oneshot.signal_finished.connect(on_finished)
sys.exit(app.exec_())
