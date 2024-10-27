from items import piItem,piItems
from collections import defaultdict
from copy import copy
from operator import itemgetter,attrgetter

def calcAmount(itemName,quantity):
    array = []
    quantity = checkAndAdjustMinimalQuantity(itemName,quantity)
    
    items = [piItem for piItem in piItems if piItem.name == itemName]

    # find first level
    for item in items:
            if item not in array:
                item.inputQuantity = item.inputQuantity * round(quantity/   item.outputQuantity)  
                item.outputQuantity = quantity
                array.append(copy(item))
    # find all other levels
    findLevelsWithValues(items,array)

    return array

def checkAndAdjustMinimalQuantity(itemName,quantity):
    for piItem in piItems:
            if piItem.name==itemName:
                minimalQuantity = piItem.outputQuantity
                break

    if quantity % minimalQuantity > 0:
          quantity = quantity + (minimalQuantity - quantity % minimalQuantity)
    return quantity


def findLevelsWithValues(resultList,array): 
    for resultItem in resultList:
        items = [piItem for piItem in piItems if piItem.name == resultItem.inputName]
        for item in items:
            item.inputQuantity = item.inputQuantity * round(resultItem.inputQuantity /   item.outputQuantity)  
            item.outputQuantity = resultItem.inputQuantity
            array.append(copy(item))
        # recursion baby
        findLevelsWithValues(items,array)
    return array


def merge_itemsLists(lists):
    merged = defaultdict(lambda: {'outputQuantity': 0, 'inputQuantity': 0, 'inputNames': set()})
    
    for piItems in lists:
        for item in piItems:
            key = (item.name, item.inputName)
            merged[key]['outputQuantity'] += item.outputQuantity
            merged[key]['inputQuantity'] += item.inputQuantity
            merged[key]['inputNames'].add(item.inputName)
    
    final_merge = {}
    for (name, inputName), values in merged.items():
        if name not in final_merge:
            final_merge[name] = {
                'outputQuantity': values['outputQuantity'],
                'inputQuantity': values['inputQuantity'],
                'inputNames': values['inputNames']
            }
        else:
            # Bei unterschiedlichem inputName keine Summation der Werte
            final_merge[name]['inputNames'].update(values['inputNames'])
    
    result = []
    for name, values in final_merge.items():
        if len(values['inputNames']) > 1:
            input_name = ""
        else:
            input_name = next(iter(values['inputNames']))
        result.append({
            'name': name,
            'inputName': input_name,
            'outputQuantity': values['outputQuantity'],
            'inputQuantity': values['inputQuantity']
        })
    
    return result

prodList = [('Wetware Mainframe',1),('Broadcast Node',500)]
resultLists = []
for item in prodList:
     resultLists.append(calcAmount(item[0],item[1]))

merged_items = merge_itemsLists(resultLists)
sorted_data = sorted(merged_items, key=lambda x: x['inputQuantity'])

for item in sorted_data:
    print(item)
