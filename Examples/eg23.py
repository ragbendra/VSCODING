A = [[1,5,8],  # 1st column. i.e 0th index
     [4,6,7],  # 2nd column i.e 1st index
     [7,2,3]]  # 3rd column i.e 2nd index
B = [[4,5,6],
     [8,9,1],
     [3,5,6]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]    # we define a result variable to store the values of sum in it
for i in range(len(A)):  # i for rows
    for j in range(len(A[0])):   # j for columns. we define A[0] because we want to iterate the value inside the column i.e 0th index value
        result[i][j] = A[i][j] + B[i][j]   #  we store the addition of two matices in result 
for r in result:   #  we iterate a value so that the result will be printed in new line
    print(r)
# Output
# [5, 10, 14]
# [12, 15, 8]
# [10, 7, 9]
#  print(len(A)) is 3

