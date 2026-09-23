import numpy as np
import math

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	row = len(a)
	cl = len(a[0])
	if (row*cl)!=(math.prod(new_shape)):
		return []
	else:
		reshaped_matrix=[]
		list_n = [x for sub in a for x in sub]
		new_shape_r = new_shape[1]
		for i in range(new_shape[0]):
			reshaped_matrix.append(list_n[i*new_shape_r:(i+1)*new_shape_r])


	return reshaped_matrix