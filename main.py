
## Correlation matrix script using plotly
# I like this version of the correlation matrix because it is interactive.

import pandas
Titanic = pandas.read_csv("titanic.csv")

corrMatrix = Titanic.corr()
print(corrMatrix)

import plotly.express as px
fig = px.imshow(corrMatrix)

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




