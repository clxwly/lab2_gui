"""
Лабораторная работа 2. Вариант 1: простое окно с кнопками.
Окно "Медиатек" с тремя кнопками; при нажатии выводится сообщение в консоль.
"""

import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget
)


class MainWindow(QMainWindow):
    """Главное окно приложения "Медиатек"."""

    def __init__(self):
        super().__init__()
        # Заголовок и размеры окна согласно заданию варианта 1
        self.setWindowTitle("Медиатек")
        self.setGeometry(100, 100, 400, 250)

        self.init_ui()

    def init_ui(self):
        """Инициализация пользовательского интерфейса."""
        # Центральный виджет, на котором располагаются элементы
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Вертикальный макет: кнопки располагаются друг под другом
        layout = QVBoxLayout()

        # Три кнопки согласно заданию
        self.open_button = QPushButton("Открыть файл")
        self.save_button = QPushButton("Сохранить")
        self.exit_button = QPushButton("Выход")

        # Подключаем сигналы clicked к слотам-обработчикам
        self.open_button.clicked.connect(self.on_open_click)
        self.save_button.clicked.connect(self.on_save_click)
        self.exit_button.clicked.connect(self.on_exit_click)

        # Добавляем кнопки в макет
        layout.addWidget(self.open_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.exit_button)

        # Устанавливаем макет на центральный виджет
        central_widget.setLayout(layout)

    def on_open_click(self):
        """Слот: нажата кнопка "Открыть файл"."""
        print("Нажата кнопка: Открыть файл")

    def on_save_click(self):
        """Слот: нажата кнопка "Сохранить"."""
        print("Нажата кнопка: Сохранить")

    def on_exit_click(self):
        """Слот: нажата кнопка "Выход" - выводим сообщение и закрываем окно."""
        print("Нажата кнопка: Выход")
        self.close()


def main():
    """Основная функция запуска приложения."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()