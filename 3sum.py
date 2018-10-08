class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        temp = float('INF')
        response = -1
        for i in range(0, len(A) - 2):
            p = A[i]
            start, end = i + 1, len(A) - 1
            while (start < end):
                q, r = A[start], A[end]
                if (abs(B - (p + q + r)) < temp):
                    temp = abs(B - (p + q + r))
                    response = p + q + r
                if (p + q + r == B):
                    return B
                elif (p + q + r > B):
                    end = end - 1
                else:
                    start = start + 1
        return response
