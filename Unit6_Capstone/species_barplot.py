import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)

protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by = 'scientific_name')

#protection_counts = pd.DataFrame(protection_counts.\
#                                 to_records())
#protection_counts.drop(['index'], axis=1, inplace = True)
print(protection_counts)

###
# Graphing
###
x_val = range(len(protection_counts['conservation_status']))

plt.figure(figsize = [10,4])
ax = plt.subplot(1,1,1)
ax.bar(x_val, protection_counts['scientific_name'], align = 'center')
ax.set_xlabel('Conservation Status')
ax.set_ylabel('Number of Species')
ax.set_title('Conservation Status by Species')
ax.set_xticks(x_val)
ax.set_xticklabels(protection_counts['conservation_status'])
plt.show()
