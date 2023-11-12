import numpy as np
#mendefinisikan duah buah array a dan b 
arrayA = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
arrayB = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

# No. 1 penjumlah a dan b 
penjumlahan = np.add(arrayA, arrayB)

# No. 2 perkalian a dan b 
perkalian = np.multiply(arrayA, arrayB)

# menampilkan hasil 
print("Array A :")
print(arrayA)

print("Array B :")
print(arrayB)

print("\nPenjumlahan")
print(penjumlahan)

print("\nPerkalian")
print(perkalian)