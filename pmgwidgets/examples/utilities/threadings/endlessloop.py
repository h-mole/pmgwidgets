import sys
import time
from qtpy.QtWidgets import QTextEdit, QApplication, QPushButton, QWidget, QVBoxLayout
from pmgwidgets import PMGEndlessLoopThreadRunner


def run(i, j):
    time.sleep(0.1)
    return i + j


def on_step_finished(result):
    global text1, stepcount
    text1.append('step:%d,result:%s\n' % (stepcount,repr(result)))
    stepcount += 1


def on_finished():
    global text1
    text1.append('thread quit, all tasks completed!')


def start_thread():
    global endless_loop
    if endless_loop is not None:
        if endless_loop.is_running():
            return
    endless_loop = PMGEndlessLoopThreadRunner(run, args=(0, 0))
    endless_loop.signal_step_finished.connect(on_step_finished)
    endless_loop.signal_finished.connect(on_finished)

def stop_thread():
    global endless_loop
    endless_loop.shut_down()

stepcount = 0
endless_loop:PMGEndlessLoopThreadRunner = None

app = QApplication(sys.argv)
basewidget = QWidget()
basewidget.setLayout(QVBoxLayout())

text1 = QTextEdit()
pushbutton_run = QPushButton('Run')
pushbutton_stop = QPushButton('Stop')
pushbutton_run.clicked.connect(start_thread)
pushbutton_stop.clicked.connect(stop_thread)
basewidget.layout().addWidget(text1)
basewidget.layout().addWidget(pushbutton_run)
basewidget.layout().addWidget(pushbutton_stop)
basewidget.show()
sys.exit(app.exec_())
