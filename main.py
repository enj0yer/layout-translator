import sys

from PyQt6.QtWidgets import QApplication, QWidget

from logic import convert, Languages

app = QApplication(sys.argv)
window = QWidget()
window.show()
app.exec()

print(convert("Руддщб цщкдв!!!", Languages.RU))

print(convert("Ghbdtn? vbh!!!", Languages.EN))