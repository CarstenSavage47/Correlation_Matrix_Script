
## Correlation matrix script using plotly
# I like this version of the correlation matrix because it is interactive.

import pandas
import seaborn as sns
import matplotlib.pyplot as plt

Titanic = pandas.read_csv("C:/Users/csavage/OneDrive - Alvarez and Marsal/Documents/titanic.csv")

corrMatrix = Titanic.corr()
print(corrMatrix)

# Correlation Matrix Version 1

import plotly.express as px
fig = px.imshow(corrMatrix)

## Correlation Matrix Version 2

Corr_Heat = sns.heatmap(corrMatrix,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size': 10},
                 yticklabels=corrMatrix.columns,
                 xticklabels=corrMatrix.columns,
                 cmap="Spectral_r")
plt.show()

# A pairplot or scatterplot matrix is effective at exploratory data analysis.
# Identify relationships between variables all at once.

Pair_Plot = px.scatter_matrix(Titanic)
Pair_Plot.show()

# Evaluating kurtosis:
# 1. Mesokurtic: Data follows a normal distribution
# 2. Leptokurtic: Heavy tails on either side, indicating large outliers. Looks like Top-Thrill Dragster.
# 3. Playtkurtic: Flat tails indicate that there aren't many outliers.

# A kurtosis value greater than +1 indicates the graph is very peaked. Leptokurtic.
# A kurtosis value less than -1 indicates the graph is relatively flat. Playtkurtic.
# A kurtosis value of 0 indicates that the graph follows a normal distribution. Mesokurtic.

# Evaluating skewness:
# 1. A negative value indicates the tail is on the left side of the distribution.
# 2. A positive value indicates the tail is on the right side of the distribution.
# 3. A value of zero indicates that there is no skewness in the distribution; it's perfectly symmetrical.

print(f"Skewness: {Titanic['Age'].skew()}")
print(f"Kurtosis: {Titanic['Age'].kurt()}")




