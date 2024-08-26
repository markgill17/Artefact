import pandas as pd
from pathlib import Path  
# read in downloaded parquet file as a dataframe
df = pd.read_parquet(r'C:\Users\Mark\Downloads\daily_weather.parquet')

# selected dates to match up with football data
df = df.loc[(df['date']>='1999-01-01')&(
    # select months of football season
    (df['date'].dt.month == 1)|
    (df['date'].dt.month == 2) |
    (df['date'].dt.month == 9) |
    (df['date'].dt.month == 10) |
    (df['date'].dt.month == 11) |
    (df['date'].dt.month == 12)
    )&
    # select relevant cities
    (df['city_name'].isin(["Phoenix", #ARI, LV, SD
                           "Columbia", #CAR
                           "Nashville", #TEN
                           "Columbus", #CIN, PIT, CLE
                           "Annapolis", #BAL
                           "Washington", #WAS
                           "Olympia", #SEA
                           "Denver", #DEN
                           "Sacramento", #LAR, LAC, LA, SF, OAK
                           "Providence", #NE
                           "Indianapolis", #IND
                           "Tallahassee", #JAX, TB, MIA, 
                           "Madison", #GB ,CHI
                           "Saint Paul", #MIN
                           "Lansing", #DET
                           "Topeka", #KC, STL
                           "Austin", #DAL, HOU
                           "Trenton", #PHI, NYJ, NYG 
                           "Albany", #BUF
                           "Atlanta", #ATL
                           "Jackson" #NO
                           ]))&(df['date'].dt.day == 15)
]
# write dataframe to a file in csv format
filepath = Path(r'C:\Users\Mark\OneDrive - Atlantic TU\Documents\Data\weatherData.csv')
filepath.parent.mkdir(parents=True, exist_ok=True) 
df.to_csv(filepath)