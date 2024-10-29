# from items import piItems
from collections import defaultdict
from copy import copy
from pyscript import document,display,HTML

# _______________________________ITEMS 
class piItem():
    # constructor
    def __init__(self, name, outputQuantity, inputName, inputQuantity):
        self.name = name
        self.outputQuantity = outputQuantity
        self.inputName = inputName
        self.inputQuantity = inputQuantity


piItems =[
piItem('Bacteria',20,'Microorganisms',3000),
piItem('Biocells',5,'Precious Metals',40),
piItem('Biocells',5,'Biofuels',40),
piItem('Biofuels',20,'Carbon Compounds',3000),
piItem('Biomass',20,'Planktic Colonies',3000),
piItem('Biotech Research Reports',3,'Nanites',10),
piItem('Biotech Research Reports',3,'Construction Blocks',10),
piItem('Biotech Research Reports',3,'Livestock',10),
piItem('Broadcast Node',1,'Neocoms',6),
piItem('Broadcast Node',1,'Data Chips',6),
piItem('Broadcast Node',1,'High-Tech Transmitters',6),
piItem('Camera Drones',3,'Silicate Glass',10),
piItem('Camera Drones',3,'Rocket Fuel',10),
piItem('Chiral Structures',20,'Non-CS Crystals',3000),
piItem('Condensates',3,'Coolant',10),
piItem('Condensates',3,'Oxides',10),
piItem('Construction Blocks',5,'Reactive Metals',40),
piItem('Construction Blocks',5,'Toxic Metals',40),
piItem('Consumer Electronics',5,'Toxic Metals',40),
piItem('Consumer Electronics',5,'Chiral Structures',40),
piItem('Coolant',5,'Water',40),
piItem('Coolant',5,'Electrolytes',40),
piItem('Cryoprotectant Solution',3,'Test Cultures',10),
piItem('Cryoprotectant Solution',3,'Fertilizer',10),
piItem('Cryoprotectant Solution',3,'Synthetic Oil',10),
piItem('Data Chips',3,'Supertensile Plastics',10),
piItem('Data Chips',3,'Microfiber Shielding',10),
piItem('Electrolytes',20,'Ionic Solutions',3000),
piItem('Enriched Uranium',5,'Toxic Metals',40),
piItem('Enriched Uranium',5,'Precious Metals',40),
piItem('Fertilizer',5,'Bacteria',40),
piItem('Fertilizer',5,'Proteins',40),
piItem('Gel-Matrix Biopaste',3,'Oxides',10),
piItem('Gel-Matrix Biopaste',3,'Biocells',10),
piItem('Gel-Matrix Biopaste',3,'Superconductors',10),
piItem('Genetically Enhanced Livestock',5,'Proteins',40),
piItem('Genetically Enhanced Livestock',5,'Biomass',40),
piItem('Guidance Systems',3,'Water-Cooled CPU',10),
piItem('Guidance Systems',3,'Transmitter',10),
piItem('Hazmat Detection Systems',3,'Transmitter',10),
piItem('Hazmat Detection Systems',3,'Viral Agent',10),
piItem('Hazmat Detection Systems',3,'Polytextiles',10),
piItem('Hermetic Membranes',3,'Genetically Enhanced Livestock',10),
piItem('Hermetic Membranes',3,'Polyaramids',10),
piItem('High-Tech Transmitters',3,'Transmitter',10),
piItem('High-Tech Transmitters',3,'Polyaramids',10),
piItem('Industrial Explosives',3,'Fertilizer',10),
piItem('Industrial Explosives',3,'Polytextiles',10),
piItem('Industrial Fibers',20,'Autotrophs',3000),
piItem('Integrity Response Drones',1,'Planetary Vehicles',6),
piItem('Integrity Response Drones',1,'Hazmat Detection Systems',6),
piItem('Integrity Response Drones',1,'Gel-Matrix Biopaste',6),
piItem('Livestock',5,'Biofuels',40),
piItem('Livestock',5,'Proteins',40),
piItem('Mechanical Parts',5,'Precious Metals',40),
piItem('Mechanical Parts',5,'Reactive Metals',40),
piItem('Microfiber Shielding',5,'Industrial Fibers',40),
piItem('Microfiber Shielding',5,'Silicon',40),
piItem('Miniature Electronics',5,'Chiral Structures',40),
piItem('Miniature Electronics',5,'Silicon',40),
piItem('Nanites',5,'Bacteria',40),
piItem('Nanites',5,'Reactive Metals',40),
piItem('Nano-Factory',1,'Reactive Metals',40),
piItem('Nano-Factory',1,'Ukomi Superconductors',6),
piItem('Nano-Factory',1,'Industrial Explosives',6),
piItem('Neocoms',3,'Biocells',10),
piItem('Neocoms',3,'Silicate Glass',10),
piItem('Nuclear Reactors',3,'Microfiber Shielding',10),
piItem('Nuclear Reactors',3,'Enriched Uranium',10),
piItem('Organic Mortar Applicators',1,'Robotics',6),
piItem('Organic Mortar Applicators',1,'Bacteria',40),
piItem('Organic Mortar Applicators',1,'Condensates',6),
piItem('Oxides',5,'Oxygen',40),
piItem('Oxides',5,'Oxidizing Compound',40),
piItem('Oxidizing Compound',20,'Reactive Gas',3000),
piItem('Oxygen',20,'Noble Gas',3000),
piItem('Planetary Vehicles',3,'Miniature Electronics',10),
piItem('Planetary Vehicles',3,'Mechanical Parts',10),
piItem('Planetary Vehicles',3,'Supertensile Plastics',10),
piItem('Plasmoids',20,'Suspended Plasma',3000),
piItem('Polyaramids',5,'Industrial Fibers',40),
piItem('Polyaramids',5,'Oxidizing Compound',40),
piItem('Polytextiles',5,'Industrial Fibers',40),
piItem('Polytextiles',5,'Biofuels',40),
piItem('Precious Metals',20,'Noble Metals',3000),
piItem('Proteins',20,'Complex Organisms',3000),
piItem('Reactive Metals',20,'Base Metals',3000),
piItem('Recursive Computing Module',1,'Transcranial Microcontrollers',6),
piItem('Recursive Computing Module',1,'Guidance Systems',6),
piItem('Recursive Computing Module',1,'Synthetic Synapses',6),
piItem('Robotics',3,'Consumer Electronics',10),
piItem('Robotics',3,'Mechanical Parts',10),
piItem('Rocket Fuel',5,'Plasmoids',40),
piItem('Rocket Fuel',5,'Electrolytes',40),
piItem('Self-Harmonizing Power Core',1,'Camera Drones',6),
piItem('Self-Harmonizing Power Core',1,'Hermetic Membranes',6),
piItem('Self-Harmonizing Power Core',1,'Nuclear Reactors',6),
piItem('Silicate Glass',5,'Silicon',40),
piItem('Silicate Glass',5,'Oxidizing Compound',40),
piItem('Silicon',20,'Felsic Magma',3000),
piItem('Smartfab Units',3,'Miniature Electronics',10),
piItem('Smartfab Units',3,'Construction Blocks',10),
piItem('Sterile Conduits',1,'Smartfab Units',6),
piItem('Sterile Conduits',1,'Vaccines',6),
piItem('Sterile Conduits',1,'Water',40),
piItem('Supercomputers',3,'Water-Cooled CPU',10),
piItem('Supercomputers',3,'Consumer Electronics',10),
piItem('Supercomputers',3,'Coolant',10),
piItem('Superconductors',5,'Water',40),
piItem('Superconductors',5,'Plasmoids',40),
piItem('Supertensile Plastics',5,'Biomass',40),
piItem('Supertensile Plastics',5,'Oxygen',40),
piItem('Synthetic Oil',5,'Electrolytes',40),
piItem('Synthetic Oil',5,'Oxygen',40),
piItem('Synthetic Synapses',3,'Supertensile Plastics',10),
piItem('Synthetic Synapses',3,'Test Cultures',10),
piItem('Test Cultures',5,'Bacteria',40),
piItem('Test Cultures',5,'Water',40),
piItem('Toxic Metals',20,'Heavy Metals',3000),
piItem('Transcranial Microcontrollers',3,'Nanites',10),
piItem('Transcranial Microcontrollers',3,'Biocells',10),
piItem('Transmitter',5,'Chiral Structures',40),
piItem('Transmitter',5,'Plasmoids',40),
piItem('Ukomi Superconductors',3,'Synthetic Oil',10),
piItem('Ukomi Superconductors',3,'Superconductors',10),
piItem('Vaccines',3,'Viral Agent',10),
piItem('Vaccines',3,'Livestock',10),
piItem('Viral Agent',5,'Biomass',40),
piItem('Viral Agent',5,'Bacteria',40),
piItem('Water',20,'Aqueous Liquids',3000),
piItem('Water-Cooled CPU',5,'Water',40),
piItem('Water-Cooled CPU',5,'Reactive Metals',40),
piItem('Wetware Mainframe',1,'Biotech Research Reports',6),
piItem('Wetware Mainframe',1,'Cryoprotectant Solution',6),
piItem('Wetware Mainframe',1,'Supercomputers',6),
]

# ------------------FUNKTIONS-----------------------------

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
            for x in values['inputNames']:
                input_name += x +", "
            # input_name = "multiple"
        else:
            input_name = next(iter(values['inputNames']))
        result.append({
            'name': name,
            'inputName': input_name,
            'outputQuantity': values['outputQuantity'],
            'inputQuantity': values['inputQuantity']
        })
    
    return result

def calculatePi(event):
    prodList = [('Wetware Mainframe',1),('Broadcast Node',500)]
    resultLists = []
    for item in prodList:
        resultLists.append(calcAmount(item[0],item[1]))

    merged_items = merge_itemsLists(resultLists)
    sorted_data = sorted(merged_items, key=lambda x: x['inputQuantity'])

    selectInput = document.querySelector("#select").value
    amountInput = document.querySelector("#amount").value

    tableOutput = document.querySelector("#output1")
    # output_div = document.querySelector("#output1")


    displayTable = "<table class=\"table table-hover\"><thead><tr><th scope=\"col\">Material</th><th scope=\"col\">Output Quantity</th><th scope=\"col\">InputName</th><th scope=\"col\">Input Quantity</th></tr></thead><tbody>" 
    for item in sorted_data:
        displayTable += "<tr><th scope=\"row\">"+ item["name"]+"</th><td>"+str(item["outputQuantity"])+"</td><td>"+ item["inputName"] +"</td><td>"+str(item["inputQuantity"])+"</td></tr>"

    displayTable += " </tbody></table>"
    # document.querySelector("#output1").innerText = selectInput + " " + amountInput

    display(HTML(displayTable),target="output2",append=False)

    document.querySelector("#output2").append = displayTable


