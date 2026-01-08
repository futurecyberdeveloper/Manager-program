class Machine:
    def __init__(self, nama, power, status):
        self.nama = nama
        self.power = power
        self.status = status

class Factory:
    def __init__(self, nama):
        self.nama = nama
        self.allmachine = {}

    def createmachine(self, nama, power):
        key = len(self.allmachine) + 1
        self.allmachine[key] = Machine(nama, power, "OFF")

    def showallmachine(self):
        for k, v in self.allmachine.items():
            print(f"No: {k} - Nama: {v.nama} - Power: {v.power} - Status: {v.status}")
    
    def onmachine(self):
        for v in self.allmachine.values():
            v.status = "ON"
            print(f"{v.nama} is now {v.status}")

    def countallpower(self):
        total = 0
        for v in self.allmachine.values():
            if v.status == "ON":
                total += v.power
        print(f"total power usage: {total}W")

    def offallmachine(self):
        for v in self.allmachine.values():
            v.status = "OFF"
            print(f"{v.nama} is now {v.status}")

    def totalonmachine(self):
        total = 0
        totalmesin = 0
        
        for v in self.allmachine.values():
            if v.status == "ON":
                total += 1
        
        totalmesin = len(self.allmachine)

        print(f"Total machines: {totalmesin}")
        print(f"Active machines: {total}")

factory = Factory("neo factory")
factory.createmachine("Tdr 300", 1200)
factory.createmachine("Tdr 400", 1250)

print("==============================")
print("SMART FACTORY SYSTEM")
print("==============================")

print(f"Factory: {factory.nama.capitalize()}")
print("Machines")
factory.showallmachine()
print()

print(">> Turning ON all machines")
print()
factory.onmachine()
print()

print(">> Check total machines")
factory.totalonmachine()
print()

print(">> Factory Report")
factory.countallpower()
print()

print(">> Shutting down factory")
print()
factory.offallmachine()

#🔹 How the this Program Work
#1.Machine class
#  Stores machine data: name, power usage, and status (ON or OFF).

#2.Factory class
#  Acts as a container that creates and owns machines.
#  All machines are stored inside a dictionary.

#3.Creating machines
#  The factory creates machines using createmachine().
#  Each machine is automatically given status "OFF" when created.

#4.Showing machine data
#  showallmachine() displays all machines with their number, name, power, and status.

#5.Turning machines ON
#  onmachine() changes the status of every machine to "ON".

#6.Counting active machines
#totalonmachine() counts:
#   Total machines
#   How many machines are currently ON

#7.Calculating power usage
#  countallpower() calculates total power only from machines that are ON.

#8.Turning machines OFF
#  offallmachine() shuts down all machines by setting their status to "OFF".
