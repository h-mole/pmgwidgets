"""
快速启动。
"""
import socket
import time
import os
import sys
import platform

fig = None


def init_matplotlib():
    global fig
    import matplotlib.pyplot as plt
    fig = plt.Figure()  # 预先准备一个画布，从而激活matplotlib的绘图引擎。这样有助于Python初始化。


init_dic = {'matplotlib.pyplot': init_matplotlib}

t0 = time.time()

# sys.argv.append(
#     r'C:\Users\12957\Documents\Developing\Python\PyMiner_dev_kit\bin\pmgwidgets\widgets\basic\others\scripts\test1_instant_boot.py')

import chardet
import importlib
import runpy
import re

t1 = time.time()
print("Boot  time elapsed: %f s" % (t1 - t0))
file_name = sys.argv[1]
assert os.path.exists(file_name)
start_line = -1
with open(file_name, 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if re.match('#[ \t]*>>>', line.lstrip()) is not None:
            if line.lstrip() == line:
                start_line = i
            else:
                print('Indentation at run symbol should be 0, so the run symbol was neglected!')

        if line.strip().startswith('from ') or line.strip().startswith('import '):
            try:
                exec(line.strip())
            except Exception:
                import traceback

                traceback.print_exc()
for __k in init_dic.keys():
    if __k in sys.modules.keys():
        init_dic[__k]()

pre_exec = '\n'.join(lines[:start_line])
# print(pre_exec)
exec(pre_exec)
os.chdir(os.path.dirname(file_name))
sys.path.append(os.path.dirname(file_name))

print('======Ready,at {0} line {1}'.format(os.path.basename(file_name), start_line + 1))
s = input('>>')

if platform.system().lower() == 'windows':
    import win32con
    import win32gui
    import win32process
    import pythoncom
    import win32com


    def get_hwnds_for_pid(pid):
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
                if found_pid == pid:
                    hwnds.append(hwnd)
                return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        return hwnds


    def scan():
        """
        扫描监视全部窗口，当窗口出现时将其闪现出来。
        Returns:

        """
        pythoncom.CoInitialize()
        import win32com.client
        while True:
            time.sleep(0.05)
            pid = os.getpid()
            hwnds = get_hwnds_for_pid(pid)
            for hwnd in hwnds:
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(hwnd)  # 将当前的窗口置顶。
            if len(hwnds) > 0:
                break


    import threading

    th = threading.Thread(target=scan)
    th.setDaemon(True)
    th.start()

with open(file_name, 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if i < start_line:
            lines[i] = ''
        else:
            break
    # print(''.join(lines))
    try:
        exec(''.join(lines))
    except SyntaxError as s:
        s.filename = file_name
        raise s
        # print(s,type(s))
# runpy.run_path(file_name, run_name='__main__')


print('======Task Finished====')
