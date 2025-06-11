# Creating a Multi-Function Calculator Project
import time
print("====Multi-Function Python Calculator====")
running = True
print("Note: The result will be shown to the user for 8 seconds.")
time.sleep(3.5)
# Starting calculator
while running:
    # Isolating each menu to easily switch between them
    function = int(input("""
    Which menu do you want to you enter 
    (Enter 1 for; Basic Arithmetic
    2; Temperature Converter
    3; Mass Converter
    4; Length Converter
    0; Exit): """))
    while (function == 1):
        # Section 1: Basic Arithmetic 
        print("-----Basic Arithmetic------")
        op = input("""\nSelect operation;
               A = Addition (+)
               S = Subtraction (-)
               M = Multiplication (*)
               D = Division (/)
               R = Remainder [Mod] (%)
               F = Floor Division (//)
               P = Power (//)
               U (Change Menu): """)
        oper = op.lower()
        if (oper == "u"):  # Changing Menus; Exiting from the isolated loop of this submenu.
            print("Choose from below: ")
            break
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("\nEnter the second number: "))
        
        if (oper == "a"):
            sum = num1 + num2
            print("The sum of",num1,"and",num2,f"is: {sum:.2f}")
            time.sleep(8)
        elif (oper == "s"):
            subtract = num1 - num2
            print("The difference of",num1,"and",num2,f"is: {subtract:.2f}")
            time.sleep(8)
        elif (oper == "m"):
            prod = num1 * num2
            print("The product of",num1,"and",num2,f"is: {prod:.2f}")
            time.sleep(8)
        elif (oper == "d"):
            if (num2 == 0):
                print("Dividing by zero (0) is not allowed.")
                time.sleep(3.5)
            else: 
                 div = num1/num2
                 print("The quotient of",num1,"and",num2,f"is: {div:.2f}")
                 time.sleep(8)
        elif (oper == "r"):
            if (num2 == 0):
                print("Dividing by zero (0) is not allowed.")
                time.sleep(3.5)
            else:
                mod = num1 % num2
                print("The remainder of",num1,"and",num2,f"is: {mod:.2f}")
                time.sleep(8)
        elif (oper == "f"):
            if (num2 == 0):
                print("Dividing by zero (0) is not allowed.")
                time.sleep(3.5)
            else:
                 fl_div = num1 // num2
                 print("The floor quotient of",num1,"and",num2,f"is: {fl_div:.2f}")
                 time.sleep(8)
        elif (oper == "p"):
            power = pow(num1, num2)
            print("The power of",num1,"to",num2,f"is: {power:.2f}")
            time.sleep(8)
        else:
            print("Error. Enter a correct value.")
            time.sleep(3)

    while (function == 2):
        # Section 2: Temperature Converter
        print("-----Temperature Converter-----")
        prime_t = input("""
               K = Kelvin 
               C = Celcius
               F = Fahrenheit
               R = Rankine
               U (Change Menu)  \nFrom which temperature scale do you want to convert FROM: """)
        prime_temp = prime_t.lower()

        if (prime_temp == "u"):  # Changing Menus; Exiting from the isolated loop of this submenu.
            break
        
        t = input("""
               K = Kelvin 
               C = Celcius
               F = Fahrenheit
               R = Rankine  \nSelect conversion TO; """)
        temp = t.lower()
        value = float(input("\nEnter the value: "))
        
        if (prime_temp == "k"):  # Converting from Kelvin to others
            match temp:
                case "c":
                    celcius = value - 273.15
                    print("The value",value,f"Kelvin, converted to Celcius is: {celcius:.2f}")
                    time.sleep(8)
                case "f":
                    fahrenheit = (value - 273.15) * 9/5 + 32
                    print("The value",value,f"Kelvin, converted to Fahrenheit is: {fahrenheit:.2f}")
                    time.sleep(8)
                case "r":
                    rankine = value * 1.8
                    print("The value",value,f"Kelvin, converted to Rankine is: {rankine:.2f}")
                    time.sleep(8)

        elif (prime_temp == "c"):  # Converting from Celcius to others
             match temp:
                case "k":
                    kelvin = 273.15 + value
                    print("The value",value,f"Celcius, converted to Kelvin is: {kelvin:.2f}")
                    time.sleep(8)
                case "f":
                    fahrenheit = (value* 9/5) + 32
                    print("The value",value,f"Celcius, converted to Fahrenheit is: {fahrenheit:.2f}")
                    time.sleep(8)
                case "r":
                    rankine = value * 9/5 + 491.67
                    print("The value",value,f"Celcius, converted to Rankine is: {rankine:.2f}")
                    time.sleep(8)

        elif (prime_temp == "f"):  # Converting from Fahrenheit to others
            match temp:
                case "k":
                    kelvin = (value - 32) * 5/9 + 273.15
                    print("The value",value,f"Fahrenheit, converted to Kelvin is: {kelvin:.2f}")
                    time.sleep(8)
                case "c":
                    celcius = (value - 32) * 5/9
                    print("The value",value,f"Fahrenheit, converted to Celcius is: {celcius:.2f}")
                    time.sleep(8)
                case "r":
                    rankine = value + 459.67
                    print("The value",value,f"Fahrenheit, converted to Rankine is: {rankine:.2f}")
                    time.sleep(8)
            
        elif (prime_temp == "r"):  # Converting from Rankine to others
            match temp:
                case "k":
                    kelvin = value * 5/9
                    print("The value",value,f"Rankine, converted to Kelvin is: {kelvin:.2f}")
                    time.sleep(8)
                case "c":
                    celcius = (value - 491.67) * 5/9 
                    print("The value",value,f"Rankine, converted to Celcius is: {celcius:.2f}")
                    time.sleep(8)
                case "f":
                    fahrenheit = value - 459.67
                    print("The value",value,f"Rankine converted to Fahrenheit is: {fahrenheit:.2f}")
                    time.sleep(8)
    
        else:
            print("Error. Enter a correct value.")
            time.sleep(3)

    while (function == 3):
        # Section 3: Mass Converter
        print("-----Mass Converter-----")
        prime_m = input("""
               KG = Kilograms 
               G = Grams
               LB = Pounds
               T = Tonne
               OZ = Ounces
               U (Change Menu) \nFrom which weight scale do you want to convert FROM: """)
        prime_mass = prime_m.lower()

        if (prime_mass == "u"):  # Changing Menus; Exiting from the isolated loop of this submenu.
            break
        
        m = input("""
               KG = Kilograms 
               G = Grams
               LB = Pounds
               T = Tonne
               OZ = Ounces \nSelect conversion TO: """)
        mass = m.lower()
        value = float(input("Enter the value: "))
        
        if (prime_mass == "kg"):  
            # Converting from KG to others
            match mass:
                case "g":
                    gm = value * 1000
                    print("The value",value,f"Kg, converted to grams is: {gm:.2f}")
                    time.sleep(8)
                case "lb":
                    lbs = value * 2.205
                    print("The value",value,f"Kg, converted to pounds is: {lbs:.2f}",)
                    time.sleep(8)
                case "t":
                    tonne = value/1000
                    print("The value",value,f"Kg, converted to tonne is: {tonne:.2f}")
                    time.sleep(8)
                case "oz":
                    oz = value * 35.274
                    print("The value",value,f"Kg, converted to ounces is: {oz:.2f}")
                    time.sleep(8)

        elif (prime_mass == "g"):  
             # Converting from Grams to others
             match mass:
                case "kg":
                    kilo = value/1000
                    print("The value",value,f"Grams, converted to KG is: {kilo:.2f}")
                    time.sleep(8)
                case "lb":
                    lbs = value/453.6
                    print("The value",value,f"Grams, converted to pounds is: {lbs:.2f}")
                    time.sleep(8)
                case "t":
                    tonne = value/1_000_000
                    print("The value",value,f"Grams, converted to tonnes is: {tonne:.2f}")
                    time.sleep(8)
                case "oz":
                    oz = value/28.35
                    print("The value",value,f"Grams, converted to ounces is: {oz:.2f}")
                    time.sleep(8)

        elif (prime_mass == "lb"):  
             # Converting from Pounds to others
             match mass:
                case "kg":
                    kilo = value/2.205
                    print("The value",value,f"Pounds, converted to KG is: {kilo:.2f}")
                    time.sleep(8)
                case "g":
                    gm = value * 453.592
                    print("The value",value,f"Pounds, converted to grams is: {gm:.2f}")
                    time.sleep(8)
                case "t":
                    tonne = value/2205
                    print("The value",value,f"Pounds, converted to tonnes is: {tonne:.2f}")
                    time.sleep(8)
                case "oz":
                    oz = value * 16
                    print("The value",value,f"Pounds, converted to ounces is: {oz:.2f}")
                    time.sleep(8)
            
        elif (prime_mass == "t"):  
             # Converting from Tonnes to others
             match mass:
                case "kg":
                    kilo = value * 1000
                    print("The value",value,f"Tonnes, converted to KG is: {kilo:.2f}")
                    time.sleep(8)
                case "lb":
                    lbs = value * 2205
                    print("The value",value,f"Tonnes, converted to pounds is: {lbs:.2f}")
                    time.sleep(8)
                case "g":
                    gm = value * 1_000_000
                    print("The value",value,f"Tonnes, converted to tonnes is: {gm:.2f}")
                    time.sleep(8)
                case "oz":
                    oz = value * 35273.962
                    print("The value",value,f"Tonnes, converted to ounces is: {oz:.2f}")
                    time.sleep(8)

        elif (prime_mass == "oz"):  
             # Converting from Ounces to others
             match mass:
                case "kg":
                    kilo = value/35.274
                    print("The value",value,f"Ounces, converted to KG is: {kilo:.2f}")
                    time.sleep(8)
                case "lb":
                    lbs = value/16
                    print("The value",value,f"Ounces, converted to pounds is: {lbs:.2f}")
                    time.sleep(8)
                case "g":
                    gm = value * 28.35
                    print("The value",value,f"Ounces, converted to grams is: {gm:.2f}")
                    time.sleep(8)
                case "t":
                    tonne = value/35273.962
                    print("The value",value,f"Ounces, converted to tonnes is: {tonne:.2f}")
                    time.sleep(8)
    
        else:
            print("Error. Enter a correct value.")
    while (function == 4):
        # Section 4: Length Converter
        print("-----Length Converter-----")
        prime_l = input("""
               KM = Kilometers 
               M = Miles
               MTR = Meters 
               IN = Inches
               CM = Centimeters
               FT = Feet/Foot
               Y = Yards
               MM = Millimeters
               U (Change Menu) \nFrom which length scale do you want to convert FROM: """)
        prime_length = prime_l.lower()

        if (prime_length == "u"):  # Changing Menus; Exiting from the isolated loop of this submenu.
            break
        
        l = input("""
               KM = Kilometers 
               M = Miles
               MTR = Meters 
               IN = Inches
               CM = Centimeters
               FT = Feet/Foot
               Y = Yards
               MM = Millimeters \nSelect conversion TO:""")
        length = l.lower()
        value = float(input("Enter the value: "))
        
        if (prime_length == "km"):  
            # Converting from Kilometers to others
            match length:
                case "m":
                    miles = value/1.60934
                    print("The value",value,f"km, converted to miles is: {miles:.2f}")
                    time.sleep(8)
                case "mtr":
                    meters = value * 1000
                    print("The value",value,f"km, converted to meters is: {meters:.2f}",)
                    time.sleep(8)
                case "in":
                    inches = value * 39370.1
                    print("The value",value,f"km, converted to inches is: {inches:.2f}")
                    time.sleep(8)
                case "cm":
                    cms = value * 100000
                    print("The value",value,f"km, converted to centimeters is: {cms:.2f}")
                    time.sleep(8)
                case "mm":
                    mms = value * 1_000_000
                    print("The value",value,f"km, converted to millimeters is: {mms:.2f}")
                    time.sleep(8)
                case "ft":
                    foot = value * 3280.84
                    print("The value",value,f"km, converted to feet/foot is: {foot:.2f}")
                    time.sleep(8)
                case "y":
                    yards = value * 1093.61
                    print("The value",value,f"km, converted to yards is: {yards:.2f}")
                    time.sleep(8)

        elif (prime_length == "m"):  
             # Converting from Miles to others
             match length:
                case "km":
                    km = value * 1.60934
                    print("The value",value,f"miles, converted to kilometers is: {km:.2f}")
                    time.sleep(8)
                case "mtr":
                    meters = value * 1609.34
                    print("The value",value,f"miles, converted to meters is: {meters:.2f}",)
                    time.sleep(8)
                case "in":
                    inches = value * 63360
                    print("The value",value,f"miles, converted to inches is: {inches:.2f}")
                    time.sleep(8)
                case "cm":
                    cms = value * 160934
                    print("The value",value,f"miles, converted to centimeters is: {cms:.2f}")
                    time.sleep(8)
                case "mm":
                    mms = value * 1_609_344
                    print("The value",value,f"miles, converted to millimeters is: {mms:.2f}")
                    time.sleep(8)
                case "ft":
                    foot = value * 5280
                    print("The value",value,f"miles, converted to feet/foot is: {foot:.2f}")
                    time.sleep(8)
                case "y":
                    yards = value * 1760
                    print("The value",value,f"miles, converted to yards is: {yards:.2f}")
                    time.sleep(8)

        elif (prime_length == "mtr"):  
             # Converting from Meters to others
             match length:
                case "km":
                    km = value/1000
                    print("The value",value,f"meters, converted to kilometers is: {km:.2f}")
                    time.sleep(8)
                case "m":
                    miles = value * 0.00062137 
                    print("The value",value,f"meters, converted to miles is: {miles:.3f}",)
                    time.sleep(8)
                case "in":
                    inches = value * 39.37
                    print("The value",value,f"meters, converted to inches is: {inches:.2f}")
                    time.sleep(8)
                case "cm":
                    cms = value * 100
                    print("The value",value,f"meters, converted to centimeters is: {cms:.2f}")
                    time.sleep(8)
                case "mm":
                    mms = value * 1000
                    print("The value",value,f"meters, converted to millimeters is: {mms:.2f}")
                    time.sleep(8)
                case "ft":
                    foot = value * 3.281
                    print("The value",value,f"meters, converted to feet/foot is: {foot:.2f}")
                    time.sleep(8)
                case "y":
                    yards = value * 1.094
                    print("The value",value,f"meters, converted to yards is: {yards:.2f}")
                    time.sleep(8)
            
        elif (prime_length == "in"):  
             # Converting from Inches to others
             match length:
                case "km":
                    km = value * 0.0000254
                    print("The value",value,f"inches, converted to kilometers is: {km:.3f}")
                    time.sleep(8)
                case "mtr":
                    meters = value/39.37
                    print("The value",value,f"inches, converted to meters is: {meters:.2f}",)
                    time.sleep(8)
                case "m":
                    miles = value/63360
                    print("The value",value,f"inches, converted to miles is: {miles:.3f}")
                    time.sleep(8)
                case "cm":
                    cms = value * 2.54
                    print("The value",value,f"inches, converted to centimeters is: {cms:.2f}")
                    time.sleep(8)
                case "mm":
                    mms = value * 25.4
                    print("The value",value,f"inches, converted to millimeters is: {mms:.2f}")
                    time.sleep(8)
                case "ft":
                    foot = value/12
                    print("The value",value,f"inches, converted to feet/foot is: {foot:.2f}")
                    time.sleep(8)
                case "y":
                    yards = value/36
                    print("The value",value,f"inches, converted to yards is: {yards:.2f}")
                    time.sleep(8)

        elif (prime_length == "cm"):  
             # Converting from Centimeters to others
             match length:
                case "km":
                    km = value/100000
                    print("The value",value,f"centimeters, converted to kilometers is: {km:.4f}")
                    time.sleep(8)
                case "mtr":
                    meters = value/100
                    print("The value",value,f"centimeters, converted to meters is: {meters:.2f}",)
                    time.sleep(8)
                case "in":
                    inches = value/2.54
                    print("The value",value,f"centimeters, converted to inches is: {inches:.2f}")
                    time.sleep(8)
                case "m":
                    miles = value/160_934.4
                    print("The value",value,f"centimeters, converted to miles is: {miles:.4f}")
                    time.sleep(8)
                case "mm":
                    mms = value * 10
                    print("The value",value,f"centimeters, converted to millimeters is: {mms:.2f}")
                    time.sleep(8)
                case "ft":
                    foot = value/30.48
                    print("The value",value,f"centimeters, converted to feet/foot is: {foot:.2f}")
                    time.sleep(8)
                case "y":
                    yards = value/91.44
                    print("The value",value,f"centimeters, converted to yards is: {yards:.2f}")
                    time.sleep(8)
        elif (prime_length == "ft"):  
             # Converting from foot to others
             match length:
                case "km":
                    km = value/3280.84
                    print("The value",value,f"feet, converted to kilometers is: {km:.4f}")
                    time.sleep(8)
                case "mtr":
                    meters = value/3.281
                    print("The value",value,f"feet, converted to meters is: {meters:.2f}",)
                    time.sleep(8)
                case "in":
                    inches = value * 12
                    print("The value",value,f"feet, converted to inches is: {inches:.2f}")
                    time.sleep(8)
                case "m":
                    miles = value/5280
                    print("The value",value,f"feet, converted to miles is: {miles:.4f}")
                    time.sleep(8)
                case "mm":
                    mms = value * 304.8
                    print("The value",value,f"feet, converted to millimeters is: {mms:.2f}")
                    time.sleep(8)
                case "cm":
                    cms = value * 30.48
                    print("The value",value,f"feet, converted to centimeters is: {cms:.2f}")
                    time.sleep(8)
                case "y":
                    yards = value/3
                    print("The value",value,f"feet, converted to yards is: {yards:.2f}")
                    time.sleep(8)
        elif (prime_length == "mm"):  
             # Converting from Millimeters to others
             match length:
                case "km":
                    km = value/1000000
                    print("The value",value,f"millimeters, converted to kilometers is: {km:.5f}")
                    time.sleep(8)
                case "mtr":
                    meters = value/1000
                    print("The value",value,f"millimeters, converted to meters is: {meters:.3f}",)
                    time.sleep(8)
                case "in":
                    inches = value/25.4
                    print("The value",value,f"millimeters, converted to inches is: {inches:.2f}")
                    time.sleep(8)
                case "m":
                    miles = value/160_9344
                    print("The value",value,f"millimeters, converted to miles is: {miles:.5f}")
                    time.sleep(8)
                case "cm":
                    cms = value/10
                    print("The value",value,f"millimeters, converted to millimeters is: {cms:.2f}")
                    time.sleep(8)
                case "ft":
                    foot = value/304.8
                    print("The value",value,f"millimeters, converted to feet/foot is: {foot:.2f}")
                    time.sleep(8)
                case "y":
                    yards = value/914.4
                    print("The value",value,f"millimeters, converted to yards is: {yards:.2f}")
                    time.sleep(8)
        elif (prime_length == "y"):  
             # Converting from Yards to others
             match length:
                case "km":
                    km = value/1094
                    print("The value",value,f"yards, converted to kilometers is: {km:.2f}")
                    time.sleep(8)
                case "mtr":
                    meters = value/1.094
                    print("The value",value,f"yards, converted to meters is: {meters:.2f}",)
                    time.sleep(8)
                case "in":
                    inches = value * 36
                    print("The value",value,f"yards, converted to inches is: {inches:.2f}")
                    time.sleep(8)
                case "m":
                    miles = value/1760
                    print("The value",value,f"yards, converted to miles is: {miles:.2f}")
                    time.sleep(8)
                case "mm":
                    mms = value * 914.4
                    print("The value",value,f"yards, converted to millimeters is: {mms:.2f}")
                    time.sleep(8)
                case "ft":
                    foot = value * 3
                    print("The value",value,f"yards, converted to feet/foot is: {foot:.2f}")
                    time.sleep(8)
                case "cm":
                    cms = value * 91.44
                    print("The value",value,f"yards, converted to yards is: {cms:.2f}")
                    time.sleep(8)
    
        else:
            print("Error. Enter a correct value.")

    if function == 0:
        print("-------------------------------------------")
        running = False        
        