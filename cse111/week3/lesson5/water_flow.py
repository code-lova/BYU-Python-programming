# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

#Declearing global variables 
EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY =	998.2
#WATER_DYNAMIC_VISCOSITY = 0.0010016

#These variable names were gotton when i did week 6 of this program

def water_column_height(tower_height, tank_height):
    """calculates and returns the height of a 
    column of water from a tower height and a tank wall height. 

    Args:
        tower_height (float): Height of the water column
        tank_height (float): Height of the tower
    Return: Height of column of water
    """
    details1 = 3 * tank_height
    details2 = details1 / 4
    height = tower_height + details2
    return height


def pressure_gain_from_water_height(height):
    """calculates and returns the pressure caused by 
    Earth’s gravity pulling on the water stored in an elevated tank.

    Args:
        height (float): Height of the column of water
    Return: Pressure
    """
    detail1 = WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height
    detail2 = detail1 / 1000
    pressure = detail2
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """calculates and returns the water pressure lost because 
    of the friction between the water and the walls of a pipe 
    that it flows through.

    Args:
        pipe_diameter (float): The diameter of the pipe in meters 'd'
        pipe_length (float): The length of the pipe in meters 'l'
        friction_factor (float): The pipe's friction factor 'f'
        fluid_velocity (float): The velocity of the water flowing through the pipe in meters / second 'v'
        
        p = density of water
        formula = pressure loss = -f*l*p*v**2 / 2000 * d
    """
    f = friction_factor
    l = pipe_length
    p_density_of_water = WATER_DENSITY
    v = fluid_velocity
    d = pipe_diameter
    
    result1 = v ** 2
    result2 = -f * l * p_density_of_water
    result3 = result2 * result1
    result4 = 2000 * d
    press_loss = result3 / result4
    return press_loss

