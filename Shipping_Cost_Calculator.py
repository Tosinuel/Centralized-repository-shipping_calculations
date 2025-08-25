# Shipping Cost Calculator

# Function to calculate shipping cost
def calculate_shipping_cost(weight, rate):
    """
    Calculate the shipping cost based on weight and rate.
    Args:
        weight (float): Package weight in kilograms.
        rate (float): Shipping rate per kilogram.
    Returns:
        float: Total shipping cost.
    """
    return weight * rate

def main():
    # Input package weight and shipping rate
    try:
        weight = float(input("Enter the package weight in kilograms: "))
        rate = float(input("Enter the shipping rate per kilogram: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculate shipping cost
    shipping_cost = calculate_shipping_cost(weight, rate)

    # Display the result
    print(f"Shipping Cost: {shipping_cost:.2f} USD")  # Display cost with 2 decimal places

if __name__ == "__main__":
    main()

# Added a function for calculation, input validation, and main guard for better structure and easier testing.
# These changes improve code readability, maintainability, and allow for automated unit testing.

