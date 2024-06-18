def show_menu():
    print("Measurement Converter Menu:")
    print("[1] Millimeters to Centimeters")
    print("[2] Centimeters to Meters")
    print("[3] Feet to Meters")
    print("[4] Inches to Centimeters")
    print("[5] Kilometers to Miles")
    print("[6] Exit")

def mm_to_cm(mm):
    return mm / 10.0

def cm_to_m(cm):
    return cm / 100.0

def ft_to_m(ft):
    return ft * 0.3048

def in_to_cm(inch):
    return inch * 2.54

def km_to_miles(km):
    return km * 0.621371

# Main program
while True:
    show_menu()
    choice = input("Enter your convertion (1-6): ")

    if choice == '1':
        mm = float(input("Enter length in millimeters: "))
        print(f"{mm} mm is equal to {mm_to_cm(mm)} cm\n")
    elif choice == '2':
        cm = float(input("Enter length in centimeters: "))
        print(f"{cm} cm is equal to {cm_to_m(cm)} meters\n")
    elif choice == '3':
        ft = float(input("Enter length in feet: "))
        print(f"{ft} ft is equal to {ft_to_m(ft)} meters\n")
    elif choice == '4':
        inch = float(input("Enter length in inches: "))
        print(f"{inch} inches is equal to {in_to_cm(inch)} cm\n")
    elif choice == '5':
        km = float(input("Enter length in kilometers: "))
        print(f"{km} km is equal to {km_to_miles(km)} miles\n")
    elif choice == '6':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.\n")
