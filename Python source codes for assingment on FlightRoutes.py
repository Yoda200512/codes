


#input   #process
print(" ")
print("                           FlightRoutes Company")
print("")
print("                                Main Menu")
print("")
print("1. Display All possible airline routes between two given countries with durations.")
print("")
print("2. Display least time airline route between two given countries.")
print("")
print("3. Exit")
print("")

while True:
    choice = input("Your choice: ").strip()

    if choice == '1':
        print("\n                          FlightRoutes Company")
        print("")
        print("     All possible airline routes between two given countries with durations")
        print("")
        print(" Please enter Starting country and destination country in the space given below")
        print("")
        x = input("Enter Starting Country: ").upper()
        y = input("Enter Destination Country: ").upper()

        if x == 'SL' and y == 'USA':
            print("Route 1: Sri Lanka (SL) -> UK -> USA                             Expected duration : 19.45 Hours")
            print("Route 2: Sri Lanka (SL) -> Japan -> USA                          Expected duration : 24 Hours")
            print("Route 3: Sri Lanka (SL) -> Singapore -> Japan -> USA             Expected duration : 24 Hours")
        elif x == 'SL' and y == 'AUSTRALIA':
            print("Route 1: Sri Lanka (SL) -> Australia                              Expected duration : 9.25 Hours")
            print("Route 2: Sri Lanka (SL) -> Singapore -> Australia                 Expected duration : 11.25 Hours")
            print("Route 3: Sri Lanka (SL) -> Japan -> Australia                     Expected duration : 18 Hours")
            print("Route 4: Sri Lanka (SL) -> Singapore -> Japan -> Australia        Expected duration : 18 Hours")
        elif x == 'SL' and y == 'JAPAN':
            print("Route 1: Sri Lanka (SL) -> Japan                                 Expected duration : 8 Hours")
            print("Route 2: Sri Lanka (SL) -> Singapore -> Japan                    Expected duration : 8 Hours")
        elif x == 'SL' and y == 'SINGAPORE':
            print("Route 1: Sri Lanka (SL) -> Singapore                             Expected duration : 4 Hours")
        elif x == 'SL' and y == 'UK':
            print("Route 1: Sri Lanka (SL) -> Singapore                            Expected duration : 4 Hours")
        elif x == 'SINGAPORE' and y == 'USA':
            print("Route 1: Singapore -> Japan -> USA                              Expected duration : 20 Hours")
        elif x == 'SINGAPORE' and y == 'AUSTRALIA':
            print("Route 1: Singapore -> Australia                                      Expected duration : 7.25 Hours")
            print("Route 2: Singapore -> Japan -> Australia                             Expected duration : 14hrs")
        elif x == 'UK' and y =='USA':   
            print("Route 1: UK -> USA 		          	                    Expected duration : 8 Hours")
        elif x == 'JAPAN' and y == 'USA':
            print("Route 1: Japan -> USA                                            Expected duration : 16 Hours")
        elif x == 'JAPAN' and y == 'AUSTRALIA':
            print("Route 1: Japan -> Australia                                      Expected duration : 10 Hours")
        

        else:
            print("                   !!!Enter a valid destination !!!")
             
        print("")
        q= input("Do you want to Exit ( Yes / No ) ? :").lower()
        if q == 'yes':
            break
        
    elif choice == '2':
        print("                             FlightRoutes Company")
        print("         Display least time airline route between two given countries.")
        print("")
        x = input("Enter Starting Country: ").upper()
        y = input("Enter Destination Country: ").upper()
        
        if x == 'SL' and y == 'USA':
            print("Route: Sri Lanka (SL) -> UK -> USA                         Expected duration: 19.45 Hours")
        elif x == 'SL' and y == 'UK':
            print("Route: Sri Lanka (SL) -> UK                                Expected duration: 11.45 Hours")
        elif x == 'SL' and y == 'JAPAN':
            print("Route: Sri Lanka (SL) -> Japan                             Expected duration: 8 Hours")
        elif x == 'SL' and y == 'SINGAPORE':
            print("Route: Sri Lanka (SL) -> Singapore                         Expected duration: 4 Hours")
        elif x == 'SL' and y == 'AUSTRALIA':
            print("Route: Sri Lanka (SL) -> Australia                         Expected duration: 9.25 Hours")
        elif x == 'UK' and y == 'USA':
            print("Route: UK -> USA                                           Expected duration: 8 Hours")
        elif x == 'JAPAN' and y == 'USA':
            print("Route: Japan -> USA                                        Expected duration: 16 Hours")
        elif x == 'SINGAPORE' and y == 'USA':
            print("Route: Singapore -> Japan -> USA                           Expected duration: 20 Hours")
        elif x == 'SINGAPORE' and y == 'JAPAN':
            print("Route: Singapore -> Japan                                  Expected duration: 4 Hours")
        elif x == 'JAPAN' and y == 'AUSTRALIA':
            print("Route: Japan -> Australia                                  Expected duration: 10 Hours")
        elif x == 'SINGAPORE' and y == 'AUSTRALIA':
            print("Route: Singapore -> Australia                              Expexted durartion: 7.25 Hours")

        else:
            print("                    Enter a valid destination !!!")
             
        print("")
        q= input("Do you want to Exit ( Yes / No ) ? :").lower()
        if q == 'yes':
            break
        
            
        # Add functionality for displaying least time airline route
        pass

    elif choice == '3':
        print("Exit Program")
        break

    else:
        print("")
        print("               !!!  Invalid choice. Please enter a valid option  !!!")
        print("")
