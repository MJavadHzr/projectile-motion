class Reader:
    def __init__(self):
        self.graph_addr = "resources/drag-coefficient.txt"  # bad coding :\
        self.x_axis = []
        self.y_axis = []

    def read_graph(self):
        reader = open(self.graph_addr)
        for line in reader.readlines():
            self.x_axis.append(float(line.split(':+++:')[0]))
            self.y_axis.append(float(line.split(':+++:')[1]))

    def get_x_data(self):
        return self.x_axis

    def get_y_data(self):
        return self.y_axis
