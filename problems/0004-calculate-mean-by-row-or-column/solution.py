def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	result=[]
	if mode == 'row':
		for row in matrix:
			temp=0
			for value in row:
				temp = temp+value
			result.append(temp/len(row))

	if mode == 'column':
		for i in range(len(matrix[0])):
			temp = 0
			for j in range(len(matrix)):
				temp = temp + matrix[j][i]
			result.append(temp/len(matrix))


	return result
