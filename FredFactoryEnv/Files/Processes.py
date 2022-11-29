import simpy


def print(machine, workers, store):

    parts_list = machine.parts_list

    while True:

        for part in parts_list:

            curr_part = part.name

            if curr_part in store.items():
                if part.sequence[0] == 1:
                    yield store.get(curr_part)
                    sequence = part.sequence.pop(0)
                    done_in = part.process_times.pop(0)

                    while done_in:

                        with machine.machine.request(priority=1) as req:
                            yield req
                            machine.busy = True

                            try:
                                start = machine.env.now
                                yield machine.env.timeout(done_in)
                                machine.machine.release(req)
                                part.comp_proc.append(sequence)
                                done_in = 0
                                machine.busy = False

                            except simpy.Interrupt:
                                for worker in workers:
                                    if not worker.busy:
                                        with worker.worker.request(priority=-1) as request:
                                            yield request #finish code here
                                done_in -= worker.env.now - start


def preprocessing(worker):
    curr_part = part.name
    process_time = part.process_times.pop(0)
    sequence = part.sequence.pop(0)

    while True:
        done_in = process_time
        while done_in:
            with worker.worker.request(priority=1) as req:
                yield req
                try:
                    start = worker.env.now
                    yield worker.env.timeout(done_in)
                    worker.worker.release(req)
                    part.comp_proc.append(sequence)
                    done_in = 0
                except simpy.Interrupt:
                    worker.busy = True
                    done_in -= worker.env.now - start

def fiber_sub(worker):
    curr_part = part.name
    process_time = part.process_times.pop(0)
    sequence = part.sequence.pop(0)

    while True:
        done_in = process_time
        while done_in:
            with worker.worker.request(priority=2) as req:
                yield req
                try:
                    start = worker.env.now
                    yield worker.env.timeout(done_in)
                    worker.worker.release(req)
                    part.comp_proc.append(sequence)
                    done_in = 0
                except simpy.Interrupt:
                    worker.busy = True
                    done_in -= worker.env.now - start

def cooling_sub(worker):
    curr_part = part.name
    process_time = part.process_times.pop(0)
    sequence = part.sequence.pop(0)

    while True:
        done_in = process_time
        while done_in:
            with worker.worker.request(priority=2) as req:
                yield req
                try:
                    start = worker.env.now
                    yield worker.env.timeout(done_in)
                    worker.worker.release(req)
                    part.comp_proc.append(sequence)
                    done_in = 0
                except simpy.Interrupt:
                    worker.busy = True
                    done_in -= worker.env.now - start

def extrusion_sub(worker):
    curr_part = part.name
    process_time = part.process_times.pop(0)
    sequence = part.sequence.pop(0)

    while True:
        done_in = process_time
        while done_in:
            with worker.worker.request(priority=2) as req:
                yield req
                try:
                    start = worker.env.now
                    yield worker.env.timeout(done_in)
                    worker.worker.release(req)
                    part.comp_proc.append(sequence)
                    done_in = 0
                except simpy.Interrupt:
                    worker.busy = True
                    done_in -= worker.env.now - start

def control_sub(worker):
    curr_part = part.name
    process_time = part.process_times.pop(0)
    sequence = part.sequence.pop(0)

    while True:
        done_in = process_time
        while done_in:
            with worker.worker.request(priority=2) as req:
                yield req
                try:
                    start = worker.env.now
                    yield worker.env.timeout(done_in)
                    worker.worker.release(req)
                    part.comp_proc.append(sequence)
                    done_in = 0
                except simpy.Interrupt:
                    worker.busy = True
                    done_in -= worker.env.now - start

def final_assem(worker):
    pass

def packing(worker):
    pass
