import numpy as np
A = [[2,1],[1,3]]
B = [3,7]
A = np.array(A)
B = np.array(B)
trace_A = int (np.trace(A))
eigen_A = [round(float(ev),6) for ev in np.linalg.eigvals(..
solution = [round(float(x),6) for x in np.linalg.solve(A,B)]
matrix_out = {"trace":trace_A,"eigenvalues":eigen_A,"solution"...
print("{")
print(f' "trace":{matrix_out["trace"]},')
print(f' "eigenvalues":{matrix_out["eigenvalues"]},')
print(f' "solution":{matrix_out["solution"]}')
print("}")
