# The Collatz Sequence practice project (page 77 AUTOMATE THE BORING STUFF)
# Added plotting support with mathplotlib, just for practice purposes
import matplotlib.pyplot as plt
import sys
matrix = []


def empty_list():
    return []


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        matrix.append(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        matrix.append(result)
        print(result)
        return result


try:
    print("Enter number 1: ")
    num = int(input())
    print("Enter number 2: ")
    num2 = int(input())
except ValueError:
    print("Wrong input data type, expected integers! Exiting...")
    sys.exit()

while num != 1:
    num = collatz(num)
matrix1 = matrix
matrix = empty_list()
while num2 != 1:
    num2 = collatz(num2)
matrix2 = matrix
matrix = empty_list()
print("List1: " + str(matrix1))
print("List2: " + str(matrix2))

# Shortening lists for plotting
if len(matrix1) > len(matrix2):
    matrix1 = matrix1[:len(matrix1)-(len(matrix1)-len(matrix2))]
elif len(matrix2) > len(matrix1):
    matrix2 = matrix2[:len(matrix2)-(len(matrix2)-len(matrix1))]
print("Plotting...")

plt.autumn()  # Sets colormap to "Autumn"
plt.plot(matrix1, matrix2)
plt.ylabel('Sequence 2')
plt.xlabel('Sequence 1')
plt.show()
