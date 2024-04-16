import sys
from PySide2.QtWidgets import QApplication
from GUI import MyApplication  # Adjust import path as needed
from soil import Soil
from crops import Crops
from sensors import Sensors
from cyberAttack import Bug
from Security import DataTamperSimulation
from weather import WeatherData  # Make sure to import WeatherData

def main():
    app = QApplication(sys.argv)

    # Initialize instances of the classes
    soil_instance = Soil()
    crops_instance = Crops(soil_instance)
    sensors_instance = Sensors()
    bug_instance = Bug()
    security_instance = DataTamperSimulation(sensors_instance)
    weather_instance = WeatherData('87596aa1a39a1925e6cf81e1c866d9ec')  # Add your API key

    # Initialize MyApplication with all instances
    window = MyApplication(soil_instance, crops_instance, sensors_instance, bug_instance, security_instance, weather_instance)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
