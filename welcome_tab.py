from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QStackedLayout, QFrame
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt


class WelcomeTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the stylesheet for the tab
        self.setStyleSheet('background-color: #f2f2f2;')
        # Create a stacked layout to hold the different elements of the welcome tab
        stacked_layout = QStackedLayout()

        # Create a frame to hold the welcome message and logo
        frame = QFrame()
        #frame.setStyleSheet("background-image: url(bg_shro.png);")

        # Create a layout to hold the welcome message and logo
        layout = QVBoxLayout(frame)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a label with the text "WELCOME TO:"
        label1 = QLabel("WELCOME TO:")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font1 = QFont("Segoe UI Black", 48, weight=QFont.Weight.Bold)
        label1.setFont(font1)
        #label1.setStyleSheet("background-image: url(bg_shro.png); opacity: 0;")

        # Create another label with the text "SHRO SUITE 2023"
        label2 = QLabel("SHRO SUITE 2023")
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font2 = QFont("Segoe UI Black", 72, weight=QFont.Weight.Bold)
        label2.setFont(font2)
        #label2.setStyleSheet("background-image: url(bg_shro.png); opacity: 0;")

        # Set the color of the text to red using the style sheet
        label2.setStyleSheet("color: red")

        # Load the image and create a label to display it
        pixmap = QPixmap("SS3.png")
        label3 = QLabel()
        label3.setPixmap(pixmap)
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(30)
        #label3.setStyleSheet("background-image: url(bg_shro.png); opacity: 0;")

        # Create the two labels for Current OBS and enrollment count
        obs_label = QLabel("Current OBS:")
        obs_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        font3 = QFont("Segoe UI Black", 28, weight=QFont.Weight.Bold)
        obs_label.setFont(font3)
        #obs_label.setStyleSheet("background-image: url(bg_shro.png); opacity: 0;")

        enrollment_label = QLabel("100")
        enrollment_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font4 = QFont("Segoe UI Black", 28, weight=QFont.Weight.Bold)
        enrollment_label.setFont(font4)
        enrollment_label.setStyleSheet("color: red")
        #enrollment_label.setStyleSheet("background-image: url(bg_shro.png); opacity: 0;")

        # Add the labels to a horizontal layout
        layout2 = QHBoxLayout()
        layout2.addWidget(obs_label)
        layout2.addWidget(enrollment_label)
        layout2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the labels and image label to the layout
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addLayout(layout2)

        # Add the layout to the stacked layout
        stacked_layout.addWidget(frame)

        # Set the layout of the WelcomeTab to the stacked layout
        self.setLayout(stacked_layout)