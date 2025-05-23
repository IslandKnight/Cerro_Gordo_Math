import math


class WaterTank:
    def __init__(self, tank_type, length_or_radius, width=None, height=None):
        self.tank_type = tank_type
        self.length_or_radius = length_or_radius
        self.width = width
        self.height = height

    def calculate_volume(self):
        if self.tank_type == 'rectangular':
            if self.width is None or self.height is None:
                raise ValueError("Width and height must be provided for rectangular tanks")
            volume = self.length_or_radius * self.width * self.height
        elif self.tank_type == 'round':
            if self.height is None:
                raise ValueError("Height must be provided for round tanks")
            volume = math.pi * (self.length_or_radius ** 2) * self.height
        else:
            raise ValueError("Invalid tank type. Must be 'rectangular' or 'round'")
        return volume


# Example usage:
# Create a rectangular water tank with length 10 meters, width 5 meters, and height 2 meters
rectangular_tank = WaterTank(tank_type='rectangular', length_or_radius=10, width=5, height=2)
rect_volume = rectangular_tank.calculate_volume()
print(f"The volume of the rectangular water tank is {rect_volume} cubic meters.")

# Create a round water tank with a radius of 3 meters and a height of 5 meters
round_tank = WaterTank(tank_type='round', length_or_radius=3, height=5)
round_volume = round_tank.calculate_volume()
print(f"The volume of the round water tank is {round_volume:.2f} cubic meters.")
