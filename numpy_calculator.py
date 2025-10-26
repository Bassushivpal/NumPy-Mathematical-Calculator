import numpy as np

# ==============================
# NumPy Mathematical Calculator
# ==============================

def basic_arithmetic_operations():
    print("\n--- Basic Arithmetic Operations ---")
    a = np.array(list(map(float, input("Enter elements of first array (space-separated): ").split())))
    b = np.array(list(map(float, input("Enter elements of second array (space-separated): ").split())))
    
    print("\nAddition:", np.add(a, b))
    print("Subtraction:", np.subtract(a, b))
    print("Multiplication:", np.multiply(a, b))
    print("Division:", np.divide(a, b))
    print("Power:", np.power(a, b))


def statistical_operations():
    print("\n--- Statistical Operations ---")
    arr = np.array(list(map(float, input("Enter elements of array (space-separated): ").split())))

    print("\nMean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Standard Deviation:", np.std(arr))
    print("Variance:", np.var(arr))
    print("Minimum:", np.min(arr))
    print("Maximum:", np.max(arr))
    print("Sum:", np.sum(arr))
    print("Product:", np.prod(arr))
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Data Type:", arr.dtype)


def array_manipulation():
    print("\n--- Array Manipulation ---")
    arr = np.array(list(map(int, input("Enter elements of array (space-separated): ").split())))

    print("\nOriginal Array:", arr)
    try:
        rows = int(input("Enter rows to reshape (or 0 to skip): "))
        cols = int(input("Enter cols to reshape (or 0 to skip): "))
        if rows and cols:
            reshaped = arr.reshape(rows, cols)
            print("Reshaped Array:\n", reshaped)
    except Exception:
        print("Reshape not possible with given dimensions.")

    print("\nSorted Array:", np.sort(arr))
    print("Reverse Sorted Array:", np.sort(arr)[::-1])

    print("Unique Elements:", np.unique(arr))

    print("First Element:", arr[0])
    print("Last Element:", arr[-1])

    mean_value = np.mean(arr)
    print(f"Mean Value: {mean_value}")
    print("Values greater than mean:", arr[arr > mean_value])


# ==============================
# Main Menu
# ==============================

def main():
    while True:
        print("\n===== NumPy Mathematical Calculator =====")
        print("1. Basic Arithmetic Operations")
        print("2. Statistical Operations")
        print("3. Array Manipulation")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            basic_arithmetic_operations()
        elif choice == '2':
            statistical_operations()
        elif choice == '3':
            array_manipulation()
        elif choice == '4':
            print("Exiting... Thank you for using NumPy Calculator!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-4).")


if __name__ == "__main__":
    main()
