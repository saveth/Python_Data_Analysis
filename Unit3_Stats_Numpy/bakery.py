import numpy as np

# Cupcake recipe
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

# Recipe collection
recipes = np.genfromtxt('recipes.csv', delimiter =',')
print(recipes)

# Eggs
eggs = recipes[: , 2]
eggs_1 = eggs[eggs == 1]

# Cookies
cookies = recipes[2, : ]

#Double batch of cupcakes
double_batch = cupcakes * 2

grocery_list = double_batch + cookies
