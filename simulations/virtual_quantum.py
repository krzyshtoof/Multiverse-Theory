import numpy as np
import scipy.linalg as la

# Parametry zegara kwantowego
offset = -0.00000001  # Odchylenie

# Generowanie stanu kwantowego zegara kwantowego
VirtualQuantum = np.random.randint(0, 2)

# Obliczanie wartości zegara kwantowego
value = VirtualQuantum

# Wykonywanie operacji "X" na stanie kwantowym zegara kwantowego
VirtualQuantum = np.dot(VirtualQuantum, np.array([[0, 1], [1, 0]]))

# Obliczanie wartości zegara kwantowego po operacji "X"
value = VirtualQuantum

# Wyświetlanie wyników
print("Stan kwantowy:", VirtualQuantum)
print("Wartość:", value)
