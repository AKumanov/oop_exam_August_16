from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = list()
    _software = list()

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)

        except IndexError:
            return f"Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)

        except IndexError:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory_consumption = sum([s.memory_consumption for s in System._software])
        total_memory = sum([h.memory for h in System._hardware])
        total_capacity_consumption = sum([s.capacity_consumption for s in System._software])
        total_capacity = sum([h.capacity for h in System._hardware])
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_memory_consumption} / {total_memory}\n" \
               f"Total Capacity Taken: {total_capacity_consumption} / {total_capacity}"

    @staticmethod
    def system_split():
        output = []
        for hardware in System._hardware:
            software_string = ', '.join(
                [s.name for s in hardware.software_components]) if hardware.software_components else 'None'
            output.append(
                f"Hardware Component - {hardware.name}\n"
                f"Express Software Components: {len([e for e in hardware.software_components if e.software_type == 'Express'])}\n"
                f"Light Software Components: {len([l for l in hardware.software_components if l.software_type == 'Light'])}\n"
                f"Memory Usage: {sum([s.memory_consumption for s in hardware.software_components])} / {hardware.memory}\n"
                f"Capacity Usage: {sum([s.capacity_consumption for s in hardware.software_components])} / {hardware.capacity}\n"
                f"Type: {hardware.hardware_type}\n"
                f"Software Components: {software_string}"
            )
        return '\n'.join(output)
