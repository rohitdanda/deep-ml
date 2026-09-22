def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	result =[]
	for value in a :
		if len(value)!= len(b):
			return -1
		test = 0
		for i in range(len(value)):
			test = test + (value[i]*b[i])
		result.append(test)
	return result
