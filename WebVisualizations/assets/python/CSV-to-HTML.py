import pandas as pd

cities_df = pd.read_csv("../../resources/cities.csv")

cities_df.to_html("../markup/cities.html", classes="table table-striped", index=False)