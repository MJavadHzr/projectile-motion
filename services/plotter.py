import matplotlib.pyplot as plt


class Plotter:

    @staticmethod
    def plot(y_axis, x_axis, y_label, x_label, name):
        plt.plot(x_axis, y_axis)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.savefig("output/" + name)
        plt.show()
