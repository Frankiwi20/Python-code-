from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QTextEdit
from PySide2.QtCore import Qt
from weather import WeatherData
from cyberAttack import Bug
import threading


class MyApplication(QWidget):
    def __init__(self, soil_instance, crops_instance, sensors_instance, bug_instance, security_instance, weather_instance):
        super().__init__()
        self.sensors_instance = sensors_instance
        self.soil_instance = soil_instance
        self.crops_instance = crops_instance
        self.bug_instance = bug_instance
        self.security_instance = security_instance
        self.weather_instance = WeatherData('87596aa1a39a1925e6cf81e1c866d9ec')  # API key
        self.initializeUI()

    def initializeUI(self):
        self.resize(900, 600)
        self.setWindowTitle('Smart Farming Application')

        # General Styling
        self.setStyleSheet("""
                QWidget {
                    font-size: 18px;  # Increased font size for better readability
                }
                QPushButton {
                    background-color: #A3C1DA;
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: beige;
                    font: bold 18px;  # Increased font size
                    min-width: 10em;
                    padding: 10px;  # Increased padding for larger buttons
                }
                QPushButton:hover {
                    background-color: #507DBC;
                    border-style: inset;
                }
                QLabel {
                    color: #3E606F;
                    font-size: 18px;  # Increased font size
                }
                QComboBox, QLineEdit, QTextEdit {
                    font-size: 16px;  # Adjust font size as needed
                    min-height: 30px;  # Increase height for QLineEdit and QComboBox
                    padding: 5px;  # Adjust padding for better visual
                }
                QTextEdit {
                    min-height: 100px;  # Specific adjustment for QTextEdit
                }
            """)

        layout = QVBoxLayout()

        # Button for toggling the bug simulation
       # bug_button = QPushButton('Toggle Bug')
        #bug_button.clicked.connect(self.toggleBug)
        #layout.addWidget(bug_button, alignment=Qt.AlignCenter)

        welcome_label = QLabel('Welcome to the Smart Farming System')
        layout.addWidget(welcome_label, alignment=Qt.AlignCenter)

        self.ph_label = QLabel(f'Soil pH Level: {self.soil_instance.get_ph_level()}')
        layout.addWidget(self.ph_label, alignment=Qt.AlignCenter)

        self.sensors_label = QLabel(
            f'Your sensor readings: 1.) {self.sensors_instance.get_first_sensor()}, 2.) {self.sensors_instance.get_second_sensor()}')
        layout.addWidget(self.sensors_label, alignment=Qt.AlignCenter)

        self.crop_selection = QComboBox()
        self.crop_selection.addItem('Select Crop')
        self.crop_selection.addItems(['Corn', 'Tomato', 'Wheat', 'Potato'])
        self.crop_selection.currentIndexChanged.connect(self.onCropSelectionChange)
        layout.addWidget(self.crop_selection, alignment=Qt.AlignCenter)

        update_button = QPushButton('Update Soil Health')
        update_button.clicked.connect(self.onUpdateButtonClick)
        layout.addWidget(update_button, alignment=Qt.AlignCenter)

        self.data_Tampering_Button = QPushButton('Simulate Data Tampering')
        self.data_Tampering_Button.clicked.connect(self.toggleDataTampering)
        layout.addWidget(self.data_Tampering_Button, alignment=Qt.AlignCenter)

        self.dos_Attack_Button = QPushButton('Simulate Dos Attack')
        self.dos_Attack_Button.clicked.connect(self.simulateDosAttack)
        layout.addWidget(self.dos_Attack_Button, alignment=Qt.AlignCenter)
        # Add weather widgets to the layout
        self.weather_input = QLineEdit()
        self.weather_input.setPlaceholderText("Enter city name for weather")
        layout.addWidget(self.weather_input)  # Add directly to the layout

        get_weather_btn = QPushButton("Get Weather")
        get_weather_btn.clicked.connect(self.display_weather)
        layout.addWidget(get_weather_btn)  # Add directly to the layout

        self.weather_display = QTextEdit()
        self.weather_display.setReadOnly(True)
        layout.addWidget(self.weather_display)  # Add directly to the layout

        #self.layout().addWidget(self.weather_input)
        #self.layout().addWidget(get_weather_btn)
        #self.layout().addWidget(self.weather_display)

        self.setLayout(layout)

    def display_weather(self):
        city = self.weather_input.text()
        weather_info = self.weather_instance.get_weather(city)
        self.weather_display.setText(weather_info)

    def onCropSelectionChange(self, index):
        crop = self.crop_selection.currentText()
        if crop != 'Select Crop':
            print(f"Selected Crop: {crop}")

    def onUpdateButtonClick(self):
        crop = self.crop_selection.currentText()
        if crop != 'Select Crop':
            self.crops_instance.set_crop_ph(crop)
            self.ph_label.setText(f'Soil pH Level: {self.soil_instance.get_ph_level()}')
            print("Soil health updated based on crop selection.")

    def toggleDataTampering(self):
        if self.security_instance.active:
            self.security_instance.stop()
            print("Data tampering stopped.")
        else:
            self.security_instance.start()
            print("Data tampering started.")

    def simulateDosAttack(self):
        print("Simulating DoS attack...")
        # Assuming simulate_dos_attack is a class method; otherwise, adjust as needed.
        threading.Thread(target=self.security_instance.simulate_dos_attack).start()
