from services.reader import Reader


class DragCoefficientService:
    def __init__(self):
        self.air_velocity = 330
        self.reader = Reader()
        self.x_data = []
        self.y_data = []

    def initialize(self):
        self.reader.read_graph()
        self.x_data = self.reader.get_x_data()
        self.y_data = self.reader.get_y_data()

    def get_coefficient(self, velocity):
        mach_number = velocity / self.air_velocity
        index = self.get_index(mach_number)
        return self.y_data[index]

    def get_index(self, value):
        for i in range(len(self.x_data) - 1):
            if (self.x_data[i] < value) & (value < self.x_data[i + 1]):
                return i
