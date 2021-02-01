from qtpy.QtWidgets import QApplication
from pmgwidgets import PMCheckTree
import sys

if __name__ == '__main__':
    foods = {
        'Program Scripts': {'.pyx': True, '.py': True, '.c': True, '.pyi': True, '.dll': True,
                            '.h': True, '.cpp': True, '.ipynb': True},
        'Documents': {'.txt': True, '.md': True, '.doc': True, '.docx': True, '.ppt': True, '.pptx': True},
        'Data Files': {'.csv': True, '.xls': True, '.xlsx': True, '.tab': True, '.dat': True, '.tsv': True,
                       '.sav': True, '.zsav': True, '.sas7bdat': True}}
    app = QApplication(sys.argv)
    tree = PMCheckTree(data=foods)
    tree.show()
    sys.exit(app.exec_())
