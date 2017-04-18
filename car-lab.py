class Car(object):
    def _init_(self, name='General', model='GM', type='Car'):
        self.name = name
        self.model = model
        self.type = type
        self.speed = 0

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.no_doors = 2
        else:
            self.no_doors = 4

        if self.type != 'trailer':
            self.no_wheels = 4
        else:
            self.no_wheels = 8

    def is_saloon(self):
        if self.type != 'trailer':
            return True
        else:
            return False

    def drive(self, spe):
        if self.type == 'Car':
            self.speed = 10 ** spe
        else:
            self.speed = 77

        return self
     
