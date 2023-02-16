from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout, QPlainTextEdit
import sys

from logic import convert, Layouts

style_text_field = """
QPlainTextEdit {
    border: 1px solid rgb(37, 39, 49);
    border-radius: 5px;
    padding: 10px;
    background-color: rgb(255, 255, 255);
    font: italic;
    color: grey;
}

QPlainTextEdit:hover {
    border: 2px solid rgb(48, 50, 62);
}

QPushButton {
    border: 1px solid rgb(230, 230, 230);
    background-color: rgb(255, 255, 255);
    border-width: 2px;
    border-radius: 10px;
    font: bold 14px;
    min-width: 10em;
    padding: 10px;
}

QPushButton:hover {
    border: 2px solid rgb(100, 107, 99);
}

QPushButton:pressed {
    background-color: rgb(230, 230, 230);
}
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.language = 'ru'

        self.setWindowTitle('Translator')
        self.setStyleSheet(style_text_field)

        layout = QVBoxLayout()
        layout_language = QHBoxLayout()
        layout_text = QHBoxLayout()
        layout_button = QHBoxLayout()

        """Кнопка смены языка"""
        self.button_language = QPushButton(self.language)
        self.button_language.clicked.connect(self.change_language)
        layout.addWidget(self.button_language)

        """Поле с исходным текстом"""
        self.input_field = QPlainTextEdit(self)

        """Поле с переведенным текстом"""
        self.output_field = QPlainTextEdit(self)
        self.output_field.setReadOnly(True)
        self.output_field.setDisabled(True)


        layout_text.addWidget(self.input_field)
        layout_text.addWidget(self.output_field)

        layout.addLayout(layout_language)
        layout.addLayout(layout_text)
        layout.addLayout(layout_button)


        """Кнопка перевода"""
        self.button_translate = QPushButton('Translate')
        self.button_translate.clicked.connect(self.getText)
        layout_button.addWidget(self.button_translate)
 
        """Кнопка очистки"""
        self.button_clear = QPushButton("Clear")
        self.button_clear.clicked.connect(self.input_field.clear)
        self.button_clear.clicked.connect(self.output_field.clear)
        layout_button.addWidget(self.button_clear)

        """Отрисовка"""
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    """Получение текста из формы"""
    def getText(self):
        text = self.input_field.toPlainText()
        if self.language == 'ru':
            translate_text = convert(text, Layouts.EN)
        else:
            translate_text = convert(text, Layouts.RU)
        self.output_field.setPlainText(translate_text)

    def change_language(self):
        if(self.language == 'ru'):
            self.language = 'en'
        else:
            self.language = 'ru'
        self.button_language.setText(self.language)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()