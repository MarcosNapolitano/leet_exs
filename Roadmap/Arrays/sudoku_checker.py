class Solution:
    def isValidSudoku(self, board):

    	if len(board)!=9: return False

    	index = {}

    	def count_index(array):

    		for i in array:

    			if i == ".": continue

    			if index.get(i): index[i]+=1

    			else: index[i] = 1	

    		for i in index.values():

    			if i>1: 
    				index.clear()
    				return False

    		index.clear()

    		return True

    	def check_horizontal(board):

		    #false in list? if true then the condition FAILS so it's false
    		return not False in list(map(count_index, board))

    	def check_vertical(board):

    		results = []

    		for i in range(9):

    			temp_array = [board[0][i],
    						  board[1][i],
    						  board[2][i],
    						  board[3][i],
    						  board[4][i],
    						  board[5][i],
    						  board[6][i],
    						  board[7][i],
    						  board[8][i]]

    			results.append(count_index(temp_array)) 
    			

    		return not False in results

    	#tiene que haber una manera menos hardcodeada
    	def check_area(board):

    		results = []

    		for i in range(0,9,3):

    			temp_array1 = [board[i][0],
    						   board[i][1],
    						   board[i][2],
    						   board[i+1][0],
    						   board[i+1][1],
    						   board[i+1][2],
    						   board[i+2][0],
    						   board[i+2][1],
    						   board[i+2][2]]

    			temp_array2 = [board[i][3],
    						   board[i][4],
    						   board[i][5],
    						   board[i+1][3],
    						   board[i+1][4],
    						   board[i+1][5],
    						   board[i+2][3],
    						   board[i+2][4],
    						   board[i+2][5]]


    			temp_array3 = [board[i][6],
    						   board[i][7],
    						   board[i][8],
    						   board[i+1][6],
    						   board[i+1][7],
    						   board[i+1][8],
    						   board[i+2][6],
    						   board[i+2][7],
    						   board[i+2][8]]

    			results.append(count_index(temp_array1))
    			results.append(count_index(temp_array2))
    			results.append(count_index(temp_array3))


    		return not False in results

    	return check_horizontal(board) & check_vertical(board) & check_area(board)


    	


board = [[".",".","1",".",".",".","3",".","."],
		 [".",".","4",".",".",".","1",".","."],
		 [".",".",".",".",".",".",".",".","."],
		 [".",".",".",".","8",".",".",".","."],
		 [".","1",".",".","2",".",".",".","."],
		 [".",".",".",".",".",".","6","3","."],
		 ["7",".",".",".",".",".",".",".","."],
		 ["5","8",".",".",".",".","4",".","."],
		 [".","5",".",".","4",".",".",".","8"]]

a = Solution()

print(a.isValidSudoku(board))