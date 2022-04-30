# Import files from UCI Machine Learning Repository
import pandas as pd
path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00547/Algerian_forest_fires_dataset_UPDATE.csv'
df = pd.read_csv(path)
print(df.iloc[:5])
