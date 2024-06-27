def matrix(m,n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter the matrix o[{i}][{j}]: "))
            row.append(inp)
        o.append(row)
    return o

def sum(A,B):
    output = []
    for i in range(len(A)):
        r = []
        for j in range(len(A[0])):
            r.append(A[i][j] + B[i][j])
        output.append(r)
    return output


m = int(input("Enter number of rows:\n"))
n = int(input("Enter number of columns:\n"))

print("Enter the matrix A:")
A = matrix(m, n)
print("The matrix A is:\n", A)

print("Enter the matrix B:")
B = matrix(m, n)
print("The matrix B is:\n", B)

S = sum(A, B)
print("The sum of matrices is:\n", S)



"""def matrix(m,n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter the matrix o[{i}][{j}]: "))
            row.append(inp)
        o.append(row)
    return o

def sum(A,B):
    output = []
    for i in range(len(A)):
        r = []
        for j in range(len(A[0])):
            x = A[i][j] + B[i][j]
            r.append(x)
        output.append(r)
    return output

m = int(input("Enter the rows number\n"))
n = int(input("Enter the columns numbers\n"))

print("Enter the matrix A: ")
A = matrix(m,n)
print("The matrix A is: ",A)

print("Enter the matrix B: ")
B = matrix(m,n)
print("The matrix B is: ",B)

S = sum(A,B)
print("The sum of entered two matrices is: ",S)"""

