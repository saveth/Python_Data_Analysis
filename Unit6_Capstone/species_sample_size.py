# Sample Size Calculation to  Identify Reduction of Foot and Mouth Disease in 
# Sheep population by 5%

baseline = 15
minimum_detectable_effect = 100 * (5.0/15)
print(minimum_detectable_effect)

sample_size_per_variant = 890

yellowstone_weeks_observing = sample_size_per_variant / 507.0

print(yellowstone_weeks_observing)

bryce_weeks_observing = sample_size_per_variant / 250.0
print bryce_weeks_observing
