import simpy
import json
import numpy as np
from FredParts import Part


class Factory:

    factory_name = "MIT/Monterrey Fred Factory"
    product_name = "Fiber Extrusion Device (FrED)"

    def __init__(self, env: simpy.Environment(), file: str):
        self.env = env
        self.part_objects = self.initialize(file)
        self.factory_workers = []

    def initialize(self, file):
        demand = int(input('What is the demand for FrED?: '))
        with open(file, 'r') as f:
            data = json.loads(f.read())
        f.close()
        part_objects = []
        for _ in range(demand):
            for attr in data["Part Attributes"]:
                part_objects.append(Part(attr))
        return part_objects

    def generate_MTTF(self, MTTF):
        return np.random.exponential(MTTF)

    def generate_MTTR(self, MTTR):
        return np.random.exponential(MTTR)


class Machine(Factory):

    def __init__(self):
        self.broken = False
        self.num_broke = int(0)
        self.process = simpy.Event(self.env)
        self.machine = simpy.Resource(self.env, capacity=1)

    def break_machine(self, MTTF):
        while True:
            yield self.env.timeout(MTTF)
            if not self.broken:
                self.process.interrupt()


class Worker(Factory):

    def __init__(self, name):
        self.name = name
        self.busy = False
        self.worker = simpy.PreemptiveResource(self.env, capacity=1)
        self.timer = 0

        self.factory_workers.append(self.worker)
