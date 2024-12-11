import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(rc={'figure.figsize':(16,6)}, style="whitegrid")

retail = pd.read_csv("datasets/raw/bank.csv", encoding="ISO-8859-1")
retail.head()
