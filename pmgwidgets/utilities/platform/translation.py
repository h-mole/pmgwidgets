def add_translation_file(file_path: str):
    from qtpy.QtWidgets import QApplication
    from qtpy.QtCore import QTranslator
    app = QApplication.instance()
    if hasattr(app, 'trans'):
        try:
            tr = QTranslator()
            path = file_path
            tr.load(path)
            app.installTranslator(tr)
        except:
            pass
