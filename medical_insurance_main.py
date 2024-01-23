import csv, utility 

insurance_obj = []
ages = []
charges = []

with open('insurance.csv', newline='') as insurance_data:
  insurance_rows = csv.DictReader(insurance_data, delimiter=',')
  for row in insurance_rows:
    insurance_obj.append(row)
    ages.append(row['age'])
    charges.append(row['charges'])


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Average Age in Sample')
average_age = utility.getAverage(ages, len(ages))
print(average_age)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Average Insurance Cost in Sample')
average_charges = utility.getAverage(charges, len(charges))
print(average_charges)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Regional Stats Object')
regional_insurance_stats = utility.buildCategoryStatsObject(insurance_obj, 'region')
print(regional_insurance_stats)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Gender Stats Object')
gender_insurance_stats = utility.buildCategoryStatsObject(insurance_obj, 'sex')
print(gender_insurance_stats)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Smoker Stats Object')
smoker_insurance_stats = utility.buildCategoryStatsObject(insurance_obj, 'smoker')
print(smoker_insurance_stats)