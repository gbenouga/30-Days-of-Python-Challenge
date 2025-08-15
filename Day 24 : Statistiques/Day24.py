## **Day 24 – Statistiques**
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
### **1. Génération de nombres aléatoires**

# Nombres aléatoires flottants entre 0 et 1
rand_float = np.random.random(5)
print("***********************************************************************************")
print("Random floats:", rand_float)

# Nombres entiers aléatoires entre 0 et 10 (exclus)
print("***********************************************************************************")
rand_int = np.random.randint(0, 10, 5)
print("Random integers:", rand_int)

### **2. Création d'un tableau NumPy d'entiers**
print("***********************************************************************************")
int_array = np.array([1, 2, 3, 4, 5])
print("Entiers Array :", int_array)

### **3. Création d'un tableau NumPy de flottants**
print("***********************************************************************************")
float_array = np.array([1.1, 2.2, 3.3])
print("Flottants Array :", float_array)

### **4. Création d'un tableau NumPy booléen**
print("***********************************************************************************")
bool_array = np.array([True, False, True])
print("Boolean array:", bool_array)

### **5. Création d’un tableau multidimensionnel**
print("***********************************************************************************")
multi_array = np.array([[1, 2, 3], [4, 5, 6]])
print("Tableaux multi-dimensionnels:\n", multi_array)

### **6. Conversion d’un tableau NumPy en liste**
print("***********************************************************************************")
array_list = multi_array.tolist()
print("Conversion en list:", array_list)

print("***********************************************************************************")
### **7. Forme d’un tableau**
print("Forme:", multi_array.shape)

### **8. Type de données d’un tableau**
print("Type de données:", multi_array.dtype)
### **9. Taille (nombre d’éléments)**

print("Taille:", multi_array.size)

### **10. Opérations de base**
print("***********************************************************************************")
a = np.array([10, 20, 30])
b = np.array([3, 5, 7])

print("Addition:", a + b)
print("Soustraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulo:", a % b)
print("Division entière:", a // b)
print("Exponentiel:", a ** b)

### **11. Tableaux multidimensionnels**
print
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(arr2d)

### **12. Accéder aux éléments**
print("***********************************************************************************")
print("Element (1,2):", arr2d[1, 2])

### **13. Slicing**
print("***********************************************************************************")
print("Deux premiers lignes:\n", arr2d[:2])
print("Deux premiers colonnes:\n", arr2d[:, :2])

### **14. Inverser les lignes et l’ensemble du tableau**
print("***********************************************************************************")
print("Inverser les lignes:\n", arr2d[::-1])
print("Inverser l’ensemble du tableau:\n", arr2d[::-1, ::-1])

### **15. Inverser lignes et colonnes séparément**

reverse_rows = arr2d[:, ::-1]
reverse_cols = arr2d[::-1, :]
print("Inverser les colonnes:\n", reverse_rows)
print("Inverser les lignes:\n", reverse_cols)
### **16. Fonctions NumPy utiles**
print("***********************************************************************************")
data = np.array([10, 20, 30, 40, 50])

print("Min:", np.min(data))
print("Max:", np.max(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Variance:", np.var(data))
print("25th Percentile:", np.percentile(data, 25))
print("Standard Deviation:", np.std(data))

print("***********************************************************************************")

# Dot Product
f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
dot_result = np.dot(f, g)  # 1*4 + 2*5 + 3*3 = 23
print("Dot Product:", dot_result)

# Matrix Multiplication (np.matmul)
h = [[1, 2],
     [3, 4]]
i = [[5, 6],
     [7, 8]]
matmul_result = np.matmul(h, i)
print("Matrix Multiplication:\n", matmul_result)

# Determinant of a Matrix
det_i = np.linalg.det(i)
print("Determinant of i:", det_i)

# Chessboard Pattern (8×8)
Z = np.zeros((8, 8))
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print("Chessboard Pattern:\n", Z)

# Vectorized Operations vs Python Lists
# Python list comprehension
new_list = [x + 2 for x in range(0, 11)]
print("List comprehension result:", new_list)

# NumPy array
np_arr = np.array(range(0, 11))
print("NumPy vectorized result:", np_arr + 2)

# Simple Linear Equation Example
temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5  # Linear relationship: P = 2T + 5

plt.plot(temp, pressure, marker='o')
plt.xlabel('Temperature (°C)')
plt.ylabel('Pressure (atm)')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.grid(True)
plt.show()

# Gaussian (Normal) Distribution
mu = 28        # Mean
sigma = 15     # Standard deviation
samples = 100000  # Number of data points

x = np.random.normal(mu, sigma, samples)
ax = sns.histplot(x,bins=50,  kde=True, color='blue')
ax.set(xlabel="x", ylabel="y")
plt.title("Gaussian (Normal) Distribution")
plt.show()
