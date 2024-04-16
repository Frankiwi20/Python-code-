class Soil:
    def __init__(self):
        self.soil_type = ''
        self.ph_level = 7  # Default realistic pH level

    def set_ph_level(self, ph):
        self.ph_level = ph
        print(f"pH level set to: {ph}")

    def get_ph_level(self):
        return self.ph_level

    def soil_health(self):
        if self.ph_level < 6 or self.ph_level > 7.5:
            health = 'Warning'
        else:
            health = 'Good'
        print(health)
        return health
