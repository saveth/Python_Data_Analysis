import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)

## Are certain types of species more likely to be endangered?
## Add species column
species['is_protected'] = species.apply( 
  lambda row: True 
  if row['conservation_status'] != 'No Intervention'
  else False,
  axis = 1)

category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()

print(category_counts.head())

# Pivot table: Contingency Table of Endangerment
category_pivot = category_counts.pivot(
  columns = 'is_protected',
  index = 'category',
  values = 'scientific_name').reset_index()

print(category_pivot)

## Rename the columns, and proportion column
# This code works but Codecademy is still giving error
#category_pivot.rename(columns= {'False': 'not_protected', 'True': 'protected'}, inplace = True)

category_pivot.columns=['category','not_protected', 'protected']

category_pivot['percent_protected'] = (category_pivot['protected'] / (category_pivot['protected'] + category_pivot['not_protected'])) 
print(category_pivot)
## Notes:
##	The proportion of protected species is highest for Bird and Mammal (15% and 17%, respectively). Other species are until 10%.
