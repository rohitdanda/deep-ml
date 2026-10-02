def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result =[]
	for inner in matrix:
		temp=[]
		for value in inner:
			temp.append(value*scalar)
		result.append(temp)
	return result
