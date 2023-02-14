import sys

from PyQt6.QtWidgets import QApplication, QWidget

from logic import convert, Layouts

app = QApplication(sys.argv)
window = QWidget()
window.show()
app.exec()

print(convert("Руддщб цщкдв!!!", Layouts.EN))

print(convert("Ghbdtn? vbh!!!", Layouts.RU))