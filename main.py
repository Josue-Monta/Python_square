import math


def calculate_square_root(number):
    if number < 0:
        return None
    else:
        return math.sqrt(number)


def main():
    number = float(input("Enter a number to calculate its square root: "))
    result = calculate_square_root(number)

    if result is None:
        print("Square root of a negative number is not defined.")
    else:
        print(f"The square root of {number} is {result:.2f}")


if __name__ == "__main__":
    main()