from pywinauto.application import Application


class PyWin:

    def __init__(self):
        self.app = Application()
        self._window = None

    def open_app(self, app):
        self.app.start(app)

    def click(self, control):
        self._window[control].click()

    def set_window(self, title=None):
        if title:
            self._window = self.app[title]
        else:
            self._window = self.app.top_window()

    def select_tab_element(self, control, name):
        self._window[control].select(name)

    def input_path(self, control, path):
        self._window[control].type_keys(path)
