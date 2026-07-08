# Central Park Squirrel Data Analysis
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_df = data["Primary Fur Color"].dropna().value_counts()
fur_df = fur_df.rename_axis("Fur Color").reset_index(name="Count")

fur_df.to_csv("squirrel_count.csv")
