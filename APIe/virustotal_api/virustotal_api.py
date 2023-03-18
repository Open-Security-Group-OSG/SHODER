from requests import get
from other.style import bold_green, bold_red, bold_yellow, bold_cyan, reset

vt_valid_keys = []
vt_invalid_keys = []


def check(key: str):
    try:
        allowance = get(f'https://virustotal.com/api/v3/users/{key}', headers={'x-apikey': key}).json()['data']['attributes']['quotas']['api_requests_daily']['allowed']
        print(f'{key} is a {bold_green}VALID{reset} {bold_yellow}VIRUSTOTAL KEY{reset} and daily requests quota is {bold_cyan}{allowance}{reset}')
        return [key, True, allowance]
    except:
        print(f'{key} is {bold_red}INVALID{reset} as {bold_yellow}VIRUSTOTAL KEY{reset}')
        return [key, False]
