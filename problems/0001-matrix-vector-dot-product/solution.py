def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	rows =  len(a)
	cols = len(a[0])
	sz = len(b)

	if(cols != sz): 
		return -1

	ans = []
	for row in a:
		sum = 0
		for x,y in zip(row, b):
			sum = sum + (x*y)
		ans.append(sum)
	return ans
