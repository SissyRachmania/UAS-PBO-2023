import pandas as pd 

# No.3 membaca kolom harga saja
data = pd.read_csv('harga_rumah.csv') # membaca file csv

# membaca salah satu kolom berdasarkan nama kolom
df = pd.DataFrame(data)
print(df.harga)
print(df['harga'])

# No. 4 buang kolom harga
data = pd.read_csv('harga_rumah.csv') # membaca file csv

#membunag kolom harga
X = df.drop(['harga'],axis=1)

print(X.head())