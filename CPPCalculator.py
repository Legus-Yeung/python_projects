# CPP Calculator for flights and hotels reward redemption created by Legus Yeung
def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def get_valid_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer value.")

def calculateCPP(fare, points, fees):
    total_cost = fare - fees

    if points == 0:
        return None
    
    cent_per_point = total_cost / points
    return round(cent_per_point, 4)

def main():
    print("Welcome to the CPP Calculator for Flights and Hotels!\n")

    fare = get_valid_float_input("Enter the fare/cost: $")

    num_options = get_valid_int_input("Enter the number of options (up to 4): ")
    num_options = min(4, max(1, num_options))  # Ensure the number is between 1 and 4

    cent_per_point_results = []

    for i in range(1, num_options + 1):
        print(f"\nOption {i}:")
        points = get_valid_int_input("Enter the points amount: ")

        include_fees = input("Does the points amount include fees? (y/n): ").lower()
        if include_fees == 'y':
            fees = get_valid_float_input("Enter the fees amount: $")
        else:
            fees = 0

        cent_per_point = calculateCPP(fare, points, fees)

        if cent_per_point is not None:
            print(f"Cent per point for Option {i}: {cent_per_point:.4f} cents") # .4f to display 4 decimal places
            cent_per_point_results.append((i, cent_per_point))
        else:
            print("Points amount cannot be zero. Please enter valid values.")   # catch invalid input

    print("\nCent Per Point Summary:")
    for option, cent_per_point in cent_per_point_results:
        print(f"Option {option}: {cent_per_point:.4f} cents")

    if cent_per_point_results:
        best_option, best_value = max(cent_per_point_results, key=lambda x: x[1])
        print(f"\nOption {best_option} has the highest cent per point value: {best_value:.4f} cents (Best Value)")
    else:
        print("No valid options to determine the best value.")

if __name__ == "__main__":
    main()
