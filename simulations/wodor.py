import numpy as np
import scipy.linalg as la

# Parametry zegara kwantowego
offset = 0.00000001  # Odchylenie

# Generowanie stanu kwantowego zegara kwantowego
qibit = np.random.randint(0, 2)

# Obliczanie wartości zegara kwantowego
value = qibit

# Wykonywanie operacji "X" na stanie kwantowym zegara kwantowego
qibit = np.dot(qibit, np.array([[0, 1], [1, 0]]))

# Obliczanie wartości zegara kwantowego po operacji "X"
value = qibit

# Wyświetlanie wyników
print("Stan kwantowy:", qibit)
print("Wartość:", value)
