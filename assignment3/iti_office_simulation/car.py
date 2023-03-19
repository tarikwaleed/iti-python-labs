class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        if velocity < 0 or velocity > 200:
            raise ValueError("Velocity must be between 0 and 200")
        if self.fuelRate <= 0:
            print("No fuel left! You cannot run the car")
            return
        time = distance / velocity
        self.fuelRate -= time * self.fuelRate
        self.velocity = velocity
        self.stop(distance)

    def stop(self, distance=0):
        self.velocity = 0
        if distance:
            print(f"You have arrived at your destination! Distance left: {distance} km.")
        else:
            print("You have stopped the car.")
