# from items import piItems
from collections import defaultdict
from copy import copy,deepcopy
from pyscript import document,display,HTML

# _______________________________ITEMS 
class piItem():
    # constructor
    def __init__(self, name, outputQuantity, inputName, inputQuantity,piLevel,requested=False):
        self.name = name
        self.outputQuantity = outputQuantity
        self.inputName = inputName
        self.inputQuantity = inputQuantity
        self.piLevel = piLevel
        self.requested = requested


piItemList =[
piItem('Bacteria',20,'Microorganisms',3000,1),
piItem('Biocells',5,'Precious Metals',40,2),
piItem('Biocells',5,'Biofuels',40,2),
piItem('Biofuels',20,'Carbon Compounds',3000,1),
piItem('Biomass',20,'Planktic Colonies',3000,1),
piItem('Biotech Research Reports',3,'Nanites',10,3),
piItem('Biotech Research Reports',3,'Construction Blocks',10,3),
piItem('Biotech Research Reports',3,'Livestock',10,3),
piItem('Broadcast Node',1,'Neocoms',6,4),
piItem('Broadcast Node',1,'Data Chips',6,4),
piItem('Broadcast Node',1,'High-Tech Transmitters',6,4),
piItem('Camera Drones',3,'Silicate Glass',10,3),
piItem('Camera Drones',3,'Rocket Fuel',10,3),
piItem('Chiral Structures',20,'Non-CS Crystals',3000,1),
piItem('Condensates',3,'Coolant',10,3),
piItem('Condensates',3,'Oxides',10,3),
piItem('Construction Blocks',5,'Reactive Metals',40,2),
piItem('Construction Blocks',5,'Toxic Metals',40,2),
piItem('Consumer Electronics',5,'Toxic Metals',40,2),
piItem('Consumer Electronics',5,'Chiral Structures',40,2),
piItem('Coolant',5,'Water',40,2),
piItem('Coolant',5,'Electrolytes',40,2),
piItem('Cryoprotectant Solution',3,'Test Cultures',10,3),
piItem('Cryoprotectant Solution',3,'Fertilizer',10,3),
piItem('Cryoprotectant Solution',3,'Synthetic Oil',10,3),
piItem('Data Chips',3,'Supertensile Plastics',10,3),
piItem('Data Chips',3,'Microfiber Shielding',10,3),
piItem('Electrolytes',20,'Ionic Solutions',3000,1),
piItem('Enriched Uranium',5,'Toxic Metals',40,2),
piItem('Enriched Uranium',5,'Precious Metals',40,2),
piItem('Fertilizer',5,'Bacteria',40,2),
piItem('Fertilizer',5,'Proteins',40,2),
piItem('Gel-Matrix Biopaste',3,'Oxides',10,3),
piItem('Gel-Matrix Biopaste',3,'Biocells',10,3),
piItem('Gel-Matrix Biopaste',3,'Superconductors',10,3),
piItem('Genetically Enhanced Livestock',5,'Proteins',40,2),
piItem('Genetically Enhanced Livestock',5,'Biomass',40,2),
piItem('Guidance Systems',3,'Water-Cooled CPU',10,3),
piItem('Guidance Systems',3,'Transmitter',10,3),
piItem('Hazmat Detection Systems',3,'Transmitter',10,3),
piItem('Hazmat Detection Systems',3,'Viral Agent',10,3),
piItem('Hazmat Detection Systems',3,'Polytextiles',10,3),
piItem('Hermetic Membranes',3,'Genetically Enhanced Livestock',10,3),
piItem('Hermetic Membranes',3,'Polyaramids',10,3),
piItem('High-Tech Transmitters',3,'Transmitter',10,3),
piItem('High-Tech Transmitters',3,'Polyaramids',10,3),
piItem('Industrial Explosives',3,'Fertilizer',10,3),
piItem('Industrial Explosives',3,'Polytextiles',10,3),
piItem('Industrial Fibers',20,'Autotrophs',3000,1),
piItem('Integrity Response Drones',1,'Planetary Vehicles',6,4),
piItem('Integrity Response Drones',1,'Hazmat Detection Systems',6,4),
piItem('Integrity Response Drones',1,'Gel-Matrix Biopaste',6,4),
piItem('Livestock',5,'Biofuels',40,2),
piItem('Livestock',5,'Proteins',40,2),
piItem('Mechanical Parts',5,'Precious Metals',40,2),
piItem('Mechanical Parts',5,'Reactive Metals',40,2),
piItem('Microfiber Shielding',5,'Industrial Fibers',40,2),
piItem('Microfiber Shielding',5,'Silicon',40,2),
piItem('Miniature Electronics',5,'Chiral Structures',40,2),
piItem('Miniature Electronics',5,'Silicon',40,2),
piItem('Nanites',5,'Bacteria',40,2),
piItem('Nanites',5,'Reactive Metals',40,2),
piItem('Nano-Factory',1,'Reactive Metals',40,4),
piItem('Nano-Factory',1,'Ukomi Superconductors',6,4),
piItem('Nano-Factory',1,'Industrial Explosives',6,4),
piItem('Neocoms',3,'Biocells',10,2),
piItem('Neocoms',3,'Silicate Glass',10,2),
piItem('Nuclear Reactors',3,'Microfiber Shielding',10,2),
piItem('Nuclear Reactors',3,'Enriched Uranium',10,2),
piItem('Organic Mortar Applicators',1,'Robotics',6,4),
piItem('Organic Mortar Applicators',1,'Bacteria',40,4),
piItem('Organic Mortar Applicators',1,'Condensates',6,4),
piItem('Oxides',5,'Oxygen',40,2),
piItem('Oxides',5,'Oxidizing Compound',40,2),
piItem('Oxidizing Compound',20,'Reactive Gas',3000,1),
piItem('Oxygen',20,'Noble Gas',3000,1),
piItem('Planetary Vehicles',3,'Miniature Electronics',10,3),
piItem('Planetary Vehicles',3,'Mechanical Parts',10,3),
piItem('Planetary Vehicles',3,'Supertensile Plastics',10,3),
piItem('Plasmoids',20,'Suspended Plasma',3000,1),
piItem('Polyaramids',5,'Industrial Fibers',40,2),
piItem('Polyaramids',5,'Oxidizing Compound',40,2),
piItem('Polytextiles',5,'Industrial Fibers',40,2),
piItem('Polytextiles',5,'Biofuels',40,2),
piItem('Precious Metals',20,'Noble Metals',3000,1),
piItem('Proteins',20,'Complex Organisms',3000,1),
piItem('Reactive Metals',20,'Base Metals',3000,1),
piItem('Recursive Computing Module',1,'Transcranial Microcontrollers',6,4),
piItem('Recursive Computing Module',1,'Guidance Systems',6,4),
piItem('Recursive Computing Module',1,'Synthetic Synapses',6,4),
piItem('Robotics',3,'Consumer Electronics',10,3),
piItem('Robotics',3,'Mechanical Parts',10,3),
piItem('Rocket Fuel',5,'Plasmoids',40,2),
piItem('Rocket Fuel',5,'Electrolytes',40,2),
piItem('Self-Harmonizing Power Core',1,'Camera Drones',6,4),
piItem('Self-Harmonizing Power Core',1,'Hermetic Membranes',6,4),
piItem('Self-Harmonizing Power Core',1,'Nuclear Reactors',6,4),
piItem('Silicate Glass',5,'Silicon',40,2),
piItem('Silicate Glass',5,'Oxidizing Compound',40,2),
piItem('Silicon',20,'Felsic Magma',3000,1),
piItem('Smartfab Units',3,'Miniature Electronics',10,3),
piItem('Smartfab Units',3,'Construction Blocks',10,3),
piItem('Sterile Conduits',1,'Smartfab Units',6,4),
piItem('Sterile Conduits',1,'Vaccines',6,4),
piItem('Sterile Conduits',1,'Water',40,4),
piItem('Supercomputers',3,'Water-Cooled CPU',10,3),
piItem('Supercomputers',3,'Consumer Electronics',10,3),
piItem('Supercomputers',3,'Coolant',10,3),
piItem('Superconductors',5,'Water',40,2),
piItem('Superconductors',5,'Plasmoids',40,2),
piItem('Supertensile Plastics',5,'Biomass',40,2),
piItem('Supertensile Plastics',5,'Oxygen',40,2),
piItem('Synthetic Oil',5,'Electrolytes',40,2),
piItem('Synthetic Oil',5,'Oxygen',40,2),
piItem('Synthetic Synapses',3,'Supertensile Plastics',10,3),
piItem('Synthetic Synapses',3,'Test Cultures',10,3),
piItem('Test Cultures',5,'Bacteria',40,2),
piItem('Test Cultures',5,'Water',40,2),
piItem('Toxic Metals',20,'Heavy Metals',3000,1),
piItem('Transcranial Microcontrollers',3,'Nanites',10,3),
piItem('Transcranial Microcontrollers',3,'Biocells',10,3),
piItem('Transmitter',5,'Chiral Structures',40,2),
piItem('Transmitter',5,'Plasmoids',40,2),
piItem('Ukomi Superconductors',3,'Synthetic Oil',10,3),
piItem('Ukomi Superconductors',3,'Superconductors',10,3),
piItem('Vaccines',3,'Viral Agent',10,3),
piItem('Vaccines',3,'Livestock',10,3),
piItem('Viral Agent',5,'Biomass',40,2),
piItem('Viral Agent',5,'Bacteria',40,2),
piItem('Water',20,'Aqueous Liquids',3000,1),
piItem('Water-Cooled CPU',5,'Water',40,2),
piItem('Water-Cooled CPU',5,'Reactive Metals',40,2),
piItem('Wetware Mainframe',1,'Biotech Research Reports',6,4),
piItem('Wetware Mainframe',1,'Cryoprotectant Solution',6,4),
piItem('Wetware Mainframe',1,'Supercomputers',6,4),
]

# ------------------FUNKTIONS-----------------------------


def checkAndAdjustMinimalQuantity(itemName,quantity):
    piItems = deepcopy(piItemList)
    for piItem in piItems:
            if piItem.name==itemName:
                minimalQuantity = piItem.outputQuantity
                break

    if quantity % minimalQuantity > 0:
          quantity = quantity + (minimalQuantity - quantity % minimalQuantity)
    return quantity

def calcAmount(itemName,InputQuantity):
    array = []
    items= []
    piItems = deepcopy(piItemList)
    
    quantity = checkAndAdjustMinimalQuantity(itemName,InputQuantity)
    
    items = [piItem for piItem in piItems if piItem.name == itemName]
 
    # find first level
    for item in items:
            if item not in array:
                item.inputQuantity = item.inputQuantity * round(quantity/   item.outputQuantity)  
                item.outputQuantity = copy(quantity)
                item.requested = True
                array.append(deepcopy(item))
    # find all other levels
    array = findLevelsWithValues(items,array)

    return array


def findLevelsWithValues(resultList,array): 
    piItems = deepcopy(piItemList)
    for resultItem in resultList:
        items = [piItem for piItem in piItems if piItem.name == resultItem.inputName]
        for item in items:
            item.inputQuantity = item.inputQuantity * round(resultItem.inputQuantity /   item.outputQuantity)  
            item.outputQuantity = resultItem.inputQuantity
            array.append(deepcopy(item))
        # recursion baby
        array = findLevelsWithValues(items,array)
    return array


def merge_itemsLists(lists):
    merged = defaultdict(lambda: {'outputQuantity': 0, 'inputQuantity': 0, 'inputNames': set(),'piLevel':0})
    
    for piItems in lists:
        for item in piItems:
            key = (item.name, item.inputName)
            merged[key]['outputQuantity'] += item.outputQuantity
            merged[key]['inputQuantity'] += item.inputQuantity
            merged[key]['inputNames'].add(item.inputName)
            merged[key]['piLevel'] = item.piLevel

    
    final_merge = {}
    for (name, inputName), values in merged.items():
        if name not in final_merge:
            final_merge[name] = {
                'outputQuantity': values['outputQuantity'],
                'inputQuantity': values['inputQuantity'],
                'inputNames': values['inputNames'],
                'piLevel': values['piLevel'],
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
            'inputQuantity': values['inputQuantity'],
            'piLevel': values['piLevel'],
        })
    
    return result

def items_to_html_options(piItems): 
    unique_names = set()
    html = "<select class=\"form-select\" id=\"select\">\n"
    html += "<option selected>Select PI-Material</option>\n"
    for item in piItems: 
        if item.name not in unique_names: 
            unique_names.add(item.name)
            html += f" <option value=\"{item.name}\">{item.name}</option>\n"
    html += "</select>" 
    display(HTML(html),target="selectOutput",append=False)

def calculatePi(event):
    quantity = 0
    selectInput = document.querySelector("#select").value
    amountInput = document.querySelector("#amount").value
    if selectInput != "" and amountInput != "" and selectInput != "Select PI-Material":
        prodList = [(selectInput,int(amountInput)),('Wetware Mainframe',1)]
        resultLists = []


        for item in prodList:
            resultLists.append(deepcopy(calcAmount(item[0],item[1])))


        merged_items = merge_itemsLists(resultLists)
        sorted_data = sorted(merged_items, key=lambda x: x['piLevel'],reverse = True)

    
        displayTable = "<table class=\"table table-hover\"><thead><tr><th scope=\"col\">PI-Level</th><th scope=\"col\">Material</th><th scope=\"col\">Output #</th><th scope=\"col\">Input Material needed</th><th scope=\"col\">Quantity needed</th></tr></thead><tbody>" 
        for item in sorted_data:         
            if len([touple for touple in prodList if touple[0] == item['name']]) == 1:
                displayTable += "<tr class=\"table-success\">"
            else:
                displayTable += "<tr>"
            displayTable += "<td scope=\"row\">"+ str(item["piLevel"])+"</td><td scope=\"row\">"+ item["name"]+"</td><td>"+str(item["outputQuantity"])+"</td><td>"+ item["inputName"] +"</td><td>"+str(item["inputQuantity"])+"</td></tr>"

        displayTable += " </tbody></table>"

        display(HTML(displayTable),target="output1",append=False)
    else:
        displayTable = "<p>Not all inputs were selected<p>"
        display(HTML(displayTable),target="output1",append=False)


items_to_html_options(piItemList)