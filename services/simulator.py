import math
from services.drag_coefficient_serivice import DragCoefficientService


class Simulator:
    x_components = []
    y_components = []
    v_x_components = []
    v_y_components = []
    a_x_components = []
    a_y_components = []
    time = []
    air_density = 1.225  # TODO
    g = 9.8  # TODO

    def __init__(self, ball_mass, velocity, angel, ball_radius, delta_t):
        self.ball_mass = ball_mass
        self.v_x_components.append(velocity * math.cos(angel))
        self.v_y_components.append(velocity * math.sin(angel))
        self.ball_area = math.pi * ball_radius * ball_radius
        self.delta_t = delta_t
        self.drag_coefficient_service = DragCoefficientService()
        self.drag_coefficient_service.initialize()
        self.x_components.append(0)
        self.y_components.append(0)
        self.time.append(0)

    def simulate(self):
        i = 0
        while True:
            self.__calculate_next_a(i)
            self.__calculate_next_v(i)
            self.__calculate_next_r(i)
            self.time.append(self.time[i] + self.delta_t)

            i += 1

            if self.y_components[i] < 0:
                break

    def __calculate_next_a(self, i):
        resiting_force_coefficient = (self.__get_cw(i) * self.air_density * self.__get_velocity(i)) / (
                2 * self.ball_mass)
        self.a_x_components.append(resiting_force_coefficient * -1 * self.v_x_components[i])
        self.a_y_components.append(resiting_force_coefficient * -1 * self.v_y_components[i] - self.g)

    def __calculate_next_v(self, i):
        new_v_x = self.__get_new_value(self.v_x_components[i], self.a_x_components[i])
        new_v_y = self.__get_new_value(self.v_y_components[i], self.a_y_components[i])
        self.v_x_components.append(new_v_x)
        self.v_y_components.append(new_v_y)

    def __calculate_next_r(self, i):
        new_x = self.__get_new_value(self.x_components[i], self.v_x_components[i])
        new_y = self.__get_new_value(self.y_components[i], self.v_y_components[i])
        self.x_components.append(new_x)
        self.y_components.append(new_y)

    def __get_velocity(self, i):
        v_x = self.v_x_components[i]
        v_y = self.v_y_components[i]
        return math.sqrt((v_x * v_x) + (v_y * v_y))

    def __get_cw(self, i):
        return self.drag_coefficient_service.get_coefficient(self.__get_velocity(i))

    def __get_new_value(self, prev, ratio):
        return prev + (ratio * self.delta_t)
