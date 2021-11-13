from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if software.capacity_consumption > (self.capacity - self.used_capacity):
            raise ValueError("Software cannot be installed")
        if software.memory_consumption > (self.memory - self.used_memory):
            raise ValueError("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])
