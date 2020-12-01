import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

figure = px.scatter(df, x="date", y="cases", color="country", title="Number of covid cases in each country", size_max=39)
figure.show()