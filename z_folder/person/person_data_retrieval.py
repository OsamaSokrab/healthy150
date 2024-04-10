from z_folder.dictionary_healthy150 import personData, list_item

# The total number of patients
def total_number_patients():
	total_number_patients = len(personData)
	return total_number_patients

# Print the total number and names of patients without cards
def patients_without_cards():
	patients_without_cards=[]
	for key in personData.keys():
		if not key.isnumeric():
			patients_without_cards.append(key)
	print(f"The patients who have no card numbers are {len(patients_without_cards)} and their names are")
	for item in patients_without_cards:
		print(item)

# Print patient summary
def patient_summary(card_number):
	patient_data = personData[card_number]
	

# Print the patients names
def print_patients_names():
	patients_names= list_item('personal data', 'name')
	for name in patients_names:
		print(name)