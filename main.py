def print_numbers_recursive(A):
    if A > 0:
        print_numbers_recursive(A - 1)
        print(A, end=" ")
    else:
        print()
if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        if num < 1:
            print("Please enter a positive integer.")
        else:
            print_numbers_recursive(num)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")
