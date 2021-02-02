# pmgwidgets

## Description

### Developers and License

This package is developed by PyMiner develop team to support the software of PyMiner, and the license should follow the qt-bindings' license.

if PyQt5, license should be **GPL**; or if PySide2, it should under **LGPL** License.

email:1295752786@qq.com

## Software Architecture

Coding on pure Python, calling the Qt-bindings.

## Installation

1. install dependencies

```shell
pip install -r requirements.txt
```

NOTE: qtpy is an upper interface on PyQt5/PySide2, which works only if either of PyQt5/PySide2 is installed. So please
make sure you have one qt-python binding installed in the site-packages.

## Quick Start

It's suggested to import widgets from pmgwidgets like this:

```python
from pmgwidgets import {Widget_name}
```

You can refer to ``pmgwidgets/examples`` folder for more demostrations.

There are some detailed documentations here:

[Parameter Dialog](docs/pmgpanel_tutorial.md)

[File Tree](docs/filetree_tutorial.md)

> NOTE:
> To avoid writing translation files,  In those docs, sentences are written in both en and zh with this format:
> `{en_US}/{zh_CN}`. The en_US and zh_CN setences are of the same meanings.
> if you cannot understand zh_CN , don't panic. Just view the English!

### Create a simple Panel to ask parameters
```python
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
```
You will get a parameter dialog like this:

![](figures\settings_panel.png)

For more details of this dialog, [CLICK HERE](docs/pmgpanel_tutorial.md)

### Create a Tree of files

code:

```python
# -*- coding:utf-8 -*-
# @Time: 2021/2/1 21:35
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: filetree.py
import os
from qtpy.QtWidgets import QApplication
from pmgwidgets import PMGFilesTreeview

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    tree = PMGFilesTreeview(os.path.expanduser('~'), None)
    tree.show()
    sys.exit(app.exec_())

```



![](figures/basic/filetree.png)
For more details of filetree, [CLICK HERE](docs/filetree_tutorial.md)

### Simpler QThread implementation

It can be confusing for start a QThread and stop it. To solve this problem, pmgwidgets offers several QThread implementations to make it easier to use QThread safely.

```python
import sys
import time

from pmgwidgets import PMGOneShotThreadRunner
from qtpy.QtWidgets import QTextEdit, QApplication, QWidget, QVBoxLayout, QPushButton


def run(loop_times):
    for i in range(loop_times):
        print(i)
        time.sleep(1)
    return 'finished!!', 'aaaaaa', ['finished', 123]


def single_shoot():
    global oneshot, textedit
    if oneshot is not None:
        if oneshot.is_running(): # 如果后台线程已经在运行，那么就不要重新创建，否则可能造成程序崩溃。在实际程序中可以考虑加一个弹出框来进行提示。
            return
    oneshot = PMGOneShotThreadRunner(run, args=(3,))
    oneshot.signal_finished.connect(lambda x: textedit.append('任务完成，函数返回值：' + repr(x)))# The text means: "Tasks finished. The return value is:"+repr(x)


oneshot = None
app = QApplication(sys.argv)
basewidget = QWidget()
basewidget.setLayout(QVBoxLayout())

textedit = QTextEdit()
pushbutton = QPushButton('run')
pushbutton.clicked.connect(single_shoot)
basewidget.layout().addWidget(textedit)
basewidget.layout().addWidget(pushbutton)
basewidget.show()
sys.exit(app.exec_())

```
When running, click the 'run' button to make the background thread run. After three seconds, the texts could be displayed.

(In the picture below, The text in the `QTextEdit` means:"Tasks finished. The return value is:('finished!!','aaaaaa',['finished',123])")

![](docs/doc_figures/test_oneshot_thread.png)

For more detailed docs of Simpler QThread, [CLICK HERE](docs/threading_and_tasking.md)

