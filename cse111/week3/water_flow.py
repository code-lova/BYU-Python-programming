# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

#Declearing global variables 
EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY =	998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016


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


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """a function named pressure_loss_from_fittings that calculates 
    the water pressure lost because of fittings such as 
    45° and 90° bends that are in a pipeline

    Args:
        fluid_velocity (float): The velocity of the water flowing through the pipe 'v'
        quantity_fittings (float): The quantity of fittings
    Return: Pressure loss due to filltings 'P'
    """
    detail1 = fluid_velocity ** 2 * quantity_fittings
    detail2 = -0.04 * WATER_DENSITY * detail1
    final = detail2 / 2000
    pressure_loss_due_to_fitting = final
    return pressure_loss_due_to_fitting

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """calculates and returns the Reynolds number for a pipe with 
    water flowing through it. The Reynolds number is a 
    unitless ratio of the inertial and viscous forces 
    in a fluid that is useful for predicting fluid flow in different situations.

    Args:
        hydraulic_diameter (float): hydraulic diameter of a pipe in meters. 
        For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter
        fluid_velocity (float): velocity of the water flowing through the pipe
    Return: The Reynolds number 'v'
    """
    d = hydraulic_diameter
    v = fluid_velocity
    μ_is_the_dynamic_viscosity_of_water = WATER_DYNAMIC_VISCOSITY
    result1 = WATER_DENSITY * d * v
    result2 = result1 / μ_is_the_dynamic_viscosity_of_water
    raynold = result2
    return raynold



def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """calculates the water pressure lost 
    because of water moving from a pipe with a 
    large diameter into a pipe with a smaller diameter. 

    Args:
        larger_diameter (float): diameter of the larger pipe in meters 'D'
        fluid_velocity (float): velocity of the water flowing through the larger diameter pipe 'v'
        reynolds_number (float): Reynolds number that corresponds to the pipe with the larger diameter 'R'
        smaller_diameter (float): diameter of the smaller pipe 'd'
    Return: 'K' constant computed by the first formula and used in the second formula
    """
    
    D = larger_diameter
    v = fluid_velocity
    R = reynolds_number
    d = smaller_diameter
    
    detail1 = 50 / R
    detail2 = 0.1 + detail1
    
    detail3 = D / d
    detail4 = detail3 ** 4 - 1
    
    detail5 = detail2 * detail4
    
    #Now finding the Lost pressure in kilopascals 'P'
    k = detail5
    density_of_water = WATER_DENSITY
    next_formula = -k * density_of_water * v ** 2
    final = next_formula / 2000
    pressure_loss_pipe_reduction = final
    return pressure_loss_pipe_reduction



def converts_kPa_to_psi(kpa_value):
    """Convert a value in Kilopascal(kpa) to pounds per square inch (psi)
    1 kPa = 0.1450377377 psi
    1 psi = 6.8947572932 kPa

    Args:
        kpa_value (float): Kilopascal(kpa) Value
    Return: psi value
    """
    psi = 0.1450377377
    result = kpa_value * psi
    psi_value = result
    return psi_value





#Running the entire code... 

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    
    #Converting from Kilopascals to Pounds per square inc (psi)
    convert_kpa = converts_kPa_to_psi(pressure)
    print(f"Pressure at house: {convert_kpa:.1f} Pounds Per Square Inch (psi)")
    

if __name__ == "__main__":
    main()
