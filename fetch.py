"""
inputs:
* sanitized_id of len 8 [str]
* year in yyyy format [str]
* semester can be WINTER/SPRING/SUMMER [SEASON Enum]

possible TODO:
* create a semesterOBJ class and pass a ref/ptr to an instance of it in instead(pyhton hanles that for me, ill just pass the instance...).


this module should receive an id, that is sanitized already, ping the endpoint
a sanitized id has 8 digits.
"""


import requests

base_url = f"https://portalex.technion.ac.il/sap/opu/odata/sap/Z_CM_EV_CDIR_DATA_SRV/"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


response = requests.get(base_url, headers=headers, timeout=10)
response.raise_for_status()