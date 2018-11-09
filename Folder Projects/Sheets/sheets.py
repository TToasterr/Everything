import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='creds.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['UR MOM xd'] = ['Rather', 'Large', 'Homo']

#open the google spreadsheet
sh = gc.open('Testing')

#select the first sheet
wks = sh[0]

#update the first sheet with df, starting at cell B2.
wks.set_dataframe(df,(5,5))
