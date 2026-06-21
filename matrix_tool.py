# ==========================================
# MATRIX OPERATIONS TOOL
# Using Python + NumPy
# ==========================================

import numpy as np


# Function to input matrix
def input_matrix(matrix_name):
    print(f"\nEnter details for {matrix_name}")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print(f"Enter elements row-wise for {matrix_name}")

    matrix = []

    for i in range(rows):
        row = []

        for j in range(cols):
            value = float(
                input(f"Element [{i+1}][{j+1}]: ")
            )
            row.append(value)

        matrix.append(row)

    return np.array(matrix)


# Function to display matrix
def display_matrix(title, matrix):

    print("\n" + "="*40)
    print(title)
    print("="*40)

    print(matrix)

    print("="*40)


# Main program
while True:

    print("\n")
    print("="*50)
    print(" MATRIX OPERATIONS TOOL ")
    print("="*50)

    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Matrix Transpose")
    print("5. Matrix Determinant")
    print("6. Exit")

    choice = input("\nEnter choice (1-6): ")

    try:

        # Matrix Addition
        if choice == "1":

            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            if A.shape == B.shape:

                result = A + B
                display_matrix(
                    "Addition Result",
                    result
                )

            else:
                print(
                    "\nError: Matrix sizes must be same."
                )

        # Matrix Subtraction
        elif choice == "2":

            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            if A.shape == B.shape:

                result = A - B

                display_matrix(
                    "Subtraction Result",
                    result
                )

            else:
                print(
                    "\nError: Matrix sizes must be same."
                )

        # Matrix Multiplication
        elif choice == "3":

            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            if A.shape[1] == B.shape[0]:

                result = np.matmul(A, B)

                display_matrix(
                    "Multiplication Result",
                    result
                )

            else:
                print(
                    "\nError: Columns of Matrix A must equal rows of Matrix B"
                )

        # Matrix Transpose
        elif choice == "4":

            A = input_matrix("Matrix")

            result = np.transpose(A)

            display_matrix(
                "Transpose Result",
                result
            )

        # Matrix Determinant
        elif choice == "5":

            A = input_matrix("Matrix")

            if A.shape[0] == A.shape[1]:

                result = np.linalg.det(A)

                print("\n"+"="*40)
                print(
                    f"Determinant = {round(result,2)}"
                )
                print("="*40)

            else:
                print(
                    "\nError: Determinant requires square matrix."
                )

        # Exit
        elif choice == "6":

            print("\nThank you for using Matrix Tool")
            break

        else:
            print(
                "\nInvalid choice! Enter 1-6."
            )

    except ValueError:
        print(
            "\nInvalid input! Enter numeric values only."
        )

    except Exception as e:
        print(
            "\nError:",
            e
        )