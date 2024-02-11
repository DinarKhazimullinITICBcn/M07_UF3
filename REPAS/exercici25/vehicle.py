class vehicle:
    def __init__(self, marca, model, portes, rodes, motor, color) :
        self.marca = marca
        self.model = model
        self.portes = portes
        self.rodes = rodes
        self.motor = motor
        self.color = color
    def get_marca(self):
        return self.marca
    def get_model(self):
        return self.model
    def get_portes(self):
        return self.portes
    def get_rodes(self):
        return self.rodes
    def get_motor(self):
        return self.motor
    def get_color(self):
        return self.color
    def set_marca(self, marca):
        self.marca = marca
    def set_model(self, model):
        self.model = model
    def set_portes(self, portes):
        self.portes = portes
    def set_rodes(self, rodes):
        self.rodes = rodes
    def set_motor(self, motor):
        self.motor = motor
    def set_color(self, color):
        self.color = color
    def parts(self):
        print(f'Marca: {self.marca}\nModel: {self.model}\nPortes: {self.portes}\nRodes: {self.rodes}\nMotor: {self.motor}\nColor: {self.color}')
    def to_dict(self):
        return {
            "Model": self.get_model(),
            "Marca": self.get_marca(),
            "Portes": self.get_portes(),
            "Rodes": self.get_rodes(),
            "Motor": self.get_motor(),
            "Color": self.get_color()
        }