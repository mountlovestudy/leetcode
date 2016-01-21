"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

"""
class Solution1(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(n):
			label = [-1] * n
			result += self.possibleResolve(label, 0, i)
        return result

    def possibleResolve(self, label, row, col):
		n = len(label)

		if self.isValid(label, row, col):
			if row == n-1:
				return 1
			label[row] = col
			result = 0
			for i in range(n):
				plabel = label
				result += self.possibleResolve(plabel, row+1, i)
			return result
		else:
			return 0

    def isValid(self, label, row, col):
		for i in range(row):
			if col == label[i]:
				return False
			if (row - i) == (col - label[i]) or (i - row) == (col - label[i]):
				return False
		return True


class Solution2(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        label = [-1] * n
        row = 0
        col = 0
        result = 0
        while row < n:
        	while col < n:
        		if self.isValid(label, row, col):
        			label[row] = col
        			break
        		else:
        			col += 1

        	if label[row] == -1:
        		if row == 0:
        			break
        		else:
        			row -= 1
        			col = label[row] + 1
        			label[row] = -1
        			continue

        	if row == n-1:
        		result += 1
        		col = label[row]+1
        		label[row] = -1
        		continue

        	row += 1
        	col = 0

        return result


    def isValid(self, label, row, col):
		for i in range(row):
			if col == label[i]:
				return False
			if (row - i) == (col - label[i]) or (i - row) == (col - label[i]):
				return False
		return True
