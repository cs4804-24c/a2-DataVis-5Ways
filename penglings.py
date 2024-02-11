import matplotlib.pyplot as plt
import csv

pengdict = {
    'Adelie':{
        'bill_length_mm':[],
        'flipper_length_mm':[],
        'body_mass_g':[]
    },
    'Gentoo':{
        'bill_length_mm':[],
        'flipper_length_mm':[],
        'body_mass_g':[]
    },
    'Chinstrap':{
        'bill_length_mm':[],
        'flipper_length_mm':[],
        'body_mass_g':[]
    }
}
with open('penglings.csv', newline='') as file:
    reader = csv.DictReader(file)
    for entry in reader:
        if (entry['bill_length_mm'] != 'NA'):
            pengdict[entry['species']]['bill_length_mm'].append(((float(entry['bill_length_mm'])-20))**2)
            pengdict[entry['species']]['flipper_length_mm'].append(float(entry['flipper_length_mm']))
            pengdict[entry['species']]['body_mass_g'].append(float(entry['body_mass_g']))

fig = plt.figure(figsize=(14,8))
plt.scatter(pengdict['Adelie']['flipper_length_mm'], pengdict['Adelie']['body_mass_g'], s=pengdict['Adelie']['bill_length_mm'], c='#FF8C00', alpha=0.8)
plt.scatter(pengdict['Gentoo']['flipper_length_mm'], pengdict['Gentoo']['body_mass_g'], s=pengdict['Gentoo']['bill_length_mm'], c='#008B8B', alpha=0.8)
plt.scatter(pengdict['Chinstrap']['flipper_length_mm'], pengdict['Chinstrap']['body_mass_g'], s=pengdict['Chinstrap']['bill_length_mm'], c='#9932CC', alpha=0.8)
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")

plt.show()
plt.savefig('pythonpenglings.png')