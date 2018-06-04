import codecademylib
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
#print(species.head())

# New Dataset identifying species in park
observations = pd.read_csv('observations.csv')
print(observations.head())

## Create a subset data containing sheep
#variable identify species as sheep
species['is_sheep'] = species.apply( 
  lambda row: True 
  if 'Sheep' in row['common_names'] 
  else False,
  axis = 1)

# Subset sheep data
species_is_sheep = species[ species.is_sheep == True]
#print(species_is_sheep)
	## Data contains "sheep" in the plant category

sheep_species = species[(species.is_sheep == True) & (species.category == 'Mammal')]
print(sheep_species)

## Question: Where are the sheeps located in the observational data?

# Create merge sheep/park dataset
sheep_observations = observations.merge(
  sheep_species)

print(sheep_observations.head())


# Stats on sighting by location
obs_by_park = sheep_observations.groupby('park_name')[['observations']].sum()
print(obs_by_park)
