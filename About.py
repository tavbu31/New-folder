from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('About Me')
        self.setGeometry(700, 100, 520, 300)
        self.setStyleSheet('background-color: #f4f6fb')

        # --- תמונה ---
        self.my_picture = QLabel(self)
        self.my_picture.setGeometry(25, 25, 170, 220)
        self.my_picture.setStyleSheet('border: 2px solid #3d5a99; border-radius: 10px; background-color: white; color: #1f2d4d')
        image = QPixmap('my_photo.jpg')
        if image.isNull():
            self.my_picture.setText('Image not found')
        else:
            image = image.scaled(166, 216, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.my_picture.setPixmap(image)

        # --- שם ---
        self.name = QLabel('Tav burkush', self)
        self.name.setGeometry(220, 35, 280, 40)
        self.name.setStyleSheet('font-size: 26px; font-weight: bold; color: #1f2d4d')

        # --- תיאור ---
        self.role = QLabel('Engineering Student', self)
        self.role.setGeometry(220, 80, 280, 30)
        self.role.setStyleSheet('font-size: 15px; color: #5b6478')

        # --- אימייל ---
        self.email = QLabel('Email: Tav745@gmail.com', self)
        self.email.setGeometry(220, 130, 280, 30)
        self.email.setStyleSheet('font-size: 15px; color: #1f2d4d')

        # --- קישור LinkedIn ---
        self.linkedin = QLabel('<a href="https://www.linkedin.com/in/tav-burkush-466930179" style="color: #1a5fd1">LinkedIn profile</a>', self)
        self.linkedin.setGeometry(220, 170, 280, 30)
        self.linkedin.setStyleSheet('font-size: 15px')
        self.linkedin.setOpenExternalLinks(True)


if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()