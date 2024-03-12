import pandas as pd

# Load Sheet1 and Sheet2 into separate dataframes
df1 = pd.read_excel(r"gradestocaltab.xlsx", sheet_name='Sheet1')
df2 = pd.read_excel(r"gradestocaltab.xlsx", sheet_name='Sheet2')

# Create a dictionary mapping university and country to their IDs
id_dict = dict(zip(zip(df2['university_name'], df2['Country']), df2['uid']))

# Replace university and country in Sheet1 with their IDs
df1['University'] = df1.apply(lambda x: id_dict.get((x['University'], x['Country']), x['University']), axis=1)

# Save the updated Sheet1 dataframe to a new Excel file
df1.to_excel('cal_insertion12.xlsx', index=False)
