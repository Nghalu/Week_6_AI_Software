import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os
# Loading data (try comma, then tab, then infer)
file_path = 'TCGA_COAD.dataset.csv'
df = None
last_exc = None
for sep in [',', '\t', None]:
	try:
		if sep is None:
			df = pd.read_csv(file_path, sep=None, engine='python')
		else:
			df = pd.read_csv(file_path, sep=sep)
		break
	except Exception as e:
		last_exc = e

if df is None:
	raise RuntimeError(f"Failed to read '{file_path}' with inferred separators") from last_exc

# If the file was read into a single column but that column contains tab-separated fields,
# re-read using the tab separator (this happens when a .csv actually uses tabs).
if df.shape[1] == 1:
	col0 = df.columns[0]
	sample_vals = df[col0].astype(str)
	if sample_vals.str.contains('\t').any() or '\t' in str(col0):
		df = pd.read_csv(file_path, sep='\t')
		print("Re-parsed the file using tab separator due to embedded tabs.")

print(df.head())
print(df.info())

# Data preprocessing
# Drop rows with any missing values
df = df.dropna()
print(f"Data shape after dropping missing values: {df.shape}")

# Exploratory Data Analysis
print(df.describe())

# Determine which column to plot: prefer 'gene_expression', else pick a numeric column
plot_col = None
if 'gene_expression' in df.columns:
	plot_col = 'gene_expression'
else:
	numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
	if numeric_cols:
		plot_col = numeric_cols[0]
		print(f"Column 'gene_expression' not found. Using numeric column '{plot_col}' for histogram.")
	else:
		print("No numeric columns available to plot. Skipping histogram.")

if plot_col is not None:
	plt.figure(figsize=(10, 6))
	sns.histplot(df[plot_col], bins=30, kde=True)
	plt.title(f'{plot_col} Distribution')
	plt.xlabel(plot_col)
	plt.ylabel('Frequency')
	plt.show()
                                                                           