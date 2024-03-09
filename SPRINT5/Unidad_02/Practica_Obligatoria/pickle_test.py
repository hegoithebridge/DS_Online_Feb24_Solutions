import pandas as pd
import pickle

# Crear un DataFrame de ejemplo
data = {'Nombre': ['Juan', 'María', 'Luis'],
        'Edad': [30, 25, 35]}
df = pd.DataFrame(data)

# Serializar el DataFrame con pickle
with open('dataframe.pickle', 'wb') as f:
    pickle.dump(df, f)

print("DataFrame serializado exitosamente.")

