import json
import time

import requests

offset = 0
page_size = 30

while True:
    resp = requests.get(f'http://www.portaldatransparencia.gov.br/beneficios/auxilio-emergencial/resultado?paginacaoSimples=false&tamanhoPagina={page_size}&offset={offset}&direcaoOrdenacao=asc&colunaOrdenacao=beneficiario&colunasSelecionadas=linkDetalhamento%2Cuf%2Cmunicipio%2Ccpf%2Cnis%2Cbeneficiario%2CnomeResponsavelFamiliar%2CcpfResponsavelFamiliar%2CnisResponsavelFamiliar%2Cobservacao%2CvalorTotalPeriodo&de=01%2F05%2F2020&ate=31%2F05%2F2020&municipio=20744&_=1591820128657')

    data = resp.json()

    with open(f'{offset}.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

    offset += page_size

    if offset > data['recordsTotal']:
        break

    time.sleep(5)