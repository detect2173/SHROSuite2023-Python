import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the size and position of the main window
        self.setGeometry(350, 100, 1210, 755)

        # Create a tab control
        self.tab_widget = QTabWidget(self)

        # Set the size of the tab control to fill the main window
        self.tab_widget.setGeometry(0, 0, 1210, 755)

        # Set the window title
        self.setWindowTitle("SHRO SUITE v3 - 2023")

        # Set the font properties of the tab names
        font = QFont("Segoe UI", 12)
        self.tab_widget.setFont(font)

        # Set the position of the tabs to the left side
        #self.tab_widget.setTabPosition(QTabWidget.West)

        # Add 10 tabs to the tab control
        tab_names = ["Welcome", "Wisely Request", "Receipt Creator", "Student Roster",
                     "Inventory Control", "FFB Documents", "Staff Directory", "Prize Vault",
                     "SHRO Training", "Student Fine"]
        for name in tab_names:
            tab = QWidget()
            if name == "Welcome":
                # Create a label with the text "WELCOME TO:"
                label1 = QLabel("WELCOME TO:")
                label1.setAlignment(Qt.AlignCenter)
                font1 = QFont("Segoe UI Black", 48, QFont.Bold)
                label1.setFont(font1)

                # Set the color of the text to red using the style sheet
                label1.setStyleSheet("color: red")

                # Create another label with the text "SHRO SUITE 2023"
                label2 = QLabel("SHRO SUITE 2023")
                label2.setAlignment(Qt.AlignCenter)
                font2 = QFont("Segoe UI Black", 72, QFont.Bold)
                label2.setFont(font2)

                # Add the labels to a vertical layout
                layout = QVBoxLayout(tab)
                layout.addWidget(label1)
                layout.addWidget(label2)

                # Load the image and create a label to display it
                pixmap = QPixmap("SS3.png")
                label3 = QLabel()
                label3.setPixmap(pixmap)
                label3.setAlignment(Qt.AlignCenter)

                # Add spacing between the image and the labels
                layout.addSpacing(70)

                # Create the two labels for Current OBS and enrollment count
                obs_label = QLabel("Current OBS:")
                obs_label.setAlignment(Qt.AlignRight)
                font3 = QFont("Segoe UI Black", 28, QFont.Bold)
                obs_label.setFont(font3)

                enrollment_label = QLabel("100")
                enrollment_label.setAlignment(Qt.AlignLeft)
                font4 = QFont("Segoe UI Black", 28, QFont.Bold)
                enrollment_label.setFont(font4)
                enrollment_label.setStyleSheet("color: red")

                # Add the labels to a horizontal layout
                layout2 = QHBoxLayout()
                layout2.addWidget(obs_label)
                layout2.addWidget(enrollment_label)
                layout2.setAlignment(Qt.AlignCenter)

                # Add the image label and horizontal layout to the vertical layout
                layout.addWidget(label3)
                layout.addLayout(layout2)
                layout.setAlignment(Qt.AlignCenter)

            self.tab_widget.addTab(tab, name)

        # Set the tab control as the central widget for the main window
        self.setCentralWidget(self.tab_widget)

        # Set the background color of the selected tab to blue
        self.tab_widget.setStyleSheet("""
        QTabBar::tab:selected {{
            background-color: blue;
        }}
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())