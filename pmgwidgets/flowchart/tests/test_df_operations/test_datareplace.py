import sys
from typing import List, Union

from qtpy.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit
from pmgwidgets.flowchart.nodes.dfoperation import DataReplace
import numpy as np
import pandas as pd

if __name__ == '__main__':
    app = QApplication(sys.argv)

    info = {
        'regulations': [
            {'input_col_name': '$ALL', 'output_col_name': 'a', 'str_to_replace': 'aa', 'replace_with': 'dddd',
             'match_words': False, 'regex': False, 'case_sensitive': False}]}
    r = DataReplace()
    r.load_info(info)
    # r.on_settings_requested(None)
    print(
        r.process(
            pd.DataFrame([['aa123', 'aa', 'bb', 7], ['bb123', 'aa1234', 'aa', 6]], columns=['a', 'b', 'c', 'd'])
        )
    )
    sys.exit(app.exec_())
