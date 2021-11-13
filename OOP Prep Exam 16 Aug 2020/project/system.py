from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                try:
                    hardware.install(express_software)
                    System._software.append(express_software)
                except ValueError as e:
                    return str(e)
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                light_software = LightSoftware(name, capacity_consumption, memory_consumption)
                try:
                    hardware.install(light_software)
                    System._software.append(light_software)
                except ValueError as e:
                    return str(e)
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware_to_remove = None
        software_to_remove = None

        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware_to_remove = hardware
        for software in System._software:
            if software.name == software_name:
                software_to_remove = software

        if hardware_to_remove and software_to_remove:
            hardware_to_remove.uninstall(software_to_remove)
            System._software.remove(software_to_remove)
        else:
            return "Some of the components do not exist"


    @staticmethod
    def analyze():
        result = ['System Analysis']
        result.append(f'Hardware Components: {len(System._hardware)}')
        result.append(f'Software Components: {len(System._software)}')
        used_capacity = sum([h.used_capacity for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])
        used_memory = sum([h.used_memory for h in System._hardware])
        total_memory = sum([h.memory for h in System._hardware])
        result.append(f"Total Operational Memory: {used_memory} / {total_memory}")
        result.append(f"Total Capacity Taken: {used_capacity} / {total_capacity}")
        return '\n'.join(result)

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            result.append(f"Hardware Component - {hardware.name}")
            express = [s for s in hardware.software_components if s.__class__.__name__ == 'ExpressSoftware']
            result.append(f"Express Software Components: {len(express)}")
            light = [s for s in hardware.software_components if s.__class__.__name__ == 'LightSoftware']
            result.append(f"Light Software Components: {len(light)}")
            result.append(f"Memory Usage: {hardware.used_memory} / {hardware.memory}")
            result.append(f"Capacity Usage: {hardware.used_capacity} / {hardware.capacity}")
            result.append(f"Type: {hardware.type}")
            software_components = [s.name for s in hardware.software_components]
            result.append(f"Software Components: {', '.join(software_components) if software_components else 'None'}")
        return '\n'.join(result)



