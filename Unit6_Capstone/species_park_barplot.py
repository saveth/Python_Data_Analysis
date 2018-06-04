import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]

observations = pd.read_csv('observations.csv')

sheep_observations = observations.merge(sheep_species)

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()

## Plot the sheep observation data
x_val = range(len(obs_by_park['park_name']))
plt.figure(figsize = [16,4])
ax = plt.subplot(1,1,1)
ax.bar(x_val, obs_by_park.observations, align = 'center')
ax.set_xticks(x_val)
ax.set_xticklabels(obs_by_park.park_name)
ax.set_ylabel('Number of Observations')
ax.set_xlabel('Park')
ax.set_title('Observations of Sheep per Week')
plt.show()