import csv, utility 

insurance_obj = []
regions = []

with open('insurance.csv', newline='') as insurance_data:
  insurance_rows = csv.DictReader(insurance_data, delimiter=',')
  for row in insurance_rows:
    insurance_obj.append(row)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Regional Stats Object')
print(utility.buildCategoryStatsObject(insurance_obj, 'region'))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Gender Stats Object')
print(utility.buildCategoryStatsObject(insurance_obj, 'sex'))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Smoker Stats Object')
print(utility.buildCategoryStatsObject(insurance_obj, 'smoker'))