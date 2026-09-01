"""HW01 — Linear Algebra

Part 1: Pure-Python implementations (no torch, no numpy).
  Vectors are list[float]; matrices are list[list[float]] (row-major order).

Part 2: PyTorch implementations of more advanced tensor operations — no manual loops.

Run tests:   uv run pytest
Check score: uv run python score.py
"""

from __future__ import annotations

import math  # noqa: F401 — students use this in vector_magnitude

import torch

# ── Part 1: From Scratch ──────────────────────────────────────────────────────


def vector_add(u: list[float], v: list[float]) -> list[float]:
    """Return the element-wise sum of two vectors.

    Both vectors must have the same length.

    Args:
        u: First vector.
        v: Second vector, same length as u.

    Returns:
        A new vector w where w[i] = u[i] + v[i].

    Example:
        >>> vector_add([1.0, 2.0], [3.0, 4.0])
        [4.0, 6.0]

    Hint:
        Think about how to iterate over two lists simultaneously, pairing
        their elements at each position.
    """
    vector_sum=[]
    for i in range(len(u)):
        vector_sum.append(u[i] + v[i])
    return vector_sum
    


def scalar_multiply(c: float, v: list[float]) -> list[float]:
    """Scale every element of a vector by a scalar.

    Args:
        c: The scalar multiplier.
        v: The vector to scale.

    Returns:
        A new vector w where w[i] = c * v[i].

    Example:
        >>> scalar_multiply(3.0, [1.0, 2.0, 3.0])
        [3.0, 6.0, 9.0]

    Hint:
        You know how to visit every element in a list. What would you do
        to each one?
    """
    scalar_multiply_list=[]
    for i in range(len(v)):
        scalar_multiply_list.append(c*v[i])
    return scalar_multiply_list
    


def dot_product(u: list[float], v: list[float]) -> float:
    """Compute the dot product (inner product) of two vectors.

    The dot product is the sum of element-wise products:
        dot(u, v) = u[0]*v[0] + u[1]*v[1] + ... + u[n-1]*v[n-1]

    Args:
        u: First vector.
        v: Second vector, same length as u.

    Returns:
        A single float — the dot product of u and v.

    Example:
        >>> dot_product([1.0, 2.0, 3.0], [4.0, 5.0, 6.0])
        32.0

    Hint:
        You already know how to pair elements from two lists. The dot product
        needs one more step: combine those products into a single number.
    """
    vector_dot_product=0
    for i in range(len(u)):
        vector_dot_product += u[i] * v[i]
    return vector_dot_product


def vector_magnitude(v: list[float]) -> float:
    """Compute the Euclidean (L2) magnitude (length) of a vector.

    magnitude(v) = sqrt(v[0]^2 + v[1]^2 + ... + v[n-1]^2)

    Args:
        v: The input vector.

    Returns:
        A non-negative float — the magnitude of v.

    Example:
        >>> vector_magnitude([3.0, 4.0])
        5.0

    Hint:
        Look at the formula in the docstring — it expresses magnitude in terms
        of an operation you've already implemented.
    """
    sum = 0
    for i in v:
        sum += i**2
    return sum**(1/2)
    


def normalize_vector(v: list[float]) -> list[float]:
    """Return the unit vector in the same direction as v.

    A unit vector has magnitude 1. To normalize, divide each element by the
    magnitude of v.

    Args:
        v: The vector to normalize.

    Returns:
        A new vector with magnitude 1, pointing in the same direction as v.

    Raises:
        ValueError: If v is the zero vector (magnitude == 0).

    Example:
        >>> normalize_vector([3.0, 4.0])
        [0.6, 0.8]

    Hint:
        You have all the pieces from earlier in Part 1. Think about what needs
        to be true about the magnitude before dividing, and what should happen
        if that condition fails.
    """
    magnitude = vector_magnitude(v)
    if magnitude == 0:
        raise ValueError
    
    scalar = 1 / magnitude
    return scalar_multiply(scalar, v)
    


def matrix_add(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """Return the element-wise sum of two matrices.

    Both matrices must have identical dimensions (same number of rows and
    the same number of columns in each row).

    Args:
        A: First matrix (list of rows).
        B: Second matrix, same shape as A.

    Returns:
        A new matrix C where C[i][j] = A[i][j] + B[i][j].

    Example:
        >>> matrix_add([[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]])
        [[6.0, 8.0], [10.0, 12.0]]

    Hint:
        You have a function that adds two vectors. How could you apply it
        to each pair of corresponding rows?
    """
    matrix_sum = []
    
    for i in range(len(A)):
        new_row=[]  
        for j in range(len(A[i])):
            new_row.append(A[i][j] + B[i][j])
        matrix_sum.append(new_row)
    return matrix_sum


def matrix_vector_multiply(A: list[list[float]], v: list[float]) -> list[float]:
    """Multiply a matrix A by a column vector v.

    The i-th element of the output is the dot product of the i-th row of A
    with v:
        result[i] = dot(A[i], v)

    Args:
        A: A matrix with shape (m, n) — m rows, n columns.
        v: A vector of length n.

    Returns:
        A vector of length m.

    Example:
        >>> matrix_vector_multiply([[1.0, 2.0], [3.0, 4.0]], [1.0, 1.0])
        [3.0, 7.0]

    Hint:
        The docstring gives you the mathematical rule. You have a function that
        computes exactly what each output element requires — apply it across the
        rows.
    """
    matrix_vector_product = []
    
    for i in A:
        matrix_vector_product.append(dot_product(i,v))
    return matrix_vector_product
            
        

    
def matrix_transpose(A: list[list[float]]) -> list[list[float]]:
    """Return the transpose of matrix A.

    The transpose swaps rows and columns: T[i][j] = A[j][i].

    Args:
        A: A matrix with shape (m, n).

    Returns:
        The transposed matrix with shape (n, m).

    Example:
        >>> matrix_transpose([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]

    Hint:
        Python's `zip` function can be surprisingly useful here. Think about
        what happens when you pass a list of lists as separate arguments — try
        it on a small example in the REPL.
    """
    zipped_tuples = zip(*A)
    list_of_tuples=list(zipped_tuples)
    list_of_lists=[]
    for i in range(len(list_of_tuples)):
        list_of_lists.append(list(list_of_tuples[i]))
    return(list_of_lists)
    



def matrix_multiply(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """Multiply two matrices A and B.

    If A has shape (m, k) and B has shape (k, n), the result has shape (m, n).
    The (i, j) entry of the result is:
        C[i][j] = dot product of row i of A with column j of B

    Args:
        A: Matrix with shape (m, k).
        B: Matrix with shape (k, n).

    Returns:
        Matrix C with shape (m, n).

    Example:
        >>> matrix_multiply([[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]])
        [[19.0, 22.0], [43.0, 50.0]]

    Hint:
        The hard part is accessing B's columns. Think about what operation
        could turn columns into something easier to work with — you've already
        implemented it.
    """
    matrix_multiplication_product = []
    B_T = matrix_transpose(B)
    for i in range(len(A)):
            matrix_multiplication_product.append(matrix_vector_multiply(B_T, A[i]))

    return matrix_multiplication_product






# ── Part 2: PyTorch Tensors ───────────────────────────────────────────────────


def batch_dot(U: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """Compute the dot product of each corresponding row pair.

    Given two matrices U and V of shape (m, n), entry i of the result
    is the dot product of row i of U with row i of V.

    Args:
        U: 2-D tensor of shape (m, n).
        V: 2-D tensor of shape (m, n), same shape as U.

    Returns:
        1-D tensor of shape (m,) — one scalar per row pair.

    Example:
        >>> U = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
        >>> V = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
        >>> batch_dot(U, V)
        tensor([17., 53.])  # 1*5+2*6=17, 3*7+4*8=53

    Hint:
        torch.dot only works on 1-D tensors. Think about how to compute
        all the element-wise products at once, then how to collapse them
        into one number per row.
    """
    tensor_product = U*V
    return tensor_product.sum(dim=1)
    


def polynomial_features(x: torch.Tensor, degree: int) -> torch.Tensor:
    """Build a polynomial feature matrix from a 1-D tensor.

    Given a vector x of length n and an integer degree d, return an
    (n, d+1) matrix where column j contains x raised to the power j.
    Column 0 is all ones (x^0), column 1 is x, column 2 is x^2, etc.

    This is called the Vandermonde matrix and is used in polynomial
    regression to fit degree-d curves to data.

    Args:
        x: 1-D tensor of length n.
        degree: Non-negative integer — the highest power to include.

    Returns:
        2-D tensor of shape (n, degree + 1).

    Example:
        >>> x = torch.tensor([2.0, 3.0])
        >>> polynomial_features(x, degree=2)
        tensor([[1., 2., 4.],
                [1., 3., 9.]])
        # col 0: x^0=[1,1], col 1: x^1=[2,3], col 2: x^2=[4,9]

    Hint:
        You need to raise x to each power from 0 to degree. Look at
        torch.arange to generate the exponents. Think about whether you
        can broadcast x and the exponent vector against each other —
        what shapes would make that work?
    """
    exponent = torch.arange(degree+1)
    polynomial_featured_matrix = x.unsqueeze(0).T ** exponent
    return polynomial_featured_matrix
    


def row_normalize(A: torch.Tensor) -> torch.Tensor:
    """Normalize each row of a matrix to unit length.

    For a matrix with m rows, returns a new matrix where every row
    has Euclidean norm equal to 1.

    Args:
        A: 2-D tensor of shape (m, n).

    Returns:
        2-D tensor of shape (m, n) where each row has norm 1.

    Raises:
        ValueError: If any row of A is the zero vector.

    Example:
        >>> A = torch.tensor([[3.0, 4.0], [0.0, 2.0]])
        >>> row_normalize(A)
        tensor([[0.6000, 0.8000],
                [0.0000, 1.0000]])

    Hint:
        Compute a norm for each row. When you divide A by the result,
        think about whether the shapes are compatible — there is a
        keyword argument that controls this.
    """
    magnitude_tensor = batch_dot(A,A)
    normalized_tensor = magnitude_tensor ** (1/2)
    for element in normalized_tensor:
        if element == 0:
            raise ValueError
    scalar_tensor = (normalized_tensor ** (-1)).unsqueeze(1)
    row_normalized_tensor = A * scalar_tensor
    return row_normalized_tensor
    


def cosine_similarity(u: torch.Tensor, v: torch.Tensor) -> float:
    """Compute the cosine similarity between two 1-D tensors.

    Cosine similarity measures the angle between two vectors:

        cos_sim(u, v) = (u . v) / (||u|| * ||v||)

    It ranges from -1 (opposite directions) to 1 (same direction).
    A value of 0 means the vectors are perpendicular.

    Args:
        u: 1-D tensor.
        v: 1-D tensor, same length as u.

    Returns:
        A Python float in [-1, 1].

    Raises:
        ValueError: If either u or v is the zero vector.

    Example:
        >>> cosine_similarity(torch.tensor([1.0, 0.0]), torch.tensor([1.0, 0.0]))
        1.0
        >>> cosine_similarity(torch.tensor([1.0, 0.0]), torch.tensor([0.0, 1.0]))
        0.0

    Hint:
        Each term in the formula maps to a PyTorch operation.
        Handle the case where either input is the zero vector.
    """

    if torch.dot(u,u) == 0 or torch.dot(v,v) == 0:
        raise ValueError
    
    numerator = torch.dot(u,v)
    denominator_u = torch.dot(u,u) ** (1/2)
    denominator_v = torch.dot(v,v) ** (1/2)
    denominator = denominator_u * denominator_v
    return (float(numerator/denominator))


def distance(u: torch.Tensor, v: torch.Tensor) -> float:
    difference = u-v
    square = difference ** 2
    distance = square.sum() ** (1/2)
    return distance

def pairwise_distances(A: torch.Tensor) -> torch.Tensor:
    """Compute the pairwise Euclidean distance between every row of A.

    For a matrix with m rows, returns an (m, m) matrix where entry (i, j)
    is the Euclidean distance between row i and row j of A.

    The diagonal will be all zeros (distance from a row to itself) and
    the matrix will be symmetric.

    Args:
        A: 2-D tensor of shape (m, n).

    Returns:
        2-D tensor of shape (m, m).

    Example:
        >>> A = torch.tensor([[0.0, 0.0], [3.0, 4.0]])
        >>> pairwise_distances(A)
        tensor([[0., 5.],
                [5., 0.]])

    Hint:
        To compute the distance between every pair of rows, think about how
        you would set up the subtraction so that all pairs are computed at
        once. Subtraction of two differently-shaped tensors can broadcast —
        what shapes would make row i of one copy and row j of the other copy
        line up correctly for all i and j simultaneously?
        Do not use torch.cdist.
    """
    m = len(A)
    result = torch.zeros((m, m))

    for i in range(m):
        for j in range(m):
            result[i][j] = distance(A[i],A[j]).item()
    return result
    


def least_squares(X: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """Find the least-squares solution to the system Xw = y.

    Given a design matrix X of shape (m, n) and target vector y of
    shape (m,), find the weight vector w that minimizes ||Xw - y||^2.

    The solution satisfies the normal equations:

        X^T X w = X^T y

    Do NOT solve by computing the inverse of X^T X. Use a dedicated
    linear system solver — it is numerically more stable and faster.

    Args:
        X: 2-D tensor of shape (m, n), where m >= n and X has full column rank.
        y: 1-D tensor of shape (m,).

    Returns:
        1-D tensor of shape (n,) — the weight vector w.

    Example:
        >>> X = torch.tensor([[1.0, 1.0], [1.0, 2.0], [1.0, 3.0]])
        >>> y = torch.tensor([2.0, 3.0, 4.0])
        >>> least_squares(X, y)
        tensor([1., 1.])  # intercept=1, slope=1 (exact fit: y = 1 + x)

    Hint:
        Build the left-hand side (X^T X) and right-hand side (X^T y) of
        the normal equations using matrix operations. Then find a function
        in torch.linalg that solves a linear system directly.
        Do not use .inverse().
    """
    left = X.T @ X
    right = X.T @ y
    w = torch.linalg.solve(left,right)
    return w