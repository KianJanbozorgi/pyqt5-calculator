from PyQt5.QtWidgets import QWidget , QApplication , QLabel , QPushButton

app = QApplication([])

window = QWidget()

btn = QPushButton("click me!" , parent=window)
window.setWindowTitle("My dear application!")
window.show()

app.exec()