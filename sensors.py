
class Sensors:
    def __init__(self):
        self.sensor1 ='Good'
        self.sensor2 = 'Bad'

    def set_first_sensor(self, sensor1):
        self.sensor1 = sensor1

    def get_first_sensor(self):
        return self.sensor1


    def set_second_sensor(self,sensor2):
        self.sensor2 = sensor2

    def get_second_sensor(self):
        return self.sensor2