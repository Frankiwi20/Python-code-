import random
import threading
import time

class DataTamperSimulation:
    def __init__(self, sensors_instance):
        self.sensors_instance = sensors_instance
        self.active = False

    def start(self):
        self.active = True
        thread = threading.Thread(target=self.run)
        thread.start()

    def stop(self):
        self.active = False

    def run(self):
        while self.active:
            # Randomly change sensor data at intervals
            self.sensors_instance.set_first_sensor(random.choice(['Good', 'Bad', 'Unknown']))
           # self.sensors_instance.set_second_sensor(random.choice(['Good', 'Bad', 'Unknown']))
            time.sleep(random.randint(1, 5))  # Random sleep to simulate unpredictable behavior

    @staticmethod
    def simulate_dos_attack(effect_duration=100):
        print(f"Starting DoS simulation for {effect_duration} seconds...")
        end_time = time.time() + effect_duration
        while time.time() < end_time:
            # Simulating heavy computation to slow down the system
            [x ** 2 for x in range(10000)]
            time.sleep(0.1)  # Small sleep to yield control and simulate delay
        print("DoS simulation ended.")
