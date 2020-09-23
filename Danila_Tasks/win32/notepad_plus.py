from pywinauto.application import Application
import pywinauto
import pywin32_bootstrap
import pywin32_system32
import pywin32_testutil


class NoteplusPage:

    def __init__(self):
        self.app = Application(backend='uia')
        self._window = None

    def open_app(self, app):
        self.app.start(app)

    def set_window(self, title=None):
        if title:
            self._window = self.app[title]
        else:
            self._window = self.app.top_window()

    def tree(self):
        check = self._window
        check.window_text()
        window_name = check.window_text()
        x = check.descendants()
        sator = []
        for i in x:
            if i.get_properties()['friendly_class_name'] != 'Toolbar' and \
               i.get_properties()['friendly_class_name'] != 'TitleBar':
                if i.get_properties()['texts'] == ['']:
                    coord = i.get_properties()['rectangle']
                    coord_x = coord.left
                    coord_y = coord.top
                    pywinauto.mouse.move(coords=(coord_x, coord_y))
                    x = check.descendants()
        for z in x:
            if z.get_properties()['friendly_class_name'] != 'Toolbar' and \
                     z.get_properties()['friendly_class_name'] != 'TitleBar':
                sator.append(z.get_properties()['texts'][0] if list else 'texts')
                sator.append(z.get_properties()['friendly_class_name'])
                sator.append(z.get_properties()['rectangle'])
                print(z.get_properties())
        elements = (list(zip(*[iter(sator)] * 3)))
        elements_name = []
        type_and_coords = []
        for i in elements:
            if i[0] == '':
                input_name = input("Введите название для элемента: ")
                type_and_coords.append(f'Тип: {i[1]}')
                type_and_coords.append(f'Координаты: {i[2]}')
                elements_name.append(input_name)
            else:
                type_and_coords.append(f'Тип: {i[1]}')
                type_and_coords.append(f'Координаты: {i[2]}')
                elements_name.append(i[0])
        type_and_coords_1 = (list(zip(*[iter(type_and_coords)] * 2)))
        dict_1 = {}
        for i in range(len(elements_name)):
            if elements_name[i] in dict_1:
                dict_1[elements_name[i] + '(2)'] = list(type_and_coords_1[i])
            else:
                dict_1[elements_name[i]] = list(type_and_coords_1[i])
        dict_2 = {}
        dict_2[window_name] = dict_1
        print(dict_2)
        GetClickablePoint


if __name__ == '__main__':
    zxc = NoteplusPage()
    zxc.open_app(r'C:\Program Files (x86)\Notepad++\notepad.exe')
    zxc.set_window()
    zxc.tree()
