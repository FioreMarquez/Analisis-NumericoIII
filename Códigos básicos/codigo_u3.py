#FEM segun Zin Li

#---- Codigos en python---
#solo estarán las estructuras, sin tests

import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def hat1(x: np.ndarray | float, x1: float, x2: float) -> np.ndarray | float:
    """Función sombrero local en [x1, x2]: vale 0 en x1 y 1 en x2."""
    return (x - x1) / (x2 - x1)


def hat2(x: np.ndarray | float, x1: float, x2: float) -> np.ndarray | float:
    """Función sombrero local en [x1, x2]: vale 1 en x1 y 0 en x2."""
    return (x2 - x) / (x2 - x1)


def int_hat1_f(f, x1: float, x2: float) -> float:
    """Aproxima int_{x1}^{x2} f(x) * hat1(x) dx con regla de Simpson."""
    xm = 0.5 * (x1 + x2)
    h = x2 - x1
    # En x1 hat1=0, en xm hat1=0.5, en x2 hat1=1
    return (h / 6.0) * (4.0 * f(xm) * 0.5 + f(x2) * 1.0)


def int_hat2_f(f, x1: float, x2: float) -> float:
    """Aproxima int_{x1}^{x2} f(x) * hat2(x) dx con regla de Simpson."""
    xm = 0.5 * (x1 + x2)
    h = x2 - x1
    # En x1 hat2=1, en xm hat2=0.5, en x2 hat2=0
    return (h / 6.0) * (f(x1) * 1.0 + 4.0 * f(xm) * 0.5)


def fem1d(x: np.ndarray, f, u_a: float = 0.0, u_b: float = 0.0) -> np.ndarray:
    """
    Resuelve -u''(x) = f(x) en (x[0], x[-1]) con u(x[0])=u_a, u(x[-1])=u_b
    usando elementos finitos lineales P1.
    """
    M = len(x)
    h = np.diff(x)  # vector de longitudes h[i] = x[i+1] - x[i], largo M-1

    A = lil_matrix((M, M), dtype=float)
    F = np.zeros(M, dtype=float)

    # 1. Ensamblaje elemento por elemento (e = 0, ..., M-2)
    for i in range(M - 1):
        k_loc = 1.0 / h[i]
        # Matriz de rigidez local: [[1, -1], [-1, 1]] / h[i]
        A[i, i] += k_loc
        A[i, i + 1] -= k_loc
        A[i + 1, i] -= k_loc
        A[i + 1, i + 1] += k_loc

        # Vector de carga local: nodo i usa hat2 (izq), nodo i+1 usa hat1 (der)
        F[i] += int_hat2_f(f, x[i], x[i + 1])
        F[i + 1] += int_hat1_f(f, x[i], x[i + 1])

    # 2. Imposición de condiciones de borde de Dirichlet (preservando simetría)
    F -= A[:, 0].toarray().ravel() * u_a
    F -= A[:, -1].toarray().ravel() * u_b

    A[0, :] = 0.0
    A[:, 0] = 0.0
    A[0, 0] = 1.0
    F[0] = u_a

    A[-1, :] = 0.0
    A[:, -1] = 0.0
    A[-1, -1] = 1.0
    F[-1] = u_b

    # 3. Resolución del sistema lineal esparsa
    U = spsolve(A.tocsr(), F)
    return U