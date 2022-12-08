def cmatrix():
    m = []
    r = int(input("Enter number of Rows : "))
    c = int(input("Enter number of Columns : "))
    for i in range(0, r):
        row = []
        for j in range(0, c):
            ele = int(input(f"Enter the ({i + 1} x {j + 1}) elements : "))
            row.append(ele)
        m.append(row)

    return m

m1 = cmatrix()
print(m1)
m2 = cmatrix()
print(m2)

def add(m1, m2):
    result = []
    for i in range(0, len(m1)):
        row = []
        for j in range(0, len(m1[0])):
            sum = m1[i][j] + m2[i][j]
            row.append(sum)
        result.append(row)
    return result

def substraction(m1, m2):
    result = []
    for i in range(0, len(m1)):
        row = []
        for j in range(0, len(m1[0])):
            substraction = m1[i][j] - m2[i][j]
            row.append(substraction)
        result.append(row)
    return result


def multiplication(m1, m2):
    result = []
    for i in range(0, len(m1)):
        row = []
        for j in range(0, len(m1[0])):
            multiplication = m1[i][j] * m2[j][i]
            row.append(multiplication)
        result.append(row)
    return result


def transpose(m1, m2):
    result = []
    for i in range(0, len(m1)):
        row = []
        for j in range(0, len(m1[0])):
            transpose = m1[j][i]
            row.append(transpose)
        result.append(row)
    return result

def menu():
    print("1.Addition of Matrices are : ")
    print("2.Substraction of two Matrices are : ")
    print("3.Multiplication of two Matrices : ")
    print("4.Transpose of the Matrix : ")
    print("5.Exit")

    mchoice = int(input())

    while mchoice:
        if mchoice == 1:
            print("Addition of two Matrices is : ", add(m1, m2))
            menu()
        elif mchoice == 2:
            print("Substraction of two Matrices is : ", substraction(m1, m2))
            menu()
        elif mchoice == 3:
            print("Multiplication of two Matrices is : ", multiplication(m1, m2))
            menu()
        elif mchoice == 4:
            print("Transpose of First Matrix is : ", transpose(m1, m2))
            menu()
        elif mchoice == 5:
            exit()
menu()
Output-
aids39@aids39-System-Product-Name:~$ python3 dsl3.py
Enter number of Rows : 2
Enter number of Columns : 2
Enter the (1 x 1) elements : 2
Enter the (1 x 2) elements : 3
Enter the (2 x 1) elements : 4
Enter the (2 x 2) elements : 5
[[2, 3], [4, 5]]
Enter number of Rows : 3
Enter number of Columns : 3
Enter the (1 x 1) elements : 3
Enter the (1 x 2) elements : 2
Enter the (1 x 3) elements : 1
Enter the (2 x 1) elements : 1
Enter the (2 x 2) elements : 2
Enter the (2 x 3) elements : 3
Enter the (3 x 1) elements : 4
Enter the (3 x 2) elements : 5
Enter the (3 x 3) elements : 6
[[3, 2, 1], [1, 2, 3], [4, 5, 6]]
1.Addition of Matrices are : 
2.Substraction of two Matrices are : 
3.Multiplication of two Matrices : 
4.Transpose of the Matrix : 
5.Exit
1
Addition of two Matrices is :  [[5, 5], [5, 7]]
1.Addition of Matrices are : 
2.Substraction of two Matrices are : 
3.Multiplication of two Matrices : 
4.Transpose of the Matrix : 
5.Exit
2
Substraction of two Matrices is :  [[-1, 1], [3, 3]]
1.Addition of Matrices are : 
2.Substraction of two Matrices are : 
3.Multiplication of two Matrices : 
4.Transpose of the Matrix : 
5.Exit
3
Multiplication of two Matrices is :  [[6, 3], [8, 10]]
1.Addition of Matrices are : 
2.Substraction of two Matrices are : 
3.Multiplication of two Matrices : 
4.Transpose of the Matrix : 
5.Exit
4
Transpose of First Matrix is :  [[2, 4], [3, 5]]
1.Addition of Matrices are : 
2.Substraction of two Matrices are : 
3.Multiplication of two Matrices : 
4.Transpose of the Matrix : 
5.Exit
5
aids39@aids39-System-Product-Name:~$ 



