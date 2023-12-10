from dataclasses import dataclass
import random

@dataclass
class SimulatorConfigure:
    max_cycles = 100000
    instruction_interval = 100

    pipelinestall_ratio = 0.2
    data_access_ratio = 0.3

    L1i_hit_ratio = 0.95
    L1d_hit_ratio = 0.85

    L1_access_time: int = 2

    L2_hit_ratio = 0.95
    L2_access_time: int = 20

    TLB_hit_ratio = 0.98
    TLB_access_time: int = 2

    page_table_level = 6
    memory_access: int = 120 * page_table_level

    cores_per_chip = 8
    max_bus_utilization = 0.8
    bus_speed = 6 * 10**9  # 6 GHz
    cache_line_size = 64  # Assuming 64 bytes cache line

class BusManager:
    def __init__(self):
        self.busy = False
        self.queue = []
        self.processing_time = -1
        self.busy_time = 0
        self.current_id = -1

    def request_bus(self, core_id,access_time):
        if self.busy:
            self.queue.append((core_id,access_time))
        else:
            self.busy = True
            self.processing_time = access_time
            self.current_id = core_id

    def release_bus(self):
        self.busy = False
        if self.queue:
            core_id, access_time = self.queue.pop(0)
            self.request_bus(core_id, access_time)
        return self.current_id

    def process_cycle(self):
        print(self.busy, self.queue, self.processing_time)
        if self.busy:
            self.busy_time += 1
            self.processing_time -=1
            if self.processing_time == 0:
                self.release_bus()

class Chip:
    def __init__(self, config: SimulatorConfigure):
        self.config = config
        self.total_time = 0
        self.bus_manager = BusManager()
        self.cores = [Core(core_id, config, self.bus_manager) for core_id in range(config.cores_per_chip)]

    def start(self):
        for cycle in range(self.config.max_cycles):
            self.total_time += 1  # Each core contributes one cycle
            coreid = self.bus_manager.process_cycle() # receive from busmanager
            if coreid is not None:
                self.cores[coreid].waiting_for_memory = False
            for core in self.cores:
                core.process_cycle()
        print("Total time:", self.bus_manager.busy_time)

        average_bus_utilization = self.bus_manager.busy_time / self.total_time
        print("Average bus utilization:", average_bus_utilization)

class Core:
    def __init__(self, core_id, config: SimulatorConfigure, bus_manager: BusManager):
        self.core_id = core_id
        self.config = config
        self.bus_manager = bus_manager
        self.waiting_for_memory = False

    def process_cycle(self):
        if self.waiting_for_memory:
            return  # Currently waiting for memory access

        if random.random() < 0.1:  # 10% chance to issue an instruction
            if random.random() > self.config.L1i_hit_ratio and random.random() > self.config.L2_hit_ratio:
                # L1 and L2 miss, need memory access
                self.waiting_for_memory = True
                if random.random() <= self.config.TLB_hit_ratio:
                    access_time = self.config.memory_access
                else:
                    access_time = self.config.memory_access  * self.config.page_table_level # page walk
                self.bus_manager.request_bus(self.core_id, access_time)

if __name__ == '__main__':
    config = SimulatorConfigure()
    simulator = Chip(config)
    simulator.start()