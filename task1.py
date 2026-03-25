# Task 1

try:
    num = float(input("Enter numerator: "))
    den = float(input("Enter denominator: "))
    result = num / den

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Operation Complete")