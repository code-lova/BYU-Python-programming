#This is a list of modules that does a specify work task as follows
#This is a seperate fuction containing function to calculate for the 
#Wind chill of a particular temperature at some wind speeed mph
def compute_wind_chill(fahrenheit, value, celcius):
    if value == 1 and celcius == 0:
        compute = fahrenheit * 1.8
        new_result = compute + 32
        
        for i in range(5, 61, 5):
            wc_formula = 35.74 + 0.6215*fahrenheit - 35.75*i**0.16 + 0.4275*fahrenheit*i**0.16
            result = wc_formula
            print("At temperature {}F, and wind {} mph, the windchill is {:.2f}F".format(fahrenheit, i, result))
    else:
        if value == 2 and celcius != 0:
            compute = celcius * 9/5
            new_result = compute + 32
        
            for i in range(5, 61, 5):
                wc_formula = 35.74 + 0.6215*new_result - 35.75*i**0.16 + 0.4275*new_result*i**0.16
                result = wc_formula
                print("At temperature {}F, and wind {} mph, the windchill is {:.2f}F".format(new_result, i, result))
                
    return result