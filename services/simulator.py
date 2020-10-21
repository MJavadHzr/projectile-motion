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
            resiting_force_coefficient = (self.__get_cw(i) * self.air_density * self.__get_velocity(i)) / (
                    2 * self.ball_mass)
            self.a_x_components.append(resiting_force_coefficient * -1 * self.v_x_components[i])
            self.a_y_components.append(resiting_force_coefficient * -1 * self.v_y_components[i] - self.g)

            new_v_x = self.v_x_components[i] + (self.a_x_components[i] * self.delta_t)
            new_v_y = self.v_y_components[i] + (self.a_y_components[i] * self.delta_t)
            self.v_x_components.append(new_v_x)
            self.v_y_components.append(new_v_y)

            new_x = self.x_components[i] + (self.v_x_components[i] * self.delta_t)
            new_y = self.y_components[i] + (self.v_y_components[i] * self.delta_t)
            self.x_components.append(new_x)
            self.y_components.append(new_y)

            new_time = self.time[i] + self.delta_t
            self.time.append(new_time)

            i += 1

            if new_y < 0:
                break

    def __get_velocity(self, i):
        v_x = self.v_x_components[i]
        v_y = self.v_y_components[i]
        return math.sqrt((v_x * v_x) + (v_y * v_y))

    def __get_cw(self, i):
        return self.drag_coefficient_service.get_coefficient(self.__get_velocity(i))
