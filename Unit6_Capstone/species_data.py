import codecademylib
import pandas as pd
import numpy as np
import matplotlib

# Load the data
species = pd.read_csv('species_info.csv')
print(species.head())

####
# Understanding the data
####

species_shape = species.shape
print(species_shape) 
	## There are 5824 rows with 4 variables

species_size = species.groupby('scientific_name').size()
species_count = len(species_size)
print(species_count)
		## There are 5541 unique species
  	## Implies there are duplicate species in the dataset
    
species_type = species.category.unique()
print(species_type)
	## There are 7 categories that includes, plants, and animal

conservation_statuses = species.conservation_status.unique()
print(conservation_statuses)
	# There are 4 levels of conservation 
  
####
# How many species are in conservation status?
####
conservation_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print(conservation_counts)

###
# Modify the data
###
species.fillna('No Intervention', inplace = True)

conservation_counts_fixed = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print(conservation_counts_fixed)
