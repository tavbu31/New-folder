from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QSpinBox,
                               QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QHBoxLayout, QFileDialog)
from About import AboutWindow


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''

        self.about_window = AboutWindow()

        self.setWindowTitle('Grades Correction')

        layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        self.open_csv_button = QPushButton()
        self.open_csv_button.clicked.connect(self.choose_csv_file)
        top_layout.addWidget(self.open_csv_button)
        top_layout.addStretch()
        layout.addLayout(top_layout)

        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(['____', '____', '____'])
        layout.addWidget(self.table)

        controls_layout = QHBoxLayout()
        self.number_input = QSpinBox()
        self.number_input.setRange(0, 100)
        self.number_input.lineEdit().returnPressed.connect(self.number_enter_pressed)
        controls_layout.addWidget(self.number_input)

        self.update_file_button = QPushButton('Update File')
        self.update_file_button.clicked.connect(self.update_file)
        controls_layout.addWidget(self.update_file_button)

        self.about_button = QPushButton('About')
        self.about_button.clicked.connect(self.show_about)
        controls_layout.addWidget(self.about_button)

        layout.addLayout(controls_layout)

    def choose_csv_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Choose CSV File', '', 'CSV Files (*.csv)')
        if file_name:
            self.process_csv_file(file_name)

    def process_csv_file(self, file_name):
        pass

    def update_table(self, list1, list2, list3):
        for row in range(50):
            values = (
                list1[row] if row < len(list1) else '',
                list2[row] if row < len(list2) else '',
                list3[row] if row < len(list3) else '',
            )
            for column, value in enumerate(values):
                self.table.setItem(row, column, QTableWidgetItem(str(value)))

    def number_enter_pressed(self):
        pass

    def update_file(self):
        pass

    def show_about(self):
        self.about_window.show()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()