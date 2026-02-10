import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))
    
    print(f"Enter elements for Matrix {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    
    return np.array(matrix)

def display_matrix(title, matrix):
    print(f"\n{title}")
    print(matrix)

while True:
    print("\n====== MATRIX OPERATIONS TOOL ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        A = input_matrix("A")
        B = input_matrix("B")
        if A.shape == B.shape:
            result = A + B
            display_matrix("Result (A + B):", result)
        else:
            print("❌ Matrices must have same dimensions")

    elif choice == 2:
        A = input_matrix("A")
        B = input_matrix("B")
        if A.shape == B.shape:
            result = A - B
            display_matrix("Result (A - B):", result)
        else:
            print("❌ Matrices must have same dimensions")

    elif choice == 3:
        A = input_matrix("A")
        B = input_matrix("B")
        if A.shape[1] == B.shape[0]:
            result = np.dot(A, B)
            display_matrix("Result (A × B):", result)
        else:
            print("❌ Columns of A must equal rows of B")

    elif choice == 4:
        A = input_matrix("A")
        result = A.T
        display_matrix("Transpose of Matrix A:", result)

    elif choice == 5:
        A = input_matrix("A")
        if A.shape[0] == A.shape[1]:
            det = np.linalg.det(A)
            print("\nDeterminant of Matrix A:", det)
        else:
            print("❌ Determinant possible only for square matrices")

    elif choice == 6:
        print("Exiting Matrix Operations Tool. Goodbye 👋")
        break

    else:
        print("❌ Invalid choice. Try again.")
