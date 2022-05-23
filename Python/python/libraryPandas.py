
#Pandas is a library for data analysis
import pandas as pd

###############################################
###############################################
#                DataFrames                   #
###############################################
###############################################

# #importamos la ruta del csv
# csv_path = 'file1.csv'
# #ahora pasamos a almancenar los datos en df 
# df = pd.read_csv(csv_path)
# #el metodo head() se usa para examinar las primeras cinco filas de un marco de datos
# df.head()

# #"Para un archivo de excel es lo mismo solo es el .xlsx"
# xlsx_path = "file.xslx"
# df = pd.read_excel(xlsx_path)
# df.head()

#Dicionario
songs = { 
          'Album': ['Thriller', 'Back in Bloack', 'The Dark side of the moon', 'The Bodyguard', 'Bad Out of Hell'], 
          'Released': [ 1982, 1980, 1973, 1992, 1977 ],  
          'Lenght': [ '00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33' ] 
        }
### ### ### ### ### ### ### ### 
songs_frame = pd.DataFrame(songs)

print(songs_frame)

#La creación de una nueva columna separada de la tabla, que se ha creado
x=songs_frame[["Lenght"]]

print(x)