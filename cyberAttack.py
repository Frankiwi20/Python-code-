# this is where the bug im creating will go, this bug will attempt to change the status of ph level, soil type and basically mess up the program
from soil import Soil
import random
class Bug:
    def __init__(self):
        self.active = False

    def activate_first_bug(self):
        self.active = True

    def deactivate_first_bug(self):
        self.active = False

    def introduce_bug_to_soil(self, soil_instance):
        if self.active:
            # setting wrong ph level
            soil_instance.set_ph_level(0)

    def introduce_bug_to_crops(self, crops_instance):
        if self.active:
            crops_instance.set_crop_ph('potato')




