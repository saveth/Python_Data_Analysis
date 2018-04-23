import codecademylib
import numpy as np

# Load and view data
calorie_stats = np.genfromtxt('cereal.csv', delimiter =',')
print(calorie_stats)

# Stats
average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print(median_calories)

first_quartile = np.percentile(calorie_stats, 25)
print(first_quartile)

percent_10 = np.percentile(calorie_stats, 2)
print(percent_10)

percent_11 = np.percentile(calorie_stats, 11)
print(percent_11)

nth_percentile = percent_11
more_calories = np.mean([calorie_stats > 60])
print(more_calories)

calorie_std = np.std(calorie_stats)
print(calorie_std)
