from FredFactory import Factory
import simpy
import numpy as np

env = simpy.Environment()
num = np.random.normal(15, 2)
factory = Factory(env, 5, 4)

print(factory)
