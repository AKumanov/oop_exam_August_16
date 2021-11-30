class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = list()

    def install(self, software):
        needed_capacity = self.get_current_capacity() + software.capacity_consumption
        needed_memory_usage = self.get_current_memory_usage() + software.memory_consumption
        if needed_capacity > self.capacity or needed_memory_usage > self.memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)

    def get_current_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    def get_current_memory_usage(self):
        return sum([s.memory_consumption for s in self.software_components])
