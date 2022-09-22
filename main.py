
## Correlation matrix script using plotly
# I like this version of the correlation matrix because it is interactive.

import pandas
Titanic = pandas.read_csv("titanic.csv")

corrMatrix = Titanic.corr()
print(corrMatrix)

import plotly.express as px
fig = px.imshow(corrMatrix)
fig.show()


