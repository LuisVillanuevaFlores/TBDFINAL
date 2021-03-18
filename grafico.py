import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

datos=pd.read_csv('result.csv',header=0)
popularity=[]
user=[]

for i in datos['popularity']:
    popularity.append(i)

for j in datos['user_name']:
    user.append(j)




# #Definimos una lista con paises como string
# paises = ['Estados Unidos', 'España', 'Mexico', 'Rusia', 'Japon']
# #Definimos una lista con ventas como entero
# ventas = [25, 32, 34, 20, 25]

fig, ax = plt.subplots()
# #Colocamos una etiqueta en el eje Y
ax.set_ylabel('Popularity')
# #Colocamos una etiqueta en el eje X
ax.set_title('Usuarios')
# #Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
plt.barh(user,popularity )
plt.savefig('barras_simple.png')
# #Finalmente mostramos la grafica con el metodo show()
plt.show()