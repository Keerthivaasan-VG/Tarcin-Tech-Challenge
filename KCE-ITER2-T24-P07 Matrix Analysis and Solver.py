import numpy as np
import json

def analyze_and_solve(A, B, b):
    result = {}
    # Determinant
    result['determinant_A'] = float(np.linalg.det(A))

    # Inverse
    try:
        result['inverse_A'] = np.linalg.inv(A).tolist()
    except np.linalg.LinAlgError:
        result['inverse_A'] = None

    # Eigenvalues
    result['eigenvalues_B'] = np.linalg.eigvals(B).tolist()

    # Solve Ax = b
    try:
        result['solution_x'] = np.linalg.solve(A, b).tolist()
    except np.linalg.LinAlgError:
        result['solution_x'] = None

    # Save to JSON
    with open("matrix_result.json", "w") as f:
        json.dump(result, f, indent=4)

    return result


if __name__ == "__main__":
    A = np.array([[2, 1], [5, 3]])
    B = np.array([[1, 2], [3, 4]])
    b = np.array([1, 2])

    res = analyze_and_solve(A, B, b)
    print(res)
