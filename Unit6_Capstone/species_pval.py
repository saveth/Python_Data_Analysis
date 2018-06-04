import codecademylib
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

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

#print(category_counts.head())

# Pivot table: Contingency Table of Endangerment
category_pivot = category_counts.pivot(
  columns = 'is_protected',
  index = 'category',
  values = 'scientific_name').reset_index()

#print(category_pivot)

## Rename the columns, and proportion column
# This code works but Codecademy is still giving error
#category_pivot.rename(columns= {'False': 'not_protected', 'True': 'protected'}, inplace = True)

category_pivot.columns=['category','not_protected', 'protected']

category_pivot['percent_protected'] = (category_pivot['protected'] / (category_pivot['protected'] + category_pivot['not_protected'])) 
print(category_pivot)
## Notes:
##	The proportion of protected species is highest for Bird and Mammal (15% and 17%, respectively). Other species are until 10%.


## Question: Are certain types of species more likely to be endangered?
##	Is the difference between bird and mammel random or is mammel more likely to be endangered?

# Create a Contingency table 
#contingency = category_pivot.set_index("category").iloc[[3,1], [1,0]]
##	Not sure by Codecademy keeps giving an error when this code runs

contingency = [[30,146], [75, 413]]
contingency = pd.DataFrame(contingency)
print(contingency)

chi2, pval, dof, ex = chi2_contingency(contingency)
print(pval)
# The difference in Endangered status of Mammel and bird is not significant (p = 0.688)

## Is there a difference between reptile and mammal?
contingency2 = [[30,146], [5, 73]]
chi2_reptile_mammal, pval_reptile_mammal, dof_reptile_mammal, ex_reptile_mammal = chi2_contingency(contingency2)
print(pval_reptile_mammal)
## There is statistical significant difference in Endangered Status between Mammal and Reptile.