def buildCategoryStatsObject(insurance_obj, insurance_property):
  stats_object = {}
  categories = getCategories(insurance_obj, insurance_property)

  for category in categories:
    total_obj = getCategoryTotals(insurance_obj, insurance_property, category)
    stats_object[category] = total_obj
    stats_object[category]['average'] = getCategoryAverage(total_obj)
  
  return stats_object

def getCategories(insurance_obj, insurance_property):
  categories_list = []

  for item in insurance_obj:
    if categories_list.count(item[insurance_property]) == 0:
      categories_list.append(item[insurance_property])
  
  return categories_list

def getCategoryTotals(insurance_obj, insurance_prop, category):
  insurance_and_category_object = {
    'count': 0,
    'total_cost': 0
  }

  for item in insurance_obj:
    if item[insurance_prop] == category:
      insurance_and_category_object['count'] += 1
      insurance_and_category_object['total_cost'] += float(item['charges'])

  return insurance_and_category_object

def getCategoryAverage(data_obj):
  average = data_obj['total_cost']/data_obj['count']
  return average

def getAverage(values, count):
  total = 0

  for value in values:
    total += float(value)
  
  average = total/count
  return average