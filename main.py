import pandas as pd

#Reading input data:
df_anime = pd.read_csv('dataIN/anime.csv')
df_rating = pd.read_csv('dataIN/rating.csv')


#Cleaning/pre-processing data:
df_anime.rename(columns={'genre' : 'genres'}, inplace=True)

listOfGenres = []
for genreList in df_anime['genres']:
    for genre in str(genreList).split(", "):
        if genre not in listOfGenres and genre != False:
            listOfGenres.append(genre)
print(listOfGenres, len(listOfGenres), "\n\n")

genre_df = df_anime['genres'].str.get_dummies(', ').add_prefix('genre_')
df_anime = pd.concat([df_anime, genre_df], axis=1)

listOfTypes = []
for type in df_anime['type']:
    if type not in listOfTypes and type != False:
        listOfTypes.append(type)
print(listOfTypes, len(listOfTypes), "\n\n")

type_df = df_anime['type'].str.get_dummies(', ').add_prefix('type_')
df_anime = pd.concat([df_anime, type_df], axis=1)

print(df_anime.head().to_string())

#Exploratory data analysis:
"""
for genre in listOfGenres:
    if genre:
        print(df_anime.groupby("genre_" + genre)["rating"].mean(), "\n")

for type in listOfTypes:
    if type:
        print(df_anime.groupby("genre_" + type)["rating"].mean(), "\n")
"""