from abc import ABC, abstractmethod

# Abstract base class
class Device(ABC):
    @abstractmethod
    def operate(self):
        pass


class SmartLamp(Device):
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type

    def operate(self):
        print(f"{self.name}: Light is turned on")


class SmartFan(Device):
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type

    def operate(self):
        print(f"{self.name}: Fan is spinning at medium speed")


class SmartDoor(Device):
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type

    def operate(self):
        print(f"{self.name}: Door is now locked")


def run_single_device(devices):
    while True:
        show_all_devices(devices)
        choice = input("Enter device number (q to quit): ")

        if choice.lower() == "q":
            break
        elif not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)
        selected_device = devices.get(choice)

        if selected_device:
            selected_device.operate()
        else:
            print("Device number not found.")


def show_all_devices(devices):
    print("====== DEVICE LIST ======")
    for key, device in devices.items():
        print(f"No: {key} | Name: {device.name} | Type: {device.device_type}")
    print("=========================")


def run_all_devices(devices):
    print("===== DEVICE OPERATION =====")
    for device in devices.values():
        device.operate()
    print("============================")


def main():
    devices = {
        1: SmartLamp("Living Room Lamp", "Smart Lamp"),
        2: SmartFan("Bedroom Fan", "Smart Fan"),
        3: SmartDoor("Front Door", "Smart Door")
    }

    while True:
        print("==============================")
        print(" SMART DEVICE SYSTEM")
        print("==============================")
        print("1. Show all devices")
        print("2. Run all device operations")
        print("3. Run single device operation")
        print("4. Exit")

        choice = input("Choose: ")

        if not choice.isdigit():
            print("Input must be a number.")
            continue

        choice = int(choice)

        if choice == 1:
            show_all_devices(devices)
        elif choice == 2:
            run_all_devices(devices)
        elif choice == 3:
            run_single_device(devices)
        elif choice == 4:
            print("Program exited.")
            break
        else:
            print("Please select a valid menu option.")

    print("==============================")


if __name__ == "__main__":
    main()