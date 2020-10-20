from services.simulator import Simulator
from services.plotter import Plotter


print("Hello and welcome to this tiny simulator")
print("-----------------------------------------------")
print("Ok you are big now and it's time to \ndon't ignoring air resistance in projectile motion")
print("-----------------------------------------------")
print("below enter your problem parameter, i will \ndraw graphs of motion in 'output' directory =)")
print("-----------------------------------------------")
print("first thing first, enter initial velocity:(m/s)")
initial_velocity = float(input())
print("-----------------------------------------------")
print("now enter the angel of projectile:(rad)")
angel = float(input())
print("-----------------------------------------------")
print("it's time for air to play its role, enter radius of ball:(m)")
radius = float(input())
print("-----------------------------------------------")
print("ohh we forget about mass :), enter the mass of projectile:(kg)")
mass = float(input())
print("-----------------------------------------------")
print("at the end enter time duration:(s)  *[the less time duration is the accurate your graphs will be]*")
delta_t = float(input())

simulator = Simulator(mass, initial_velocity, angel, radius, delta_t)
simulator.simulate()
Plotter.plot(simulator.x_components, simulator.y_components, "x", "y")



