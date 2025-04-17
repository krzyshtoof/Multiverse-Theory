import numpy as np
import scipy.linalg as la

# Parametry cząsteczki wodoru
m = 9.1094e-31  # Masa elektronu
e = 1.602e-19  # Ładunek elektronu
hbar = 1.054e-34  # Stawka Plancka

# Generowanie stanu kwantowego elektronu
psi = np.random.rand(2)

# Obliczanie energii elektronu
E = (e ** 2) / (4 * np.pi * hbar ** 2 * (m / 2)) * (1 - psi[0] ** 2)

# Obliczanie oddziaływania między elektronem a jądrem
V = -e ** 2 / (4 * np.pi * hbar ** 2 * m) * (1 / np.sqrt((psi[0] ** 2 + psi[1] ** 2) ** 2 - (2 * psi[0] * psi[1]) ** 2))

# Rozwiązywanie równania Schrödingera
psi_t = la.solve(H - E, psi)

# Wyświetlanie wyników
print("Energia:", E)
print("Stan kwantowy:", psi_t)

