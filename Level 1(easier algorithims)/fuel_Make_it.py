def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if fuel_left/mpg >= distance_to_pump else False


#returns whether the car can make it with the fuel available