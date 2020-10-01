import pywinauto
import win32api
import win32con
from pywinauto.application import Application
from pywinauto import mouse
from ctypes.wintypes import tagPOINT


class AutoAssembler:

    def __init__(self):
        self.app = Application(backend='uia')
        self._window = None
        self.types_and_coords = []

    def open_app(self, app):
        self.app.start(app)

    def set_window(self, title=None):
        if title:
            self._window = self.app[title]
        else:
            self._window = self.app.top_window()
        return self._window

    def search_for_elements(self):
        check = self._window
        elements_tree = check.descendants()
        for i in elements_tree:
            if i.get_properties()['friendly_class_name'] != 'Toolbar' and \
               i.get_properties()['friendly_class_name'] != 'TitleBar' and \
               ['class_name'] != 'Scintilla':
                if i.get_properties()['texts'] == ['']:
                    coord = i.get_properties()['rectangle']
                    coord_x = coord.left
                    coord_y = coord.top
                    pywinauto.mouse.move(coords=(coord_x, coord_y))
                    elements_tree = check.descendants()
        return elements_tree

    def list_of_elements(self):
        elements_tree = self.search_for_elements()
        dictionary_of_elements = []
        for z in elements_tree:
            if z.get_properties()['friendly_class_name'] != 'Toolbar' and \
                     z.get_properties()['friendly_class_name'] != 'TitleBar':
                dictionary_of_elements.append(z.get_properties()['texts'][0] if list else 'texts')
                dictionary_of_elements.append(z.get_properties()['friendly_class_name'])
                dictionary_of_elements.append(z.get_properties()['rectangle'])
        elements_list = (list(zip(*[iter(dictionary_of_elements)] * 3)))
        return elements_list

    def names_types_coords(self):
        elements_list = self.list_of_elements()
        elements_name = []
        types_and_coords_1 = []
        for i in elements_list:
            if not i[0]:
                input_name = input("Введите название для элемента: ")
                types_and_coords_1.append(i[1])
                types_and_coords_1.append(i[2])
                elements_name.append(input_name)
            else:
                types_and_coords_1.append(i[1])
                types_and_coords_1.append(i[2])
                elements_name.append(i[0])
        self.types_and_coords = list(zip(*[iter(types_and_coords_1)] * 2))
        return elements_name, self.types_and_coords

    def window_dictionary(self):
        elements_name, self.types_and_coords = self.names_types_coords()
        window_name = self._window.window_text()
        dict_1 = {}
        for i in range(len(elements_name)):
            if elements_name[i] in dict_1:
                dict_1[elements_name[i] + '(2)'] = list(self.types_and_coords[i])
            else:
                dict_1[elements_name[i]] = list(self.types_and_coords[i])
        print({window_name: dict_1})

    def check_methods(self):
        self._window.set_focus()
        for element in self.types_and_coords:
            if element[0] == 'Button':
                point = tagPOINT(element[1].left, element[1].top)
                win32api.SetCursorPos((point.x, point.y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, element[1].left, element[1].top, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, element[1].left, element[1].top, 0, 0)
                yield


if __name__ == '__main__':
    zxc = AutoAssembler()
    zxc.open_app(r'C:\Program Files (x86)\Notepad++\notepad++.exe')
    zxc.set_window()
    zxc.window_dictionary()
    zxc.check_methods()
    next(zxc.check_methods())
    next(zxc.check_methods())
