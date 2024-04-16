from soil import Soil


class Crops:
    def __init__(self, soil_instance):
        self.soil = soil_instance
        self.corn_ph = 6.0
        self.tomato_ph = 6.5
        self.wheat_ph = 6.5
        self.potato_ph = 5.4

    def set_crop_ph(self, crop):
        if crop.lower() == 'corn':
            self.soil.set_ph_level(self.corn_ph)
        elif crop.lower() == 'tomato':
            self.soil.set_ph_level(self.tomato_ph)
        elif crop.lower() == 'wheat':
            self.soil.set_ph_level(self.wheat_ph)
        elif crop.lower() == 'potato':
            self.soil.set_ph_level(self.potato_ph)
        else:
            print("Unknown crop")

        # Optionally check soil health status after setting the pH
        self.soil.soil_health()
