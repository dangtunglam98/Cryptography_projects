
def mat_mul(X,Y):
	result = [[sum(x * y for x, y in zip(X_row, Y_col))%2 for Y_col in zip(*Y)] for X_row in X]
	return result

def exp(matrix, n):
    temp_n = n
    temp_a = matrix
    result = i_mat(len(matrix))
    while temp_n != 0:
        if temp_n % 2 == 1:
            result = mat_mul(temp_a, result)
        temp_a = mat_mul(temp_a,temp_a)
        temp_n //= 2
    return result

def display_mat(mat):
	string = ""
	for i in range(len(mat)):
		line = " ".join([str(x) for x in mat[i]])
		string += line + "\n"
	print(string)

def i_mat(s):
	res = [[0 for i in range(s)] for j in range(s)]
	for i in range(s):
		res[i][i] = 1
	return res

def a_mat(s):
	res = [[0 for i in range(2*s)] for j in range(2*s)]
	for j in range(2*s):
		for i in range(2*s):
			if (i>=s and j>=s):
				if i == j:
					if i-1 >= s:
						res[j][i-1] = 1
					if i+1 <= 2*s-1:
						res[j][i+1] = 1
					res[j][i] = 1
			if (i>=s and j<s):
				if i-s == j:
					res[j][i] = 1
			if (i<s and j>=s):
				if i == j-s:
					res[j][i] = 1
	return res

def puzzle(l,r,n):
	mat_a = a_mat(len(r))
	temp_l = [[int(c)] for c in l]
	temp_r = [[int(c)] for c in r]
	res_mat_a = exp(mat_a,n)
	result = mat_mul(res_mat_a,temp_l+temp_r)
	result = [str(x[0]) for x in result]
	return ''.join(result[:len(r)]), ''.join(result[len(r):])

if __name__ == "__main__":
	with open("input.txt",'r') as f:
		f = f.read().split()
		res_l, res_r = puzzle(f[0],f[1],int(f[2]))
		with open("output.txt",'w') as o:
			o.write(res_l+'\n')
			o.write(res_r+'\n')