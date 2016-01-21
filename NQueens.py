# coding=utf-8
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

"""


class Solution(object):
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		result = []
		label = [-1] * n
		iterLabel = [-1] * n
		row = 0
		col = 0
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

			if row == n - 1:
				self.addResult(label, result)
				col = label[row] + 1
				label[row] = -1
				continue

			row += 1
			col = 0

		return result

	def addResult(self, label, result):
		length = len(label)
		strList = []
		for i in label:
			s = "." * i
			s += "Q"
			s += "." * (length - i - 1)
			strList.append(s)
		result.append(strList)

	def isValid(self, label, row, col):
		for i in range(row):
			if col == label[i]:
				return False
			if (row - i) == (col - label[i]):
				return False
			if (i - row) == (col - label[i]):
				return False
		return True


if __name__ == "__main__":
	r = Solution().solveNQueens(4)
	print "Finish"
