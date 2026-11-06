import os
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QStatusBar,
)


class Statistic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Статистика чисел из файла")
        self.setMinimumWidth(420)
        central_widget = QWidget()
        layout = QFormLayout(central_widget)
        self.filenameEdit = QLineEdit()
        self.filenameEdit.setObjectName("filenameEdit")
        self.filenameEdit.setPlaceholderText("Например, input_1_KDO.txt")
        self.button = QPushButton("Рассчитать")
        self.button.setObjectName("button")
        self.button.clicked.connect(self.calculate_statistics)
        self.minEdit = QLineEdit()
        self.minEdit.setObjectName("minEdit")
        self.minEdit.setReadOnly(True)
        self.maxEdit = QLineEdit()
        self.maxEdit.setObjectName("maxEdit")
        self.maxEdit.setReadOnly(True)
        self.avgEdit = QLineEdit()
        self.avgEdit.setObjectName("avgEdit")
        self.avgEdit.setReadOnly(True)
        layout.addRow("Имя файла:", self.filenameEdit)
        layout.addRow(self.button)
        layout.addRow("Минимальное значение:", self.minEdit)
        layout.addRow("Максимальное значение:", self.maxEdit)
        layout.addRow("Среднее значение:", self.avgEdit)
        self.setCentralWidget(central_widget)
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("Введите имя файла")
    def clear_outputs(self):
        self.minEdit.clear()
        self.maxEdit.clear()
        self.avgEdit.clear()

    def calculate_statistics(self):
        self.clear_outputs()
        filename = self.filenameEdit.text().strip()

        try:
            with open(filename, "r", encoding="utf-8") as input_file:
                content = input_file.read()
        except FileNotFoundError:
            self.statusBar().showMessage("Файл не существует")
            return
        except UnicodeDecodeError:
            self.statusBar().showMessage("Файл содержит некорректные данные")
            return

        if not content.strip():
            self.statusBar().showMessage("Файл пуст")
            return

        try:
            numbers = [int(value) for value in content.split()]
        except ValueError:
            self.statusBar().showMessage("Файл содержит некорректные данные")
            return

        minimum = min(numbers)
        maximum = max(numbers)
        average = sum(numbers) / len(numbers)

        try:
            with open("out_KDO.txt", "w", encoding="utf-8") as output_file:
                output_file.write(f"Максимальное значение = {maximum}\n")
                output_file.write(f"Минимальное значение = {minimum}\n")
                output_file.write(f"Среднее значение = {average:.2f}\n")
        except OSError:
            self.statusBar().showMessage("Не удалось сохранить файл out_KDO.txt")
            return

        self.minEdit.setText(str(minimum))
        self.maxEdit.setText(str(maximum))
        self.avgEdit.setText(f"{average:.2f}")
        self.statusBar().showMessage("Данные успешно обработаны. Результат сохранён в out_KDO.txt")


def create_test_files():
    test_files = {
        "input_1_KDO.txt": "\n".join(str(number) for number in range(1, 101)),
        "input_2_KDO.txt": "\n".join(f"{number}.5" for number in range(1, 21)),
        "input_3_KDO.txt": "",
    }

    for filename, content in test_files.items():
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as test_file:
                test_file.write(content)


if __name__ == "__main__":
    create_test_files()
    app = QApplication(sys.argv)
    window = Statistic()
    window.show()
    sys.exit(app.exec())
