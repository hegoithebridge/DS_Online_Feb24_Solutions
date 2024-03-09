import pickle

# Deserializar el DataFrame con pickle
with open('dataframe.pickle', 'rb') as f:
    df = pickle.load(f)

print("DataFrame deserializado:")
print(df)