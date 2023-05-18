"""Python program that computes and prints the storage 
efficiency for each of the following 12 steel can sizes. 
Then visually examine the output and answer this question, 
“Which can size has the highest storage efficiency?”
"""
import math

#Assigning global scope variable to all empty list's used in our programm
can_name_list = []
radius_list = []
height_list = []
cost_list = []
storage_efficeincy_list = []


    # print(can_name_list[0], radius_list[0], height_list[0],end=" ")
    # print()    
    # print()

#Main function definition starts here.
def main():
    #Here we open the can_sizes.txt and looped through each line
    with open("can_sizes.txt") as can_size:
        for cans in can_size: #Looping through each line in the txt file
            parts = cans.split(":") #Seperating each line into a list
            #print(parts)
            
            #Here we strip off any space in each list and seperate them into different data types using
            #their index number [1][2]
            name = str(parts[0].strip())
            radius = float(parts[1].strip())
            height = float(parts[2].strip())
            cost = float(parts[4].strip())
            #print(cost)
            
            #Appending new values into seperate new list for each parameter
            radius_list.append(radius)
            height_list.append(height)
            can_name_list.append(name)
            cost_list.append(cost)
    
        for i, radius in enumerate(radius_list):
            #Looping through radius list
            #with index of each values in the radius list i got the corresponding values in height_list and 
            #The can_size_names and also cost amount
            
            height = height_list[i] #Using the index [i] of each value in the radius list to get corrsponding value in the height list
            can_name = can_name_list[i] #doing same thing here to get the cylinder name
            cost_eff = cost_list[i] #doing same thing here to get the cost value of each cylinder
            
            #Calling our functions here, then assigning arguement to compute 
            vol = compute_volume(radius=radius, height=height) 
            surf_area = compute_surface_area(radius=radius, height=height)
            storage_efficiency = compute_storage_efficiency(volume=vol, surface_area=surf_area)
            cost_efficiency = compute_cost_efficiency(volume=vol, cost=cost_eff)

            print("{} {:.2f} ${:,.0f}".format(can_name, storage_efficiency, cost_efficiency))
            
            #To find the can with the best storage efficiency 
            #lets make a new list appending all the computed storeage efficiency to it
            #so we can loop through it 
            storage_efficeincy_list.append(storage_efficiency)
            
            #declearing varables to hold the maximum cost efficiency and best storage efficiency 
            #giving then a value of -1 or 0. Any
            max_cost_efficiency = -1
            best_storage_efficiency = -1
            
            #finding the Maximum cost effieciency or can size with the highest cost in the cost list
            for j, cost in enumerate(cost_list):
                can_size_name = can_name_list[j]
                if cost > max_cost_efficiency:
                    max_cost_efficiency = cost
                    max_can_size_name = can_size_name
                    
            #Finding the can with the BEST Storage Efficiency from the storage efficiency list above
            for m, best_can_size_efficiency in enumerate(storage_efficeincy_list):
                can_size_name = can_name_list[m]
                if best_can_size_efficiency > best_storage_efficiency:
                    best_storage_efficiency = best_can_size_efficiency
                    best_can_size_eff_name =  can_size_name    
                    
                                   
        print("The can size with the Highest Cost Efficiency is {} with cost of ${} USD".format(max_can_size_name, max_cost_efficiency))
        print("The can size with the Best Storage Efficiency is {} with Efficiency of {:.2f}".format(best_can_size_eff_name, best_storage_efficiency))
    pass
#Our function definitions starts here 
def compute_volume(radius, height):
    """Compute the volume of 12 can sizes

    Args:
        radius (float): radius of the cylinder
        height (float): height of the cylinder

    Returns:
        Result: The volume of the cylinder
    """
    pi = math.pi
    volume = pi * radius ** 2 * height
    return volume


def compute_surface_area(radius, height):
    """compute the surface area of all 12 can sizes.

    Args:
        radius (float): radius of the cylinder
        height (float): height of the cylinder

    Returns:
        Result: The surface area of the cylinder
    """
    pi = math.pi
    result = radius + height
    surface_area = 2 * pi * radius * result
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    """compute the storage efficiency of all 12 can sizes.

    Args:
        volume (float): volume of the cylinder
        surface_area (float): surface area of the cylinder

    Returns:
        result: The storage efficiency 
    """
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(volume, cost):
    """compute the cost efficiency of all 12 can sizes.

    Args:
        volume (float): volume of the cylinder
        cost (float): cost per each can 

    Returns:
        result: The cost efficiency 
    """
    cost_efficiency = volume / cost
    return cost_efficiency


main()
    
    