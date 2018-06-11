
#This is a function that takes a matrix and multiplies it with a vector, taking a n by m matrix and a m by p vector and outputs a n by p vector.
def matVec(matrix,vector):

    n = len(matrix)
    m = len(vector)
    p = len(vector[0])
    C = [[0] * p for row in range(m)]
    if(len(matrix[0]) != m): # I decided to just put this in because I like to have outputs instead of errors to help
        print('You cannot multiply those inputs')
    else:
        #setting all of the variables and setting C equal to the size of the vector
        for i in range(n): #goes through all of the matrix for the rows of the matrix
            for j in range(p): #goes through all of the vector for every row in the vector
                c_ij = 0   #setting c_ij to 0
                for k in range(m): #goes through all of the vector for every column, which since its a vector is 1

                    c_ij += matrix[i][k]*vector[k][j]  #the multiplication of the matrix and vector
                    C[i][j] = c_ij

        return C

# I took most of the test stuff from the scalar multiplication example

testMatrix01 = 4
testMatrix02 = [[1,2,3],[3,1,1],[2,4,2]]
testMatrix03 = 'this is a test'

testVector01 = [[1], [2], [3]]
testVector02 = 2
testVector03 = True

#These are all of the test out puts
print(matVec(testMatrix02,testVector01)) #matrix and vector, prints out [[14],[8],[16]] which is correct
#print(matVec(testVector01,testMatrix02)) #gives an index error because the columns in the vector is not equal to the rows in the matrix
#print(matVec(testMatrix03,testVector02)) #I get an error in line 36 and 9 and the type error is object of type 'int' has no len()




