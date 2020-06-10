import csv
import glob
import json
import re

with open('urussanga.csv', mode='w') as csv_file:
    fieldnames = ['beneficiario', 'cpf', 'valor']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    files = glob.glob('*.json')
    files.sort(key=lambda v: int(re.findall('\d+', v)[0]))

    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            
            for benef in data['data']:
                writer.writerow({'beneficiario': benef['beneficiario'], 'cpf': benef['cpf'], 'valor': benef['valorTotalPeriodo']})
