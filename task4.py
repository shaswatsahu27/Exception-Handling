# Task 4

filename = input("Enter filename: ")

try:
    file = open(filename, 'r')
    
    print("First 3 lines:")
    for i in range(3):
        print(file.readline(), end='')

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("\nFile operation attempted.")