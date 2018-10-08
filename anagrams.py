class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        if A == None: 
            return A
        d = {}
        collection_of_grps = []
        temp = 0
        for i in range(len(A)):
            sorted_A = ''.join(sorted(A[i]))
            if sorted_A not in d:
                collection_of_grps.append([i+1])
                d[sorted_A] = temp
                temp += 1
            else:
                collection_of_grps[d[sorted_A]].append(i+1)
        return collection_of_grps
