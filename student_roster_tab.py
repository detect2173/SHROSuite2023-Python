from PyQt5.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel

class StudentRosterTab(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create a vertical layout to hold the other widgets
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Create the title container and set its properties
        title_container = QWidget(self)
        title_container.setFixedHeight(70)
        title_container.setAutoFillBackground(True)
        title_container.setStyleSheet("border: 3px solid black;")

        # Set the background color of the title container to white
        palette = title_container.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        title_container.setPalette(palette)

        # Add the title container to the main layout
        layout.addWidget(title_container)

        # Create the form fields container and set its properties
        form_container = QWidget(self)
        form_container.setAutoFillBackground(True)
        form_container.setStyleSheet("border: 3px solid black;")
        form_container.setGeometry(0, title_container.height(), self.width()*0.7, 355)

        # Set the background color of the form fields container to white
        palette = form_container.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        form_container.setPalette(palette)

        # Add the form fields container to the main layout
        layout.addWidget(form_container)

        self.setLayout(layout)
