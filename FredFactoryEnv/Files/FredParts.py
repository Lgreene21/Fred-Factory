class Part:

    def __init__(self, attr):
        self.attr = attr
        self.name = self.attr['part_num']
        self.desc = self.attr['part_name']
        self.subassembly = self.attr['subassembly']
        self.sub_code = self.attr['assembly_station']
        self.material = self.attr['material']
        self.process_times = []
        self.sequence = []
        self.comp_proc = []

    def __str__(self):
        return print('Part {name} is a {desc} and belongs to the {subassembly} subassembly'.format_map(vars(self)))

    def create_sequence(self):
        if self.attr[7] != "":
            self.sequence.append(1)
            self.process_times.append(self.attr['fab_time'])
        if self.attr[9] != "":
            self.sequence.append(2)
            self.process_times.append(self.attr['preassembly_time'])
        if self.sub_code != 7:
            self.sequence.append(self.sub_code)
            self.sequence.append(7)
            self.sequence.append(8)
            self.process_times.append(self.attr['production_time'])
            self.process_times.append(self.attr['production_time'])
            self.process_times.append(self.attr['production_time'])
        else:
            self.sequence.append(self.sub_code)
            self.sequence.append(8)
            self.process_times.append(self.attr['production_time'])
            self.process_times.append(self.attr['production_time'])

