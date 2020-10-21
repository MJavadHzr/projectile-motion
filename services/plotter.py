import matplotlib.pyplot as plt
import os


class Plotter:
    output_addr = "output"

    @classmethod
    def plot(cls, y_axis, x_axis, y_label, x_label, name):
        plt.plot(x_axis, y_axis)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        cls.__check_dir()
        plt.savefig(cls.output_addr + "/" + name)
        plt.show()

    @classmethod
    def __check_dir(cls):
        if not os.path.exists(cls.output_addr):
            os.mkdir(cls.output_addr)
