
import familiar
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

#Import Vein Data
vein_pack_lifespans = familiar.lifespans(package = 'vein')

#Stats Test
vein_pack_test= ttest_1samp(vein_pack_lifespans, 71)
print(vein_pack_test)

if vein_pack_test[1] < 0.05:
  print "The Vein Pack Is Proven To Make You Live Longer!"
else:
  print "The Vein Pack Is Probably Good For You Somehow!"
  
# Import Artery Data
artery_pack_lifespans = familiar.lifespans(package = 'artery')

#Stat Test
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
if package_comparison_results[1] < 0.05:
  print "The Artery Package guarantees even stronger results!"
else:
  print "The Artery Package is also a great product!"
  
# Iron Level Contingency Table
iron_contingency_table = familiar.iron_counts_for_package()
print(iron_contingency_table)
iron_t, iron_pvalue, iron_degree, iron_exp = chi2_contingency(iron_contingency_table)

if iron_pvalue < 0.05:
  print "The Artery Package Is Proven To Make You Healthier!"
else:
  print "While We Can't Say The Artery Package Will Help You, I Bet It's Nice!"
  
