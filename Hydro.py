# АВТОМАТИЧЕСКАЯ ГЕНЕРАЦИЯ КОДА В ФОРМАТЕ ".py" ИЗ ФАЙЛОВ В ФОРМАТЕ ".ui"
"""
import subprocess
subprocess.run(["pyuic5", "-x", "MainWindow.ui", "-o", "MainWindow.py"])
subprocess.run(["pyuic5", "-x", "NewWindow.ui", "-o", "NewWindow.py"])
subprocess.run(["pyuic5", "-x", "Warning.ui", "-o", "Warning.py"])
subprocess.run(["pyuic5", "-x", "Error.ui", "-o", "Error.py"])
subprocess.run(["pyuic5", "-x", "Save.ui", "-o", "Save.py"])
subprocess.run(["pyuic5", "-x", "Exit.ui", "-o", "Exit.py"])
"""


# ИМПОРТ БИБЛИОТЕК И СГЕНЕРИРОВАННЫХ ФАЙЛОВ
import math
import pandas as pd

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QAction, QToolTip

from MainWindow import Ui_MainWindow
from NewWindow import Ui_NewWindow
from Warning import Ui_Warning
from Error import Ui_Error
from Save import Ui_Save
from Exit import Ui_Exit


# ОКНО "ВВОД ДАННЫХ"
class MainWindow(QMainWindow, Ui_MainWindow):
    # Конструктор класса
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Установка автора в статус бар
        self.statusbar.setStyleSheet("font-family: Cambria; font-size: 9pt; color: grey; text-decoration: none;")
        self.statusbar.showMessage('    Автор: Дмитрий Чанчиков')

        # Импорт и установка иконки и чертежа
        self.setWindowIcon(QIcon('icons8-pipes-96.png'))
        self.label_chert.setPixmap(QPixmap("uzel_2.png"))
        self.label_chert.setScaledContents(True)

        # Словарь названий и значений
        self.var_dict = {"chastota": 0, "lin_skoroct": 0, "davlenie": 0, "nach_temp": 0, "konech_temp": 0,
                         "rashod_vody": 0, "moshnoct_tepl": 0, "temp_uplotn_n_P": 0, "temp_uplotn_Kst_Kupl": 0,
                         "temp_uplotn_V_P_Dpr_Lpr": 0, "diam_nar": 0, "diam_vnutr": 0, "diam_priv": 0,
                         "dlina_uplotn": 0, "dlina_otv": 0, "dlina_priv": 0, "sheroh": 0,
                         "trenie_uplotn": 0, "tepl_stali": 0, "tepl_uplotn": 0}

        # Частота и лин. скорость не могут быть выбраны одновременно (но могут быть не выбраны одновременно)
        self.checkBox_chastota.clicked.connect(lambda: self.change_with_element(self.checkBox_lin_skoroct))
        self.checkBox_lin_skoroct.clicked.connect(lambda: self.change_with_element(self.checkBox_chastota))

        # При изменении шероховатости устанавливается флажок в коэфф. трения и наоборот
        self.checkBox_sheroh.clicked.connect(lambda state: self.change_flag(state, self.checkBox_trenie_uplotn))
        self.checkBox_trenie_uplotn.clicked.connect(lambda state: self.change_flag(state, self.checkBox_sheroh))

        # Следующие величины не могут быть отмечены флажками
        self.checkBox_nach_temp.clicked.connect(lambda: self.checkBox_nach_temp.setCheckState(QtCore.Qt.Unchecked))
        self.checkBox_konech_temp.clicked.connect(lambda: self.checkBox_konech_temp.setCheckState(QtCore.Qt.Unchecked))
        self.checkBox_dlina_uplotn.clicked.connect(lambda: self.checkBox_dlina_uplotn.setCheckState(QtCore.Qt.Unchecked))
        self.checkBox_dlina_otv.clicked.connect(lambda: self.checkBox_dlina_otv.setCheckState(QtCore.Qt.Unchecked))
        self.checkBox_tepl_stali.clicked.connect(lambda: self.checkBox_tepl_stali.setCheckState(QtCore.Qt.Unchecked))
        self.checkBox_tepl_uplotn.clicked.connect(lambda: self.checkBox_tepl_uplotn.setCheckState(QtCore.Qt.Unchecked))

        # Следующие величины отмечены флажками, которые нельзя снять
        self.checkBox_rashod_vody.clicked.connect(lambda: self.checkBox_rashod_vody.setCheckState(QtCore.Qt.Checked))
        self.checkBox_moshnoct_tepl.clicked.connect(lambda: self.checkBox_moshnoct_tepl.setCheckState(QtCore.Qt.Checked))
        self.checkBox_temp_uplotn_n_P.clicked.connect(lambda: self.checkBox_temp_uplotn_n_P.setCheckState(QtCore.Qt.Checked))
        self.checkBox_temp_uplotn_Kst_Kupl.clicked.connect(lambda: self.checkBox_temp_uplotn_Kst_Kupl.setCheckState(QtCore.Qt.Checked))
        self.checkBox_temp_uplotn_V_P_Dpr_Lpr.clicked.connect(lambda: self.checkBox_temp_uplotn_V_P_Dpr_Lpr.setCheckState(QtCore.Qt.Checked))
        self.checkBox_diam_priv.clicked.connect(lambda: self.checkBox_diam_priv.setCheckState(QtCore.Qt.Checked))
        self.checkBox_dlina_priv.clicked.connect(lambda: self.checkBox_dlina_priv.setCheckState(QtCore.Qt.Checked))

        # При установке флажка название и значение становятся не активными, при снятии наоборот
        for name, var in self.var_dict.items():
            self.change_enable(name)

        # Установка фокуса
        self.doubleSpinBox_chastota.setFocus()
        for index, name in enumerate(list(self.var_dict.keys())):
            if index >= (len(list(self.var_dict.keys())) - 1): break
            element_prev = getattr(self, f"checkBox_{list(self.var_dict.keys())[index]}")
            element_cur = getattr(self, f"doubleSpinBox_{list(self.var_dict.keys())[index]}")
            element_next = getattr(self, f"checkBox_{list(self.var_dict.keys())[index + 1]}")
            self.setTabOrder(element_prev, element_cur)
            self.setTabOrder(element_cur, element_next)

        # Подключение кнопок "Рассчитать" и "Выйти"
        self.pushButton_calculate.clicked.connect(self.calculate)
        self.pushButton_exit.clicked.connect(self.close)

        # Создаем экземпляр нового окна и диалоговых окон
        self.new_window = NewWindow(self)
        self.warning = Warning(self)
        self.error = Error(self)
        self.save = Save(self)
        self.exit = Exit(self)

    # Переопределение метода изменения размера окна
    def resizeEvent(self, event):
        if self.label_chert.geometry().width() == 450:
            self.label_chert.setMaximumHeight(330)
        else:
            self.label_chert.setMaximumHeight(1000)  # print(f"Window resized to: {event.size().width()}x{event.size().height()}")

    # Переопределение метода нажатия клавиш
    def keyPressEvent(self, event):
        # Клавиша "Enter"
        if event.key() == Qt.Key_Return:
            if self.focusWidget() == self.pushButton_calculate or self.focusWidget() == self.checkBox_chastota or \
                    self.focusWidget() == self.checkBox_lin_skoroct or self.focusWidget() == self.checkBox_davlenie or \
                    self.focusWidget() == self.checkBox_diam_nar or self.focusWidget() == self.checkBox_diam_vnutr or \
                    self.focusWidget() == self.checkBox_sheroh or self.focusWidget() == self.checkBox_trenie_uplotn:
                self.focusWidget().click()
        # Клавиша "Esc"
        if event.key() == Qt.Key_Escape:
            self.close()

    # Переопределение метода закрытия окна
    def closeEvent(self, event):
        if self.exit.exec_() == 1:
            self.new_window.close()
            super().closeEvent(event)
        else:
            event.ignore()

    # Метод для снятия флажка с переданного элемента (если на нем стоит флажок, то он снимается)
    def change_with_element(self, element):
        if element.isChecked():
            element.setChecked(False)

    # Метод для смены установки флажков (RadioButton)
    def change_flag(self, state, element):
        element.setChecked(not state)

    # Метод для смены активности элементов (1 - не акт, 0 - акт)
    def change_enable(self, name):
        checkbox = getattr(self, f"checkBox_{name}")
        label = getattr(self, f"label_{name}")
        spinbox = getattr(self, f"doubleSpinBox_{name}")
        checkbox.stateChanged.connect(lambda state: label.setEnabled(not state))
        checkbox.stateChanged.connect(lambda state: spinbox.setEnabled(not state))

    # Метод для получения значений из активных элементов
    def get_value_if_element_enabled(self):
        result_dict = {}
        for name, var in self.var_dict.items():
            if getattr(self, f"doubleSpinBox_{name}").isEnabled():
                var = getattr(self, f"doubleSpinBox_{name}").value()
            else: var = 0
            result_dict[name] = var
        return result_dict

    # Метод для вызова предупреждения
    def show_warning(self, name_0):
        self.warning.label_0.setText(getattr(self, f"label_{name_0}").text())
        return self.warning.exec_()

    # Метод для вызова ошибки
    def show_error(self, name_0, num, name_1):
        self.error.label_0.setText(getattr(self, f"label_{name_0}").text())
        self.error.label_1.setText(getattr(self, f"label_{name_1}").text())
        if num == 2:
            if self.var_dict["lin_skoroct"] == 0: self.error.label_2.setText(self.label_lin_skoroct.text())
            else: self.error.label_2.setText(self.label_chastota.text())
            self.error.label_or.setVisible(True)
            self.error.checkBox_2.setVisible(True)
        else:
            self.error.label_2.setText('')
            self.error.label_or.setVisible(False)
            self.error.checkBox_2.setVisible(False)
        self.error.exec_()

    # Метод для расчета и вывода в новое окно
    def calculate(self):
        # Обновление словаря
        updated_dict = self.get_value_if_element_enabled()
        self.var_dict.update(updated_dict)

        # Рассчет параметров переменной активности
        if self.var_dict["davlenie"] != 0:
            t = 4.8 * math.exp(0.0161 * self.var_dict["davlenie"])  # Толщина стенки через давление
            print(t)
            if (self.var_dict["chastota"] != 0 and self.var_dict["lin_skoroct"] == 0) or \
                    (self.var_dict["chastota"] == 0 and self.var_dict["lin_skoroct"] != 0):
                if self.var_dict["diam_nar"] != 0:
                    if self.var_dict["diam_vnutr"] != 0 and self.show_warning("diam_vnutr") == 0: return
                    self.var_dict["diam_vnutr"] = self.var_dict["diam_nar"] - 2 * t
                elif self.var_dict["diam_nar"] == 0 and self.var_dict["diam_vnutr"] != 0:
                    self.var_dict["diam_nar"] = self.var_dict["diam_vnutr"] + 2 * t
                else:
                    self.show_error("diam_nar", 2, "diam_vnutr")
                    return
                if self.var_dict["lin_skoroct"] == 0:
                    self.var_dict["lin_skoroct"] = math.pi * self.var_dict["diam_nar"] * self.var_dict["chastota"] / (60000)
                else:
                    self.var_dict["chastota"] = 60000 * self.var_dict["lin_skoroct"] / (math.pi * self.var_dict["diam_nar"])
            else:
                if self.var_dict["diam_nar"] == 0 and self.var_dict["diam_vnutr"] == 0:
                    self.var_dict["diam_nar"] = 60000 * self.var_dict["lin_skoroct"] / (math.pi * self.var_dict["chastota"])
                else:
                    if self.var_dict["diam_nar"] != 0 and self.show_warning("lin_skoroct") == 0: return
                    if self.var_dict["diam_vnutr"] != 0 and self.show_warning("diam_vnutr") == 0: return
                    self.var_dict["lin_skoroct"] = math.pi * self.var_dict["diam_nar"] * self.var_dict["chastota"] / (60000)
                self.var_dict["diam_vnutr"] = self.var_dict["diam_nar"] - 2 * t
        else:
            if (self.var_dict["chastota"] != 0 and self.var_dict["lin_skoroct"] == 0) or \
                    (self.var_dict["chastota"] == 0 and self.var_dict["lin_skoroct"] != 0):
                if self.var_dict["diam_nar"] != 0 and self.var_dict["diam_vnutr"] != 0:
                    t = self.var_dict["diam_nar"] - self.var_dict["diam_vnutr"]  # Толщина стенки через разность диаметров
                    self.var_dict["davlenie"] = math.log2(t / (2 * 4.8)) / 0.0161
                else:
                    if self.var_dict["diam_nar"] == 0:
                        self.show_error("davlenie", 2, "diam_nar")
                        return
                    if self.var_dict["diam_vnutr"] == 0:
                        self.show_error("davlenie", 1, "diam_vnutr")
                        return
                if self.var_dict["lin_skoroct"] == 0:
                    self.var_dict["lin_skoroct"] = math.pi * self.var_dict["diam_nar"] * self.var_dict["chastota"] / (60000)
                else:
                    self.var_dict["chastota"] = 60000 * self.var_dict["lin_skoroct"] / (math.pi * self.var_dict["diam_nar"])
            else:
                if self.var_dict["diam_vnutr"] != 0:
                    if self.var_dict["diam_nar"] == 0:
                        self.var_dict["diam_nar"] = 60000 * self.var_dict["lin_skoroct"] / (math.pi * self.var_dict["chastota"])
                    else:
                        if self.show_warning("lin_skoroct") == 0: return
                        self.var_dict["lin_skoroct"] = math.pi * self.var_dict["diam_nar"] * self.var_dict["chastota"] / (60000)
                    t = self.var_dict["diam_nar"] - self.var_dict["diam_vnutr"]  # Толщина стенки через разность диаметров
                    if t > 0: self.var_dict["davlenie"] = math.log2(t / (2 * 4.8)) / 0.0161
                    else: self.var_dict["davlenie"] = 0
                else:
                    self.show_error("davlenie", 1, "diam_vnutr")
                    return
        if self.var_dict["sheroh"] != 0: self.var_dict["trenie_uplotn"] = 0.15 * math.log2(self.var_dict["sheroh"]) + 0.7
        else: self.var_dict["sheroh"] = math.exp((self.var_dict["trenie_uplotn"] - 0.7) / 0.15)

        # Рассчет остальных параметров
        self.var_dict["diam_priv"] = self.var_dict["diam_vnutr"] / self.var_dict["diam_nar"]
        self.var_dict["dlina_priv"] = self.var_dict["dlina_otv"] / self.var_dict["dlina_uplotn"]
        self.var_dict["rashod_vody"] = 3500 * self.var_dict["trenie_uplotn"] \
                        * math.pow(self.var_dict["lin_skoroct"], 1.418) * math.pow(self.var_dict["davlenie"], 0.843) \
                        * math.pow(self.var_dict["nach_temp"], 0.253) / math.pow(self.var_dict["konech_temp"], 1.282)
        coefficient = (2 * math.pi * self.var_dict["diam_nar"] * self.var_dict["dlina_uplotn"]) / 100000
        self.var_dict["moshnoct_tepl"] = coefficient * 4.25 * math.pow(self.var_dict["lin_skoroct"], 0.576) \
                        * math.pow(self.var_dict["trenie_uplotn"], 0.876) * math.pow(self.var_dict["davlenie"], 0.783)
        self.var_dict["temp_uplotn_n_P"] = 3 * math.pow(self.var_dict["chastota"], 0.514) \
                                             * math.pow(self.var_dict["davlenie"], 0.639)
        self.var_dict["temp_uplotn_Kst_Kupl"] = 6722 * math.pow(self.var_dict["tepl_uplotn"], 0.0027) \
                                             / math.pow(self.var_dict["tepl_stali"], 0.96)
        self.var_dict["temp_uplotn_V_P_Dpr_Lpr"] = \
                    130 * math.pow(self.var_dict["davlenie"], 0.59) * math.pow(self.var_dict["lin_skoroct"], 0.445) \
                        * math.pow(self.var_dict["diam_priv"], 0.12) * math.pow(self.var_dict["dlina_priv"], 1.08)

        # Выгрузка значений в новое окно и его вывод
        self.new_window.set_value_and_change_enable(self.var_dict)  # self.new_window.move(1052, 0)
        self.new_window.show()


# ОКНО "ПОЛУЧЕННЫЕ ЗНАЧЕНИЯ"
class NewWindow(QMainWindow, Ui_NewWindow):
    # Конструктор класса
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window  # Сохранение ссылки на MainWindow
        self.setWindowIcon(QIcon('icons8-pipes-96.png'))  # Импорт и установка иконки
        QToolTip.setFont(QFont('Cambria', 10))  # Установка формата текста подсказок

        # Установка фокуса
        self.buttonBox.button(QDialogButtonBox.Ok).setFocus()
        self.setTabOrder(self.buttonBox.button(QDialogButtonBox.Ok), self.buttonBox.button(QDialogButtonBox.Save))
        for index, name in enumerate(list(self.main_window.var_dict.keys())):
            if index >= (len(list(self.main_window.var_dict.keys())) - 1): break
            element_prev = getattr(self, f"doubleSpinBox_{list(self.main_window.var_dict.keys())[index]}")
            element_next = getattr(self, f"doubleSpinBox_{list(self.main_window.var_dict.keys())[index + 1]}")
            self.setTabOrder(element_prev, element_next)

        # Подключение кнопок "OK" и "Save"
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(lambda: self.close())
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.save_results)

        # Создаем экземпляр диалогового окна
        self.save = Save(self)

    # Переопределение метода нажатия клавиш
    def keyPressEvent(self, event):
        # Клавиша "Enter"
        if event.key() == Qt.Key_Return:
            if self.focusWidget() == self.buttonBox.button(QDialogButtonBox.Ok) or \
                    self.focusWidget() == self.buttonBox.button(QDialogButtonBox.Save):
                self.focusWidget().click()
        # Клавиша "Esc"
        if event.key() == Qt.Key_Escape:
            self.close()

    # Метод для вывода значений в новое окно и установки подсказок
    def set_value_and_change_enable(self, values_dict):
        for name, value in values_dict.items():
            label = getattr(self, f"label_{name}")
            doubleSpinBox = getattr(self, f"doubleSpinBox_{name}")
            enable = getattr(self.main_window, f"doubleSpinBox_{name}").isEnabled()
            label.setEnabled(not enable)
            doubleSpinBox.setEnabled(not enable)
            getattr(self, f"doubleSpinBox_{name}").setValue(value)
            getattr(self, f"doubleSpinBox_{name}").setToolTip(str(round(value, 6)))  # Установка подсказок

    # Метод для сохранения результатов
    def save_results(self):
        # Преобразование словаря в DataFrame и сохранение DataFrame в эксель
        df = pd.DataFrame.from_dict(self.main_window.var_dict, orient='index', columns=['Значение'])
        df.to_excel('Data.xlsx', index_label='Параметр')
        # Вызов диалогового окна
        self.save.exec_()


# ОКНО "ПРЕДУПРЕЖДЕНИЕ"
class Warning(QDialog, Ui_Warning):
    # Конструктор класса
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window  # Сохранение ссылки на MainWindow
        self.setWindowIcon(QIcon('icons8-pipes-96.png'))  # Импорт и установка иконки


# ОКНО "ОШИБКА"
class Error(QDialog, Ui_Error):
    # Конструктор класса
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window  # Сохранение ссылки на MainWindow
        self.setWindowIcon(QIcon('icons8-pipes-96.png'))  # Импорт и установка иконки
        self.checkBox_0.clicked.connect(lambda: self.checkBox_0.setCheckState(QtCore.Qt.Checked))


# ОКНО "СОХРАНЕНИЕ"
class Save(QDialog, Ui_Save):
    # Конструктор класса
    def __init__(self, new_window):
        super().__init__()
        self.setupUi(self)
        self.new_window = new_window  # Сохранение ссылки на MainWindow
        self.setWindowIcon(QIcon('icons8-pipes-96.png'))  # Импорт и установка иконки


# ОКНО "ВЫВОД"
class Exit(QDialog, Ui_Exit):
    # Конструктор класса
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window  # Сохранение ссылки на MainWindow
        self.setWindowIcon(QIcon('icons8-pipes-96.png'))  # Импорт и установка иконки


# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
    app = QApplication([])
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    window = MainWindow()  # window.move(0, 0)
    window.show()
    app.exec_()


# СОЗДАНИЕ ИСПОЛНЯЕМОГО ФАЙЛА ".exe" (ввести команду в терминал)
""" pyinstaller --onefile --noconsole Hydro.py """