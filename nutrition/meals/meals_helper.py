#create a meal
def create_meal(*items):
	meal= list(items)
	return meal


# adding a function to meal_helper file that can add items to meals
def add_meal_item(meal,item):
	meal.append(item)

#creating print meal function to helper file
def print_meal(meal, date):
	print('I ate', len(meal), 'items in my breakfast in',date ,'which are:')

	for item in meal:
		if meal.index(item) < 9 and len(meal)> 9:
			print('  ',meal.index(item)+1, '. ' ,item.capitalize())
		else:
			print(' ',meal.index(item)+1, '. ' ,item.capitalize())
