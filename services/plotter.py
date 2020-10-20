import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot(x_axis, y_axis, x_label, y_label):
        plt.plot(x_axis, y_axis)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
