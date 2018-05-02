import numpy as np
import pandas as pd
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency
# Tail Length data
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
print(np.mean(rottweiler_tl), np.std(rottweiler_tl))

#Rescue dogs
whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)
pval = binom_test(num_whippet_rescues, num_whippets, 0.08)
print(pval)

# Weight of dogs
#anova
whippet = fetchmaker.get_weight("whippet")
terrier = fetchmaker.get_weight("terrier")
pitbull = fetchmaker.get_weight("pitbull")

fstat, pval = f_oneway(whippet, terrier, pitbull)
print(fstat, pval)

#Multiple Comparison
weight_breeds = np.concatenate([whippet, terrier, pitbull])
labels = ['whippet'] * len(whippet) + ['terrier'] * len(terrier) + ['pitbull'] * len(pitbull)

breed_weight_results = pairwise_tukeyhsd(weight_breeds, labels, 0.05)
print(breed_weight_results)

# Color of dogs
poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")
poodle_vals, poodle_counts = np.unique(poodle_colors, return_counts=True)
shihtzu_vals, shihtzu_counts = np.unique(shihtzu_colors, return_counts=True)
#print(poodle_vals, poodle_counts)
#print(shihtzu_vals, shihtzu_counts)

color_table = map(list,zip(poodle_counts, shihtzu_counts))
print(color_table)
chi2, pval, dof, ex = chi2_contingency(color_table)
print(pval)