from PyQt5.QtWidgets import QWidget , QApplication , QLabel

app = QApplication([])

window = QWidget()
window.setWindowTitle("My dear application!")
window.show()

app.exec()