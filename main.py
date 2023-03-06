from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout, QPlainTextEdit
from PyQt6.QtGui import QFontDatabase, QFont, QShortcut, QKeySequence
import sys

from logic import convert, Languages

style_text_field = """
MainWindow {
    border-image: url("./image/background.jpg");
    background-color: rgb(250, 240, 0);
}

QPlainTextEdit {
    border-radius: 5px;
    padding: 10px;
    background-color: rgba(0, 255, 210, 0.5);
    font: bold 24px;
}

QPlainTextEdit:hover {
    border: 1px solid rgb(48, 50, 62);
    font: bold 24px;
}

QPushButton {
    border: 1px solid rgb(0, 90, 97);
    background-color: rgb(0, 0, 0);
    border-width: 2px;
    border-radius: 10px;
    font: bold 24px;
    min-width: 10em;
    padding: 10px;
    color: rgb(0, 90, 97);
}

QPushButton:hover {
    border: 2.5px solid rgb(0, 90, 97);
}

QPushButton:pressed {
    background-color: rgb(230, 230, 230);
}
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.language = 'Английский -> Русский'

        """Получаем шрифт"""
        self.families = QFontDatabase.applicationFontFamilies(fontfamily_id)

        self.setWindowTitle('Translator')
        self.setStyleSheet(style_text_field)

        layout = QVBoxLayout()
        layout_language = QHBoxLayout()
        layout_text = QHBoxLayout()
        layout_button = QHBoxLayout()

        """Кнопка смены языка"""
        self.button_language = QPushButton(self.language)
        self.button_language.clicked.connect(self.change_language)
        self.hotkey_change_language = QShortcut(QKeySequence('Ctrl+r'), self)
        self.hotkey_change_language.activated.connect(self.change_language)
        self.button_language.setFont(QFont(self.families[0]))
        layout_language.addWidget(self.button_language)

        """Поле с исходным текстом"""
        self.input_field = QPlainTextEdit(self)
        self.input_field.setFont(QFont(self.families[0]))
        self.input_field.textChanged.connect(self.getText)
        

        """Поле с переведенным текстом"""
        self.output_field = QPlainTextEdit(self)
        self.output_field.setFont(QFont(self.families[0]))
        self.output_field.setReadOnly(True)


        layout_text.addWidget(self.input_field)
        layout_text.addWidget(self.output_field)

        layout.addLayout(layout_language)
        layout.addLayout(layout_text)
        layout.addLayout(layout_button)
        
 
        """Кнопка очистки"""
        self.hotkey_clear = QShortcut(QKeySequence('Alt+Delete'), self)
        self.hotkey_clear.activated.connect(self.clear_field)

        self.button_clear = QPushButton("Clear")
        self.button_clear.clicked.connect(self.clear_field)
        self.button_clear.setFont(QFont(self.families[0]))
        layout_button.addWidget(self.button_clear)

        """Отрисовка"""
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    """Получение текста из формы"""
    def getText(self):
        text = self.input_field.toPlainText()
        if self.language == 'Английский -> Русский':
            translate_text = convert(text, Languages.EN)
        else:
            translate_text = convert(text, Languages.RU)
        self.output_field.setPlainText(translate_text)

    def change_language(self):
        if(self.language == 'Английский -> Русский'):
            self.language = 'Русский -> Английский'
        else:
            self.language = 'Английский -> Русский'
        self.button_language.setText(self.language)
        self.getText()

    def clear_field(self):
        self.input_field.clear()
        self.output_field.clear()

app = QApplication(sys.argv)
fontfamily_id = QFontDatabase.addApplicationFont('./crystal/crystal.otf')
window = MainWindow()
window.show()
app.exec()

