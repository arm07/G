
***** Spiral Order Matrix *****

Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:

Given the following matrix:

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

You should return

[1, 2, 3, 6, 9, 8, 7, 4, 5]


class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        ret=[]
        n=len(A) #no of rows
        m=len(A[0]) #no of columns
        T = 0
        B = n-1
        L = 0
        R = m-1
        direction = 0
        num = 1
        while T <=B and L <=R:
        	if direction == 0:
        		for i in range(L,R+1):
        			ret.append(A[T][i])
        		T += 1
        		direction = 1
        	elif direction == 1:
        		for i in range(T,B+1):
        			ret.append(A[i][R])
        		R -= 1
        		direction = 2
        	elif direction == 2:
        		for i in range(R,L-1,-1):
        			ret.append(A[B][i])
        		B -= 1
        		direction = 3
        	else:
        		for i in range(B,T-1,-1):
        			ret.append(A[i][L])
        		L += 1
        		direction = 0
        return ret
        
