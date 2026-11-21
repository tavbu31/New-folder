from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('About Me')
        self.setGeometry(700, 100, 520, 300)
        self.setObjectName('aboutWindow')

        # --- תמונה ---
        self.my_picture = QLabel(self)
        self.my_picture.setGeometry(25, 25, 170, 220)
        self.my_picture.setObjectName('pictureLabel')
        image = QPixmap('my_photo.jpg')
        if image.isNull():
            self.my_picture.setText('Image not found')
        else:
            image = image.scaled(166, 216, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.my_picture.setPixmap(image)

        # --- שם ---
        self.name = QLabel('Tav burkush', self)
        self.name.setGeometry(220, 35, 280, 40)
        self.name.setObjectName('nameLabel')

        # --- תיאור ---
        self.role = QLabel('Engineering Student', self)
        self.role.setGeometry(220, 80, 280, 30)
        self.role.setObjectName('roleLabel')

        # --- אימייל ---
        self.email = QLabel('Email: Tav745@gmail.com', self)
        self.email.setGeometry(220, 130, 280, 30)
        self.email.setObjectName('emailLabel')

        # --- קישור LinkedIn ---
        self.linkedin = QLabel('<a href="https://www.linkedin.com/in/tav-burkush-466930179">LinkedIn profile</a>', self)
        self.linkedin.setGeometry(220, 170, 280, 30)
        self.linkedin.setObjectName('linkedinLabel')
        self.linkedin.setOpenExternalLinks(True)


if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()