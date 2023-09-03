from PyQt5.QtWidgets import QWidget , QApplication , QLabel , QPushButton

app = QApplication([])
btn = QPushButton()
window = QWidget()
window.setWindowTitle("My dear application!")
window.show()

app.exec()