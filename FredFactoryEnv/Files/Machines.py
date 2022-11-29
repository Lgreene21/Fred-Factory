import simpy
from FredFactory import Factory, Machine, Worker
import Processes as p


class PrinterSN(Machine):

    def __init__(self, name, parts_list):
        self.env = env
        self.name = name
        self.MTTF = int(300)
        self.MTTR = int(20)
        self.busy = False
        self.parts_list = parts_list

        self.process = self.env.process(p.print(self.machine, Factory.workers))
        self.env.process(self.break_machine(lambda: self.generate_MTTF(self.MTTF)))
