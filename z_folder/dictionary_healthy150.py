import json
from datetime import datetime
from statistics import mean

#read json file contents and convert it to python dictionary
def read_file_json_to_dict(file_path):
	with open(file_path, 'r') as file:
		dict1= json.load(file)
	return dict1

#Convert data from json to dictionary
personData = read_file_json_to_dict('data_healthy150_2.json')

#save data to personData
def save_data_to_personData():
	with open('data_healthy150_2.json', 'w') as file:
		json.dump(personData, file, indent=6)

#Add a person item
def add_item(person_id, item, **kwargs):
	if person_id in personData.keys():
		dict1 = {item: kwargs}
		personData[person_id].update(dict1)
	else:
		dict1 = {person_id: {item: kwargs}}
		personData.update(dict1)

#Add a person item with subitem
def add_item_with_subitem(person_id, item, subitem, **kwargs):
	if item not in personData[person_id].keys():
		dict3 = {item:{subitem:kwargs}}
		personData[person_id].update(dict3)
		print("step1")
	else:
		dict2 = {subitem:kwargs}
		personData[person_id][item].update(dict2)
	
	

#Add a person item with two subitem
def add_item_with_two_subitems(person_id, item, subitem1, subitem2, **kwargs):

	# if person_id not in personData.keys():
	# 	dict1 = {person_id: {item: {subitem1: {subitem2: kwargs}}}}
	# 	personData.update(dict1)
	if item not in personData[person_id]:
		print('step 2')
		dict3 = {item:{subitem1: {subitem2:kwargs}}}
		personData[person_id].update(dict3)
	elif subitem1 not in personData[person_id][item].keys():
		print('step 3')
		dict2 = {subitem1: {subitem2: kwargs}}
		personData[person_id][item].update(dict2)
	else:
		print('step 4')
		dict2 = {subitem2: kwargs}
		personData[person_id][item][subitem1].update(dict2)

#Add a person item with three subitem
def add_item_with_three_subitems(person_id, item, subitem1, subitem2, subitem3, **kwargs):
	# date = datetime(date).strftime("%A %d/%B/%Y")

	# if person_id not in personData.keys():
	# 	print('step 5')
	# 	dict1 = {person_id: {item: {subitem1: {subitem2: {subitem3: kwargs}}}}}
	# 	personData.update(dict1)
	if item not in personData[person_id].keys():
		print('step 6')
		dict3 = {item:{subitem1: {subitem2: {subitem3: kwargs}}}}
		personData[person_id].update(dict3)
	elif subitem1 not in personData[person_id][item].keys():
		print('step 7')
		dict2 = {subitem1: {subitem2: {subitem3: kwargs}}}
		personData[person_id][item].update(dict2)
	elif subitem2 not in personData[person_id][item][subitem1].keys():
		print('step 8')
		dict2 = {subitem2: {subitem3: kwargs}}
		personData[person_id][item][subitem1].update(dict2)
	else:
		print('step 9')
		dict2 = {subitem3: kwargs}
		personData[person_id][item][subitem1][subitem2].update(dict2)

#Add a person item with date
# def add_item_with_date(person_id, date, item, **kwargs):
# 	# date = datetime(date).strftime("%A %d/%B/%Y")

# 	if person_id not in personData.keys():
# 		dict1 = {person_id: {date: {item: kwargs}}}
# 		add_data_to_json(dict1)
# 	elif date not in personData[person_id].keys():
# 		dict2 = {date:{item:kwargs}}
# 		personData[person_id].update(dict2)
# 		save_data_to_personData()
# 	else:
# 		dict3 = {item:kwargs}
# 		personData[person_id][date].update(dict3)
# 		save_data_to_personData()

#Add a person item with date with subitem
# def add_item_with_subitem_with_date(person_id, date, item, subitem, **kwargs):
# 	# date = datetime(date).strftime("%A %d/%B/%Y")

# 	if person_id not in personData.keys():
# 		dict1 = {person_id: {date: {item: {subitem:kwargs}}}}
# 		add_data_to_json(dict1)
# 	elif date not in personData[person_id].keys():
# 		dict2 = {date:{item:kwargs}}
# 		personData[person_id].update(dict2)
# 		save_data_to_personData()
# 	elif item not in personData[person_id][date]:
# 		dict3 = {item:{subitem:kwargs}}
# 		personData[person_id][date].update(dict3)
# 		save_data_to_personData()
# 	elif person_id in personData.keys() and date in personData[person_id].keys() and item in personData[person_id][date]:
# 		dict4 = {subitem:kwargs}
# 		personData[person_id][date][item].update(dict4)
# 		save_data_to_personData()
# form a list an item from persondata
		
def list_item(item, subitem):
	items_list=[]
	for value in personData.values():
		items_list.append(value[item][subitem])
	return items_list

# form a list an item from persondata with subitem related to another item
def list_item_related(item, item2,  subitem1):
	items_list=[]
	for value in personData.values():
		for key in value.keys():
			if item2 in key:
				items_list.append(value[item][subitem1])
	return items_list

# form a list an item from persondata with subitem related to another subitem
def list_subitem_related(item, subitem1, subitem2, content):
	items_list=[]
	for value in personData.values():
		if value[item][subitem2] == content:
			items_list.append(value[item][subitem1])
	return items_list

#the total number and percentage of an item content
def total_number_item(item, subitem, content1, content2):
	item_list= list_item(item, subitem)

	print(f"the total number of {content1} patients is: {item_list.count(content1)}%")
	print(f"the percentage of {content1} patients is:   {round(item_list.count(content1)*100/len(item_list),2)}%")
	print(f"the total number of {content2} patients is: {item_list.count(content2)}")
	print(f"the percentage of {content2} patients is:   {round(item_list.count(content2)*100/len(item_list),2)}%")

# calculate the mean of an item
def mean_of_item(item, subitem):
	item_list= list_item(item, subitem)
	mean_item= round(mean(item_list), 1)
	return mean_item

#calculate the mean of an item related to another item
def mean_of_subitem_related(item, subitem1, subitem2, content):
	item_list = list_subitem_related(item, subitem1, subitem2, content)
	item_list_mean = round(mean(item_list))
	return item_list_mean

